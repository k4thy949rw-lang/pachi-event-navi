import json
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

path = Path(__file__).with_name("events.json")
data = json.loads(path.read_text(encoding="utf-8"))
if not isinstance(data.get("events"), list):
    raise ValueError("events must be a list")
for event in data["events"]:
    for field in ("shop", "date", "pref", "city", "type", "detail", "source", "confidence"):
        if not event.get(field):
            raise ValueError(f"missing {field}")
    datetime.strptime(event["date"], "%Y-%m-%d")
    if event["pref"] not in ("奈良県", "大阪府"):
        raise ValueError("invalid prefecture")
    if not event["source"].startswith("https://"):
        raise ValueError("source must use https")
# Validation only. Never misrepresent this run as an event-source verification.
print(f"Validated {len(data['events'])} events at {datetime.now(ZoneInfo('Asia/Tokyo')).isoformat()}")
