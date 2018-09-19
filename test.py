import unittest

from id_generator import IDGenerator


class IDGeneratorTest(unittest.TestCase):

    def test_default_with_initial(self):
        id_generator = IDGenerator(length=6, initial='01209v')
        targets = [
            '01209w',
            '01209x',
            '01209y',
            '01209z',
            '0120a0',
            '0120a1',
            '0120a2',
            '0120a3',
            '0120a4',
            '0120a5'
        ]
        results = []
        for i in range(10):
            results.append(id_generator.next())
        self.assertEqual(results, targets)

    def test_custom_length_and_chars(self):
        id_generator = IDGenerator(length=3, chars=['0', '1'])
        targets = ['001', '010', '011', '100', '101', '110', '111']
        results = []
        for i in range(7):
            results.append(id_generator.next())
        self.assertEqual(results, targets)

    def test_chinese_chars_with_initial(self):
        id_generator = IDGenerator(
            length=3,
            chars=['零', '一', '二', '三', '四', '五', '六', '七', '八', '九'],
            initial='一二零'
        )
        targets = [
            '一二一',
            '一二二',
            '一二三',
            '一二四',
            '一二五',
            '一二六',
            '一二七',
            '一二八',
            '一二九',
            '一三零'
        ]
        results = []
        for i in range(10):
            results.append(id_generator.next())
        self.assertEqual(results, targets)

    def test_id_out_of_range(self):
        with self.assertRaises(IDGenerator.IDOutOfRange):
            id_generator = IDGenerator(length=3, chars=['0', '1'])
            for i in range(10):
                id_generator.next()

    def test_duplicate_chars(self):
        with self.assertRaises(IDGenerator.DuplicateChars):
            IDGenerator(length=3, chars=['1', '2', '1'])

    def test_illegal_initial_length_mismatch(self):
        with self.assertRaises(IDGenerator.IllegalInitialID):
            IDGenerator(length=3, chars=['0', '1'], initial='11')

    def test_illegal_initial_chars_mismatch(self):
        with self.assertRaises(IDGenerator.IllegalInitialID):
            IDGenerator(length=3, chars=['0', '1'], initial='121')


if __name__ == '__main__':
    unittest.main()
