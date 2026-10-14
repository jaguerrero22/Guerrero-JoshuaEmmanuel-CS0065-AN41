
import random

# ==========================================
# BONUS TASK: 3-ROOM ENVIRONMENT & AGENT
# ==========================================


def is_dirty(environment, room):
    """Checks if a room is dirty"""
    return environment[room] == "Dirty"


def clean_room(environment, room):
    """Cleans the specified room"""
    environment[room] = "Clean"


def print_grid(environment, agent_location):
    """Prints the text-based grid visualization"""
    grid_items = []
    for room in ["A", "B", "C"]:
        # If the agent is in this room, display [Room-Agent]
        if room == agent_location:
            grid_items.append(f"[{room}-Agent]")
        else:
            # Otherwise display [Room-State] (e.g., [A-Clean] or [B-Dirty])
            grid_items.append(f"[{room}-{environment[room]}]")

    print("  ".join(grid_items))


class BonusVacuumAgent:

    def __init__(self, start_room="A"):
        self.location = start_room

    def perceive_and_act(self, environment):
        current_room = self.location

        # Rule 1: If current room is dirty, clean it
        if is_dirty(environment, current_room):
            clean_room(environment, current_room)
            return f"Room {current_room} has been cleaned."

        # Rule 2: If current room is clean, randomly choose a dirty room to move to
        dirty_rooms = [
            room for room in environment if is_dirty(environment, room)
        ]

        if dirty_rooms:
            # Randomly select one dirty room
            next_room = random.choice(dirty_rooms)
            self.location = next_room
            return f"Moving to room {self.location}"
        else:
            # If all rooms are clean
            return "All rooms are clean. Agent is idle."


def main_bonus():
    # Take initial room inputs (Room A defaults to clean in sample output or we can ask)
    room_a = input("Is room A Dirty or Clean? ").strip().capitalize()
    room_b = input("Is room B Dirty or Clean? ").strip().capitalize()
    room_c = input("Is room C Dirty or Clean? ").strip().capitalize()

    environment = {"A": room_a, "B": room_b, "C": room_c}

    print()
    steps = int(input("How many steps should the agent run? "))
    print()

    agent = BonusVacuumAgent(start_room="A")

    for step in range(1, steps + 1):
        print(f"Step {step}:")

        # 1. Show grid state BEFORE action
        print_grid(environment, agent.location)

        # 2. Perform action
        action_message = agent.perceive_and_act(environment)
        print(action_message)

        # 3. Show grid state AFTER action
        print_grid(environment, agent.location)
        print()


if __name__ == "__main__":
    main_bonus()