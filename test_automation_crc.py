import subprocess
import json


def test_inject_crc_error_script(byte_index, byte_value, calculated_crc):
    command = [
        "python",
        "crc.py",
        str(byte_index),
        byte_value,
        calculated_crc,
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()


# Load test cases from JSON file
with open("test_cases.json") as file:
    data = json.load(file)
    test_cases = data["test_cases"]

    # Iterate through test cases
    for (
        i,
        test_case,
    ) in enumerate(test_cases):
        print("Test Case", i + 1)
        try:
            byte_index = int(test_case["byte_index"])
            byte_value = int(test_case["byte_value"], 16)
            crc = int(test_case["calculated_crc"], 16)
            expected_output = test_case["expected_output"]

        except ValueError:
            print("Invalid Input")
            print()
            continue
        if (
            byte_index < 0
            or byte_value < 0
            or crc < 0
            or byte_index > 5
            or crc > 0xFFFFFFFF
            or byte_value > 0xFF
        ):
            print("Invalid Input")
            print()
        else:
            # call the function
            recalculated_crc = test_inject_crc_error_script(
                byte_index, hex(byte_value), hex(crc)
            )
            # Print the test case details and the result

            print("Byte Index:", byte_index)
            print("Byte Value:", hex(byte_value)[2:].upper())
            print("Calculated CRC:", hex(crc)[2:].upper())
            print("Expected Output:", expected_output)
            print("Actual Output:", recalculated_crc)
            print(
                "Result:", "Passed" if recalculated_crc == expected_output else "Failed"
            )

            print()
