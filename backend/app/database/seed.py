# RUN SEPARATELY WITH "python -m app.database.seed"

from app.database.database import Base, engine, SessionLocal

from app.models.landing_model.teammember_model import TeamMember

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")

db = SessionLocal()

team_members = [
    {
        "name": "Reza MK",
        "role": "CEO & Former Educator"
    },
    {
        "name": "Morteza P",
        "role": "CTO & AITeach Architect"
    },
    {
        "name": "Soheil MV",
        "role": "Head of Curriculum Design"
    }
]

db.add_all([
    TeamMember(**item)
    for item in team_members
])

db.commit()
db.close()

print("✅ TeamMember seed completed")