#!/usr/bin/env python3
'''
Virtual Memory Lab.

'''
__author__ = 'Alex DeCesare'
__version__ = '05-November-2020'


class VirtualMemory:
    '''This is the constructor for VirtualMemory objects:
    self._vmem_size_in_bytes, self._ram_size_in_bytes, and
    self._page_size_in_bytes are available to your methods as
    instance variables (aka "data members", aka "fields")
    '''
    def __init__(self, vmem_size_in_GiB, ram_size_in_GiB, page_size_in_KiB):
        self._vmem_size_in_bytes = vmem_size_in_GiB * 1024 * 1024 * 1024
        self._ram_size_in_bytes = ram_size_in_GiB * 1024 * 1024 * 1024
        self._page_size_in_bytes = page_size_in_KiB * 1024

    def num_pages(self):
        '''
        Calculates the number of pages.
        '''
        return self._vmem_size_in_bytes / self._page_size_in_bytes

    def num_page_frames(self):
        '''
        Calculates the number of page frames.
        '''
        return self._ram_size_in_bytes / self._page_size_in_bytes

    def start_address_of_page(self, page_num):
        '''
        Calculates the address of a page.
        '''
        return page_num * self._page_size_in_bytes

    def start_address_of_page_frame(self, page_frame_num):
        '''
        Calculates the start address of a page frame
        '''
        return page_frame_num * self._page_size_in_bytes

    def page_for_address(self, address):
        '''
        Calculates the address of a page
        '''
        return address // self._page_size_in_bytes

    def page_offset_for_address(self, address):
        '''
        Calculates the page offset for an address
        '''
        return address % self._page_size_in_bytes

    def page_frame_offset_for_address(self, address):
        '''
        Calculates the page frame offset for an address
        '''
        return address % self._page_size_in_bytes

    def translate_virtual_address_to_physical_address(self, vmem_address, page_frame_num):
        '''
        Converts a virtual address to a physical address
        '''
        return self.page_offset_for_address(vmem_address) + self.start_address_of_page_frame(page_frame_num)
