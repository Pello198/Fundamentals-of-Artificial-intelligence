
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}
current_room = "A"


def vacuum_agent(room):

    global current_room
    if rooms[room] == "Dirty":

        print("Room", room, "is Dirty.")
        print("Cleaning room", room)
        rooms[room] = "Clean"

    else:
        print("Room", room, "is already Clean.")

vacuum_agent("A")
print("Moving to Room B")
current_room = "B"

vacuum_agent("B")
print("\nFinal Room Status")

for room in rooms:
    print("Room", room, ":", rooms[room])
    
