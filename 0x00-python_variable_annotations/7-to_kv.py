#!/usr/bin/env python3
""" module for annotation work python"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        function to_kv that takes a string k and an int OR
        float v as arguments and returns a tuple.
    """
    return ((k, v**2))
