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

FLOWERS = list_flowers()
POPULATION_SIZE = 4
SELECTION = 1
REJECTION = 2
INTERLIGNE = "-"*80
