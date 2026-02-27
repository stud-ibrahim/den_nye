# Coffee Shop demo

This document explains how to run the Coffee Shop notebook demo.

## Prerequisites

- Activate the project virtualenv: `source .venv/bin/activate`.
- Install dev/notebook deps: `pip install -e ".[dev,notebooks]"`.
- Ensure an MQTT broker is available (local Mosquitto or a cloud broker).

## Google Maps

- To use Google Maps tiles set the environment variable `GOOGLE_MAPS_API_KEY` to your key.
- If the key is not set the notebook falls back to OpenStreetMap tiles.

## Running the notebook

1. Open `notebooks/03_mqtt_random_walk/coffee_shop.ipynb`.
2. Run all cells (Cell → Run All).
3. The demo runs for ~30 seconds (100 steps × 0.3s).
4. Open `notebooks/03_mqtt_random_walk/map_viewer.ipynb` in another tab to see the live map.

## Running the script variant

Run the script from project root:

```
./.venv/bin/python scripts/demo/coffee_shop.py
```

## What happens

- 3 persons (`coffee-1`, `coffee-2`, `coffee-3`) walk randomly near City Hall
- Every 20 seconds it starts raining for 10 seconds
- Person markers turn red (`#ff0000`) during rain
- Rain state published on `weather/rain` topic
- Person locations published on `persons/{name}/location` topics

## Stopping

- In the notebook press Ctrl+C or stop the kernel.
- If running the script press Ctrl+C to stop.
