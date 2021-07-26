"""Test file loading of eda_data.streams package."""
from edam_data.streams import tabular_stream


def test_tabular_stream():
    """Assert tabular_stream() yeilds TextIO tabular data containing EDAM terms."""
    term_count = 0
    with tabular_stream() as handle:
        for line in handle.readlines():
            fields = line.split('\t')
            if not fields[0].startswith('http://edamontology.org/'):
                continue
            term_count += 1

    assert term_count > 100
