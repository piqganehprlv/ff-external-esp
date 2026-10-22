"""Helpers for drawing ESP boxes, health bars and skeleton lines."""
from __future__ import annotations

import tkinter as tk


def draw_box(canvas: tk.Canvas, x: int, y: int, w: int, h: int, color: str = "#00ff88") -> None:
    canvas.create_rectangle(x, y, x + w, y + h, outline=color, width=1)


def draw_health_bar(canvas: tk.Canvas, x: int, y: int, w: int, h: int, hp: float) -> None:
    canvas.create_rectangle(x, y, x + w, y + h, outline="#ffffff")
    fill = int(w * max(0.0, min(hp, 100.0)) / 100.0)
    canvas.create_rectangle(x, y, x + fill, y + h, fill="#ff3355", outline="")


def draw_snapline(canvas: tk.Canvas, x1: int, y1: int, x2: int, y2: int) -> None:
    canvas.create_line(x1, y1, x2, y2, fill="#00ff88", width=1)