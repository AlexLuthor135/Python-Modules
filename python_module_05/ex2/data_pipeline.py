#!/usr/bin/python3

from typing import Any
from typing import Protocol
import abc


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        result: list[str] = []
        for item in data:
            value: str = item[1]
            if any(char in value for char in [",", '"', "\n", "\r"]):
                value = value.replace('"', '""')
                value = f'"{value}"'
            result.append(value)
        print(",".join(result))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        result: list[str] = []
        for item in data:
            value: str = item[1].replace('\\', r'\\')
            value = value.replace('"', r'\"')
            value = value.replace('\n', r'\n')
            value = value.replace('\r', r'\r')
            value = value.replace('\t', r'\t')
            value = value.replace('\b', r'\b')
            value = value.replace('\f', r'\f')
            result.append(f'"item_{item[0]}": "{value}"')
        print('{', ", ".join(result), '}', sep="")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if nb <= 0:
            return
        for proc in self._processors:
            output: list[tuple[int, str]] = []
            outputs: int = min(nb, len(proc._data))
            for _ in range(outputs):
                output.append(proc.output())
            plugin.process_output(output)


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
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()
    print("Registering Processors")
    data_stream.register_processor(NumericProcessor())
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())
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
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CSVPlugin())
    print()
    data_stream.print_processors_stats()
    data = [
        21,
        ['I hate AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE',
          'log_message': 'Certificateexpires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    data_stream.process_stream(data)
    print()
    data_stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JSONPlugin())
    print()
    data_stream.print_processors_stats()
