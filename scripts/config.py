"""Path constants and configuration for the personal knowledge base."""

import json
from pathlib import Path
from datetime import datetime, timezone

# ── Paths ──────────────────────────────────────────────────────────────
ROOT_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT_DIR / "scripts"
HOOKS_DIR = ROOT_DIR / "hooks"
AGENTS_FILE = ROOT_DIR / "AGENTS.md"
REPORTS_DIR = ROOT_DIR / "reports"
STATE_FILE = SCRIPTS_DIR / "state.json"

# Load custom paths if available (for cross-project integration)
PATHS_CONFIG = ROOT_DIR / ".claude-paths.json"
if PATHS_CONFIG.exists():
    try:
        paths_config = json.loads(PATHS_CONFIG.read_text(encoding="utf-8"))
        DAILY_DIR = Path(paths_config.get("daily_dir", ROOT_DIR / "daily"))
        KNOWLEDGE_DIR = Path(paths_config.get("knowledge_dir", ROOT_DIR / "knowledge"))
        PROJECT_NAME = paths_config.get("project_name", "default")

        # Optional: custom wiki index and log paths
        INDEX_FILE = Path(paths_config.get("wiki_index", KNOWLEDGE_DIR / "index.md"))
        LOG_FILE = Path(paths_config.get("wiki_log", KNOWLEDGE_DIR / "log.md"))
    except (json.JSONDecodeError, OSError) as e:
        # Fall back to default paths
        DAILY_DIR = ROOT_DIR / "daily"
        KNOWLEDGE_DIR = ROOT_DIR / "knowledge"
        PROJECT_NAME = "default"
        INDEX_FILE = KNOWLEDGE_DIR / "index.md"
        LOG_FILE = KNOWLEDGE_DIR / "log.md"
else:
    # Default paths (original compiler behavior)
    DAILY_DIR = ROOT_DIR / "daily"
    KNOWLEDGE_DIR = ROOT_DIR / "knowledge"
    PROJECT_NAME = "default"
    INDEX_FILE = KNOWLEDGE_DIR / "index.md"
    LOG_FILE = KNOWLEDGE_DIR / "log.md"

CONCEPTS_DIR = KNOWLEDGE_DIR / "concepts"
CONNECTIONS_DIR = KNOWLEDGE_DIR / "connections"
QA_DIR = KNOWLEDGE_DIR / "qa"

# ── Timezone ───────────────────────────────────────────────────────────
TIMEZONE = "Europe/London"


def now_iso() -> str:
    """Current time in ISO 8601 format."""
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def today_iso() -> str:
    """Current date in ISO 8601 format."""
    return datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d")
