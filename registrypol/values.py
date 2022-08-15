class RegistryValue():
    _types = {
        'REG_NONE': 0,
        'REG_SZ': 1,
        'REG_EXPAND_SZ': 2,
        'REG_BINARY': 3,
        'REG_DWORD': 4,
        'REG_DWORD_LITTLE_ENDIAN': 4,
        'REG_DWORD_BIG_ENDIAN': 5,
        'REG_LINK': 6,
        'REG_MULTI_SZ': 7,
        'REG_QWORD': 11,
        'REG_QWORD_LITTLE_ENDIAN': 11
    }

    def __init__(self, *, key, value, type, size, data):
        self.key = key
        self.value = value
        self.type = type
        self.size = size
        self.data = data

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        if isinstance(key, str):
            self._key = key
        else:
            raise TypeError(f'invalid type for key')

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            raise TypeError(f'invalid type for value')

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, int):
            self._type = type
        elif isinstance(type, str):
            if type in self._types:
                self._type = self._types[type]
            else:
                raise ValueError(f'invalid value for type')
        else:
            raise TypeError(f'invalid type for type')

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            raise TypeError(f'invalid type for size')

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        if isinstance(data, bytes):
            self._data = data
        else:
            raise TypeError(f'invalid type for data')

    @classmethod
    def from_bytes(cls, bytes):
        key, value, type, size, data = bytes[2:-2].split(b'\x3b\x00')

        return cls(
            key=key.decode('utf-16-le'),
            value=value.decode('utf-16-le'),
            type=int.from_bytes(type, 'little'),
            size=int.from_bytes(size, 'little'),
            data=data
        )

    def to_bytes(self):
        return b'\x5b\x00%b\x3b\x00%b\x3b\x00%b\x3b\x00%b\x3b\x00%b\x5d\x00' % (
            self.key.encode('utf-16-le'),
            self.value.encode('utf-16-le'),
            self.type.to_bytes(4, 'little'),
            self.size.to_bytes(4, 'little'),
            self.data
        )
