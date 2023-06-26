# Siemens-QA-Assignment
# CRC Error Injection

This project provides a script to inject CRC errors into a given byte index of a data packet. It takes the byte index, byte value, and calculated CRC value as inputs and returns the recalculated CRC value after injecting the error.

## Installation

1. Clone the repository:
   
     ```git clone https://github.com/AliKhalaf1/Siemens-QA-Assignment.git```
   
2. Navigate to the project directory:
   
      ```cd Siemens QA Assignment```

   
## Usage

Run the `crc.py` script with the following command:

    python crc.py <byte_index> <byte_value> <calculated_crc>

Replace `<byte_index>`, `<byte_value>`, and `<calculated_crc>` with the appropriate values.

Example:

    python crc.py 2 33 AA11BB22

This will inject the byte value `0x33` at byte index 2 and recalculate the CRC based on the given calculated CRC value.


## Automated Test Cases
The `test_cases.json` file contains a set of test cases to verify the correctness of the script. You can run the test cases using the provided `test_automation_crc.py`:

    python test_automation_crc.py

The test results will be logged in the `test_results.log` file.

