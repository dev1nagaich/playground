from fastapi import FastAPI
from fastapi.responses import FileResponse
from db import Base, engine, SessionLocal
from models import Profile

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/profile")
def get_profile():
    db = SessionLocal()
    profile = db.query(Profile).first()
    if not profile:
        return {"message": "Profile not created yet"}
    return profile
@app.put("/profile")
def update_profile():
    db = SessionLocal()
    profile = db.query(Profile).first()

    if not profile:
        return {"error": "Profile not found"}

    profile.skills = "Python,FastAPI,SQL,Git"
    profile.projects = "Updated project info"
    db.commit()

    return {"message": "Profile updated"}
@app.get("/projects")
def get_projects(skill: str = ""):
    db = SessionLocal()
    profile = db.query(Profile).first()

    if not profile:
        return []

    if skill.lower() in profile.skills.lower():
        return profile.projects

    return []


@app.post("/profile")
def create_profile():
    db = SessionLocal()

    profile = Profile(
        name="Your Name",
        email="you@email.com",
        education="Your college",
        skills="python,fastapi",
        projects="Me API Playground",
        links="github.com/you"
    )

    db.add(profile)
    db.commit()

    return {"message": "Profile created successfully"}
