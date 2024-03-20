#!/usr/bin/env python3
from typing import Callable
"""
doc
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    doc
    """
    return lambda arg: multiplier * arg
