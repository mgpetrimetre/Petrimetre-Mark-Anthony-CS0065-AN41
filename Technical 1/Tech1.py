import agentpy as ap
import random
import matplotlib.pyplot as plt


class RandomWalker(ap.Agent):
    def setup(self):
        # Pick an initial position within the grid boundaries
        gx, gy = self.model.p.grid_size
        self.position = (random.randint(0, gx - 1), random.randint(0, gy - 1))
        
        # Track path history throughout the run
        self.path = [self.position]

    def step(self):
        gx, gy = self.model.p.grid_size
        x, y = self.position

        # Candidate directions: Right, Left, Up, Down
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Task 2: Movement rules (Unbiased vs Biased Direction)
        if self.model.p.movement_mode == 'drift_right':
            # 55% chance to move right, remaining probability split evenly
            weights = [0.55, 0.15, 0.15, 0.15]
            dx, dy = random.choices(directions, weights=weights)[0]
        else:
            # Standard uniform random walk
            dx, dy = random.choice(directions)

        # Boundary clamping to stay inside the grid
        new_x = max(0, min(gx - 1, x + dx))
        new_y = max(0, min(gy - 1, y + dy))
        next_pos = (new_x, new_y)

        # Collision avoidance check against other agents
        if self.model.p.avoid_collision:
            occupied = {other.position for other in self.model.agents if other != self}
            if next_pos in occupied:
                # If target cell is already occupied, stay in current position
                next_pos = (x, y)

        self.position = next_pos
        self.path.append(self.position)



class RandomWalkModel(ap.Model):
    def setup(self):
        self.agents = ap.AgentList(self, self.p.agents, RandomWalker)
        self.grid = ap.Grid(self, self.p.grid_size, torus=False)
        self.grid.add_agents(self.agents)

    def step(self):
        self.agents.step()

    def end(self):
        # Log final coordinates and quadrant distribution
        print(f"\n--- Final Position Analysis: {self.p.scenario_name} ---")
        mid_x = self.p.grid_size[0] / 2
        mid_y = self.p.grid_size[1] / 2
        
        q_counts = {"Q1 (Top-Right)": 0, "Q2 (Top-Left)": 0, "Q3 (Bottom-Left)": 0, "Q4 (Bottom-Right)": 0}

        for idx, agent in enumerate(self.agents):
            x, y = agent.position
            print(f"Agent {idx + 1} final position: ({x}, {y})")
            
            if x >= mid_x and y >= mid_y:
                q_counts["Q1 (Top-Right)"] += 1
            elif x < mid_x and y >= mid_y:
                q_counts["Q2 (Top-Left)"] += 1
            elif x < mid_x and y < mid_y:
                q_counts["Q3 (Bottom-Left)"] += 1
            else:
                q_counts["Q4 (Bottom-Right)"] += 1

        print("Distribution across quadrants:")
        for q, count in q_counts.items():
            print(f"  {q}: {count}")



if __name__ == "__main__":
    # Console prompts
    num_agents = int(input("Enter number of agents: "))
    grid_size = int(input("Enter grid size (e.g., 10 for 10x10): "))
    num_steps = int(input("Enter number of steps: "))

    # Simulation parameters
    parameters = {
        'scenario_name': 'Standard vs Collision-Avoidance Walk',
        'agents': num_agents,
        'grid_size': (grid_size, grid_size),
        'steps': num_steps,
        'movement_mode': 'standard',     # Options: 'standard' or 'drift_right'
        'avoid_collision': True          # Toggle collision avoidance
    }

    model = RandomWalkModel(parameters)
    model.run()

    # Plotting agent trajectories on the grid
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_xlim(-0.5, grid_size - 0.5)
    ax.set_ylim(-0.5, grid_size - 0.5)
    ax.set_xticks(range(grid_size))
    ax.set_yticks(range(grid_size))
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.set_title("Agent Paths and Final Positions")

    colors = plt.cm.tab10.colors

    for i, agent in enumerate(model.agents):
        c = colors[i % len(colors)]
        xs = [pos[0] for pos in agent.path]
        ys = [pos[1] for pos in agent.path]

        # Draw trajectory line
        ax.plot(xs, ys, color=c, alpha=0.5, linewidth=2, label=f"Agent {i + 1}")
        # Mark start (square) and end (circle)
        ax.scatter(xs[0], ys[0], color=c, marker='s', s=50)
        ax.scatter(xs[-1], ys[-1], color=c, marker='o', s=90, edgecolors='black')

    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()