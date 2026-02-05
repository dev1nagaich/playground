from fastapi import FastAPI
from fastapi.responses import FileResponse
from database import EntityBase, db_engine, DBSession
from schema import UserProfile

# Initialize FastAPI application
application = FastAPI()

# Create database tables
EntityBase.metadata.create_all(bind=db_engine)

@application.get("/")
def render_homepage():
    """Serve the main HTML page"""
    return FileResponse("frontend.html")

@application.get("/health")
def check_health():
    """Health check endpoint"""
    return {"status": "operational"}

@application.get("/profile")
def fetch_user_profile():
    """Retrieve user profile information"""
    db_session = DBSession()
    user_data = db_session.query(UserProfile).first()
    
    if not user_data:
        return {"message": "No profile exists yet"}
    
    return user_data

@application.put("/profile")
def modify_user_profile():
    """Update existing user profile"""
    db_session = DBSession()
    user_data = db_session.query(UserProfile).first()

    if not user_data:
        return {"error": "Profile does not exist"}

    user_data.technical_skills = "Python,FastAPI,SQL,Git"
    user_data.project_portfolio = "Updated portfolio information"
    db_session.commit()

    return {"message": "Profile successfully updated"}

@application.get("/projects")
def filter_projects_by_skill(skill: str = ""):
    """Search projects by technical skill"""
    db_session = DBSession()
    user_data = db_session.query(UserProfile).first()

    if not user_data:
        return []

    if skill.lower() in user_data.technical_skills.lower():
        return user_data.project_portfolio

    return []

@application.post("/profile")
def initialize_user_profile():
    """Create a new user profile"""
    db_session = DBSession()

    user_data = UserProfile(
        full_name="Your Name",
        email_address="you@email.com",
        educational_background="Your University",
        technical_skills="python,fastapi",
        project_portfolio="Portfolio API Application",
        social_links="github.com/username"
    )

    db_session.add(user_data)
    db_session.commit()

    return {"message": "Profile created successfully"}