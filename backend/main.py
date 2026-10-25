from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


app = FastAPI(
    title="CareerPathAI API",
    description="Career recommendations and structured learning roadmaps.",
    version="2.0.0",
)


# ============================================================
# CORS
# ============================================================

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


# ============================================================
# CAREER DATABASE
# ============================================================

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
            "Python or Java",
            "Data Structures and Algorithms",
            "Object-Oriented Programming",
            "Git and GitHub",
            "SQL and APIs",
            "Problem Solving",
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
            "Linear Algebra",
            "Robot Kinematics",
            "ROS 2",
            "Gazebo",
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
            "Statistics and Probability",
            "NumPy",
            "Pandas",
            "SQL",
            "Data Visualization",
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
            "Linux",
            "Computer Networks",
            "Operating Systems",
            "Python",
            "Web Security",
            "Security Fundamentals",
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
            "Responsive Design",
            "Git and GitHub",
            "APIs",
            "Backend Fundamentals",
        ],
    },
    {
        "id": "entrepreneur",
        "title": "Entrepreneur",
        "category": "Business",
        "description": (
            "Turn innovative ideas into useful products "
            "and sustainable businesses."
        ),
        "skills": [
            "Problem Solving",
            "Market Research",
            "Communication",
            "Business Planning",
            "Financial Literacy",
            "Marketing",
            "Leadership",
        ],
    },
]


# ============================================================
# LEARNING ROADMAP DATABASE
#
# Durations are estimates, not guarantees.
# Assume approximately 8-12 hours of learning per week.
# ============================================================

