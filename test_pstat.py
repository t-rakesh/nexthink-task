import unittest
import multiprocessing
import sys
import os
from unittest import TestCase
from pstat import pstat
from parameterized import parameterized


class PstatTest(TestCase):
    TEST_PROC = 'java'

    def worker(self):
        # implementation to increase cpu usage
        # implementation to increase memory usage
        # implementation to increase open file counts
        # implementation to decrease memory usage
        print('inside worker: to be implemented')

    @classmethod
    def setUpClass(cls):
        cls.process = multiprocessing.Process()
        cls.process.start()
        # use this name to test metrics functionally
        cls.pname = cls.process.name

    @classmethod
    def tearDownClass(cls):
        cls.process.terminate()

    def setUp(self):
        sys.argv.clear()
        sys.argv.extend(['test_pstat.py'])

    def tearDown(self):
        p_files = os.listdir('.')
        for f in p_files:
            if f.endswith('.csv'):
                os.remove(f)

    def set_args(self, name, duration, interval):
        if name:
            sys.argv.extend(['-n', name])
        if duration:
            sys.argv.extend(['-d', duration])
        if interval:
            sys.argv.extend(['-i', interval])

    @parameterized.expand([
        [TEST_PROC, '2', '1'],
        [TEST_PROC, '2', '']
    ])
    def test_syntax_valid_args(self, name, duration, interval):
        self.set_args(name, duration, interval)
        pstat()

    def test_syntax_invalid_args(self):
        self.set_args('no_such_process', '2', '1')
        with self.assertRaises(Exception):
            pstat()

    @parameterized.expand([
        ['', '2', '1'],
        [TEST_PROC, '', '1']
    ])
    def test_syntax_missing_args(self, name, duration, interval):
        self.set_args(name, duration, interval)
        with self.assertRaises(SystemExit):
            pstat()

    def test_file_creation(self):
        self.set_args(self.TEST_PROC, '2', '1')
        pstat()
        created = False
        p_files = os.listdir('.')
        for f in p_files:
            if f.endswith('.csv') and f.startswith(self.TEST_PROC):
                created = True
        self.assertTrue(created, 'failed to create csv file')

    def test_file_content(self):
        pass

    def test_avg_calculation(self):
        pass

    def test_memory_leak(self):
        pass


if __name__ == '__main__':
    unittest.main()

