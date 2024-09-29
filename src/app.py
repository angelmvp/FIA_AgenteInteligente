if __name__ == '__main__':

    print(mountain_terrain)
    print("Costo de movimiento para humano:", mountain_terrain.get_movement_cost('human'))
    print("Costo de movimiento para mono:", mountain_terrain.get_movement_cost('monkey'))
    print("Costo de movimiento para pulpo:", mountain_terrain.get_movement_cost('octopus'))
    print("Costo de movimiento para pie grande:", mountain_terrain.get_movement_cost('sasquatch'))