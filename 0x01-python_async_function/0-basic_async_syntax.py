#!/usr/bin/env python3
"""
Basic asynchronous task
"""
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Co-routine that take in max_delay
    Returns the max_delay using random module
    """
    return random.uniform(0, max_delay)
