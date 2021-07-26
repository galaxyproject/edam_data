"""Return text streams to EDAM data.

Keep parsing and such to minimum to maintain maximum backward compatibility.
"""
from importlib.resources import open_text
from typing import TextIO


def tabular_stream() -> TextIO:
    """Yield EDAM data in TSV format as a Python UTF-8 encoded text stream."""
    return open_text("edam_data", 'EDAM.tsv')
