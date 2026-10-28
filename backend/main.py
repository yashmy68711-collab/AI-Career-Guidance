from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(
    title="CareerPathAI API",
    description="Career exploration, learning roadmaps, and career recommendations.",
    version="1.1.0",
)

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

# =====================================================
# CAREER DATA
# =====================================================

CAREERS = [
    {
        "id": "software",
        "title": "Software Developer",
        "category": "Technology",
        "description": (
            "Build, test, and maintain software applications "
            "that solve real-world problems."
        ),
        "skills": [
            "Python or Java",
            "Programming fundamentals",
            "Git and GitHub",
            "Data Structures and Algorithms",
            "Problem Solving",
            "Testing and Debugging",
            "APIs and Databases",
        ],
        "roadmap": {
            "estimated_duration": "6–9 months",
            "weekly_study_hours": "8–10 hours",
            "stages": [
                {
                    "title": "Programming Foundations",
                    "duration": "4 weeks",
                    "topics": [
                        "Variables, data types, and operators",
                        "Conditions and loops",
                        "Functions and modules",
                        "Lists, dictionaries, and strings",
                        "Error handling and debugging",
                    ],
                    "completion_goal": (
                        "Write 8–10 small programs independently."
                    ),
                },
                {
                    "title": "Object-Oriented Programming",
                    "duration": "3 weeks",
                    "topics": [
                        "Classes and objects",
                        "Constructors and methods",
                        "Inheritance and composition",
                        "File handling",
                        "Exceptions and modules",
                    ],
                    "completion_goal": (
                        "Build a command-line application using classes "
                        "and file storage."
                    ),
                },
                {
                    "title": "Git and GitHub",
                    "duration": "2 weeks",
                    "topics": [
                        "Repositories and commits",
                        "Branches and merges",
                        "README files",
                        "GitHub collaboration",
                    ],
                    "completion_goal": (
                        "Publish a documented project on GitHub."
                    ),
                },
                {
                    "title": "Data Structures and Algorithms",
                    "duration": "8 weeks",
                    "topics": [
                        "Arrays and strings",
                        "Stacks and queues",
                        "Hash maps",
                        "Searching and sorting",
                        "Big-O notation",
                        "Recursion and trees",
                    ],
                    "completion_goal": (
                        "Solve at least 40 beginner problems and explain "
                        "common time complexities."
                    ),
                },
                {
                    "title": "Databases and APIs",
                    "duration": "4 weeks",
                    "topics": [
                        "SQL fundamentals",
                        "Tables and relationships",
                        "CRUD operations",
                        "HTTP and JSON",
                        "REST APIs",
                    ],
                    "completion_goal": (
                        "Build an application that stores data and "
                        "exposes a small API."
                    ),
                },
                {
                    "title": "Testing and Portfolio Project",
                    "duration": "5–8 weeks",
                    "topics": [
                        "Unit testing",
                        "Input validation",
                        "Logging",
                        "Clean code",
                        "Deployment fundamentals",
                    ],
                    "completion_goal": (
                        "Publish a complete application with a README, "
                        "screenshots, and setup instructions."
                    ),
                },
            ],
        },
        "resources": [
            {
                "title": "Python Official Tutorial",
                "url": "https://docs.python.org/3/tutorial/",
            },
            {
                "title": "GitHub Skills",
                "url": "https://skills.github.com/",
            },
            {
                "title": "freeCodeCamp",
                "url": "https://www.freecodecamp.org/",
            },
            {
                "title": "LeetCode",
                "url": "https://leetcode.com/",
            },
        ],
    },

    {
        "id": "robotics",
        "title": "AI & Robotics Engineer",
        "category": "AI & Robotics",
        "description": (
            "Develop robots, autonomous systems, and intelligent "
            "machines using software, sensors, control, and AI."
        ),
        "skills": [
            "Python",
            "C++",
            "Linux and Git",
            "Linear Algebra",
            "Robot Kinematics",
            "ROS 2",
            "Gazebo",
            "Computer Vision",
            "Machine Learning",
        ],
        "roadmap": {
            "estimated_duration": "9–15 months",
            "weekly_study_hours": "8–12 hours",
            "stages": [
                {
                    "title": "Python for Robotics",
                    "duration": "4 weeks",
                    "topics": [
                        "Python fundamentals",
                        "Functions and classes",
                        "NumPy arrays and matrices",
                        "Processing sensor-like data",
                        "Git and GitHub",
                    ],
                    "completion_goal": (
                        "Write Python scripts that process arrays "
                        "and simulated sensor readings."
                    ),
                },
                {
                    "title": "C++ Fundamentals",
                    "duration": "6 weeks",
                    "topics": [
                        "Variables, data types, and operators",
                        "Conditions and loops",
                        "Functions and references",
                        "Pointers fundamentals",
                        "Vectors and strings",
                        "Classes and objects",
                        "Compilation and debugging",
                    ],
                    "completion_goal": (
                        "Build and compile a small multi-file C++ "
                        "program using classes and vectors."
                    ),
                },
                {
                    "title": "Linux, Mathematics, and Robotics Basics",
                    "duration": "4 weeks",
                    "topics": [
                        "Linux terminal commands",
                        "Git workflow",
                        "Vectors and matrices",
                        "Coordinate frames and rotations",
                        "Sensors and basic mechanics",
                    ],
                    "completion_goal": (
                        "Use a Linux development workspace and calculate "
                        "simple 2D coordinate transformations."
                    ),
                },
                {
                    "title": "Robot Kinematics",
                    "duration": "5 weeks",
                    "topics": [
                        "Robot joints and degrees of freedom",
                        "Forward kinematics",
                        "Inverse kinematics concepts",
                        "Denavit–Hartenberg parameters",
                        "Transformation matrices",
                        "Jacobian fundamentals",
                    ],
                    "completion_goal": (
                        "Model a 2–3 DOF robot arm and verify its "
                        "forward-kinematics calculations in code."
                    ),
                },
                {
                    "title": "ROS 2 Fundamentals",
                    "duration": "6 weeks",
                    "topics": [
                        "ROS 2 workspaces and packages",
                        "Nodes, topics, and messages",
                        "Publishers and subscribers",
                        "Services and actions",
                        "Launch files and parameters",
                        "Basic robot communication",
                    ],
                    "completion_goal": (
                        "Create a ROS 2 package containing two nodes "
                        "that communicate with each other."
                    ),
                },
                {
                    "title": "Gazebo Simulation",
                    "duration": "4 weeks",
                    "topics": [
                        "Gazebo worlds and models",
                        "URDF robot descriptions",
                        "Robot joints and sensors",
                        "Spawning a robot",
                        "ROS 2 and Gazebo integration",
                    ],
                    "completion_goal": (
                        "Spawn a robot in simulation and control a joint "
                        "or read simulated sensor data."
                    ),
                },
                {
                    "title": "Computer Vision and AI",
                    "duration": "6 weeks",
                    "topics": [
                        "OpenCV image processing",
                        "Colour and shape detection",
                        "Camera fundamentals",
                        "Dataset preparation",
                        "Machine learning basics",
                        "Model evaluation",
                    ],
                    "completion_goal": (
                        "Build a computer-vision demonstration that "
                        "detects a chosen object or visual feature."
                    ),
                },
                {
                    "title": "Robotics Capstone Project",
                    "duration": "4–8 weeks",
                    "topics": [
                        "Combine ROS 2 and simulation",
                        "Build a sensor-to-action pipeline",
                        "Test robot behaviour",
                        "Document the architecture",
                        "Record a demonstration",
                    ],
                    "completion_goal": (
                        "Demonstrate a simulated robot that senses, "
                        "makes a decision, and acts. Publish the "
                        "project with a README and screenshots."
                    ),
                },
            ],
        },
        "resources": [
            {
                "title": "Python Official Tutorial",
                "url": "https://docs.python.org/3/tutorial/",
            },
            {
                "title": "Learn C++",
                "url": "https://www.learncpp.com/",
            },
            {
                "title": "ROS 2 Documentation",
                "url": "https://docs.ros.org/",
            },
            {
                "title": "Gazebo Documentation",
                "url": "https://gazebosim.org/docs",
            },
            {
                "title": "OpenCV Tutorials",
                "url": "https://docs.opencv.org/",
            },
        ],
    },

    {
        "id": "data",
        "title": "Data Scientist",
        "category": "Data Science",
        "description": (
            "Use programming, statistics, and machine learning "
            "to discover patterns and support decisions with data."
        ),
        "skills": [
            "Python",
            "SQL",
            "Pandas",
            "NumPy",
            "Statistics",
            "Data Visualization",
            "Machine Learning",
            "Model Evaluation",
        ],
        "roadmap": {
            "estimated_duration": "6–10 months",
            "weekly_study_hours": "8–10 hours",
            "stages": [
                {
                    "title": "Python for Data",
                    "duration": "4 weeks",
                    "topics": [
                        "Python fundamentals",
                        "Functions and collections",
                        "NumPy arrays",
                        "Jupyter notebooks",
                        "CSV files",
                    ],
                    "completion_goal": (
                        "Load a CSV file and calculate summary statistics."
                    ),
                },
                {
                    "title": "Pandas and Data Cleaning",
                    "duration": "4 weeks",
                    "topics": [
                        "DataFrames and Series",
                        "Filtering and sorting",
                        "Missing values and duplicates",
                        "GroupBy and merge",
                        "Date and text processing",
                    ],
                    "completion_goal": (
                        "Clean a real dataset and explain your "
                        "data-cleaning decisions."
                    ),
                },
                {
                    "title": "SQL and Databases",
                    "duration": "4 weeks",
                    "topics": [
                        "SELECT and WHERE",
                        "GROUP BY and aggregate functions",
                        "JOIN operations",
                        "Subqueries",
                        "Basic database design",
                    ],
                    "completion_goal": (
                        "Answer at least 15 sample business questions "
                        "using SQL."
                    ),
                },
                {
                    "title": "Statistics and Visualization",
                    "duration": "5 weeks",
                    "topics": [
                        "Mean, median, and variance",
                        "Probability fundamentals",
                        "Sampling",
                        "Correlation versus causation",
                        "Charts and visualizations",
                    ],
                    "completion_goal": (
                        "Create an exploratory data report with charts "
                        "and evidence-based conclusions."
                    ),
                },
                {
                    "title": "Machine Learning",
                    "duration": "7 weeks",
                    "topics": [
                        "Training and testing datasets",
                        "Regression and classification",
                        "Data preprocessing",
                        "Overfitting and cross-validation",
                        "Evaluation metrics",
                    ],
                    "completion_goal": (
                        "Train and compare at least two models using "
                        "appropriate evaluation metrics."
                    ),
                },
                {
                    "title": "Data Science Portfolio Project",
                    "duration": "4–6 weeks",
                    "topics": [
                        "Choose a dataset",
                        "Define a meaningful question",
                        "Perform reproducible analysis",
                        "Visualize findings",
                        "Explain limitations",
                    ],
                    "completion_goal": (
                        "Publish a complete data project with a notebook, "
                        "visualizations, findings, and README."
                    ),
                },
            ],
        },
        "resources": [
            {
                "title": "Pandas Getting Started",
                "url": "https://pandas.pydata.org/docs/getting_started/",
            },
            {
                "title": "Kaggle Learn",
                "url": "https://www.kaggle.com/learn",
            },
            {
                "title": "SQLBolt",
                "url": "https://sqlbolt.com/",
            },
            {
                "title": "Scikit-learn Tutorials",
                "url": "https://scikit-learn.org/stable/tutorial/index.html",
            },
        ],
    },

    {
        "id": "cybersecurity",
        "title": "Cybersecurity Engineer",
        "category": "Technology",
        "description": (
            "Protect systems, networks, and applications through "
            "secure configuration, monitoring, and testing."
        ),
        "skills": [
            "Computer Networking",
            "Linux",
            "Python Scripting",
            "Operating Systems",
            "Security Principles",
            "Log Analysis",
            "Web Security",
        ],
        "roadmap": {
            "estimated_duration": "6–10 months",
            "weekly_study_hours": "7–10 hours",
            "stages": [
                {
                    "title": "Computer and Networking Foundations",
                    "duration": "5 weeks",
                    "topics": [
                        "Operating-system fundamentals",
                        "IP addresses and subnetting",
                        "DNS and HTTP/HTTPS",
                        "TCP and UDP",
                        "Ports, routers, and firewalls",
                    ],
                    "completion_goal": (
                        "Explain how a web request travels through a "
                        "network and use basic diagnostic tools."
                    ),
                },
                {
                    "title": "Linux and Scripting",
                    "duration": "4 weeks",
                    "topics": [
                        "Files and permissions",
                        "Users and processes",
                        "Shell commands",
                        "Python scripting",
                        "Log processing",
                    ],
                    "completion_goal": (
                        "Write a script that summarises events from "
                        "a sample log file."
                    ),
                },
                {
                    "title": "Security Fundamentals",
                    "duration": "4 weeks",
                    "topics": [
                        "Confidentiality, integrity, and availability",
                        "Authentication and authorization",
                        "Least privilege",
                        "Patching and backups",
                        "Threat modelling",
                    ],
                    "completion_goal": (
                        "Create a basic threat model and hardening "
                        "checklist for a test machine."
                    ),
                },
                {
                    "title": "Web and Application Security",
                    "duration": "5 weeks",
                    "topics": [
                        "Common web vulnerabilities",
                        "Input validation",
                        "Sessions and access control",
                        "Secure configuration",
                        "OWASP Top 10",
                    ],
                    "completion_goal": (
                        "Complete beginner labs in a legal training "
                        "environment and document remediation steps."
                    ),
                },
                {
                    "title": "Monitoring and Incident Response",
                    "duration": "5 weeks",
                    "topics": [
                        "Log review",
                        "Alert triage",
                        "Evidence handling",
                        "Incident-response lifecycle",
                    ],
                    "completion_goal": (
                        "Analyse sample logs and write a short "
                        "incident-response report."
                    ),
                },
                {
                    "title": "Defensive Security Portfolio",
                    "duration": "4–6 weeks",
                    "topics": [
                        "Build a safe home lab",
                        "Secure system configuration",
                        "Create log monitoring or detection rules",
                        "Document findings and fixes",
                    ],
                    "completion_goal": (
                        "Publish a defensive security project with "
                        "scope, findings, and remediation steps."
                    ),
                },
            ],
        },
        "resources": [
            {
                "title": "Cisco Skills for All",
                "url": "https://skillsforall.com/",
            },
            {
                "title": "OverTheWire Learning Games",
                "url": "https://overthewire.org/wargames/",
            },
            {
                "title": "OWASP Top 10",
                "url": "https://owasp.org/www-project-top-ten/",
            },
            {
                "title": "Linux Journey",
                "url": "https://linuxjourney.com/",
            },
        ],
    },

    {
        "id": "web",
        "title": "Web Developer",
        "category": "Technology",
        "description": (
            "Create accessible, responsive websites and web "
            "applications using frontend and backend technologies."
        ),
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "Responsive Design",
            "Git and GitHub",
            "APIs",
            "Backend Fundamentals",
            "Databases",
        ],
        "roadmap": {
            "estimated_duration": "4–7 months",
            "weekly_study_hours": "8–10 hours",
            "stages": [
                {
                    "title": "HTML Foundations",
                    "duration": "2 weeks",
                    "topics": [
                        "Semantic HTML",
                        "Headings and forms",
                        "Links and images",
                        "Accessibility basics",
                    ],
                    "completion_goal": (
                        "Build a multi-section webpage using "
                        "semantic HTML."
                    ),
                },
                {
                    "title": "CSS and Responsive Design",
                    "duration": "4 weeks",
                    "topics": [
                        "Selectors and box model",
                        "Flexbox and Grid",
                        "Typography and spacing",
                        "Media queries",
                        "Colour contrast",
                    ],
                    "completion_goal": (
                        "Build a landing page that works on mobile "
                        "and desktop screens."
                    ),
                },
                {
                    "title": "JavaScript",
                    "duration": "5 weeks",
                    "topics": [
                        "Variables and functions",
                        "Arrays and objects",
                        "DOM manipulation",
                        "Events and forms",
                        "Promises and async/await",
                    ],
                    "completion_goal": (
                        "Build an interactive application with "
                        "search, filtering, and form validation."
                    ),
                },
                {
                    "title": "Git and APIs",
                    "duration": "3 weeks",
                    "topics": [
                        "Commits and branches",
                        "Fetch API",
                        "JSON",
                        "Loading and error states",
                    ],
                    "completion_goal": (
                        "Connect a webpage to an API and handle "
                        "successful and failed requests."
                    ),
                },
                {
                    "title": "Backend and Databases",
                    "duration": "5 weeks",
                    "topics": [
                        "HTTP methods and status codes",
                        "REST APIs",
                        "CRUD operations",
                        "SQL fundamentals",
                        "Validation and CORS",
                    ],
                    "completion_goal": (
                        "Connect a frontend to a backend that "
                        "reads and writes database records."
                    ),
                },
                {
                    "title": "Capstone and Deployment",
                    "duration": "4–6 weeks",
                    "topics": [
                        "Testing",
                        "Accessibility improvements",
                        "Deployment",
                        "Documentation",
                    ],
                    "completion_goal": (
                        "Publish a polished full-stack project with "
                        "screenshots and a README."
                    ),
                },
            ],
        },
        "resources": [
            {
                "title": "MDN Web Docs",
                "url": "https://developer.mozilla.org/",
            },
            {
                "title": "freeCodeCamp",
                "url": "https://www.freecodecamp.org/",
            },
            {
                "title": "The Odin Project",
                "url": "https://www.theodinproject.com/",
            },
            {
                "title": "GitHub Skills",
                "url": "https://skills.github.com/",
            },
        ],
    },

    {
        "id": "entrepreneur",
        "title": "Entrepreneur",
        "category": "Business",
        "description": (
            "Turn a customer problem into a tested product or service "
            "and build a sustainable business around it."
        ),
        "skills": [
            "Problem Discovery",
            "Customer Interviews",
            "Market Research",
            "Business Models",
            "Communication",
            "Budgeting",
            "Marketing",
            "Experimentation",
        ],
        "roadmap": {
            "estimated_duration": "3–6 months for a first validated idea",
            "weekly_study_hours": "5–8 hours",
            "stages": [
                {
                    "title": "Problem Discovery",
                    "duration": "2 weeks",
                    "topics": [
                        "Choose a specific audience",
                        "Identify recurring problems",
                        "Write a clear problem statement",
                    ],
                    "completion_goal": (
                        "Describe a target user, their problem, "
                        "and evidence that the problem matters."
                    ),
                },
                {
                    "title": "Customer and Market Research",
                    "duration": "3 weeks",
                    "topics": [
                        "Customer interview questions",
                        "Competitor analysis",
                        "Market segments",
                        "Existing customer alternatives",
                    ],
                    "completion_goal": (
                        "Conduct 5–10 ethical customer interviews "
                        "and summarise the patterns."
                    ),
                },
                {
                    "title": "Business Model and Costs",
                    "duration": "3 weeks",
                    "topics": [
                        "Value proposition",
                        "Revenue models",
                        "Fixed and variable costs",
                        "Pricing assumptions",
                    ],
                    "completion_goal": (
                        "Create a one-page business model and "
                        "a basic cost and revenue estimate."
                    ),
                },
                {
                    "title": "Prototype and Validation",
                    "duration": "4 weeks",
                    "topics": [
                        "Minimum viable product",
                        "Build a simple prototype",
                        "Create a landing page",
                        "Collect user feedback",
                    ],
                    "completion_goal": (
                        "Show a prototype to target users and "
                        "collect measurable feedback."
                    ),
                },
                {
                    "title": "Marketing Experiment",
                    "duration": "4 weeks",
                    "topics": [
                        "Positioning",
                        "Marketing messages",
                        "Small launch experiment",
                        "Feedback and conversion tracking",
                    ],
                    "completion_goal": (
                        "Run a low-cost experiment and document "
                        "the results and lessons learned."
                    ),
                },
                {
                    "title": "Review and Next Steps",
                    "duration": "2 weeks",
                    "topics": [
                        "Review evidence",
                        "Update assumptions",
                        "Estimate budget and risks",
                        "Plan next steps",
                    ],
                    "completion_goal": (
                        "Prepare a concise pitch, basic budget, "
                        "and realistic next-step plan."
                    ),
                },
            ],
        },
        "resources": [
            {
                "title": "Y Combinator Startup School",
                "url": "https://www.startupschool.org/",
            },
            {
                "title": "Strategyzer",
                "url": "https://www.strategyzer.com/",
            },
            {
                "title": "SBA Business Guide",
                "url": "https://www.sba.gov/business-guide",
            },
        ],
    },
]


