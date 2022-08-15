import re

from registrypol.values import RegistryValue


class RegistryPolicy():
    _header = b'\x50\x52\x65\x67\x01\x00\x00\x00'

    def __init__(self, *, values=[]):
        self.values = values

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        if isinstance(values, list):
            for value in values:
                if isinstance(value, RegistryValue):
                    pass
                else:
                    raise TypeError(f'invalid type for values element')
            self._values = values
        else:
            raise TypeError(f'invalid type for values')

    @classmethod
    def from_bytes(cls, bytes):
        values = []

        matches = re.findall(rb'(\x5b\x00.*?\x5d\x00)', bytes[len(cls._header):])

        for match in matches:
            values.append(RegistryValue.from_bytes(match))

        return cls(values=values)
    
    def to_bytes(self):
        return b'%b%b' % (self._header, b''.join([value.to_bytes() for value in self.values]))
