"""Read-and-cache module bases and pointer chains for the FreeFire client."""
from __future__ import annotations

import json
from pathlib import Path

from loguru import logger

from src.core.injector import ExternalInjector


class MemoryReader:
    def __init__(self, handle: int, offsets_file: str) -> None:
        self.handle = handle
        self.offsets = self._load_offsets(offsets_file)
        self._cache: dict[str, int] = {}

    @staticmethod
    def _load_offsets(path: str) -> dict:
        p = Path(path)
        if not p.exists():
            logger.warning("offsets file {} missing, using empty map", path)
            return {}
        return json.loads(p.read_text(encoding="utf-8"))

    def module_base(self, module: str) -> int:
        if module not in self._cache:
            import pymem.process
            base = pymem.process.module_from_name(self.handle, module).lpBaseOfDll
            self._cache[module] = base
        return self._cache[module]

    def resolve(self, chain: list[int], base: int | None = None) -> int:
        import pymem
        addr = base if base is not None else self.module_base("GameCore.dll")
        for off in chain:
            addr = pymem.read_longlong(self.handle, addr) + off
        return addr

    def read_player_list(self) -> list[dict]:
        """Placeholder: real implementation lives in esp plugin."""
        return []