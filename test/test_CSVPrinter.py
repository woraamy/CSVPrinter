import unittest
from speciallecture.CSVPrinter import CSVPrinter


class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        printer = CSVPrinter('test/sample.csv')
        line = printer.read()
        print(line)
        self.assertEqual(3, len(line))

    def test_read2(self):
        printer = CSVPrinter('test/sample.csv')
        line = printer.read()
        self.assertEqual("value2B", line[1][1])

    def test_read3(self):
        with self.assertRaises(FileNotFoundError):
            printer = CSVPrinter('nonexistent.csv')
            printer.read()

# def setUpModule():
#     print("Setting up the module...")
#
# def tearDownModule():
#     print("Tearing down the module...")
#
#
# class TestCSVPrinter(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print("Setting up the class...")
#
#     @classmethod
#     def tearDownClass(cls):
#         print("Tearing down the class...")
#
#     def setUp(self):
#         print("Setting up the test case...")
#
#     def tearDown(self):
#         print("Tearing down the test case...")
#
#     def test_read(self):
#         print("Running test_read... ")
#
#     def test_read2(self):
#         print("Running test_read2... ")


