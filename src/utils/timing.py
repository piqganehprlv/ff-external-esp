"""Frame timing helpers used by the overlay loop."""
from __future__ import annotations

import time
from contextlib import contextmanager


@contextmanager
def frame_budget(fps: int):
    start = time.perf_counter()
    yield
    target = 1.0 / fps
    elapsed = time.perf_counter() - start
    if elapsed < target:
        time.sleep(target - elapsed)