import random, math, csv
from constants import FLOWERS, POPULATION_SIZE, SELECTION, REJECTION

class Bee():
    def __init__(self, bee_id, bee_path = [], modified_path = []):
        self.bee_id = bee_id
        self.flowers_list = FLOWERS.copy()
        self.path = bee_path
        self.modified_path = modified_path
        random.shuffle(self.flowers_list)
    
    def distance_a_to_b(self ,a ,b) -> float:
        """Calculates the Euclidean distance between two points."""
        stage_distance = round(math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2),2)
        return stage_distance

    def total_distance(self) -> float:
        """Calculates the total distance from the hive, through every shuffled flower,back to the hive."""
        hive = (500, 500)
        current_position = hive
        total_distance = 0

        for flower in self.flowers_list:
            stage_distance = self.distance_a_to_b(current_position, flower)
            total_distance += stage_distance
            current_position = flower
        
        return_to_hive_distance = self.distance_a_to_b(current_position, hive)
        total_distance += return_to_hive_distance
        total_distance = round(total_distance,2)
            
        # print(f"\n'total_distance'-> Distance totale parcourue : {total_distance}")
        return total_distance

    def gathering_path(self) -> list[(int, int)]:
        """ Returns the path of flower collection """
        self.path = self.flowers_list
        return self.path
    
    # Dispays bee's informations when the objet is printed
    def __repr__(self) -> str:
        return f"Bee id : {self.bee_id}, \nBee path : {self.gathering_path()}\n"

memorized_paths = []
generated_bees = []

#---------------------First Generation---------------------------------


def generate_bees() -> list[Bee]:
    ''' generates as many bees as defined in POPULATION '''
    # Avoid creating a new list of bees if there is one already
    if generated_bees:
        return generated_bees
    # Creates a list of bees if there is none, Use .extend instead of .append to add Bees to the list
    else:
        generated_bees.extend([Bee(i) for i in range(POPULATION_SIZE)])
        return generated_bees
# print(generate_bees())

def sorted_distances() -> list[tuple[float, Bee]]:
    ''' sorts the distances_and_bees list
    shortest distance first, longest distance last'''
    distances_and_bees = [(bee.total_distance(), bee) for bee in generate_bees()]
    sorted_distances = sorted(distances_and_bees, key=lambda x: x[0])
    return sorted_distances
# print(sorted_distances()) 

sorted_bees = sorted_distances()

def selected_bees(SELECTION) -> list[tuple[float, Bee]]:
    return sorted_bees[:SELECTION]

def rejected_bees(REJECTION) -> list[tuple[float, Bee]]:
    return sorted_bees[-REJECTION:]

def selected_paths(SELECTION) -> list[Bee]:
    ''' lists the paths of the best bees '''
    selected_paths = []
    chosen_bees = selected_bees(SELECTION)
    for distance, bee in chosen_bees:
        selected_paths.append(bee)
        memorized_paths.append(bee.gathering_path())
    return selected_paths
# print("\nselected_paths (liste d'objets bee):\n\n", selected_paths(SELECTION))



#-----------------------Modifications--------------------------------------------


def modify_first_to_last(selected_bees: list[Bee]) -> list[Bee]:
    for bee in selected_bees:
        # creates a shallow copy of the path
        path = bee.gathering_path()[:]
        path[0], path[-1] = path[-1], path[0]
        # assign the modified path back to bee.path
        bee.modified_path = path
        modified_bees = selected_bees
    return modified_bees  # Return the modified bees


# On a :
# les meilleurs trajet
# les pires trajets


def cross():
    # Mélanger les meilleurs trajets
    pass

def mutate():
    # objectif : tester différent chemin et les compare
    # assigne les trajets mélangé aux abeilles disponibles 
    pass


# ? ? ? 
def reproduce():
    pass


