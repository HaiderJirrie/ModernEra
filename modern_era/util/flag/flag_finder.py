from enum import Enum
from typing import List


class Flag(Enum):
    PREFIX = "flag{"
    SUFFIX = "}"
    BYTES = 4


def find_flag_in_list(list: List[str]):
    flag_found = False
    flag_index = 0
    flag = ""

    for index, list_item in enumerate(list):
        if list_item.find(Flag.PREFIX.value) != -1:
            flag += list_item
            flag_index = index
            flag_found = True

        if flag_found and len(list) >= (flag_index + Flag.BYTES.value):
            remainder = list[flag_index + 1 : flag_index + Flag.BYTES.value]
            for part in remainder:
                flag += part
            return flag
