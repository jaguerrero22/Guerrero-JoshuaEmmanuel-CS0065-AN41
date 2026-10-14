
# TASK 1: SET UP THE ENVIRONMENT

def is_dirty(environment, room):
    """Checks if a room is dirty"""
    return environment[room] == "Dirty"


def clean_room(environment, room):
    """Cleans the specified room"""
    environment[room] = "Clean"

# TASK 2: IMPLEMENT THE RULE-BASED AGENT

class VacuumAgent:

    def __init__(self, start_room="A"):
        self.location = start_room

    def move(self):
        """Switches location between Room A and Room B"""
        if self.location == "A":
            self.location = "B"
        else:
            self.location = "A"

    def perceive_and_act(self, environment):
        current_room = self.location

        # Rule 1: If current room is dirty, clean it
        if is_dirty(environment, current_room):
            clean_room(environment, current_room)
            return f"Room {current_room} has been cleaned."

        # Rule 2: If current room is clean, move to the other room
        else:
            self.move()
            return f"Moving to room {self.location}"

# TASK 3: RUN THE SIMULATION

def main():
    # Ask user for initial states
    room_a = input("Is room A Dirty or Clean? ").strip().capitalize()
    room_b = input("Is room B Dirty or Clean? ").strip().capitalize()

    # Create environment dictionary (Task 1)
    environment = {"A": room_a, "B": room_b}

    print()
    steps = int(input("How many steps should the agent run? "))
    print()

    # Create agent instance (Task 2)
    agent = VacuumAgent(start_room="A")

    # Run simulation loop
    for step in range(1, steps + 1):
        print(f"Step {step}: Agent is in room {agent.location}")
        action_message = agent.perceive_and_act(environment)
        print(action_message)
        print(f"Environment state: {environment}")
        print()


if __name__ == "__main__":
    main()