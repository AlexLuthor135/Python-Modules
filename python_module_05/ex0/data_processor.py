#!/usr/bin/python3

from typing import Any
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self._data: list[tuple[int, str]] = []
        self._counter: int = 0

    @abc.abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self._data.pop(0)


class NumericProcessor(DataProcessor):

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._data.append((self._counter, str(item)))
                self._counter += 1
            return
        self._data.append((self._counter, str(data)))
        self._counter += 1

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            if all(isinstance(item, (int, float)) for item in data):
                return True
        return False


class TextProcessor(DataProcessor):

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._data.append((self._counter, item))
                self._counter += 1
            return
        self._data.append((self._counter, data))
        self._counter += 1

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            if all(isinstance(item, str) for item in data):
                return True
        return False


class LogProcessor(DataProcessor):

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                values: str = f'{item["log_level"]}: {item["log_message"]}'
                self._data.append((self._counter, values))
                self._counter += 1
            return
        self._data.append(
            (self._counter, f'{data["log_level"]}: {data["log_message"]}')
        )
        self._counter += 1

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            if (all(isinstance(key, str)
                    and isinstance(value, str) for key, value in data.items())
                    and "log_level" in data
                    and "log_message" in data):
                return True
        if isinstance(data, list):
            if all(isinstance(item, dict) for item in data):
                for pair in data:
                    if (not all(
                        (isinstance(key, str)
                            and isinstance(value, str))
                            for key, value in pair.items())
                            or "log_level" not in pair
                            or "log_message" not in pair):
                        return False
                return True
        return False


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest('foo')
    except ValueError as e:
        print(f"Got exception: {e}")
    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    rank, value = numeric.output()
    print(f"Numeric value {rank}: {value}")
    rank, value = numeric.output()
    print(f"Numeric value {rank}: {value}")
    rank, value = numeric.output()
    print(f"Numeric value {rank}: {value}")
    print("\nTesting Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 1 value...")
    rank, value = text.output()
    print(f"Text value {rank}: {value}")
    print("\nTesting Log Processor...")
    log = LogProcessor()
    data: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    print(f"Processing data: {data}")
    log.ingest(data)
    print("Extracting 2 values...")
    rank, value = log.output()
    print(f"Log entry {rank}: {value}")
    rank, value = log.output()
    print(f"Log entry {rank}: {value}")
