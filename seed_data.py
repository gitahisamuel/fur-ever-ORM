# seed_data.py

from datetime import date
from database import SessionLocal, engine, Base
import models  # ensure models are imported so SQLAlchemy knows all tables
from models.user import User
from models.animal import Animal
from models.interaction import UserAnimalInteraction

def seed():
    session = SessionLocal()

    # Example users
    user1 = User(username="alice", email="alice@example.com")
    user2 = User(username="bob",   email="bob@example.com")

    # Example animals
    animal1 = Animal(name="Buddy",   species="Dog", age=3, status="available")
    animal2 = Animal(name="Mittens", species="Cat", age=2, status="available")
    animal3 = Animal(name="Charlie", species="Parrot", age=1, status="available")

    session.add_all([user1, user2, animal1, animal2, animal3])
    session.commit()

    # Example interactions
    # user1 donates to animal1
    interaction1 = UserAnimalInteraction(
        user_id=user1.id,
        animal_id=animal1.id,
        interaction_type="donation",
        interaction_date=date.today(),
        amount=100.00
    )

    # user2 adopts animal2
    interaction2 = UserAnimalInteraction(
        user_id=user2.id,
        animal_id=animal2.id,
        interaction_type="adopt",
        interaction_date=date.today(),
        amount=None  # adoption may not require donation
    )

    session.add_all([interaction1, interaction2])
    session.commit()

    print("Seed data inserted:")
    print("Users:", session.query(User).all())
    print("Animals:", session.query(Animal).all())
    print("Interactions:", session.query(UserAnimalInteraction).all())

    session.close()

if __name__ == "__main__":
    # Only create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    seed()
