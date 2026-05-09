# Australia map colouring problem
colors = ["Blue", "Red", "Green"]

neighbors = {
    "Western Australia": ["Northern Territory", "South Australia"],
    
    "Northern Territory": ["Western Australia", "South Australia", "Queensland"],
    
    "South Australia": [
        "Western Australia",
        "Northern Territory",
        "Queensland",
        "New South Wales",
        "Victoria"
    ],
    
    "Queensland": [
        "Northern Territory",
        "South Australia",
        "New South Wales"
    ],
    
    "New South Wales": [
        "Queensland",
        "South Australia",
        "Victoria"
    ],
    
    "Victoria": [
        "South Australia",
        "New South Wales"
    ],
    
    "Tasmania": []   # island state with no land borders
}


# store final colour assignments
assignment = {}

def is_valid(region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
def solve(regions):
   
    if len(assignment) == len(regions):
        return True

  
    region = regions[len(assignment)]

    for color in colors:
        if is_valid(region, color):
            assignment[region] = color

            if solve(regions):
                return True

            del assignment[region]

    return False

regions = list(neighbors.keys())


if solve(regions):
    print("\nsolution found:\n")
    for region, color in assignment.items():
        print(region, "->", color)
else:
    print("no solution found")