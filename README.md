# simulated-city-template

This is a template repository.

Get started by reading [docs/setup.md](docs/setup.md).
See [docs/overview.md](docs/overview.md) for an overview of the base module content.

## Template for a project
Use this section as your project build prompt.
Think about these four components and the messages they send between each other.

Before you write any code, use the coding agent in planning mode and focus on documentation first. Draft the docs that explain the feature, workflow, and configuration as part of the plan, then implement only after the docs are clear.

### My Smart City Project: [coffe shop]

#### 1. The Trigger (Who/What is moving?)
Five people are moving around the city square. When it starts to rain, the people will go inside a random coffee shop to find shelter.

#### 2. The Observer (What does the city see?)
The city detects when it starts raining. It also sees the five people walking around the square and checks whether they are outside or inside a coffee shop.

#### 3. The Control Center (The Logic)
When rain begins, each person outside the square is assigned to a random coffee shop and moves inside.
While it is raining, the environment becomes darker.
When the rain stops, the environment becomes bright again, and the people leave the coffee shop they entered and go back outside to the square.

#### 4. The Response (What happens next?)
The system responds in two ways:
- Person markers turn red during rain (visual feedback)
- Rain state is published on `weather/rain` topic every 20 seconds (10 seconds rain, then dry)

#### Implementation

See [docs/coffee_shop.md](docs/coffee_shop.md) for running instructions.

**Quick start:**
1. Open `notebooks/03_mqtt_random_walk/coffee_shop.ipynb`
2. Run all cells (Cell → Run All)
3. Open `notebooks/03_mqtt_random_walk/map_viewer.ipynb` in another tab to see the live map

Or run the script version:
```bash
python scripts/demo/coffee_shop.py
```