ROADMAPS = {
    "software": {
        "estimated_duration": "6-9 months",
        "weekly_study_hours": "8-12 hours",
        "stages": [
            {
                "title": "Programming Fundamentals",
                "duration": "4-6 weeks",
                "topics": [
                    "Variables and data types",
                    "Conditions and loops",
                    "Functions",
                    "Lists, dictionaries, and sets",
                    "File handling and exceptions",
                ],
                "completion_goal": (
                    "Write small programs independently "
                    "and solve basic coding problems."
                ),
                "project": "Command-line expense tracker",
            },
            {
                "title": "Object-Oriented Programming",
                "duration": "3-4 weeks",
                "topics": [
                    "Classes and objects",
                    "Constructors",
                    "Inheritance and composition",
                    "Encapsulation",
                    "Exception handling",
                ],
                "completion_goal": (
                    "Organize a program into reusable classes "
                    "and modules."
                ),
                "project": "Library management application",
            },
            {
                "title": "Data Structures and Algorithms",
                "duration": "6-8 weeks",
                "topics": [
                    "Arrays and strings",
                    "Stacks and queues",
                    "Linked lists",
                    "Trees and hash maps",
                    "Searching and sorting",
                    "Time and space complexity",
                ],
                "completion_goal": (
                    "Choose suitable data structures and "
                    "explain the complexity of your solutions."
                ),
                "project": "Algorithm practice repository",
            },
            {
                "title": "Databases and APIs",
                "duration": "4-5 weeks",
                "topics": [
                    "SQL and relational databases",
                    "CRUD operations",
                    "HTTP and REST APIs",
                    "JSON",
                    "Backend validation",
                ],
                "completion_goal": (
                    "Build an application that stores data "
                    "and exposes API endpoints."
                ),
                "project": "Task management API",
            },
            {
                "title": "Git, Testing, and Deployment",
                "duration": "3-4 weeks",
                "topics": [
                    "Git and GitHub",
                    "Unit testing",
                    "Debugging",
                    "Environment variables",
                    "Application deployment",
                ],
                "completion_goal": (
                    "Publish a documented project that "
                    "another person can run."
                ),
                "project": "Deploy a complete portfolio application",
            },
        ],
        "resources": [
            {
                "name": "Python Tutorial",
                "url": "https://docs.python.org/3/tutorial/",
            },
            {
                "name": "GitHub Skills",
                "url": "https://skills.github.com/",
            },
            {
                "name": "freeCodeCamp",
                "url": "https://www.freecodecamp.org/",
            },
        ],
    },

    "robotics": {
        "estimated_duration": "8-12 months",
        "weekly_study_hours": "8-12 hours",
        "stages": [
            {
                "title": "Python for Robotics",
                "duration": "3-4 weeks",
                "topics": [
                    "Functions and modules",
                    "Object-oriented programming",
                    "File handling and exceptions",
                    "NumPy arrays and matrices",
                    "Plotting sensor data",
                ],
                "completion_goal": (
                    "Write reusable Python programs and "
                    "process numerical data."
                ),
                "project": "Simulated robot sensor-data analyzer",
            },
            {
                "title": "C++ Fundamentals",
                "duration": "4-6 weeks",
                "topics": [
                    "Variables, conditions, and loops",
                    "Functions and references",
                    "Pointers and memory basics",
                    "Classes and objects",
                    "Constructors and inheritance",
                    "STL containers and algorithms",
                    "Compilation and debugging",
                ],
                "completion_goal": (
                    "Write and compile a multi-file C++ program "
                    "using classes, vectors, and functions."
                ),
                "project": "C++ robot command and sensor simulator",
            },
            {
                "title": "Mathematics for Robotics",
                "duration": "4-6 weeks",
                "topics": [
                    "Vectors and coordinate systems",
                    "Matrices and matrix multiplication",
                    "Trigonometry",
                    "Rotation matrices",
                    "Basic calculus concepts",
                    "Basic probability",
                ],
                "completion_goal": (
                    "Calculate coordinate transformations and "
                    "perform basic vector and matrix operations."
                ),
                "project": "2D robot coordinate transformation tool",
            },
            {
                "title": "Robotics Fundamentals and Kinematics",
                "duration": "4-6 weeks",
                "topics": [
                    "Robot links and joints",
                    "Degrees of freedom",
                    "Coordinate frames",
                    "Forward kinematics",
                    "Inverse kinematics",
                    "DH parameters",
                    "Basic Jacobian concepts",
                ],
                "completion_goal": (
                    "Calculate the end-effector position of a "
                    "simple robot arm for known joint angles."
                ),
                "project": "Two-link robotic arm kinematics simulator",
            },
            {
                "title": "ROS 2",
                "duration": "4-6 weeks",
                "topics": [
                    "ROS 2 workspace and packages",
                    "Nodes and executors",
                    "Topics and messages",
                    "Publishers and subscribers",
                    "Services and parameters",
                    "Launch files",
                    "Python and C++ ROS 2 nodes",
                ],
                "completion_goal": (
                    "Create a ROS 2 package with communicating "
                    "nodes and run it successfully."
                ),
                "project": "ROS 2 robot telemetry and control nodes",
            },
            {
                "title": "Robot Simulation with Gazebo",
                "duration": "3-4 weeks",
                "topics": [
                    "Robot models and links",
                    "Joints and physics",
                    "Sensors in simulation",
                    "Robot spawning",
                    "Movement and control",
                    "Connecting ROS 2 to simulation",
                ],
                "completion_goal": (
                    "Spawn a robot in simulation, observe its "
                    "sensors, and control its movement."
                ),
                "project": "Simulated mobile robot controlled with ROS 2",
            },
            {
                "title": "Computer Vision",
                "duration": "4-6 weeks",
                "topics": [
                    "Images and color spaces",
                    "OpenCV image processing",
                    "Thresholding and contours",
                    "Camera input",
                    "Object detection fundamentals",
                    "Connecting vision output to robot behavior",
                ],
                "completion_goal": (
                    "Process camera images and identify a simple "
                    "object or visual feature."
                ),
                "project": "Camera-based object detection prototype",
            },
            {
                "title": "Integration and Portfolio",
                "duration": "4-6 weeks",
                "topics": [
                    "Combine ROS 2 and simulation",
                    "Connect perception to robot behavior",
                    "Test and debug the system",
                    "Write clear documentation",
                    "Record a project demonstration",
                ],
                "completion_goal": (
                    "Demonstrate a working robotics system and "
                    "explain its design and limitations."
                ),
                "project": "Autonomous simulated robot using camera input",
            },
        ],
        "resources": [
            {
                "name": "Official C++ Documentation",
                "url": "https://isocpp.org/",
            },
            {
                "name": "ROS 2 Tutorials",
                "url": "https://docs.ros.org/en/jazzy/Tutorials.html",
            },
            {
                "name": "Gazebo Documentation",
                "url": "https://gazebosim.org/docs",
            },
            {
                "name": "OpenCV Tutorials",
                "url": "https://docs.opencv.org/",
            },
        ],
    },

    "data": {
        "estimated_duration": "6-9 months",
        "weekly_study_hours": "8-12 hours",
        "stages": [
            {
                "title": "Python Fundamentals",
                "duration": "4-6 weeks",
                "topics": [
                    "Python syntax and data types",
                    "Functions and modules",
                    "Lists and dictionaries",
                    "File handling",
                    "Exceptions",
                ],
                "completion_goal": (
                    "Write scripts to load, transform, and "
                    "summarize simple datasets."
                ),
                "project": "CSV data summary tool",
            },
            {
                "title": "Mathematics and Statistics",
                "duration": "4-6 weeks",
                "topics": [
                    "Mean, median, and variance",
                    "Probability",
                    "Distributions",
                    "Correlation",
                    "Sampling and hypothesis basics",
                ],
                "completion_goal": (
                    "Explain basic statistical measures and "
                    "interpret simple data distributions."
                ),
                "project": "Exploratory statistical report",
            },
            {
                "title": "NumPy and Pandas",
                "duration": "4-5 weeks",
                "topics": [
                    "Arrays and vectorized operations",
                    "DataFrames and Series",
                    "Missing-value handling",
                    "Filtering and grouping",
                    "Merging datasets",
                ],
                "completion_goal": (
                    "Clean and analyze a real-world dataset."
                ),
                "project": "Complete data-cleaning notebook",
            },
            {
                "title": "SQL and Visualization",
                "duration": "4-5 weeks",
                "topics": [
                    "SELECT and WHERE",
                    "GROUP BY and JOIN",
                    "Subqueries",
                    "Charts and distributions",
                    "Communicating findings",
                ],
                "completion_goal": (
                    "Answer business questions using SQL and "
                    "present findings visually."
                ),
                "project": "Sales analytics dashboard",
            },
            {
                "title": "Machine Learning Fundamentals",
                "duration": "6-8 weeks",
                "topics": [
                    "Train, validation, and test sets",
                    "Regression",
                    "Classification",
                    "Feature engineering",
                    "Model evaluation",
                    "Overfitting and data leakage",
                ],
                "completion_goal": (
                    "Train and evaluate a baseline predictive model."
                ),
                "project": "House-price or customer-churn prediction",
            },
            {
                "title": "Portfolio Project",
                "duration": "3-4 weeks",
                "topics": [
                    "Problem definition",
                    "Data preparation",
                    "Model comparison",
                    "Visualization",
                    "Documentation",
                ],
                "completion_goal": (
                    "Present a reproducible analysis with "
                    "clear conclusions and limitations."
                ),
                "project": "End-to-end data science case study",
            },
        ],
        "resources": [
            {
                "name": "Pandas Documentation",
                "url": "https://pandas.pydata.org/docs/",
            },
            {
                "name": "Kaggle Learn",
                "url": "https://www.kaggle.com/learn",
            },
            {
                "name": "Scikit-learn Documentation",
                "url": "https://scikit-learn.org/stable/",
            },
        ],
    },

    "cybersecurity": {
        "estimated_duration": "6-10 months",
        "weekly_study_hours": "8-12 hours",
        "stages": [
            {
                "title": "Linux and Operating Systems",
                "duration": "4-5 weeks",
                "topics": [
                    "Linux commands",
                    "Files and permissions",
                    "Processes",
                    "Users and groups",
                    "Shell scripting basics",
                ],
                "completion_goal": (
                    "Navigate Linux and perform basic "
                    "system administration tasks."
                ),
                "project": "Linux system information script",
            },
            {
                "title": "Networking Fundamentals",
                "duration": "4-6 weeks",
                "topics": [
                    "TCP/IP",
                    "IP addresses and subnets",
                    "DNS and DHCP",
                    "HTTP and HTTPS",
                    "Ports and common protocols",
                ],
                "completion_goal": (
                    "Explain how a client communicates with "
                    "a server and diagnose basic connectivity issues."
                ),
                "project": "Network protocol study report",
            },
            {
                "title": "Python and Automation",
                "duration": "3-4 weeks",
                "topics": [
                    "Python fundamentals",
                    "Files and logs",
                    "Regular expressions",
                    "Error handling",
                    "Automation scripts",
                ],
                "completion_goal": (
                    "Write a script that safely analyzes "
                    "sample system logs."
                ),
                "project": "Log analysis tool",
            },
            {
                "title": "Security Fundamentals",
                "duration": "4-6 weeks",
                "topics": [
                    "Confidentiality, integrity, and availability",
                    "Authentication and authorization",
                    "Encryption fundamentals",
                    "Common web vulnerabilities",
                    "Security updates and backups",
                ],
                "completion_goal": (
                    "Identify common security risks and "
                    "recommend basic defensive controls."
                ),
                "project": "Security checklist for a demo application",
            },
            {
                "title": "Legal Security Labs",
                "duration": "4-6 weeks",
                "topics": [
                    "Web request inspection",
                    "Secure configuration",
                    "Vulnerability assessment concepts",
                    "Lab-based testing",
                    "Responsible disclosure",
                ],
                "completion_goal": (
                    "Complete guided exercises in authorized "
                    "training environments and document findings."
                ),
                "project": "Write a lab security assessment report",
            },
            {
                "title": "Defensive Security Portfolio",
                "duration": "3-4 weeks",
                "topics": [
                    "Security logging",
                    "Basic incident response",
                    "Risk assessment",
                    "Documentation",
                ],
                "completion_goal": (
                    "Present a defensive security project with "
                    "clear findings and remediation steps."
                ),
                "project": "Security monitoring and incident report",
            },
        ],
        "resources": [
            {
                "name": "Cisco Networking Academy",
                "url": "https://www.netacad.com/",
            },
            {
                "name": "OWASP",
                "url": "https://owasp.org/",
            },
            {
                "name": "TryHackMe",
                "url": "https://tryhackme.com/",
            },
        ],
    },

    "web": {
        "estimated_duration": "4-7 months",
        "weekly_study_hours": "8-12 hours",
        "stages": [
            {
                "title": "HTML Fundamentals",
                "duration": "2-3 weeks",
                "topics": [
                    "Semantic HTML",
                    "Headings and sections",
                    "Links and images",
                    "Forms",
                    "Accessibility basics",
                ],
                "completion_goal": (
                    "Create a structured multi-page website."
                ),
                "project": "Personal profile website",
            },
            {
                "title": "CSS and Responsive Design",
                "duration": "3-4 weeks",
                "topics": [
                    "Selectors and the box model",
                    "Flexbox",
                    "CSS Grid",
                    "Typography and colors",
                    "Responsive layouts",
                ],
                "completion_goal": (
                    "Build a consistent layout that works "
                    "on mobile and desktop."
                ),
                "project": "Responsive landing page",
            },
            {
                "title": "JavaScript",
                "duration": "5-7 weeks",
                "topics": [
                    "Variables and functions",
                    "Arrays and objects",
                    "DOM manipulation",
                    "Events and forms",
                    "Promises and async/await",
                ],
                "completion_goal": (
                    "Build interactive features without "
                    "relying on copied code."
                ),
                "project": "Interactive task manager",
            },
            {
                "title": "Git and APIs",
                "duration": "3-4 weeks",
                "topics": [
                    "Git and GitHub",
                    "HTTP and JSON",
                    "Fetch API",
                    "Error handling",
                    "Browser developer tools",
                ],
                "completion_goal": (
                    "Connect a frontend to a public or "
                    "locally developed API."
                ),
                "project": "Weather or information dashboard",
            },
            {
                "title": "Backend and Databases",
                "duration": "5-7 weeks",
                "topics": [
                    "HTTP requests and responses",
                    "REST APIs",
                    "Database fundamentals",
                    "Input validation",
                    "Authentication basics",
                ],
                "completion_goal": (
                    "Build an API that stores and retrieves data."
                ),
                "project": "Full-stack task management application",
            },
            {
                "title": "Testing and Deployment",
                "duration": "3-4 weeks",
                "topics": [
                    "Testing and debugging",
                    "Environment variables",
                    "Deployment",
                    "Documentation",
                    "Basic security practices",
                ],
                "completion_goal": (
                    "Publish a working application and "
                    "document how to run it."
                ),
                "project": "Deploy a complete portfolio project",
            },
        ],
        "resources": [
            {
                "name": "MDN Web Docs",
                "url": "https://developer.mozilla.org/",
            },
            {
                "name": "freeCodeCamp",
                "url": "https://www.freecodecamp.org/",
            },
            {
                "name": "GitHub Skills",
                "url": "https://skills.github.com/",
            },
        ],
    },

    "entrepreneur": {
        "estimated_duration": "4-8 months",
        "weekly_study_hours": "6-10 hours",
        "stages": [
            {
                "title": "Problem Discovery",
                "duration": "2-3 weeks",
                "topics": [
                    "Identify real customer problems",
                    "Interview potential customers",
                    "Research existing solutions",
                    "Define a target audience",
                ],
                "completion_goal": (
                    "Describe one specific problem and the "
                    "people who experience it."
                ),
                "project": "Customer discovery report",
            },
            {
                "title": "Market Research",
                "duration": "3-4 weeks",
                "topics": [
                    "Competitor analysis",
                    "Market segmentation",
                    "Customer needs",
                    "Value proposition",
                ],
                "completion_goal": (
                    "Explain who the product serves and "
                    "why customers might choose it."
                ),
                "project": "Market research presentation",
            },
            {
                "title": "Business Model and Finance",
                "duration": "4-5 weeks",
                "topics": [
                    "Business model canvas",
                    "Revenue and costs",
                    "Pricing fundamentals",
                    "Cash flow",
                    "Basic budgeting",
                ],
                "completion_goal": (
                    "Prepare a basic business model and "
                    "financial estimate."
                ),
                "project": "Business model and budget plan",
            },
            {
                "title": "Prototype and Validation",
                "duration": "4-6 weeks",
                "topics": [
                    "Define minimum viable product",
                    "Create a prototype",
                    "Collect customer feedback",
                    "Prioritize improvements",
                ],
                "completion_goal": (
                    "Test an early version of the idea with "
                    "potential users."
                ),
                "project": "Prototype or MVP",
            },
            {
                "title": "Marketing and Sales",
                "duration": "3-4 weeks",
                "topics": [
                    "Brand positioning",
                    "Content and digital marketing",
                    "Customer acquisition",
                    "Sales fundamentals",
                    "Measuring results",
                ],
                "completion_goal": (
                    "Create a simple marketing plan and "
                    "define how to measure its performance."
                ),
                "project": "Marketing campaign plan",
            },
            {
                "title": "Launch and Improvement",
                "duration": "3-4 weeks",
                "topics": [
                    "Launch planning",
                    "Customer support",
                    "Feedback collection",
                    "Basic business metrics",
                    "Iterative improvement",
                ],
                "completion_goal": (
                    "Present a launch plan based on customer "
                    "feedback and basic financial assumptions."
                ),
                "project": "Business launch proposal",
            },
        ],
        "resources": [
            {
                "name": "Y Combinator Startup Library",
                "url": "https://www.ycombinator.com/library",
            },
            {
                "name": "Startup India",
                "url": "https://www.startupindia.gov.in/",
            },
        ],
    },
}


