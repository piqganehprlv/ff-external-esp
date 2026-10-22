"""Shared contract every FreeFire cheat plugin must implement."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import tkinter as tk
    from src.core.memory_reader import MemoryReader


class CheatPlugin(ABC):
    name: str = "unnamed"
    description: str = ""

    def __init__(self, reader: MemoryReader) -> None:
        self.reader = reader
        self.enabled = False

    def toggle(self) -> None:
        self.enabled = not self.enabled

    @abstractmethod
    def render(self, canvas: "tk.Canvas") -> None:
        """Paint overlay for this frame."""