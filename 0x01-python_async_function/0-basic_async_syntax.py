#!/usr/bin/env python3
"""
module doc
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    func doc
    """
    delay: int
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
