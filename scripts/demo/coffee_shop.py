"""Demo: Coffee shop simulation that publishes MQTT person location messages.

- Simulates 5 people walking around a central square.
- When it rains, people move into random coffee shops.
- Publishes person location JSON to `persons/{name}/location`.
- Publishes rain state to `weather/rain`.

Run with:
    python scripts/demo/coffee_shop.py

Requires project environment (paho-mqtt installed and config.yaml pointing to broker).
"""

import time
import random
import json
import signal
import sys
from datetime import datetime

from simulated_city.config import load_config
from simulated_city.mqtt import MqttConnector, MqttPublisher

CITY_HALL = (12.5683, 55.6761)

NAMES = ["alice", "bob", "carol"]
COLORS = ["red", "green", "blue"]

COFFEE_SHOPS = [
    (12.5678, 55.6765),
    (12.5687, 55.6759),
    (12.5690, 55.6763),
    (12.5680, 55.6760),
]

RUNNING = True

def _now_ts():
    return datetime.utcnow().timestamp()


def make_person_payload(name, lng, lat, color):
    return json.dumps({
        "name": name,
        "lng": float(lng),
        "lat": float(lat),
        "color": color,
        "timestamp": _now_ts(),
    })


def main(publish_interval: float = 1.0):
    global RUNNING

    cfg = load_config()
    connector = MqttConnector(cfg.mqtt, client_id_suffix="coffee-shop-demo")
    connector.connect()
    if not connector.wait_for_connection(timeout=5.0):
        print("Failed to connect to MQTT broker; exiting.")
        return

    publisher = MqttPublisher(connector)

    # Initialize person states: position (lng, lat), inside_shop (None or index)
    persons = {}
    for i, name in enumerate(NAMES):
        # small random offset around CITY_HALL
        lng = CITY_HALL[0] + random.uniform(-0.001, 0.001)
        lat = CITY_HALL[1] + random.uniform(-0.001, 0.001)
        persons[name] = {"lng": lng, "lat": lat, "color": COLORS[i % len(COLORS)], "inside": None}

    raining = False
    rain_timer = random.uniform(10, 25)
    last_rain_toggle = time.time()

    def _publish_weather(is_raining: bool):
        payload = json.dumps({"raining": bool(is_raining), "timestamp": _now_ts()})
        topic = "weather/rain"
        publisher.publish_json(topic, payload)
        print(f"Published weather: {payload}")

    def _publish_person(name, state):
        topic = f"persons/{name}/location"
        payload = make_person_payload(name, state["lng"], state["lat"], state["color"])
        publisher.publish_json(topic, payload)

    def _enter_shop(name):
        shop_idx = random.randrange(len(COFFEE_SHOPS))
        lng, lat = COFFEE_SHOPS[shop_idx]
        persons[name]["lng"] = lng
        persons[name]["lat"] = lat
        persons[name]["inside"] = shop_idx
        print(f"{name} enters shop {shop_idx}")

    def _leave_shop(name):
        # move back to outside square near CITY_HALL
        persons[name]["inside"] = None
        persons[name]["lng"] = CITY_HALL[0] + random.uniform(-0.001, 0.001)
        persons[name]["lat"] = CITY_HALL[1] + random.uniform(-0.001, 0.001)
        print(f"{name} leaves shop")

    def _random_walk(name):
        # small random drift when outside
        persons[name]["lng"] += random.uniform(-0.0003, 0.0003)
        persons[name]["lat"] += random.uniform(-0.0003, 0.0003)

    def _handle_sigint(sig, frame):
        global RUNNING
        print("Stopping demo...")
        RUNNING = False

    signal.signal(signal.SIGINT, _handle_sigint)

    print("Starting coffee-shop demo (CTRL+C to stop)")
    _publish_weather(raining)

    while RUNNING:
        now = time.time()
        # toggle rain occasionally
        if now - last_rain_toggle > rain_timer:
            raining = not raining
            last_rain_toggle = now
            rain_timer = random.uniform(8, 18)
            _publish_weather(raining)

            # When rain starts, send everyone inside; when stops, send everyone out
            if raining:
                for name in NAMES:
                    if persons[name]["inside"] is None:
                        _enter_shop(name)
            else:
                for name in NAMES:
                    if persons[name]["inside"] is not None:
                        _leave_shop(name)

        # Update positions and publish
        for name in NAMES:
            if persons[name]["inside"] is None:
                _random_walk(name)
            # if inside, remain at shop coords
            _publish_person(name, persons[name])

        time.sleep(publish_interval)

    connector.disconnect()


if __name__ == "__main__":
    try:
        main(publish_interval=1.0)
    except Exception as e:
        print(f"Demo error: {e}")
        sys.exit(1)
