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

Day 5 — Learning Academy and Topic-Level Learning

    Added a dedicated Learning Academy section to the frontend.
    Integrated the Academy with the existing FastAPI career endpoints.
    Added a career selection dropdown populated with career data from the backend.
    Organized career roadmaps into curriculum modules and individual learning topics.
    Added learning objectives for each topic.
    Created topic-specific subtopic outlines to support structured learning.
    Added generated study notes to help learners review important concepts.
    Included practice tasks to encourage hands-on learning.
    Added YouTube search links for topics and subtopics.
    Implemented previous-topic and next-topic navigation.
    Added functionality to mark topics as completed or incomplete.
    Implemented browser local storage to preserve topic completion progress.
    Added a progress indicator showing the percentage of completed topics.
    Added a print option so learners can print their study notes or save them as PDF.
    Improved the Academy layout with responsive styling for different screen sizes.

Note: Study notes are generated learning prompts rather than complete textbook chapters. Tutorial links open YouTube search results; individual videos are not automatically verified.
The project currently uses a rules-based recommendation system. AI/ML-based recommendations and other advanced features are potential future improvements.

Day 6 — Learning Academy and Assessment System

CareerPathAI currently includes:
Career exploration across six career paths.
Rules-based career recommendations.
Structured learning roadmaps.
Topic-level Learning Academy.
Generated study notes and practice tasks.
Topic-wise and subtopic-wise MCQ assessments.
Automatic evaluation, scoring, and answer explanations.
Browser-based learning progress and quiz-result storage.
The project currently uses a rules-based recommendation system and a frontend-based assessment engine. AI/ML integration, database-backed progress tracking, and more advanced assessment features are planned for future development.

✨ Key Features
1. Career Exploration
    Explore six different career paths.
    Search for careers by name.
    Filter careers by category.
    View career descriptions and required skills.

2. Career Assessment
    Receive career recommendations based on interests and strengths.
    View recommended careers and their learning roadmaps.

3. Learning Roadmaps

    Access structured learning roadmaps for different careers.
    View roadmap stages, topics, estimated durations, and completion goals.
    Explore recommended learning resources.
    Track completed roadmap stages using browser local storage.

4. Learning Academy

    Select a career and load its curriculum from the backend.
    Browse curriculum modules and learning topics.
    Review learning objectives and subtopic outlines.
    Access study notes and practice tasks.
    Open YouTube tutorial searches.
    Navigate between learning topics.
    Mark topics as completed or incomplete.
    Track learning progress through a percentage indicator.
    Print study notes or save them as PDF.
    Preserve topic completion progress using browser local storage.

5. Assessment System

    Topic-wise MCQ assessments.
    Subtopic-wise MCQ assessments.
    Multiple-choice question navigation.
    Automatic answer evaluation.
    Instant score calculation.
    70% passing threshold.
    Pass and retake functionality.
    Correct-answer review.
    Explanations for answers.
    Save assessment results using browser local storage.

   🛠️ Technology Stack

Frontend

HTML5
CSS3
JavaScript

Backend

Python
FastAPI
Data and Progress Management
Backend-managed career and roadmap data.
JavaScript-based quiz question bank.
Browser local storage for learning progress and quiz results.

📁 Main Project Structure

Project_career-guidance/
│
├── backend/
│   └── main.py
│
├── frontend/
│   │
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   ├── script.js
│   │   ├── academy.js
│   │   ├── quiz-data.js
│   │   └── quiz.js
│   │
│   └── index.html
│
├── .gitignore
├── README.md
└── requirements.txt

🔌 Main API Endpoints

Method
Endpoint
Purpose
GET
/

Backend welcome endpoint
GET
/health
Check backend health

GET
/api/careers
Retrieve all available careers

GET
/api/careers/{career_id}
Retrieve details and roadmap for a career

POST
/api/recommend
Generate a career recommendation
The Learning Academy uses the existing career endpoints to retrieve career information and roadmap topics.
The quiz system currently runs on the frontend using its JavaScript question bank.

▶️ Running the Project

1. Clone the Repository

git clone https://github.com/yashmy68711-collab/AI-Career-Guidance.git
cd Project_career-guidance

2. Activate the Virtual Environment

source .venv/bin/activate
If the virtual environment does not exist, create it:
python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Start the Backend

python3 -m uvicorn backend.main:app --reload
Backend URL: http://127.0.0.1:8000
Interactive API documentation: http://127.0.0.1:8000/docs

5. Start the Frontend

Open a second terminal:
python3 -m http.server 5500 --directory frontend
Frontend URL: http://127.0.0.1:5500

6. Test the Application

Open CareerPathAI in your browser.
Explore the available career options.
Try the career search and category filters.
Open a career to view its skills and learning roadmap.
Complete the career assessment.
Open the Learning Academy.
Select a career and explore its curriculum.
Read topic notes and explore subtopics.
Attempt topic-wise and subtopic-wise MCQ tests.
Submit assessments and review scores and explanations.
Retake assessments and check saved results.
