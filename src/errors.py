"""Fehler für zu hohe oder zu niedrige Eingaben"""

class OutOfRangeError(Exception):
    """Fehler für zu hohe oder zu niedrige Eingaben"""
    def __init__(self, value: int, minValue: int, maxValue: int) -> None:
        self._value = value
        self._min = minValue
        self._max = maxValue

    def __str__(self):
        return f"{self._value} is out of the Possible Range ({self._min+1}-{self._max+1})"
