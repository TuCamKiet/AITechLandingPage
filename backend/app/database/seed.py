# RUN SEPARATELY WITH "python -m app.database.seed"



from app.database.database import Base, engine, SessionLocal

from app.models.landing_model.workflowstep_model import WorkflowStep

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")

db = SessionLocal()

workflow_steps = [
    {
        "step": "01",
        "title": "Curriculum Ingestion",
        "detail": "Upload your existing syllabus, textbooks, and past exams. Our AI securely learns your specific course material and teaching style."
    },
    {
        "step": "02",
        "title": "Deploy Your Custom Tutor",
        "detail": "Launch an AI teaching assistant directly to your students. It answers questions strictly based on your approved curriculum."
    },
    {
        "step": "03",
        "title": "Learn, Adapt, & Improve",
        "detail": "As students interact, the platform identifies common stumbling blocks and suggests curriculum improvements to the educator."
    }
]

db.add_all([
    WorkflowStep(**item)
    for item in workflow_steps
])

db.commit()
db.close()

print("✅ WorkflowStep seed completed")