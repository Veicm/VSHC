from typing import Callable, TypeVar, Any
import time
from functools import wraps

__all__ = ["measure_time"]

F = TypeVar("F", bound=Callable[..., Any])


def measure_time(func: F) -> F:
    """
    Measure the execution time of a function and print the duration.

    This decorator wraps a function, measures its execution time using
    time.perf_counter(), and prints the elapsed time to stdout.
    It is intended for debugging and development purposes only.

    This function is not suitable for production code, as printing to
    stdout and measuring execution time on every call introduces
    measurable overhead and can slightly slow down program execution.

    Example:
        @measure_time
        def add(a, b):
            return a + b

        add(2, 3)
        -> prints execution time
        -> returns 5

    Args:
        func (Callable[..., Any]):
            The function whose execution time should be measured.

    Returns:
        Callable[..., Any]:
            The wrapped function with execution time measurement.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start: float = time.perf_counter()
        result = func(*args, **kwargs)
        end: float = time.perf_counter()
        print(
            f"The function '{func.__name__}' took {end - start:.6f} seconds to execute."
        )
        return result

    return wrapper  # type: ignore
