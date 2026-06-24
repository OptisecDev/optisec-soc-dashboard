# Optisec SOC Dashboard

A real-time Security Operations Center (SOC) web dashboard built with FastAPI. Visualizes network scan events collected by the [Optisec SOC Agent](https://github.com/OptisecDev/optisec-soc-agent) with a dark cybersecurity theme and Arabic/English bilingual support.

## Features

- **Live event table** — displays the 100 most recent scan events, newest first, auto-refreshing every 10 seconds
- **Summary statistics** — total events, threats detected, and networks monitored at a glance
- **Threat badges** — each event row is colour-coded: `CLEAN` (green) or `THREAT` (red)
- **Dark cyberpunk UI** — black/green terminal aesthetic with glowing accents
- **Arabic / English toggle** — full RTL layout switch with a single button
- **Optisec branding** — logo, live-monitoring indicator, and footer

## Project Structure

```
optisec-soc-dashboard/
├── main.py             # FastAPI application (API routes + static file serving)
├── static/
│   └── index.html      # Single-page dashboard (vanilla JS, no build step)
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10+
- A running [Optisec SOC Agent](https://github.com/OptisecDev/optisec-soc-agent) writing to `~/optisec-soc-agent/logs/events.json`

## Installation

```bash
git clone https://github.com/OptisecDev/optisec-soc-dashboard.git
cd optisec-soc-dashboard

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Running

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Then open **http://localhost:8000** in your browser.

## API Endpoints

| Method | Path          | Description                                      |
|--------|---------------|--------------------------------------------------|
| GET    | `/api/events` | Last 100 events from `events.json`, newest first |
| GET    | `/api/stats`  | Aggregate stats: total events, threats, networks |

## Configuration

The path to the events file is set at the top of `main.py`:

```python
EVENTS_FILE = Path.home() / "optisec-soc-agent" / "logs" / "events.json"
```

Change this if your agent writes logs to a different location.

## License

Proprietary — © 2026 Optisec. All rights reserved.
