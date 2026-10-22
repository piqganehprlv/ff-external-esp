"""Runtime registry mapping plugin names to instances."""
from __future__ import annotations

from src.plugins.contract import CheatPlugin


class PluginRegistry:
    _builtins = ["esp", "aimbot", "radar", "no_recoil"]

    def __init__(self) -> None:
        self._plugins: dict[str, CheatPlugin] = {}

    def register(self, plugin: CheatPlugin) -> None:
        self._plugins[plugin.name] = plugin

    def get(self, name: str) -> CheatPlugin | None:
        return self._plugins.get(name)

    def active(self) -> list[CheatPlugin]:
        return [p for p in self._plugins.values() if p.enabled]

    @classmethod
    def builtin_names(cls) -> list[str]:
        return list(cls._builtins)