import pytest
from src.lab3.file_handler import FileHandler


def test_write_read(tmp_path):
    fh = FileHandler(str(tmp_path / "test.txt"))
    fh.write("hello")
    assert fh.read() == "hello"


def test_append(tmp_path):
    fh = FileHandler(str(tmp_path / "test.txt"))
    fh.write("a\n")
    fh.append("b\n")
    assert fh.read() == "a\nb\n"


def test_delete(tmp_path):
    fh = FileHandler(str(tmp_path / "test.txt"))
    fh.write("x")
    assert fh.delete() is True
    assert fh.delete() is False


def test_read_missing(tmp_path):
    fh = FileHandler(str(tmp_path / "missing.txt"))
    with pytest.raises(FileNotFoundError):
        fh.read()