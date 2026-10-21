"use strict";

document.addEventListener("DOMContentLoaded", () => {

    // ============================================================
    // 1. CAREER DATABASE
    // ============================================================

    const careers = {
        software: {
            id: "software",
            title: "Software Developer",
            category: "technology",

            description:
                "Build applications, websites, and software solutions to solve real-world problems.",

            skills: [
                "Python or Java",
                "Data Structures and Algorithms",
                "Object-Oriented Programming",
                "Git and GitHub",
                "Problem Solving"
            ],

            roadmap: [
                "Learn a programming language such as Python or Java.",
                "Master Data Structures and Algorithms.",
                "Learn Object-Oriented Programming.",
                "Build projects and upload them to GitHub.",
                "Learn databases, APIs, and software development tools.",
                "Apply for internships and entry-level software positions."
            ],

            resources: [
                {
                    name: "freeCodeCamp",
                    url: "https://www.freecodecamp.org/"
                },
                {
                    name: "GitHub",
                    url: "https://github.com/"
                },
                {
                    name: "LeetCode",
                    url: "https://leetcode.com/"
                }
            ]
        },

        robotics: {
            id: "robotics",
            title: "AI & Robotics Engineer",
            category: "ai",

            description:
                "Develop intelligent robots, autonomous systems, and AI-powered machines.",

            skills: [
                "Python",
                "C++",
                "ROS 2",
                "Robot Kinematics",
                "Computer Vision",
                "Machine Learning"
            ],

            roadmap: [
                "Learn Python and C++ programming.",
                "Strengthen mathematics, linear algebra, and basic physics.",
                "Study robot joints, degrees of freedom, and kinematics.",
                "Learn ROS 2 and robot communication.",
                "Practice robot simulation using Gazebo or Webots.",
                "Learn computer vision and machine learning.",
                "Build robotics projects and document them on GitHub."
            ],

            resources: [
                {
                    name: "ROS 2 Documentation",
                    url: "https://docs.ros.org/"
                },
                {
                    name: "Gazebo Documentation",
                    url: "https://gazebosim.org/docs"
                },
                {
                    name: "OpenCV Documentation",
                    url: "https://docs.opencv.org/"
                },
                {
                    name: "Kaggle",
                    url: "https://www.kaggle.com/"
                }
            ]
        },

        data: {
            id: "data",
            title: "Data Scientist",
            category: "data",

            description:
                "Analyze data and build predictive models to discover meaningful patterns.",

            skills: [
                "Python",
                "SQL",
                "Statistics",
                "NumPy",
                "Pandas",
                "Machine Learning"
            ],

            roadmap: [
                "Learn Python programming.",
                "Study statistics and probability.",
                "Learn NumPy and Pandas.",
                "Practice data cleaning and exploratory data analysis.",
                "Learn SQL and data visualization.",
                "Study machine learning fundamentals.",
                "Build data analysis and prediction projects."
            ],

            resources: [
                {
                    name: "Kaggle",
                    url: "https://www.kaggle.com/"
                },
                {
                    name: "Pandas Documentation",
                    url: "https://pandas.pydata.org/docs/"
                },
                {
                    name: "Scikit-learn Documentation",
                    url: "https://scikit-learn.org/stable/"
                }
            ]
        },

        cybersecurity: {
            id: "cybersecurity",
            title: "Cybersecurity Engineer",
            category: "technology",

            description:
                "Protect computer systems, networks, and applications against cyber threats.",

            skills: [
                "Computer Networks",
                "Linux",
                "Python",
                "Operating Systems",
                "Web Security",
                "Security Fundamentals"
            ],

            roadmap: [
                "Understand computer hardware and operating systems.",
                "Learn Linux and command-line tools.",
                "Study networking fundamentals.",
                "Learn Python scripting.",
                "Understand web security and common vulnerabilities.",
                "Practice in legal cybersecurity labs.",
                "Build defensive security projects and document your learning."
            ],

            resources: [
                {
                    name: "Cisco Networking Academy",
                    url: "https://www.netacad.com/"
                },
                {
                    name: "TryHackMe",
                    url: "https://tryhackme.com/"
                },
                {
                    name: "OWASP",
                    url: "https://owasp.org/"
                }
            ]
        },

        web: {
            id: "web",
            title: "Web Developer",
            category: "technology",

            description:
                "Design and develop interactive websites and web applications.",

            skills: [
                "HTML",
                "CSS",
                "JavaScript",
                "Responsive Web Design",
                "Git and GitHub",
                "APIs"
            ],

            roadmap: [
                "Learn HTML and semantic page structure.",
                "Learn CSS, layouts, and responsive design.",
                "Master JavaScript fundamentals.",
                "Build interactive websites.",
                "Learn Git and GitHub.",
                "Learn APIs and a frontend framework.",
                "Build and deploy portfolio projects."
            ],

            resources: [
                {
                    name: "MDN Web Docs",
                    url: "https://developer.mozilla.org/"
                },
                {
                    name: "freeCodeCamp",
                    url: "https://www.freecodecamp.org/"
                },
                {
                    name: "GitHub",
                    url: "https://github.com/"
                }
            ]
        },

        entrepreneur: {
            id: "entrepreneur",
            title: "Entrepreneur",
            category: "business",

            description:
                "Turn ideas into products or services by solving problems and building businesses.",

            skills: [
                "Communication",
                "Problem Solving",
                "Business Planning",
                "Market Research",
                "Financial Basics",
                "Leadership"
            ],

            roadmap: [
                "Identify a problem that people need solved.",
                "Research the market and potential customers.",
                "Develop a business idea and value proposition.",
                "Create a simple prototype or minimum viable product.",
                "Collect feedback and improve the product.",
                "Learn basic finance, marketing, and business operations.",
                "Develop a sustainable business plan."
            ],

            resources: [
                {
                    name: "Y Combinator Startup Library",
                    url: "https://www.ycombinator.com/library"
                },
                {
                    name: "Startup India",
                    url: "https://www.startupindia.gov.in/"
                },
                {
                    name: "Harvard Business Review",
                    url: "https://hbr.org/"
                }
            ]
        }
    };


    // ============================================================
    // 2. HTML ELEMENTS
    // ============================================================

    const careerSearch = document.getElementById("careerSearch");

    const filterButtons = document.querySelectorAll(".filter-btn");

    const careerCards = document.querySelectorAll(".career-card");

    const noCareersMessage =
        document.getElementById("noCareersMessage");

    const searchMessage =
        document.getElementById("searchMessage");

    const careerDetails =
        document.getElementById("career-details");

    const backToCareers =
        document.getElementById("backToCareers");

    const detailTitle =
        document.getElementById("detailTitle");

    const detailDescription =
        document.getElementById("detailDescription");

    const detailSkills =
        document.getElementById("detailSkills");

    const detailRoadmap =
        document.getElementById("detailRoadmap");

    const detailResources =
        document.getElementById("detailResources");


    // ============================================================
    // 3. SEARCH AND CATEGORY FILTERING
    // ============================================================

    let selectedCategory = "all";


    function matchesSearch(card, searchTerm) {
        const cardText = card.textContent.toLowerCase();

        return cardText.includes(searchTerm);
    }


    function matchesCategory(card, category) {
        if (category === "all") {
            return true;
        }

        const cardCategory =
            (card.dataset.category || "").toLowerCase();

        const cardCareer =
            (card.dataset.career || "").toLowerCase();

        // Technology filter also includes the cybersecurity career.
        if (category === "technology") {
            return (
                cardCategory === "technology" ||
                cardCareer === "cybersecurity"
            );
        }

        // Support both "ai" and "robotics" category names.
        if (category === "ai") {
            return (
                cardCategory === "ai" ||
                cardCategory === "robotics"
            );
        }

        return cardCategory === category;
    }


    function filterCareers() {
        const searchTerm = careerSearch
            ? careerSearch.value.trim().toLowerCase()
            : "";

        let visibleCount = 0;

        careerCards.forEach((card) => {
            const searchMatches =
                matchesSearch(card, searchTerm);

            const categoryMatches =
                matchesCategory(card, selectedCategory);

            const shouldDisplay =
                searchMatches && categoryMatches;

            card.hidden = !shouldDisplay;

            if (shouldDisplay) {
                visibleCount++;
            }
        });

        if (noCareersMessage) {
            noCareersMessage.hidden = visibleCount !== 0;
        }

        if (searchMessage) {
            if (visibleCount === 0) {
                searchMessage.textContent =
                    "No careers found. Try another search or category.";
            } else {
                searchMessage.textContent =
                    `${visibleCount} career${visibleCount === 1 ? "" : "s"} found.`;
            }
        }
    }


    if (careerSearch) {
        careerSearch.addEventListener("input", filterCareers);
    }


    filterButtons.forEach((button) => {
        button.addEventListener("click", () => {

            selectedCategory =
                (button.dataset.category || "all").toLowerCase();

            filterButtons.forEach((filterButton) => {
                filterButton.classList.remove("active");

                filterButton.setAttribute(
                    "aria-pressed",
                    "false"
                );
            });

            button.classList.add("active");

            button.setAttribute("aria-pressed", "true");

            filterCareers();
        });
    });


    // ============================================================
    // 4. CAREER DETAILS
    // ============================================================

    function showCareerDetails(careerKey) {

        const career = careers[careerKey];

        if (!career) {
            console.error(
                "Career not found:",
                careerKey
            );

            return;
        }

        if (detailTitle) {
            detailTitle.textContent = career.title;
        }

        if (detailDescription) {
            detailDescription.textContent = career.description;
        }

        if (detailSkills) {
            detailSkills.replaceChildren();

            career.skills.forEach((skill) => {
                const listItem = document.createElement("li");

                listItem.textContent = skill;

                detailSkills.appendChild(listItem);
            });
        }

        if (detailRoadmap) {
            detailRoadmap.replaceChildren();

            career.roadmap.forEach((step) => {
                const listItem = document.createElement("li");

                listItem.textContent = step;

                detailRoadmap.appendChild(listItem);
            });
        }

        if (detailResources) {
            detailResources.replaceChildren();

            career.resources.forEach((resource) => {
                const listItem = document.createElement("li");

                const link = document.createElement("a");

                link.textContent = resource.name;

                link.href = resource.url;

                link.target = "_blank";

                link.rel = "noopener noreferrer";

                listItem.appendChild(link);

                detailResources.appendChild(listItem);
            });
        }

        if (careerDetails) {
            careerDetails.hidden = false;

            careerDetails.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }

        // Update the URL fragment without reloading the page.
        history.replaceState(
            null,
            "",
            "#career-details"
        );
    }


    // Connect the Explore Career links on the career cards.
    document.querySelectorAll(".career-link").forEach((link) => {

        link.addEventListener("click", (event) => {

            const careerKey = link.dataset.career;

            if (!careerKey) {
                return;
            }

            event.preventDefault();

            showCareerDetails(careerKey);
        });
    });


    // Back to the career listing.
    if (backToCareers) {

        backToCareers.addEventListener("click", () => {

            if (careerDetails) {
                careerDetails.hidden = true;
            }

            history.replaceState(
                null,
                "",
                "#careers"
            );

            const careersSection =
                document.getElementById("careers");

            if (careersSection) {
                careersSection.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }
        });
    }


    // ============================================================
    // 5. CAREER ASSESSMENT - FASTAPI BACKEND
    // ============================================================

    const assessmentForm =
        document.getElementById("assessmentForm");

    const assessmentResult =
        document.getElementById("assessmentResult");

    const resultTitle =
        document.getElementById("resultTitle");

    const resultDescription =
        document.getElementById("resultDescription");

    const resultCareers =
        document.getElementById("resultCareers");


    if (assessmentForm) {

        assessmentForm.addEventListener(
            "submit",
            async (event) => {

                event.preventDefault();

                const formData =
                    new FormData(assessmentForm);

                // Read the user's assessment answers.
                const assessmentData = {
                    interest: String(
                        formData.get("interest") || ""
                    ).trim().toLowerCase(),

                    strength: String(
                        formData.get("strength") || ""
                    ).trim().toLowerCase(),

                    experience: String(
                        formData.get("experience") || ""
                    ).trim().toLowerCase()
                };


                // Validate that the required answers are present.
                if (
                    !assessmentData.interest ||
                    !assessmentData.strength ||
                    !assessmentData.experience
                ) {
                    if (assessmentResult) {
                        assessmentResult.hidden = false;
                    }

                    if (resultTitle) {
                        resultTitle.textContent =
                            "Please complete the assessment";
                    }

                    if (resultDescription) {
                        resultDescription.textContent =
                            "Answer all the questions before requesting a career recommendation.";
                    }

                    return;
                }


                // Display a loading message.
                if (assessmentResult) {
                    assessmentResult.hidden = false;

                    assessmentResult.scrollIntoView({
                        behavior: "smooth",
                        block: "nearest"
                    });
                }

                if (resultTitle) {
                    resultTitle.textContent =
                        "Finding your career recommendation...";
                }

                if (resultDescription) {
                    resultDescription.textContent =
                        "Connecting to CareerPathAI...";
                }

                if (resultCareers) {
                    resultCareers.replaceChildren();
                }


                try {

                    // Send the assessment answers to FastAPI.
                    const response = await fetch(
                        "http://127.0.0.1:8000/api/recommend",
                        {
                            method: "POST",

                            headers: {
                                "Content-Type": "application/json"
                            },

                            body: JSON.stringify(assessmentData)
                        }
                    );


                    // Read the JSON response.
                    const data = await response.json();


                    // Handle HTTP errors returned by the backend.
                    if (!response.ok) {

                        const errorMessage =
                            typeof data.detail === "string"
                                ? data.detail
                                : "The backend could not generate a recommendation.";

                        throw new Error(errorMessage);
                    }


                    // The backend should return recommended_career.
                    const recommended =
                        data.recommended_career;


                    if (
                        !recommended ||
                        !recommended.id ||
                        !recommended.title
                    ) {
                        throw new Error(
                            "The backend response does not contain a valid recommended career."
                        );
                    }


                    // Display the recommended career.
                    if (resultTitle) {
                        resultTitle.textContent =
                            "Your Recommended Career: " +
                            recommended.title;
                    }

                    if (resultDescription) {
                        resultDescription.textContent =
                            recommended.description ||
                            "Explore this career to learn more about the skills you need.";
                    }


                    // Display the skills returned by the backend.
                    if (resultCareers) {

                        resultCareers.replaceChildren();

                        if (
                            Array.isArray(recommended.skills) &&
                            recommended.skills.length > 0
                        ) {
                            const skillsHeading =
                                document.createElement("h4");

                            skillsHeading.textContent =
                                "Recommended Skills";

                            resultCareers.appendChild(skillsHeading);

                            const skillsList =
                                document.createElement("ul");

                            recommended.skills.forEach((skill) => {

                                const listItem =
                                    document.createElement("li");

                                listItem.textContent = skill;

                                skillsList.appendChild(listItem);
                            });

                            resultCareers.appendChild(skillsList);
                        }


                        // Create a button to open the full career details.
                        const exploreButton =
                            document.createElement("button");

                        exploreButton.type = "button";

                        exploreButton.className = "career-link";

                        exploreButton.textContent =
                            "Explore " + recommended.title;

                        exploreButton.addEventListener(
                            "click",
                            () => {

                                const careerKey =
                                    recommended.id;

                                // Use the local career information
                                // to display the full roadmap.
                                if (careers[careerKey]) {

                                    showCareerDetails(careerKey);

                                } else {

                                    console.error(
                                        "No local details found for:",
                                        careerKey
                                    );

                                    if (resultDescription) {
                                        resultDescription.textContent +=
                                            " Detailed roadmap information is not yet available for this career.";
                                    }
                                }
                            }
                        );

                        resultCareers.appendChild(exploreButton);
                    }

                    console.log(
                        "Career recommendation received:",
                        data
                    );

                } catch (error) {

                    console.error(
                        "Career assessment error:",
                        error
                    );


                    if (resultTitle) {
                        resultTitle.textContent =
                            "Unable to Get Recommendation";
                    }

                    if (resultDescription) {
                        resultDescription.textContent =
                            "Could not connect to the backend. Check that FastAPI is running at http://127.0.0.1:8000 and try again. Error: " +
                            error.message;
                    }

                    if (resultCareers) {
                        resultCareers.replaceChildren();
                    }
                }
            }
        );
    }


    // ============================================================
    // 6. INITIALIZE THE PAGE
    // ============================================================

    filterCareers();

    console.log("CareerPathAI frontend initialized successfully.");

});