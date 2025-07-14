from app.entities.plants.defensive_plant import DefensivePlant
from app.entities.plants.instantaneous_plant import InstantaneousPlant
from app.entities.plants.offensive_plant import OffensivePlant
from app.entities.plants.sunproducer_plant import SunProducerPlant


class PlantFactory:
    def create_plant(self, name, type, context, pos, pos_in_board):
        if type == "offensive":
            return OffensivePlant(name, context, pos, pos_in_board)
        if type == "sun_producer":
            return SunProducerPlant(name, context, pos, pos_in_board)
        if type == "defensive":
            return DefensivePlant(name, context, pos, pos_in_board)
        if type == "instantaneous":
            return InstantaneousPlant(name, context, pos, pos_in_board)

        return None