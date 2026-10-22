"""Aimbot plugin — smooths cursor toward nearest enemy bone (educational)."""
from __future__ import annotations

import tkinter as tk

from src.plugins.contract import CheatPlugin


class AimbotPlugin(CheatPlugin):
    name = "aimbot"
    description = "Smooth aim assist toward head bone"

    def __init__(self, reader) -> None:
        super().__init__(reader)
        self.smoothing = 0.35
        self.fov_px = 220

    def render(self, canvas: tk.Canvas) -> None:
        canvas.create_oval(
            960 - self.fov_px, 540 - self.fov_px,
            960 + self.fov_px, 540 + self.fov_px,
            outline="#33aaff", width=1,
        )
        target = self._pick_target()
        if target:
            canvas.create_line(960, 540, target["screen_x"], target["screen_y"],
                               fill="#33aaff", width=2)

    def _pick_target(self) -> dict | None:
        players = [p for p in self.reader.read_player_list() if p.get("alive")]
        if not players:
            return None
        return min(players, key=lambda p: (p["screen_x"] - 960) ** 2 + (p["screen_y"] - 540) ** 2)