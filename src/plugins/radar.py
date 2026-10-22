"""Minimap radar plugin — renders a small enemy radar in the corner."""
from __future__ import annotations

import tkinter as tk

from src.plugins.contract import CheatPlugin

RADAR_SIZE = 180
RADAR_ORIGIN = (30, 30)


class RadarPlugin(CheatPlugin):
    name = "radar"
    description = "Corner radar with enemy bearings"

    def render(self, canvas: tk.Canvas) -> None:
        ox, oy = RADAR_ORIGIN
        canvas.create_oval(ox, oy, ox + RADAR_SIZE, oy + RADAR_SIZE,
                           outline="#00ff88", width=1)
        for p in self.reader.read_player_list():
            if not p.get("alive"):
                continue
            rx = ox + RADAR_SIZE // 2 + int(p.get("world_dx", 0) / 10)
            ry = oy + RADAR_SIZE // 2 + int(p.get("world_dy", 0) / 10)
            canvas.create_oval(rx - 2, ry - 2, rx + 2, ry + 2, fill="#ff3355", outline="")