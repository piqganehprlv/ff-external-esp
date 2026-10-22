"""Stub tests for config loading."""
from pathlib import Path

from src.core.config import HostConfig, load_config


def test_defaults_when_missing(tmp_path: Path) -> None:
    cfg = load_config(tmp_path / "nope.yaml")
    assert isinstance(cfg, HostConfig)
    assert cfg.target_process == "FreeFire.exe"


def test_parse_overlay(tmp_path: Path) -> None:
    f = tmp_path / "c.yaml"
    f.write_text("overlay:\n  width: 1280\n  height: 720\n  fps: 30\n", encoding="utf-8")
    cfg = load_config(f)
    assert cfg.overlay.width == 1280
    assert cfg.overlay.fps == 30
</final>
</final>