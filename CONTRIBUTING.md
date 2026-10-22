# Contributing to ff-external-esp

Thanks for your interest in this educational FreeFire external cheat research project.

## Ground rules

- Everything in this repo is **for educational and reverse-engineering research purposes only**.
- Do not submit offsets for live/competitive matches.
- No obfuscated binaries. All modules must be readable Python.
- No requests to add "undetected" guarantees — this is a study repo, not a service.

## Adding a plugin

1. Drop a new module under `src/plugins/` that subclasses `CheatPlugin`.
2. Register it in `src/plugins/registry.py`.
3. Provide a matching stub test in `tests/`.

## Style

- Black + ruff, line length 100.
- Type hints on all public functions.
- Log through `loguru`, never `print`.

## Pull requests

Include a short description of what the plugin demonstrates and which FreeFire
client version it targets (for documentation purposes).