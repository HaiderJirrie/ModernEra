import re


def filter_hex_values(text: str):
    hex_pattern = r"\b0x[0-9a-fA-F]+\b|\b[0-9a-fA-F]+\b"
    return re.findall(hex_pattern, text)

def convert_hex_to_ascii(hex_value: str):
    try:
        ascii_str = bytes.fromhex(hex_value).decode("ascii")
        ascii_str = ascii_str[::-1] # the string needs to be reversed, given the values are stored in reverse in the buffer.
    except ValueError:
        ascii_str = ""

    return ascii_str