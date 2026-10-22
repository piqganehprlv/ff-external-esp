"""No-recoil plugin — zeroes weapon recoil offsets by patching the local view."""
from __future__ import annotations

import tkinter as tk

from src.plugins.contract import CheatPlugin


class NoRecoilPlugin(CheatPlugin):
    name = "no_recoil"
    description = "Zero out recoil / spread values in weapon struct"

    def render(self, canvas: tk.Canvas) -> None:
        # No visual — this plugin only mutates local weapon state via reader.
        state = self.reader.offsets.get("weapon", {})
        if not state:
            canvas.create_text(20, 20, text="no_recoil: offsets missing", fill="#ff3355")