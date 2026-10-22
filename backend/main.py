from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


# ==========================================
# CareerPathAI Backend
# ==========================================

app = FastAPI(
    title="CareerPathAI API",
    description="Backend API for career exploration and recommendations.",
    version="1.0.0",
)


# ==========================================
# CORS CONFIGURATION
# Allows the frontend to communicate with
# the backend during local development.
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# CAREER DATA
# Initial in-memory data for development.
# Later, we can move this into a database.
# ==========================================

CAREERS = [
    {
        "id": "software",
        "title": "Software Developer",
        "category": "Technology",
        "description": (
            "Build applications, websites, and software "
            "solutions to solve real-world problems."
        ),
        "skills": [
            "Python",
            "Java",
            "Data Structures and Algorithms",
            "Problem Solving",
            "Git",
        ],
    },
    {
        "id": "robotics",
        "title": "AI & Robotics Engineer",
        "category": "AI & Robotics",
        "description": (
            "Develop intelligent robots, autonomous systems, "
            "and AI-powered machines."
        ),
        "skills": [
            "Python",
            "C++",
            "ROS 2",
            "Robot Kinematics",
            "Computer Vision",
            "Machine Learning",
        ],
    },
    {
        "id": "data",
        "title": "Data Scientist",
        "category": "Data Science",
        "description": (
            "Analyze data and build predictive models "
            "to discover meaningful patterns."
        ),
        "skills": [
            "Python",
            "SQL",
            "Statistics",
            "Pandas",
            "Machine Learning",
        ],
    },
    {
        "id": "cybersecurity",
        "title": "Cybersecurity Engineer",
        "category": "Technology",
        "description": (
            "Protect computer systems, networks, "
            "and applications against cyber threats."
        ),
        "skills": [
            "Networking",
            "Linux",
            "Python",
            "Cybersecurity Fundamentals",
        ],
    },
    {
        "id": "web",
        "title": "Web Developer",
        "category": "Technology",
        "description": (
            "Design and develop interactive websites "
            "and modern web applications."
        ),
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "APIs",
            "Git",
        ],
    },
    {
        "id": "entrepreneur",
        "title": "Entrepreneur",
        "category": "Business",
        "description": (
            "Turn innovative ideas into products "
            "and businesses."
        ),
        "skills": [
            "Communication",
            "Leadership",
            "Business Planning",
            "Problem Solving",
        ],
    },
]


# ==========================================
# REQUEST MODEL
# ==========================================

class RecommendationRequest(BaseModel):
    interest: str = Field(min_length=1, max_length=100)
    strength: str = Field(min_length=1, max_length=100)
    experience: str = Field(min_length=1, max_length=50)


# ==========================================
# ROOT ENDPOINT
# ==========================================

@app.get("/")
def home():
    return {
        "message": "Welcome to CareerPathAI Backend!",
        "status": "running",
        "documentation": "/docs",
    }


# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "CareerPathAI",
    }


# ==========================================
# GET ALL CAREERS
# ==========================================

@app.get("/api/careers")
def get_careers():
    return {
        "total": len(CAREERS),
        "careers": CAREERS,
    }


# ==========================================
# GET CAREER BY ID
# ==========================================

@app.get("/api/careers/{career_id}")
def get_career(career_id: str):
    for career in CAREERS:
        if career["id"] == career_id.lower():
            return career

    raise HTTPException(
        status_code=404,
        detail="Career not found.",
    )


# ==========================================
# CAREER RECOMMENDATION
# Initial rules-based recommendation system.
# This is not a trained AI model.
# ==========================================

@app.post("/api/recommend")
def recommend_career(request: RecommendationRequest):

    interest = request.interest.strip().lower()
    strength = request.strength.strip().lower()

    career_id = "software"

    if any(
        keyword in interest
        for keyword in [
            "robot",
            "artificial intelligence",
            "robotics",
        ]
    ):
        career_id = "robotics"

    elif any(
        keyword in interest
        for keyword in [
            "cybersecurity",
            "cyber security",
            "security",
        ]
    ):
        career_id = "cybersecurity"

    elif any(
        keyword in interest
        for keyword in [
            "data science",
            "data",
            "analytics",
        ]
    ):
        career_id = "data"

    elif any(
        keyword in interest
        for keyword in [
            "web development",
            "web",
            "website",
            "design",
        ]
    ):
        career_id = "web"

    elif any(
        keyword in interest
        for keyword in [
            "business",
            "entrepreneurship",
            "entrepreneur",
        ]
    ):
        career_id = "entrepreneur"

    elif (
        "leadership" in strength
        or "business" in strength
    ):
        career_id = "entrepreneur"

    recommended_career = next(
        career
        for career in CAREERS
        if career["id"] == career_id
    )

    return {
        "message": "Career recommendation generated successfully.",
        "recommendation_type": "rules-based",
        "input": {
            "interest": request.interest,
            "strength": request.strength,
            "experience": request.experience,
        },
        "recommended_career": recommended_career,
    }
