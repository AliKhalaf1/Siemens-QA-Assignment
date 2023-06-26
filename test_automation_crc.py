import subprocess
import json
import logging

# Configure logging
logging.basicConfig(
    filename="test_results.log",
    level=logging.INFO,
    format=" %(levelname)s - %(message)s",
)


def validate_inputs(byte_index, byte_value, crc):
    if (
        byte_index < 0
        or byte_index > 5
        or byte_value < 0
        or byte_value > 0xFF
        or crc < 0
        or crc > 0xFFFFFFFF
    ):
        raise ValueError("Invalid input")


def test_inject_crc_error_script(byte_index, byte_value, calculated_crc):
    command = [
        "python",
        "crc.py",
        str(byte_index),
        byte_value,
        calculated_crc,
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Subprocess execution failed: {e}")
        return None


# Load test cases from JSON file
with open("test_cases.json") as file:
    data = json.load(file)
    test_cases = data["test_cases"]

    # Iterate through test cases
    for i, test_case in enumerate(test_cases):
        logging.info("")
        logging.info(f"Test Case {i + 1}")
        try:
            byte_index = int(test_case["byte_index"])
            byte_value = int(test_case["byte_value"], 16)
            crc = int(test_case["calculated_crc"], 16)
            expected_output = test_case["expected_output"]

            validate_inputs(byte_index, byte_value, crc)

            # Call the function
            recalculated_crc = test_inject_crc_error_script(
                byte_index, hex(byte_value)[2:].upper(), hex(crc)[2:].upper()
            )

            # Log the test case details and the result
            logging.info(f"   Byte Index: {byte_index}")
            logging.info(f"   Byte Value: {hex(byte_value)[2:].upper()}")
            logging.info(f"   Calculated CRC: {hex(crc)[2:].upper()}")
            logging.info(f"   Expected Output: {expected_output}")
            logging.info(f"   Actual Output: {recalculated_crc}")
            if recalculated_crc == expected_output:
                logging.info("   Status: Passed")
            else:
                logging.error("   Status: Failed")
        except ValueError as e:
            logging.warning(f"Invalid Input: {e}")
