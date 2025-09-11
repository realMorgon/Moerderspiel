from typing import Iterable
from pathlib import Path

def find_root(start: Path | None = None, markers: Iterable[str]=("README.md","LICENCE")) -> Path:
    start = (start or Path(__file__)).resolve()
    low_dir = start if start.is_dir() else start.parent
    for cur in [low_dir, *low_dir.parents]:
        for marker in markers:
            if (cur / marker).exists():
                return cur
    return Path(__file__).resolve().parent

DATA = find_root() / "data"
USER_DATA = DATA / "user"
SESSION_DATA = DATA / "session"

def ensure_dirs() -> None:
    for dir in (USER_DATA, SESSION_DATA):
        dir.mkdir(parents=True, exist_ok=True)