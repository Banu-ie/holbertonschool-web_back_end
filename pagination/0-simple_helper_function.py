#!/usr/bin/env python3
"""Module providing pagination helper functions."""


def index_range(page, page_size):
    """Return a tuple containing start and end indexes."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
