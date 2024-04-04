#!/usr/bin/python3
"""0-validate_utf8 module
"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding
    """
    rem_bytes = 0

    # iterate through each byte
    for byte in data:
        if rem_bytes == 0:
            if byte >> 7 == 0b0:
                rem_bytes = 0
            elif byte >> 5 == 0b110:
                rem_bytes = 1
            elif byte >> 4 == 0b1110:
                rem_bytes = 2
            elif byte >> 3 == 0b11110:
                rem_bytes = 3
            else:
                return False
        else:
            if byte >> 6 == 0b10:
                rem_bytes -= 1
            else:
                return False
    return rem_bytes == 0
