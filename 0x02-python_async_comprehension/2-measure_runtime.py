#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Octo 15 15:34:00 2024

@Author: Tinayo Keiya
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of async_comprehension"""
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.time()

    total_time = end_time - start_time
    return total_time
