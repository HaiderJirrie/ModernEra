from util.validate_path import get_valid_path
from util.change_directory import change_working_dir
from analysis.import_analysis import analyse_imports
from exploits.string_format_attack import StringFormatAttack
from exploits.buffer_overflow_attack import BufferOverflowAttack

class ModernEra:
    def __init__(self):
        self._path = get_valid_path()
        self._exploits = [StringFormatAttack(), BufferOverflowAttack()]

    @property
    def path(self):
        return self._path

    @property
    def exploits(self):
        return self._exploits

    def start(self):
        change_working_dir(self.path)
        analyse_imports(self.path, self.exploits)

        for exploit in self.exploits:
            if len(exploit.found_vulnerable_functions) > 0:
                exploit.attempt_exploit(self.path)
