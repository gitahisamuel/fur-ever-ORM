from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    status = Column(String, nullable=False)

    interactions = relationship(
        "UserAnimalInteraction",
        back_populates="animal",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Animal(id={self.id}, name={self.name}, species={self.species}, age={self.age}, status={self.status})>"
