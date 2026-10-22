"""Overlay render loop — paints ESP boxes and aimbot FOV via customtkinter canvas."""
from __future__ import annotations

import time

import customtkinter as ctk
from loguru import logger

from src.core.config import OverlayConfig
from src.plugins.registry import PluginRegistry


class OverlayLoop:
    def __init__(self, cfg: OverlayConfig, registry: PluginRegistry) -> None:
        self.cfg = cfg
        self.registry = registry
        self.root = ctk.CTk()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        if cfg.transparent:
            self.root.attributes("-transparentcolor", "black")
        self.root.geometry(f"{cfg.width}x{cfg.height}+0+0")
        self.root.configure(fg_color="black")
        self.canvas = ctk.CTkCanvas(self.root, width=cfg.width, height=cfg.height,
                                    bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

    def _tick(self) -> None:
        self.canvas.delete("all")
        for plugin in self.registry.active():
            try:
                plugin.render(self.canvas)
            except Exception as exc:  # noqa: BLE001
                logger.error("plugin {} render failed: {}", plugin.name, exc)
        self.root.after(int(1000 / self.cfg.fps), self._tick)

    def run(self) -> None:
        logger.info("overlay started {}x{}@{}", self.cfg.width, self.cfg.height, self.cfg.fps)
        self._tick()
        self.root.mainloop()

    def stop(self) -> None:
        time.sleep(0)
        self.root.destroy()