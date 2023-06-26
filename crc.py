import argparse


def inject_crc_error(byte_index, byte_value, crc_value):
    # Convert the CRC value to a 32-bit binary string
    crc_binary = format(crc_value, "032b")

    # Convert the desired byte value to an 8-bit binary string
    byte_binary = format(byte_value, "08b")

    # Replace all bytes before the specified byte index with the desired byte value
    end_position = 8 * byte_index
    crc_binary = byte_binary * byte_index + crc_binary[end_position:]

    # Recalculate the CRC value
    recalculated_crc = int(crc_binary, 2)

    return recalculated_crc


# parse arguments for the function
parser = argparse.ArgumentParser(description="Inject CRC error")
parser.add_argument(
    "byte_index", type=int, help="Index of the byte to inject the error"
)
parser.add_argument(
    "byte_value",
    type=lambda x: int(x, 16),
    help="Desired byte value in hexadecimal format",
)
parser.add_argument(
    "calculated_crc",
    type=lambda x: int(x, 16),
    help="Calculated CRC value in hexadecimal format",
)
args = parser.parse_args()
# call the function
if (
    args.byte_index < 0
    or args.byte_value < 0
    or args.calculated_crc < 0
    or args.byte_index > 5
    or args.calculated_crc > 0xFFFFFFFF
    or args.byte_value > 0xFF
):
    print("Invalid Input")
else:
    # call the function
    recalculated_crc = inject_crc_error(
        args.byte_index, args.byte_value, args.calculated_crc
    )
    if recalculated_crc is None:
        print("Invalid Input")
    else:
        print(format(recalculated_crc, "08X"))
