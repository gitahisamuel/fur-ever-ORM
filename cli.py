
import sys
from datetime import date

from database import SessionLocal, engine, Base
import models
from models.user import User
from models.animal import Animal
from models.interaction import UserAnimalInteraction

def init_db():
    Base.metadata.create_all(engine)

def create_user(session):
    username = input("Enter username: ").strip()
    email = input("Enter email: ").strip()
    if not username or not email:
        print("Username and email required.")
        return
    u = User(username=username, email=email)
    session.add(u)
    session.commit()
    print(f"User created: {u.id} — {u.username}, {u.email}")

def list_users(session):
    users = session.query(User).all()
    if not users:
        print("No users found.")
    else:
        for u in users:
            print(f"{u.id}: {u.username} ({u.email})")

def create_animal(session):
    name = input("Enter animal name: ").strip()
    species = input("Species: ").strip()
    age = input("Age (integer): ").strip()
    status = input("Status (e.g. available): ").strip() or "available"
    try:
        age = int(age)
    except ValueError:
        print("Invalid age.")
        return
    a = Animal(name=name, species=species, age=age, status=status)
    session.add(a)
    session.commit()
    print(f"Animal created: {a.id} — {a.name}, {a.species}, age {a.age}, status {a.status}")

def list_animals(session):
    animals = session.query(Animal).all()
    if not animals:
        print("No animals found.")
    else:
        for a in animals:
            print(f"{a.id}: {a.name} ({a.species}), age {a.age}, status {a.status}")

def adopt_or_donate(session):
    list_users(session)
    uid = input("Enter user id: ").strip()
    # choose animal
    list_animals(session)
    aid = input("Enter animal id: ").strip()
    action = input("Type 'adopt' or 'donation': ").strip().lower()
    amount = None
    if action == "donation":
        amt = input("Enter donation amount (or blank): ").strip()
        try:
            amount = float(amt) if amt else None
        except ValueError:
            print("Invalid amount; skipping donation amount.")
            amount = None
    # validate
    try:
        uid = int(uid); aid = int(aid)
    except ValueError:
        print("Invalid IDs.")
        return
    u = session.query(User).get(uid)
    a = session.query(Animal).get(aid)
    if not u or not a:
        print("User or Animal not found.")
        return
    interaction = UserAnimalInteraction(
        user=u,
        animal=a,
        interaction_type=action,
        interaction_date=date.today(),
        amount=amount
    )
    session.add(interaction)
    # optionally update animal status if adopted
    if action == "adopt":
        a.status = "adopted"
    session.commit()
    print(f"Recorded {action} by user {u.username} for animal {a.name}")

def list_interactions(session):
    interactions = session.query(UserAnimalInteraction).all()
    if not interactions:
        print("No interactions found.")
    else:
        for i in interactions:
            print(f"{i.id}: user {i.user.username} — animal {i.animal.name} — {i.interaction_type}, date {i.interaction_date}, amount {i.amount}")

def help_menu():
    print("""
Commands:
  help                 Show this help
  create-user          Add a new user
  list-users           List all users
  create-animal        Add a new animal
  list-animals         List all animals
  interact             Adopt or donate to an animal
  list-interactions    List all interactions
  exit                 Exit the CLI
""")

def main():
    init_db()
    session = SessionLocal()

    print("Welcome to Fur-Ever CLI!")
    help_menu()

    while True:
        cmd = input(">>> ").strip().lower()
        if cmd == "help":
            help_menu()
        elif cmd == "create-user":
            create_user(session)
        elif cmd == "list-users":
            list_users(session)
        elif cmd == "create-animal":
            create_animal(session)
        elif cmd == "list-animals":
            list_animals(session)
        elif cmd == "interact":
            adopt_or_donate(session)
        elif cmd == "list-interactions":
            list_interactions(session)
        elif cmd == "exit":
            print("Goodbye.")
            break
        else:
            print("Unknown command; type 'help' to see commands.")

    session.close()

if __name__ == "__main__":
    main()
