class IDGenerator:

    class CircleUniqueList:

        def __init__(self, initial):
            self.list = initial

        def next_of(self, char):
            index = self.list.index(char) + 1
            carry = False
            if index == len(self.list):
                index = 0
                carry = True
            return {
                'char': self.list[index],
                'carry': carry
            }

        def get(self, index):
            return self.list[index]

        def index(self, char):
            try:
                return self.list.index(char)
            except ValueError:
                return -1

    def __init__(self, length, chars=None, initial=None):
        if not chars:
            chars = self.__default_chars()
        else:
            for i in range(0, len(chars) - 1):
                for j in range(i + 1, len(chars)):
                    if chars[i] == chars[j]:
                        raise self.DuplicateChars
        self.chars = self.CircleUniqueList(chars)
        self.current_id = list()
        self.length = length
        if not initial:
            for i in range(length):
                self.current_id.append(self.chars.get(0))
        else:
            self.set_id(initial)

    @staticmethod
    def __default_chars():
        default_chars = list()
        for char_ord in range(ord('0'), ord('9') + 1):
            default_chars.append(chr(char_ord))
        for char_ord in range(ord('a'), ord('z') + 1):
            default_chars.append(chr(char_ord))
        return default_chars

    def __next_char(self, index):
        current_char = self.current_id[index]
        self.current_id[index] = self.chars.next_of(current_char)['char']
        return self.chars.next_of(current_char)['carry']

    def next(self):
        carry = True
        for i in range(self.length - 1, -1, -1):
            if carry:
                carry = self.__next_char(i)
        if carry:
            raise self.IDOutOfRange
        return self.get_id()

    def set_id(self, new_id):
        id_list = list(new_id)
        if self.length != len(id_list):
            raise self.IllegalInitialID
        for i in range(0, self.length):
            if self.chars.index(id_list[i]) == -1:
                raise self.IllegalInitialID
        self.current_id = list(id_list)

    def get_id(self):
        return ''.join(self.current_id)

    class DuplicateChars(Exception):
        pass

    class IllegalInitialID(Exception):
        pass

    class IDOutOfRange(Exception):
        pass
