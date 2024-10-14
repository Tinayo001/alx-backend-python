#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Octo 10 14:29:00 2024

@Author: Tinayo Keiya
"""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns a coroutine that waits a random number of seconds"""
    delays = []
    tasks = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