# =====================================================
# REQUEST MODEL
# =====================================================

class RecommendationRequest(BaseModel):
    interest: str = Field(min_length=1, max_length=100)
    strength: str = Field(min_length=1, max_length=100)
    experience: str = Field(min_length=1, max_length=50)


# =====================================================
# ROOT AND HEALTH CHECK
# =====================================================

@app.get("/")
def home():
    return {
        "message": "Welcome to CareerPathAI Backend!",
        "status": "running",
        "documentation": "/docs",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "CareerPathAI",
    }


# =====================================================
# GET ALL CAREERS
# =====================================================

@app.get("/api/careers")
def get_careers():
    return {
        "total": len(CAREERS),
        "careers": CAREERS,
    }


# =====================================================
# GET CAREER DETAILS, ROADMAP, AND RESOURCES
# =====================================================

@app.get("/api/careers/{career_id}")
def get_career(career_id: str):
    for career in CAREERS:
        if career["id"] == career_id.lower():
            return career

    raise HTTPException(
        status_code=404,
        detail="Career not found.",
    )


# =====================================================
# RULES-BASED CAREER RECOMMENDATION
# =====================================================

def choose_career(interest: str, strength: str) -> str:
    combined = f"{interest} {strength}".lower()

    if any(
        word in combined
        for word in [
            "robot",
            "artificial intelligence",
            "machine learning",
            "autonomous",
        ]
    ):
        return "robotics"

    if any(
        word in combined
        for word in [
            "cybersecurity",
            "cyber security",
            "security",
            "networking",
            "ethical hacking",
        ]
    ):
        return "cybersecurity"

    if any(
        word in combined
        for word in [
            "data science",
            "data analysis",
            "analytics",
            "statistics",
            "data",
        ]
    ):
        return "data"

    if any(
        word in combined
        for word in [
            "web development",
            "website",
            "frontend",
            "front-end",
            "backend",
            "web",
        ]
    ):
        return "web"

    if any(
        word in combined
        for word in [
            "business",
            "entrepreneur",
            "startup",
            "leadership",
            "marketing",
        ]
    ):
        return "entrepreneur"

    return "software"


@app.post("/api/recommend")
def recommend_career(request: RecommendationRequest):
    career_id = choose_career(
        request.interest.strip(),
        request.strength.strip(),
    )

    career = next(
        item for item in CAREERS
        if item["id"] == career_id
    )

    return {
        "message": "Career recommendation generated successfully.",
        "recommendation_type": "rules-based",
        "input": {
            "interest": request.interest,
            "strength": request.strength,
            "experience": request.experience,
        },
        "recommended_career": career,
    }