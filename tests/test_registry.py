"""Stub tests for the plugin registry."""
from src.plugins.contract import CheatPlugin
from src.plugins.registry import PluginRegistry


class DummyPlugin(CheatPlugin):
    name = "dummy"

    def render(self, canvas) -> None:
        pass


def test_register_and_activate() -> None:
    reg = PluginRegistry()
    p = DummyPlugin(reader=None)  # type: ignore[arg-type]
    reg.register(p)
    assert reg.get("dummy") is p
    assert reg.active() == []
    p.toggle()
    assert reg.active() == [p]


def test_builtin_names() -> None:
    names = PluginRegistry.builtin_names()
    assert "esp" in names and "aimbot" in names