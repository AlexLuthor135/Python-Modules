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


class DataStream():
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            for proc in self._processors:
                if proc.validate(item):
                    proc.ingest(item)
                    break
            else:
                print(
                    "DataStream error - Can't process element in stream:",
                    item)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self._processors) == 0:
            print("No processor found, no data")
        else:
            for proc in self._processors:
                name = type(proc).__name__.replace("Processor", " Processor")
                print(
                    f"{name}: total {proc._counter} items processed, "
                    f"remaining {len(proc._data)} on processor"
                )


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
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()
    print("Registering Numeric Processor")
    data_stream.register_processor(NumericProcessor())
    data: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
        42,
        ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {data}")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()
    print("\nRegistering other data processors")
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())
    print("Send the same batch again")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()
    print("\nConsume some elements from the data processors:",
          "Numeric 3, Text 2, Log 1"
          )
    for proc in data_stream._processors:
        if isinstance(proc, NumericProcessor):
            for _ in range(3):
                proc.output()
        elif isinstance(proc, TextProcessor):
            for _ in range(2):
                proc.output()
        elif isinstance(proc, LogProcessor):
            for _ in range(1):
                proc.output()
    data_stream.print_processors_stats()
