"""ESP/wallhack plugin — draws boxes and health bars around enemies."""
from __future__ import annotations

import tkinter as tk

from src.overlay.draw_utils import draw_box, draw_health_bar, draw_snapline
from src.plugins.contract import CheatPlugin


class EspPlugin(CheatPlugin):
    name = "esp"
    description = "Wallhack ESP — boxes, health bars, snaplines"

    def render(self, canvas: tk.Canvas) -> None:
        players = self.reader.read_player_list()
        for p in players:
            if not p.get("alive", True):
                continue
            x, y = p["screen_x"], p["screen_y"]
            w, h = 40, 100
            draw_box(canvas, x - w // 2, y - h, w, h)
            draw_health_bar(canvas, x - w // 2, y - h - 8, w, 4, p.get("health", 100.0))
            draw_snapline(canvas, 960, 1080, x, y)