# ============================================================
# REQUEST MODEL
# ============================================================

class RecommendationRequest(BaseModel):
    interest: str = Field(min_length=1, max_length=100)
    strength: str = Field(min_length=1, max_length=100)
    experience: str = Field(min_length=1, max_length=50)


# ============================================================
# HELPERS
# ============================================================

def get_career_details(career_id: str):
    career = next(
        (
            item for item in CAREERS
            if item["id"] == career_id
        ),
        None,
    )

    if career is None:
        return None

    # Return a new object so roadmap information is included
    # without modifying the original career record.
    result = career.copy()
    result["roadmap"] = ROADMAPS[career_id]

    return result


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def home():
    return {
        "message": "Welcome to CareerPathAI Backend!",
        "status": "running",
        "documentation": "/docs",
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "CareerPathAI",
    }


# ============================================================
# GET ALL CAREERS
# ============================================================

@app.get("/api/careers")
def get_careers():
    return {
        "total": len(CAREERS),
        "careers": [
            get_career_details(career["id"])
            for career in CAREERS
        ],
    }


# ============================================================
# GET ONE CAREER AND ITS ROADMAP
# ============================================================

@app.get("/api/careers/{career_id}")
def get_career(career_id: str):
    career = get_career_details(career_id.lower())

    if career is None:
        raise HTTPException(
            status_code=404,
            detail="Career not found.",
        )

    return career


# ============================================================
# CAREER RECOMMENDATION
# Rules-based recommendation; not a trained AI model.
# ============================================================

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

    recommended_career = get_career_details(career_id)

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