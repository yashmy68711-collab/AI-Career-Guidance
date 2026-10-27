CareerPathAI 🚀

AI-Based Career Guidance Platform

CareerPathAI is a web-based career guidance platform designed to help students explore career options based on their interests, strengths, and experience. It provides career information, required skills, learning roadmaps, and learning resources to help users plan their professional journeys.

📅 Development Progress

Day 1 — Project Planning and Initial Setup
Defined the main objective of the CareerPathAI project.
Planned a platform to help students explore suitable career paths.
Identified the core features required for the application.
Planned the frontend and backend architecture.
Created the initial project structure with separate frontend and backend directories.
Started developing the user interface using HTML, CSS, and JavaScript.
Goal: Establish the project foundation and define its main features.

Day 2 — Frontend Development
Developed the initial website interface.
Created the navigation bar and homepage hero section.
Added career cards to display different career options.
Implemented career categories and filtering functionality.
Added a search feature to help users find careers.
Improved the layout and styling using CSS.
Used JavaScript to make the frontend interactive.
Goal: Build an interactive and user-friendly career exploration interface.


Day 3 — Backend Development and API Integration Preparation

    Started developing the backend using Python and FastAPI.
    Created the backend application and API endpoints.
    Organized career information in the backend.
    Implemented endpoints to retrieve available careers and individual career details.
    Added a basic health-check endpoint to verify that the backend is running.
    Prepared the backend structure for career recommendation functionality.

Goal: Establish the backend and create APIs to provide career information.
Day 4 — Career Recommendation and Learning Roadmaps

    Expanded the backend career database to cover six career paths:

        Software Developer
        AI and Robotics Engineer
        Data Scientist
        Cybersecurity Engineer
        Web Developer
        Entrepreneur

    Added career descriptions and required skills.
    Created detailed learning roadmaps for the six career paths.
    Organized roadmaps into stages with estimated durations, topics, and completion goals.
    Added recommended learning resources for each career.
    Implemented a rules-based career recommendation system using user interests and strengths.
    Updated the JavaScript functionality to fetch career information from the backend.
    Added functionality to display career details, skills, learning roadmaps, and resources.
    Added roadmap stage checkboxes and local storage support for tracking completed stages.
    Improved the assessment results section to display the recommended career and its learning roadmap.

Goal: Connect career recommendations with structured learning roadmaps so students can understand what to learn and track their progress.
✨ Key Features

    Explore six different career paths.
    Search for careers by name.
    Filter careers by category.
    View career descriptions and required skills.
    Receive career recommendations based on interests and strengths.
    Access structured learning roadmaps.
    View estimated roadmap durations and learning goals.
    Explore recommended learning resources.
    Track completed roadmap stages using browser local storage.

🛠️ Technologies Used
Frontend

    HTML5
    CSS3
    JavaScript

🔌 Main API Endpoints
Method	Endpoint	Purpose
GET	/	Check the backend welcome endpoint
GET	/health	Check backend health
GET	/api/careers	Retrieve all career options
GET	/api/careers/{career_id}	Retrieve details for a specific career
POST	/api/recommend	Generate a career recommendation
▶️ Running the Project
1. Start the Backend

From the project root directory, run:

python3 -m uvicorn backend.main:app --reload

Backend URL: http://127.0.0.1:8000

Interactive API documentation: http://127.0.0.1:8000/docs
2. Start the Frontend

Open a second terminal and run:

python3 -m http.server 5500 --directory frontend

Frontend URL: http://127.0.0.1:5500
3. Test the Application

    Open the frontend in your browser.
    Explore the available career options.
    Try the career search and category filters.
    Open a career to view its skills and learning roadmap.
    Complete the career assessment to see the recommendation.

🔮 Future Improvements

    Integrate AI or machine learning for more personalized career recommendations.
    Add user accounts and authentication.
    Save learning progress to a database.
    Add quizzes and skill assessments.
    Recommend courses based on each student's skill level.
    Improve the user interface and mobile responsiveness.
    Deploy the application so users can access it online.

📌 Project Status

Current Stage: Day 4 — Career recommendations and detailed learning roadmaps.

The project currently uses a rules-based recommendation system. AI/ML-based recommendations and other advanced features are potential future improvements.
