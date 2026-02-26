# Setup

This project targets **Python 3.11+**.

## Create and activate a virtual environment

macOS / Linux:

```bash
 python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```

Windows (PowerShell):

```powershell
 py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
```

If you get an execution policy error, run this once:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Install the library (editable) + workshop tools

```bash
pip install -e ".[dev,notebooks]"
```

## Optional: geospatial transforms (CRS)

If you plan to work with real-world coordinates, install the optional geospatial
extra to enable EPSG transforms.

Geo helpers live in `simulated_city.geo` and include convenience functions like
`wgs2utm(...)` / `utm2wgs(...)` plus the general `transform_xy(...)`.

```bash
pip install -e ".[geo]"
```

Tip: for notebooks that include both mapping + CRS transforms, you can install both extras:

```bash
pip install -e ".[notebooks,geo]"
```

## Set up a local MQTT broker (optional)

If you want to test MQTT locally before connecting to a public broker, install **Mosquitto**:

### macOS (using Homebrew)

```bash
brew install mosquitto
brew services start mosquitto
```

Verify it's running:

```bash
lsof -i :1883
```

You should see `mosquitto` listening on port 1883.

### Linux (Ubuntu/Debian)

```bash
sudo apt-get install mosquitto
sudo systemctl start mosquitto
```

### Windows

Download the installer from [mosquitto.org](https://mosquitto.org/download/) or use Windows Subsystem for Linux (WSL).

## Run notebooks

- VS Code: open a notebook in `notebooks/` and select the `.venv` kernel.
- Or start Jupyter:

```bash
jupyter lab
```

You can also run:

```bash
python -m jupyterlab
```

## Recommended learning path

1. Start with `notebooks/01_maps_and_coordinates.ipynb` to learn coordinate transforms
2. Move to `notebooks/02_mqtt_intro/` for MQTT basics:
   - `Broker_publisher.ipynb` — Publishing to local and public brokers
   - `Broker_subscriber.ipynb` — Subscribing to messages
3. Build your simulation using both concepts

## Run tests

```bash
python -m pytest
```
