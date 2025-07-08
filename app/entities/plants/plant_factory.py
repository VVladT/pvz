from app.entities.plants.defensive_plant import DefensivePlant
from app.entities.plants.instantaneous_plant import InstantaneousPlant
from app.entities.plants.offensive_plant import OffensivePlant
from app.entities.plants.sunproducer_plant import SunProducerPlant


class PlantFactory:
    def create_plant(self, name, type, spritesheet):
        if type == "offensive":
            return OffensivePlant(name, spritesheet)
        if type == "sun_producer":
            return SunProducerPlant(name, spritesheet)
        if type == "defensive":
            return DefensivePlant(name, spritesheet)
        if type == "instantaneous":
            return InstantaneousPlant(name, spritesheet)

        return None