"""YAML config loader with sensible defaults for the external cheat host."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class OverlayConfig:
    width: int = 1920
    height: int = 1080
    fps: int = 60
    transparent: bool = True
    font: str = "Consolas"


@dataclass
class HostConfig:
    target_process: str = "FreeFire.exe"
    offsets_file: str = "offsets/1.98.1.json"
    overlay: OverlayConfig = field(default_factory=OverlayConfig)
    enabled_plugins: list[str] = field(default_factory=lambda: ["esp", "aimbot"])


def load_config(path: str | Path) -> HostConfig:
    p = Path(path)
    if not p.exists():
        return HostConfig()
    raw = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    overlay = OverlayConfig(**raw.get("overlay", {}))
    return HostConfig(
        target_process=raw.get("target_process", "FreeFire.exe"),
        offsets_file=raw.get("offsets_file", "offsets/1.98.1.json"),
        overlay=overlay,
        enabled_plugins=raw.get("enabled_plugins", ["esp", "aimbot"]),
    )