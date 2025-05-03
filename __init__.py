"""
Binance Data Downloader - A command-line tool for downloading cryptocurrency data from Binance.
"""

__version__ = "0.1.0"

# Import the main function from the src package
from .src.cli.cli import main

__all__ = ["main"]
