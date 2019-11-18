def type_error_message(name, bound_type):
    return 'Argument \'{}\' must be instance of \'{}\'.'.format(name, bound_type)


class IDGenerator:
    class CircleSet:

        def __init__(self, initial):
            self.__list = initial

        def next_of(self, char):
            index = self.__list.index(char) + 1
            carry = False
            if index == len(self.__list):
                index = 0
                carry = True
            return {
                'char': self.__list[index],
                'carry': carry
            }

        def get(self, index):
            return self.__list[index]

        def index(self, char):
            try:
                return self.__list.index(char)
            except ValueError:
                return -1

    def __init__(self, length, chars=None, initial=None):
        if not isinstance(length, int):
            raise TypeError(type_error_message('length', 'int'))
        if length < 1:
            raise ValueError('\'length\' must be positive.')
        if not chars:
            chars = self.__default_chars()
        else:
            if not isinstance(chars, list):
                raise TypeError(type_error_message('chars', 'list'))
            for i in range(0, len(chars) - 1):
                for j in range(i + 1, len(chars)):
                    if chars[i] == chars[j]:
                        raise self.DuplicateChars
        self.__chars = self.CircleSet(chars)
        self.__current_id = []
        self.__length = length
        if not initial:
            for i in range(length):
                self.__current_id.append(self.__chars.get(0))
        else:
            self.set_id(initial)

    @staticmethod
    def __default_chars():
        default_chars = []
        for char_ord in range(ord('0'), ord('9') + 1):
            default_chars.append(chr(char_ord))
        for char_ord in range(ord('a'), ord('z') + 1):
            default_chars.append(chr(char_ord))
        return default_chars

    def __next_char(self, index):
        current_char = self.__current_id[index]
        self.__current_id[index] = self.__chars.next_of(current_char)['char']
        return self.__chars.next_of(current_char)['carry']

    def next(self):
        carry = True
        for i in range(self.__length - 1, -1, -1):
            if carry:
                carry = self.__next_char(i)
        return {
            'id': self.get_id(),
            'carry': carry
        }

    def set_id(self, new_id):
        if not isinstance(new_id, str):
            raise TypeError(type_error_message('new_id', 'str'))
        id_list = list(new_id)
        if self.__length != len(id_list):
            raise self.IllegalIDFormat
        for i in range(0, self.__length):
            if self.__chars.index(id_list[i]) == -1:
                raise self.IllegalIDFormat
        self.__current_id = list(id_list)

    def get_id(self):
        return ''.join(self.__current_id)

    class DuplicateChars(Exception):
        pass

    class IllegalIDFormat(Exception):
        pass


class IDManager:

    def __init__(self):
        self.__id_set = []
        self.__separator_set = []
        self.__pattern = []
        self.__auto_increase = []

    def add_id(self, length, chars=None, initial=None, auto_increase=False):
        if not isinstance(auto_increase, bool):
            raise TypeError(type_error_message('auto_increase', 'bool'))
        self.__id_set.append(
            IDGenerator(length=length, chars=chars, initial=initial)
        )
        self.__pattern.append(True)
        self.__auto_increase.append(auto_increase)

    def add_separator(self, separator):
        if not isinstance(separator, str):
            raise TypeError(type_error_message('separator', 'str'))
        self.__separator_set.append(separator)
        self.__pattern.append(False)

    def next(self, index=None):
        if index is None:
            index = len(self.__id_set) - 1
        if not isinstance(index, int):
            raise TypeError(type_error_message('index', 'int'))
        if index < 0:
            raise ValueError('\'index\' must not be negative.')
        carry = False
        for i in range(index, -1, -1):
            if carry and self.__auto_increase[i] == True or i == index:
                carry = self.__id_set[i].next()['carry']
            else:
                break

    def set_id(self, index, new_id):
        if not isinstance(index, int):
            raise TypeError(type_error_message('index', 'int'))
        if index < 0:
            raise ValueError('\'index\' must not be negative.')
        self.__id_set[index].set_id(new_id)

    def get_id(self):
        tmp_id = ''
        id_index = 0
        separator_index = 0
        for i in range(0, len(self.__pattern)):
            if self.__pattern[i]:
                tmp_id += self.__id_set[id_index].get_id()
                id_index += 1
            else:
                tmp_id += self.__separator_set[separator_index]
                separator_index += 1
        return tmp_id
