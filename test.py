# TODO: 简化测试案例
# TODO: 修改文档

import unittest

from id_manager import IDManager, IDGenerator


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
            results.append(id_generator.next()['id'])
        self.assertEqual(targets, results)

    def test_custom_length_and_chars(self):
        id_generator = IDGenerator(length=3, chars=['0', '1'])
        targets = ['001', '010', '011', '100', '101', '110', '111']
        results = []
        for i in range(7):
            results.append(id_generator.next()['id'])
        self.assertEqual(targets, results)

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
            results.append(id_generator.next()['id'])
        self.assertEqual(targets, results)

    def test_id_with_carry(self):
        id_generator = IDGenerator(length=2, chars=['0', '1'], initial='10')
        self.assertFalse(id_generator.next()['carry'])
        self.assertTrue(id_generator.next()['carry'])

    def test_duplicate_chars(self):
        with self.assertRaises(IDGenerator.DuplicateChars):
            IDGenerator(length=3, chars=['1', '2', '1'])

    def test_illegal_initial_length_mismatch(self):
        with self.assertRaises(IDGenerator.IllegalIDFormat):
            IDGenerator(length=3, chars=['0', '1'], initial='11')

    def test_illegal_initial_chars_mismatch(self):
        with self.assertRaises(IDGenerator.IllegalIDFormat):
            IDGenerator(length=3, chars=['0', '1'], initial='121')

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            IDGenerator(length=0, chars=['0', '1'], initial='121')

    def test_type_error_length(self):
        with self.assertRaises(TypeError):
            IDGenerator(length='3', chars=['0', '1'], initial='121')

    def test_type_error_chars(self):
        with self.assertRaises(TypeError):
            IDGenerator(length=3, chars='12', initial='121')

    def test_type_error_initial(self):
        with self.assertRaises(TypeError):
            IDGenerator(length=3, chars=['0', '1'], initial=12)


class IDManagerTest(unittest.TestCase):

    def setUp(self):
        self.id_manager = IDManager()
        self.id_manager.add_id(length=2, chars=['0', '1'], auto_increase=True)
        self.id_manager.add_id(length=2, chars=['0', '1'], initial='11')
        self.id_manager.add_separator('/')
        self.id_manager.add_id(
            length=2,
            chars=['0', '1'],
            auto_increase=True,
            initial='11'
        )
        self.id_manager.add_separator('/')
        self.id_manager.add_id(
            length=2,
            chars=['0', '1'],
            auto_increase=True,
            initial='11'
        )
        self.id_manager.add_separator('-')
        self.id_manager.add_id(length=2, chars=['0', '1'], initial='11')

    def test_get_id(self):
        self.assertEqual('0011/11/11-11', self.id_manager.get_id())

    def test_set_id(self):
        self.id_manager.set_id(1, '10')
        self.assertEqual('0010/11/11-11', self.id_manager.get_id())

    def test_next_auto_increase_default(self):
        self.id_manager.next()
        self.assertEqual('0011/00/00-00', self.id_manager.get_id())

    def test_next_auto_increase_not_default(self):
        self.id_manager.next(3)
        self.assertEqual('0011/00/00-11', self.id_manager.get_id())

    def test_next_not_auto_increase(self):
        self.id_manager.next(1)
        self.assertEqual('0100/11/11-11', self.id_manager.get_id())


if __name__ == '__main__':
    unittest.main()
