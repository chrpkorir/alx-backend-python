#!/usr/bin/env python3
""" A coroutine that takes no arguments. """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Loops 10 times asynchronously, yields a random number"""

    for i in range(10):
        yield random.random()
        await asyncio.sleep(1)
