import agentpy as ap
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# User Input 

num_agents = int(input("Enter number of agents: "))
grid_size = int(input("Enter grid size (e.g., 10 for 10x10): "))
num_steps = int(input("Enter number of steps: "))

# Agent Definitions 
# Task 1: Track agent paths

class RandomWalker(ap.Agent):

    def setup(self):
        self.path = []

    def step(self):

        direction = random.choice([
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ])

        x, y = self.position

        new_x = max(
            0,
            min(self.model.p.grid_size[0] - 1, x + direction[0])
        )

        new_y = max(
            0,
            min(self.model.p.grid_size[1] - 1, y + direction[1])
        )

        self.position = (new_x, new_y)
        self.path.append(self.position)


# Task 2: Change Movement rules

class AvoidWalker(ap.Agent):

    def setup(self):
        self.path = []

    def step(self):

        direction = random.choice([
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ])

        x, y = self.position

        new_x = max(
            0,
            min(self.model.p.grid_size[0] - 1, x + direction[0])
        )

        new_y = max(
            0,
            min(self.model.p.grid_size[1] - 1, y + direction[1])
        )

        occupied = [
            a.position
            for a in self.model.agents
            if a != self
        ]

        if (new_x, new_y) not in occupied:
            self.position = (new_x, new_y)

        self.path.append(self.position)


# Model Definition 

class RandomWalkModel(ap.Model):

    def setup(self):

        self.agents = ap.AgentList(
            self,
            self.p.agents,
            self.p.agent_type
        )

        for agent in self.agents:

            agent.position = (
                random.randint(
                    0,
                    self.p.grid_size[0] - 1
                ),
                random.randint(
                    0,
                    self.p.grid_size[1] - 1
                )
            )

            agent.path.append(agent.position)

        self.grid = ap.Grid(
            self,
            self.p.grid_size,
            torus=False
        )

        self.grid.add_agents(self.agents)

    def step(self):

        for agent in self.agents:
            agent.step()


# Parameters 

parameters = {
    "agents": num_agents,
    "grid_size": (grid_size, grid_size),
    "steps": num_steps,
    "agent_type": RandomWalker
    # Change to AvoidWalker for Task 2
}

# Run Model 

model = RandomWalkModel(parameters)
model.setup()

# Visualization 

fig, ax = plt.subplots()

ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)
ax.grid(True)

scat = ax.scatter([], [], s=200)

def update(frame):

    model.step()

    x = [agent.position[0] for agent in model.agents]
    y = [agent.position[1] for agent in model.agents]

    scat.set_offsets(list(zip(x, y)))

    return scat,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=num_steps,
    blit=True,
    repeat=False
)

plt.show()

#  Task Outputs 

print("\nTask 1: Agent Paths")

for i, agent in enumerate(model.agents):
    print(f"Agent {i+1}: {agent.path}")

# Task 3: Analyze the Final Positions

print("\nTask 3: Final Positions")

positions = [agent.position for agent in model.agents]
print(positions)

x = [p[0] for p in positions]
y = [p[1] for p in positions]

plt.figure()
plt.scatter(x, y, s=200)
plt.title("Final Agent Positions")
plt.grid(True)
plt.show()

# ---------------- Task 4: Compare Scenarios ----------------

print("\nTask 4: Scenario Comparison")

# Scenario A

params_A = {
    "agents": 5,
    "grid_size": (10, 10),
    "steps": 20,
    "agent_type": RandomWalker
}

model_A = RandomWalkModel(params_A)
model_A.setup()

for _ in range(model_A.p.steps):
    model_A.step()

positions_A = [
    a.position
    for a in model_A.agents
]

# Scenario B

params_B = {
    "agents": 20,
    "grid_size": (10, 10),
    "steps": 50,
    "agent_type": RandomWalker
}

model_B = RandomWalkModel(params_B)
model_B.setup()

for _ in range(model_B.p.steps):
    model_B.step()

positions_B = [
    a.position
    for a in model_B.agents
]

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.scatter(*zip(*positions_A))
plt.title("Scenario A (5 agents, 20 steps)")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(*zip(*positions_B))
plt.title("Scenario B (20 agents, 50 steps)")
plt.grid(True)

plt.show()