#!/usr/bin/env python3
'''
Ensures correct functionality of the VirtualMemory class.
'''
import unittest
from vmem import *

class VirtualMemoryTests(unittest.TestCase):
    '''
        Ensures correct functionality of the VirtualMemory class.
    '''
    def setUp(self):
        self.vmem = VirtualMemory(16, 128/1024, 4)

    def test_num_pages(self):
        self.assertEqual(4194304, self.vmem.num_pages())

    def test_num_page_frames(self):
        self.assertEqual(32768, self.vmem.num_page_frames())

    def test_start_address_of_page(self):
        self.assertEqual(1130496, self.vmem.start_address_of_page(276))

    def test_start_address_of_page_frame(self):
        self.assertEqual(1130496, self.vmem.start_address_of_page_frame(276))

    def test_page_for_address(self):
        self.assertEqual(74565, self.vmem.page_for_address(305419896))

    def test_page_offset_for_address(self):
        self.assertEqual(1656, self.vmem.page_offset_for_address(305419896))

    def test_page_frame_offset_for_address(self):
        self.assertEqual(1656, self.vmem.page_frame_offset_for_address(305419896))

    def test_translate_virtual_address_to_physical_address(self):
        self.assertEqual(0x00B1DF2C, self.vmem.translate_virtual_address_to_physical_address(0x048B3F2C, 2845))

if __name__ == '__main__':
    unittest.main()
