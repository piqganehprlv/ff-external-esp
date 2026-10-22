"""Entry point for ff-external-esp. Boots the plugin host."""
from __future__ import annotations

import argparse
import sys

from loguru import logger

from src.core.config import load_config
from src.core.injector import ExternalInjector
from src.core.memory_reader import MemoryReader
from src.overlay.render_loop import OverlayLoop
from src.plugins.loader import PluginLoader
from src.plugins.registry import PluginRegistry


def build_host(config_path: str) -> int:
    cfg = load_config(config_path)
    logger.info("ff-external-esp starting, target={}", cfg.target_process)

    injector = ExternalInjector(cfg.target_process)
    if not injector.attach():
        logger.error("failed to attach to {}", cfg.target_process)
        return 1

    reader = MemoryReader(injector.handle, cfg.offsets_file)
    registry = PluginRegistry()
    loader = PluginLoader(registry, reader, cfg)
    loader.discover("src.plugins")

    overlay = OverlayLoop(cfg.overlay, registry)
    overlay.run()
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ff-external-esp")
    parser.add_argument("-c", "--config", default="config/default.yaml")
    parser.add_argument("--list-plugins", action="store_true")
    args = parser.parse_args(argv)

    if args.list_plugins:
        from src.plugins.registry import PluginRegistry
        for name in PluginRegistry.builtin_names():
            print(name)
        return 0

    return build_host(args.config)


if __name__ == "__main__":
    sys.exit(main())