#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue 11 15:03:00 2024

@Author: Tinayo Keiya
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
