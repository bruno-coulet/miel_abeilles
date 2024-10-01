import csv

def list_flowers():
    flowers = []

    with open('data/fleurs.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        # skips the header
        next(reader)
        # adds the coordinates tuple in the flowers list
        for row in reader:
            x = int(row[0])
            y = int(row[1])
            flowers.append((x, y))
    return flowers

GENERATION_COUNT = 10
FLOWERS = list_flowers()
POPULATION_SIZE = 4
SELECTION = 2
REJECTION = 2
INTERLIGNE = "-"*80
