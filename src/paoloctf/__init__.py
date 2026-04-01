"""paoloctf - CLI tool for creating and managing CTF challenges for PascalCTF."""

__version__ = "0.1.2"
__author__ = "Paolo"

from .generator import Generator
from .loader import Loader

__all__ = ["Generator", "Loader", "__version__"]
