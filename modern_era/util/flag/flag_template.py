from enum import Enum


class DefaultFlag(Enum):
    PREFIX = "flag{"
    SUFFIX = "}"


class FlagTemplate:

    def __init__(
        self, prefix=DefaultFlag.PREFIX.value, suffix=DefaultFlag.SUFFIX.value
    ):
        self._prefix = prefix
        self._suffix = suffix

    @property
    def prefix(self):
        return self._prefix

    @property
    def suffix(self):
        return self._suffix
