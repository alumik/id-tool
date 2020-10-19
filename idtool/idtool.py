import typing


def type_error(var_name: str, bound_type: str) -> str:
    return f"Argument '{var_name}' must be an instance of '{bound_type}'."


class IDGenerator:

    def __init__(self, length: int = None, chars: typing.Sequence = None, initial: str = None):
        if length is not None:
            if not isinstance(length, int):
                raise TypeError(type_error('length', 'int'))
            if length < 1:
                raise ValueError("'length' must be positive.")
        if not chars:
            chars = self._default_chars()
        else:
            if not isinstance(chars, typing.Sequence):
                raise TypeError(type_error('chars', 'typing.Sequence'))
            if len(chars) != len(set(chars)):
                raise self.DuplicateChars

        self._chars = chars
        self._len_chars = len(chars)
        self._length = length
        self._state = []
        if not initial:
            self._state = [0]
        else:
            self.set_id(initial)

    @staticmethod
    def _default_chars() -> typing.Sequence:
        default_chars = []
        for char_ord in range(ord('0'), ord('9') + 1):
            default_chars.append(chr(char_ord))
        for char_ord in range(ord('a'), ord('z') + 1):
            default_chars.append(chr(char_ord))
        return default_chars

    def next(self) -> bool:
        carry = True
        for i in range(len(self._state) - 1, -1, -1):
            if carry:
                self._state[i] += 1
            if self._state[i] >= self._len_chars:
                self._state[i] = 0
                carry = True
            else:
                carry = False
                break
        if carry:
            if self._length is not None and len(self._state) == self._length:
                return True
            self._state = [1] + self._state
        return False

    def set_id(self, new_id: str):
        if not isinstance(new_id, str):
            raise TypeError(type_error('new_id', 'str'))
        if self._length is not None and self._length != len(new_id):
            raise self.IllegalIDFormat
        for c in new_id:
            if c not in self._chars:
                raise self.IllegalIDFormat

        new_id = new_id.lstrip(self._chars[0])
        if len(new_id) == 0:
            new_id = self._chars[0]
        self._state = []
        for c in new_id:
            self._state.append(self._chars.index(c))

    def get_id(self) -> str:
        current_id = ''
        for i in self._state:
            current_id += self._chars[i]
        if self._length is not None:
            current_id = current_id.rjust(self._length, self._chars[0])
        return current_id

    class DuplicateChars(Exception):
        pass

    class IllegalIDFormat(Exception):
        pass


class IDManager:

    def __init__(self):
        self._id_set = []
        self._separator_set = []
        self._pattern = []
        self._auto_increase = []

    def add_id(self, generator: IDGenerator, auto_increase: bool = False):
        if not isinstance(generator, IDGenerator):
            raise TypeError(type_error('generator', 'idtool.IDGenerator'))
        if not isinstance(auto_increase, bool):
            raise TypeError(type_error('auto_increase', 'bool'))

        self._id_set.append(generator)
        self._pattern.append(True)
        self._auto_increase.append(auto_increase)

    def add_separator(self, separator: str):
        if not isinstance(separator, str):
            raise TypeError(type_error('separator', 'str'))

        self._separator_set.append(separator)
        self._pattern.append(False)

    def next(self, index: int = None):
        if index is None:
            index = len(self._id_set) - 1
        if not isinstance(index, int):
            raise TypeError(type_error('index', 'int'))
        if index < 0:
            raise ValueError('\'index\' must be greater than or equal to 0.')

        carry = False
        for i in range(index, -1, -1):
            if carry and self._auto_increase[i] or i == index:
                carry = self._id_set[i].next()
            else:
                break

    def set_id(self, index: int, new_id: str):
        if not isinstance(index, int):
            raise TypeError(type_error('index', 'int'))
        if index < 0:
            raise ValueError('\'index\' must be greater than or equal to 0.')

        self._id_set[index].set_id(new_id)

    def get_id(self) -> str:
        current_id = ''
        id_index = 0
        separator_index = 0
        for p in self._pattern:
            if p:
                current_id += self._id_set[id_index].get_id()
                id_index += 1
            else:
                current_id += self._separator_set[separator_index]
                separator_index += 1
        return current_id
