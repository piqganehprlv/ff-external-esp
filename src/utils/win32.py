"""Thin win32 helpers for window enumeration and DPI awareness."""
from __future__ import annotations

import ctypes

user32 = ctypes.windll.user32


def set_dpi_aware() -> None:
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:  # noqa: BLE001
        user32.SetProcessDPIAware()


def find_window(title: str) -> int:
    return user32.FindWindowW(None, title)


def foreground_window() -> int:
    return user32.GetForegroundWindow()