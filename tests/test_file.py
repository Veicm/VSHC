from pathlib import Path
from vshc.file import txt


def test_read_text_file(tmp_path: Path):
    test_content = "Hello Connor"
    file_path = tmp_path / "test.txt"

    file_path.write_text(test_content, encoding="utf-8")

    result = txt.read_text_file(file_path)

    assert result == test_content
