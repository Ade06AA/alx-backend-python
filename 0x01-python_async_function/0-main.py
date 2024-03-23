#!/usr/bin/env python3

import asyncio
import time

wait_random = __import__('0-basic_async_syntax').wait_random

t = time.perf_counter()
print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(15)))
print(asyncio.run(wait_random(15)))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
print(f"{time.perf_counter() - t} time elaps")
