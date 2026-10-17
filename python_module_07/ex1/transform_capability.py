from abc import ABC, abstractmethod


class TransformCapability(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
