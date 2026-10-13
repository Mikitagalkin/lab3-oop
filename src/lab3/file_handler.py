"""Работа с файлами."""

from pathlib import Path


class FileHandler:
    def __init__(self, filepath: str, encoding: str = "utf-8"):
        self.filepath = Path(filepath)
        self.encoding = encoding

    def exists(self) -> bool:
        return self.filepath.exists()

    def write(self, content: str) -> None:
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        self.filepath.write_text(content, encoding=self.encoding)

    def append(self, content: str) -> None:
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(self.filepath, "a", encoding=self.encoding) as f:
            f.write(content)

    def read(self) -> str:
        if not self.exists():
            raise FileNotFoundError(f"Файл не найден: {self.filepath}")
        return self.filepath.read_text(encoding=self.encoding)

    def delete(self) -> bool:
        if self.exists():
            self.filepath.unlink()
            return True
        return False