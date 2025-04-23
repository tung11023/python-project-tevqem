import pytest
from src.utils import process_data

def test_process_data():
    data = process_data("dummy_path")
    assert len(data) == 100
