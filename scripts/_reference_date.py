"""Explicit fixture date for reproducible demo builds; wall clock otherwise."""
from datetime import date
import os


def reference_date() -> date:
    value = os.environ.get("OBSIDIAN_BRAIN_REFERENCE_DATE")
    return date.fromisoformat(value) if value else date.today()
