# Simple Vacuum Cleaner Agent in Python

# Environment setup
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

# Vacuum cleaner starting location
current_room = "A"


def vacuum_agent(room):

    global current_room

    # Check room condition
    if rooms[room] == "Dirty":

        print("Room", room, "is Dirty.")
        print("Cleaning room", room)

        # Clean the room
        rooms[room] = "Clean"

    else:
        print("Room", room, "is already Clean.")

# Clean Room A
vacuum_agent("A")

# Move to Room B
print("Moving to Room B")
current_room = "B"

# Clean Room B
vacuum_agent("B")

# Final environment status
print("\nFinal Room Status")

for room in rooms:
    print("Room", room, ":", rooms[room])
    