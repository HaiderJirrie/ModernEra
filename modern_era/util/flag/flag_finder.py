import sys
from enum import Enum
from typing import List


class Flag(Enum):
    PREFIX = "flag{"
    SUFFIX = "}"


def __flag_found(flag: str):
    print(flag)
    sys.exit()


def search_for_flag_in_list(list: List[str]):
    flag = ""
    flag_prefix_index = None

    for index, list_item in enumerate(list):
        if not flag_prefix_index and list_item.find(Flag.PREFIX.value) >= 0:
            flag_prefix_index = index

        last_list_item_index = len(list) - 1

        if flag_prefix_index and flag_prefix_index <= last_list_item_index:
            flag_remainder = list[flag_prefix_index:last_list_item_index]

            for flag_part in flag_remainder:
                flag += flag_part

            suffix_index = flag.find(Flag.SUFFIX.value)

            if suffix_index >= 0:
                flag = flag[: suffix_index + 1]
                __flag_found(flag)
