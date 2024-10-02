import csv
from random import random

# Define terrain types based on the provided JSON
terrain_types = [1, 2, 3, 4, 5, 6, 7]


# Function to generate a 500x500 grid with logical terrain distribution
def generate_terrain_csv(filename):
  with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    for _ in range(500):
      row = []
      for _ in range(500):
        # Generate a random number between 0 and 1
        random_number = random()
        # Assign a terrain type based on the random number
        if random_number < 0.1:
          row.append(terrain_types[0])
        elif random_number < 0.2:
          row.append(terrain_types[1])
        elif random_number < 0.3:
          row.append(terrain_types[2])
        elif random_number < 0.4:
          row.append(terrain_types[3])
        elif random_number < 0.5:
          row.append(terrain_types[4])
        elif random_number < 0.6:
          row.append(terrain_types[5])
        else:
          row.append(terrain_types[6])
      writer.writerow(row)


# Generate the CSV file
generate_terrain_csv('resources/map/terrain_500x500.csv')
