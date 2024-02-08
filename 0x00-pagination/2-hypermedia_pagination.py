#!/usr/bin/env python3
"""document"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page, page_size):
        """
            The function should return a tuple of size two containing a start
            index and an end index corresponding to the
            range of indexes to return in a list for those particular parameter
        """
        return ((page * page_size) - page_size, page * page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            get page function
        """
        assert isinstance(
            page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(
            page_size, int) and page_size > 0, "Page size must be a\
                positive integer."
        tup = self.index_range(page, page_size)
        return self.dataset()[tup[0]:tup[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """get hyper function"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
