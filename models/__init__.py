# This makes the models package load all models,
# so that metadata knows about them when creating tables.
from .user import User
from .animal import Animal
from .interaction import UserAnimalInteraction
