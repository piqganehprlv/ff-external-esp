"""Plugin loader — discovers and instantiates CheatPlugin subclasses."""
from __future__ import annotations

import importlib
import inspect
import pkgutil

from loguru import logger

from src.core.config import HostConfig
from src.core.memory_reader import MemoryReader
from src.plugins.contract import CheatPlugin
from src.plugins.registry import PluginRegistry


class PluginLoader:
    def __init__(self, registry: PluginRegistry, reader: MemoryReader, cfg: HostConfig) -> None:
        self.registry = registry
        self.reader = reader
        self.cfg = cfg

    def discover(self, package: str) -> None:
        pkg = importlib.import_module(package)
        for mod_info in pkgutil.iter_modules(pkg.__path__):
            if mod_info.name in {"contract", "loader", "registry"}:
                continue
            module = importlib.import_module(f"{package}.{mod_info.name}")
            for _, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, CheatPlugin) and obj is not CheatPlugin:
                    plugin = obj(self.reader)
                    self.registry.register(plugin)
                    if plugin.name in self.cfg.enabled_plugins:
                        plugin.toggle()
                    logger.debug("loaded plugin {}", plugin.name)