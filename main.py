import json
import os
from pathlib import Path
from datetime import datetime

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

EVENTS_FILE = Path.home() / "optisec-soc-agent" / "logs" / "events.json"

app = FastAPI(title="Optisec SOC Dashboard")


def load_events() -> list:
    if not EVENTS_FILE.exists():
        return []
    try:
        with open(EVENTS_FILE) as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


@app.get("/api/events")
def get_events():
    events = load_events()
    # Return last 100 events, newest first
    return JSONResponse(content=list(reversed(events[-100:])))


@app.get("/api/stats")
def get_stats():
    events = load_events()
    total_events = len(events)

    networks = set()
    threats = 0

    for event in events:
        for scan in event.get("scans", []):
            net = scan.get("network")
            if net:
                networks.add(net)
        threats += len(event.get("suspicious", []))

    last_updated = (
        events[-1].get("timestamp") if events else datetime.utcnow().isoformat() + "Z"
    )

    return {
        "total_events": total_events,
        "threats_detected": threats,
        "networks_monitored": len(networks),
        "last_updated": last_updated,
    }


app.mount("/", StaticFiles(directory=Path(__file__).parent / "static", html=True), name="static")
