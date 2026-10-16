class VacuumAgent:
    def __init__(self, start_room="A"):
        self.current_room = start_room

    def perceive_and_act(self, environment):
        """
        Rule 1: If current room is Dirty -> clean it.
        Rule 2: If current room is Clean -> switch to the other room.
        """
        current_state = environment[self.current_room]

        if current_state == "Dirty":
            # Action: Clean
            environment[self.current_room] = "Clean"
            action = f"Cleaned room {self.current_room}"
        else:
            # Action: Move
            action = self.move()

        return action

    def move(self):
        old_room = self.current_room
        self.current_room = "B" if self.current_room == "A" else "A"
        return f"Moved from Room {old_room} to Room {self.current_room}"



def is_dirty(room, environment):
    return environment.get(room) == "Dirty"

def clean_room(room, environment):
    environment[room] = "Clean"


def main():
    print("=== Rule-Based Agent Simulation ===")

    state_a = input("Enter state for Room A (Clean/Dirty): ").strip().capitalize()
    state_b = input("Enter state for Room B (Clean/Dirty): ").strip().capitalize()

    environment = {
        "A": "Dirty" if state_a == "Dirty" else "Clean",
        "B": "Dirty" if state_b == "Dirty" else "Clean"
    }

    start_pos = input("Enter initial agent location (A/B): ").strip().upper()
    if start_pos not in ["A", "B"]:
        start_pos = "A"

    steps = int(input("Enter number of simulation steps: "))

    agent = VacuumAgent(start_room=start_pos)

    print("\nInitial Environment:", environment)
    print(f"Agent starting at Room {agent.current_room}\n" + "-" * 40)

    for step in range(1, steps + 1):
        loc_before = agent.current_room
        action_taken = agent.perceive_and_act(environment)

        print(f"Step {step}:")
        print(f"  Agent Location : Room {loc_before}")
        print(f"  Action Taken   : {action_taken}")
        print(f"  Environment    : {environment}")
        print("-" * 40)


if __name__ == "__main__":
    main()