colors = ["Blue", "Red", "Green"]

neighbors = {
    "Westlands": ["Starehe", "Roysambu", "Kibra"],
    
    "Dagoretti North": ["Dagoretti South", "Kibra", "Langata"],
    "Dagoretti South": ["Dagoretti North", "Kibra"],
    
    "Langata": ["Dagoretti North", "Kibra", "Embakasi South"],
    
    "Kibra": ["Westlands", "Dagoretti North", "Dagoretti South", "Langata"],
    
    "Embakasi Central": ["Embakasi East", "Embakasi North", "Embakasi West"],
    "Embakasi East": ["Embakasi Central", "Embakasi North"],
    "Embakasi North": ["Embakasi Central", "Embakasi East", "Roysambu"],
    "Embakasi South": ["Langata", "Makadara"],
    "Embakasi West": ["Embakasi Central", "Makadara"],
    
    "Kamukunji": ["Starehe", "Makadara", "Mathare"],
    "Makadara": ["Kamukunji", "Embakasi South", "Embakasi West"],
    
    "Mathare": ["Kamukunji", "Ruaraka"],
    
    "Ruaraka": ["Mathare", "Roysambu", "Kasarani"],
    
    "Roysambu": ["Westlands", "Ruaraka", "Starehe", "Kasarani"],
    
    "Starehe": ["Westlands", "Kamukunji", "Roysambu"],
    
    "Kasarani": ["Ruaraka", "Roysambu"]
}

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
    print("\nNairobi Sub-county Coloring Solution:\n")
    for r, c in assignment.items():
        print(r, "->", c)
else:
    print("No solution found")