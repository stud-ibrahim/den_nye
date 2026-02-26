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
WhThe system responds in two ways:
The people stop walking around the square and move into coffee shops.
The city lighting changes so it becomes darker during rain and brighter again when the rain stops.