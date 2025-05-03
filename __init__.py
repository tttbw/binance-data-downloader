"""
Binance Data Downloader - A command-line tool for downloading cryptocurrency data from Binance.
"""

from src.cli.cli import main as _main

__version__ = "0.1.0"


# Re-export the main function
def main():
    """Main entry point for the CLI application."""
    return _main()


__all__ = ["main"]
