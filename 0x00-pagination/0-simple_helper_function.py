#!/usr/bin/env python3
"""index_range function"""


def index_range(page, page_size):
	"""
	The function should return a tuple of size two containing a start
	index and an end index corresponding to the 
	range of indexes to return in a list for those particular pagination parameters.
	"""
	return ((page * page_size) - page_size, page * page_size)