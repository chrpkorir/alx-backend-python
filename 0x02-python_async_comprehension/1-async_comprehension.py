#!/usr/bin/env python3
""" Coroutine with comprehension. """

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Collect 10 random numbers and return them using comprehension """

    return [i async for i in async_generator()]
