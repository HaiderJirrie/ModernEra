import re


def filter_hex_values(text: str):
    hex_pattern = r"\b0x[0-9a-fA-F]+\b|\b[0-9a-fA-F]+\b"
    return re.findall(hex_pattern, text)


def convert_hex_to_ascii(hex_value: str):
    try:
        ascii_str = bytes.fromhex(hex_value).decode("ascii")
    except ValueError:
        ascii_str = ""

    return ascii_str
