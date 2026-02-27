from vshc.decorator.timing import measure_time


def test_measure_time(capsys):
    @measure_time
    def multiply(a: int, b: int) -> int:
        return a * b

    result = multiply(3, 4)

    captured = capsys.readouterr()

    assert result == 12
    assert "multiply" in captured.out
    assert "seconds" in captured.out
