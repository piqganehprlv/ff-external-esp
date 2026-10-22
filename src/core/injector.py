"""External injector — attaches to FreeFire.exe for read-only memory access."""
from __future__ import annotations

import ctypes
from ctypes import wintypes

import pymem
from loguru import logger

PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010


class ExternalInjector:
    """Attaches to the FreeFire process for external (non-injected) reads."""

    def __init__(self, process_name: str) -> None:
        self.process_name = process_name
        self.handle: int | None = None
        self.pm: pymem.Pymem | None = None

    def attach(self) -> bool:
        try:
            self.pm = pymem.Pymem(self.process_name)
            self.handle = self.pm.process_handle
            logger.success("attached to {} pid={}", self.process_name, self.pm.process_id)
            return True
        except pymem.exception.ProcessNotFound:
            logger.warning("{} not running", self.process_name)
            return False
        except Exception as exc:  # noqa: BLE001
            logger.exception("attach failed: {}", exc)
            return False

    def close(self) -> None:
        if self.pm is not None:
            self.pm.close_process()
            self.pm = None
            self.handle = None