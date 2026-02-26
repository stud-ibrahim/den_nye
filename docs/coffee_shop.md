# Coffee Shop demo

This document explains how to run the Coffee Shop notebook demo.

Prerequisites
- Activate the project virtualenv: `source .venv/bin/activate`.
- Install dev/notebook deps: `pip install -e ".[dev,notebooks]"`.
- Ensure an MQTT broker is available (local Mosquitto or a cloud broker).

Google Maps
- To use Google Maps tiles set the environment variable `GOOGLE_MAPS_API_KEY` to your key.
- If the key is not set the notebook falls back to OpenStreetMap tiles.

Running the notebook
1. Open `notebooks/03_mqtt_random_walk/coffee_shop.ipynb`.
2. Run the cells top-to-bottom. Run the `publish_demo(...)` cell manually to start publishing demo messages.

Running the script variant
- Alternatively run the script demo from project root (venv recommended):
```
./.venv/bin/python scripts/demo/coffee_shop.py
```

Stopping
- In the notebook call `stop_demo()` to disconnect.
- If running the script press Ctrl+C to stop.
