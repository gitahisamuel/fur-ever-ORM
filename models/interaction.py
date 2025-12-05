from sqlalchemy import Column, Integer, ForeignKey, String, Date, Numeric
from sqlalchemy.orm import relationship
from database import Base
from datetime import date

class UserAnimalInteraction(Base):
    __tablename__ = "user_animals_interactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    animal_id = Column(Integer, ForeignKey("animals.id"), nullable=False)

    interaction_type = Column(String, nullable=False)    
    interaction_date = Column(Date, default=date.today, nullable=False)
    amount = Column(Numeric(10, 2), nullable=True)        

    user = relationship("User", back_populates="interactions")
    animal = relationship("Animal", back_populates="interactions")

    def __repr__(self):
        return (f"<Interaction(id={self.id}, user_id={self.user_id}, animal_id={self.animal_id}, "
                f"type={self.interaction_type}, date={self.interaction_date}, amount={self.amount})>")
