from id_generator import IDGenerator, type_error_message


class IDManager:

    def __init__(self, auto_increase=False):
        if not isinstance(auto_increase, bool):
            raise TypeError(type_error_message('auto_increase', 'bool'))
        self.__id_set = []
        self.__separator_set = []
        self.__pattern = []
        self.__auto_increase = auto_increase

    def add_id(self, id_generator):
        if not isinstance(id_generator, IDGenerator):
            raise TypeError(type_error_message('id_generator', 'IDGenerator'))
        self.__id_set.append(id_generator)
        self.__pattern.append(True)

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
        if self.__auto_increase:
            carry = True
            for i in range(index, -1, -1):
                if carry:
                    carry = self.__id_set[i].next()['carry']
        else:
            self.__id_set[index].next()

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
