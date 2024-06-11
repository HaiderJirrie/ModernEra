import sys
from util.flag.flag_template import FlagTemplate
from typing import List


class FlagFinder:

    def __init__(self):
        self._flag_template = FlagFinder.__get_flag_template()

    @property
    def flag_template(self):
        return self._flag_template

    @staticmethod
    def __get_flag_template() -> FlagTemplate:
        if len(sys.argv) > 3:
            return FlagTemplate(sys.argv[2], sys.argv[3])
        else:
            return FlagTemplate()

    @staticmethod
    def __flag_found(flag: str):
        print(flag)
        sys.exit()

    def search_for_flag_in_list(self, list: List[str]):
        flag_index = None
        
        for index, list_item in enumerate(list):
            flag = ""

            if not flag_index and list_item.find(self.flag_template.prefix) >= 0:
                flag_index = index

            last_list_item_index = len(list) - 1

            if flag_index and flag_index <= last_list_item_index:
                flag_remainder = list[flag_index:last_list_item_index]

                for flag_part in flag_remainder:
                    flag += flag_part

                prefix_index = list[index].find(self.flag_template.prefix)
                suffix_index = flag.find(self.flag_template.suffix)

                if suffix_index >= 0:
                    flag = flag[prefix_index : suffix_index + 1]
                    self.__flag_found(flag)
