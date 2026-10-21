"use strict";

// ============================================
// CAREERPATHAI
// Career Search, Filters, Details and Assessment
// ============================================

document.addEventListener("DOMContentLoaded", function () {

    // ========================================
    // 1. GET HTML ELEMENTS
    // ========================================

    const careerSearch = document.getElementById("careerSearch");

    const filterButtons = document.querySelectorAll(".filter-btn");

    const careerCards = document.querySelectorAll(".career-card");

    const searchMessage = document.getElementById("searchMessage");

    const noCareersMessage = document.getElementById(
        "noCareersMessage"
    );

    const careerGrid = document.querySelector(".career-grid");

    const careerFilters = document.querySelector(".career-filters");

    const careerSearchContainer = document.querySelector(
        ".career-search"
    );

    const sectionHeader = document.querySelector(
        ".careers .section-header"
    );

    const careerDetails = document.getElementById("career-details");

    const backButton = document.getElementById("backToCareers");

    const detailTitle = document.getElementById("detailTitle");

    const detailDescription = document.getElementById(
        "detailDescription"
    );

    const detailSkills = document.getElementById("detailSkills");

    const detailRoadmap = document.getElementById("detailRoadmap");

    const detailResources = document.getElementById("detailResources");

    const assessmentForm = document.getElementById("assessmentForm");

    const assessmentResult = document.getElementById(
        "assessmentResult"
    );

    const assessmentMessage = document.getElementById(
        "assessmentMessage"
    );

    const viewRecommendedCareer = document.getElementById(
        "viewRecommendedCareer"
    );


    // ========================================
    // 2. CAREER DATA
    // ========================================

    const careers = {

        software: {

            title: "Software Developer",

            category: "technology",

            description:
                "Software developers design, build, test, and maintain applications that solve real-world problems.",

            skills: [
                "Python or Java",
                "Data Structures and Algorithms",
                "Object-Oriented Programming",
                "Git and GitHub",
                "Database fundamentals",
                "Problem-solving"
            ],

            roadmap: [
                "Learn programming fundamentals.",
                "Master Object-Oriented Programming.",
                "Study Data Structures and Algorithms.",
                "Learn databases, Git, and software development tools.",
                "Build practical projects and publish them on GitHub.",
                "Prepare for internships and technical interviews."
            ],

            resources: [
                "Python documentation — https://docs.python.org/3/",
                "Git documentation — https://git-scm.com/doc",
                "Coding practice — https://leetcode.com/"
            ]

        },


        robotics: {

            title: "AI & Robotics Engineer",

            category: "ai",

            description:
                "AI and robotics engineers develop intelligent robots, autonomous systems, and machines that interact with the real world.",

            skills: [
                "Python and C++",
                "Linear algebra and calculus",
                "Robot kinematics",
                "ROS 2",
                "Computer vision",
                "Machine learning",
                "Linux and simulation tools"
            ],

            roadmap: [
                "Learn Python and C++ programming.",
                "Study linear algebra, calculus, and robotics kinematics.",
                "Learn ROS 2 and create basic robot nodes.",
                "Explore robot simulation and autonomous navigation.",
                "Study computer vision and machine learning.",
                "Build robotics projects and document them on GitHub."
            ],

            resources: [
                "ROS 2 documentation — https://docs.ros.org/",
                "OpenCV documentation — https://docs.opencv.org/",
                "Python documentation — https://docs.python.org/3/"
            ]

        },


        data: {

            title: "Data Scientist",

            category: "data",

            description:
                "Data scientists analyze datasets, identify patterns, and develop predictive models to support informed decisions.",

            skills: [
                "Python programming",
                "NumPy and Pandas",
                "Statistics and probability",
                "SQL",
                "Data visualization",
                "Machine learning"
            ],

            roadmap: [
                "Learn Python programming.",
                "Study statistics and probability.",
                "Practice data cleaning and analysis.",
                "Learn SQL and data visualization.",
                "Study machine learning fundamentals.",
                "Build data analysis and prediction projects."
            ],

            resources: [
                "Pandas — https://pandas.pydata.org/",
                "Scikit-learn — https://scikit-learn.org/",
                "SQLBolt — https://sqlbolt.com/"
            ]

        },


        cybersecurity: {

            title: "Cybersecurity Engineer",

            category: "technology",

            description:
                "Cybersecurity engineers help protect computer systems, applications, and networks from security threats.",

            skills: [
                "Computer networking",
                "Linux",
                "Operating systems",
                "Python scripting",
                "Security fundamentals",
                "Ethical testing practices"
            ],

            roadmap: [
                "Learn networking fundamentals.",
                "Understand Linux and operating systems.",
                "Study security principles and common vulnerabilities.",
                "Practice using authorized cybersecurity labs.",
                "Learn security monitoring and defensive tools.",
                "Create a portfolio of security projects."
            ],

            resources: [
                "Ubuntu tutorials — https://ubuntu.com/tutorials",
                "OWASP — https://owasp.org/",
                "Cisco Networking Academy — https://www.netacad.com/"
            ]

        },


        web: {

            title: "Web Developer",

            category: "technology",

            description:
                "Web developers create interactive websites and applications using frontend and backend technologies.",

            skills: [
                "HTML",
                "CSS",
                "JavaScript",
                "Responsive web design",
                "Git and GitHub",
                "Backend development",
                "Database fundamentals"
            ],

            roadmap: [
                "Master HTML and CSS.",
                "Learn JavaScript fundamentals.",
                "Practice DOM manipulation and browser events.",
                "Build responsive websites.",
                "Learn backend development and databases.",
                "Deploy projects and create a portfolio."
            ],

            resources: [
                "MDN Web Docs — https://developer.mozilla.org/",
                "JavaScript Guide — https://javascript.info/",
                "GitHub — https://github.com/"
            ]

        },


        entrepreneur: {

            title: "Entrepreneur",

            category: "business",

            description:
                "Entrepreneurs identify problems, develop solutions, and build businesses around products or services.",

            skills: [
                "Problem-solving",
                "Business planning",
                "Communication",
                "Financial fundamentals",
                "Market research",
                "Leadership"
            ],

            roadmap: [
                "Identify a real-world problem.",
                "Research potential customers and competitors.",
                "Develop a business model.",
                "Create and test a minimum viable product.",
                "Collect feedback and improve the product.",
                "Develop a sustainable business strategy."
            ],

            resources: [
                "Startup India — https://www.startupindia.gov.in/",
                "Y Combinator resources — https://www.ycombinator.com/resources"
            ]

        }

    };


    // ========================================
    // 3. CAREER SEARCH AND CATEGORY FILTERS
    // ========================================

    let selectedCategory = "all";


    function filterCareers() {

        const searchText = careerSearch.value
            .toLowerCase()
            .trim();

        let visibleCount = 0;


        careerCards.forEach(function (card) {

            const category = card.dataset.category;

            const careerKey = card.dataset.career;

            const career = careers[careerKey];

            const cardText = (
                card.textContent + " " +
                career.title + " " +
                career.description + " " +
                career.skills.join(" ") + " " +
                career.roadmap.join(" ")
            ).toLowerCase();


            const matchesCategory =
                selectedCategory === "all" ||
                category === selectedCategory;


            const matchesSearch =
                cardText.includes(searchText);


            const shouldDisplay =
                matchesCategory && matchesSearch;


            card.hidden = !shouldDisplay;


            if (shouldDisplay) {

                visibleCount++;

            }

        });


        noCareersMessage.hidden = visibleCount !== 0;


        if (searchText !== "") {

            searchMessage.textContent =
                visibleCount + " career(s) found.";

        } else {

            searchMessage.textContent = "";

        }

    }


    // Live search

    if (careerSearch) {

        careerSearch.addEventListener(
            "input",
            filterCareers
        );

    }


    // Category filter buttons

    filterButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            selectedCategory = button.dataset.category;


            filterButtons.forEach(function (btn) {

                const isActive = btn === button;

                btn.classList.toggle("active", isActive);

                btn.setAttribute(
                    "aria-pressed",
                    String(isActive)
                );

            });


            filterCareers();

        });

    });


    // ========================================
    // 4. DISPLAY CAREER DETAILS
    // ========================================

    function addListItems(container, items) {

        container.replaceChildren();


        items.forEach(function (item) {

            const listItem = document.createElement("li");

            listItem.textContent = item;

            container.appendChild(listItem);

        });

    }


    function openCareer(careerKey) {

        const career = careers[careerKey];


        if (!career) {

            console.error(
                "Career information not found:",
                careerKey
            );

            return;

        }


        detailTitle.textContent = career.title;

        detailDescription.textContent = career.description;


        addListItems(
            detailSkills,
            career.skills
        );


        addListItems(
            detailRoadmap,
            career.roadmap
        );


        // Make the resource URLs clickable.

        detailResources.replaceChildren();


        career.resources.forEach(function (resource) {

            const listItem = document.createElement("li");

            const separator = resource.indexOf(" — ");

            const label = separator !== -1
                ? resource.slice(0, separator)
                : resource;

            const url = separator !== -1
                ? resource.slice(separator + 3)
                : "";


            if (
                url.startsWith("https://") ||
                url.startsWith("http://")
            ) {

                const link = document.createElement("a");

                link.textContent = label;

                link.href = url;

                link.target = "_blank";

                link.rel = "noopener noreferrer";

                listItem.appendChild(link);

            } else {

                listItem.textContent = resource;

            }


            detailResources.appendChild(listItem);

        });


        // Hide the career listing.

        careerGrid.hidden = true;

        careerDetails.hidden = false;


        if (careerFilters) {

            careerFilters.hidden = true;

        }


        if (careerSearchContainer) {

            careerSearchContainer.hidden = true;

        }


        if (sectionHeader) {

            sectionHeader.hidden = true;

        }


        noCareersMessage.hidden = true;


        history.replaceState(
            null,
            "",
            "#career-details"
        );


        careerDetails.scrollIntoView({

            behavior: "smooth",

            block: "start"

        });

    }


    // Listen to every Explore Career link.

    document.querySelectorAll(
        ".career-card .career-link[data-career]"
    ).forEach(function (link) {

        link.addEventListener("click", function (event) {

            event.preventDefault();

            openCareer(link.dataset.career);

        });

    });


    // Return to the career cards.

    function showCareerGrid() {

        careerDetails.hidden = true;

        careerGrid.hidden = false;


        if (careerFilters) {

            careerFilters.hidden = false;

        }


        if (careerSearchContainer) {

            careerSearchContainer.hidden = false;

        }


        if (sectionHeader) {

            sectionHeader.hidden = false;

        }


        filterCareers();


        history.replaceState(
            null,
            "",
            "#careers"
        );


        document.getElementById("careers").scrollIntoView({

            behavior: "smooth",

            block: "start"

        });

    }


    backButton.addEventListener(
        "click",
        showCareerGrid
    );


    // ========================================
    // 5. CAREER ASSESSMENT
    // ========================================

    let recommendedCareerKey = null;


    function recommendCareer(interest, strength) {

        // Strongest interest is the primary signal.

        const interestRecommendations = {

            technology: "software",

            robotics: "robotics",

            data: "data",

            security: "cybersecurity",

            web: "web",

            business: "entrepreneur"

        };


        let careerKey = interestRecommendations[interest];


        // Use the strength as an additional signal.

        if (strength === "leadership" && interest === "business") {

            careerKey = "entrepreneur";

        } else if (
            strength === "building" &&
            interest === "robotics"
        ) {

            careerKey = "robotics";

        } else if (
            strength === "analysis" &&
            interest === "data"
        ) {

            careerKey = "data";

        } else if (
            strength === "creativity" &&
            interest === "web"
        ) {

            careerKey = "web";

        }


        return careerKey;

    }


    if (assessmentForm) {

        assessmentForm.addEventListener(
            "submit",
            function (event) {

                event.preventDefault();


                const interest = document.getElementById(
                    "interest"
                ).value;


                const strength = document.getElementById(
                    "strength"
                ).value;


                const experience = document.getElementById(
                    "experience"
                ).value;


                if (!interest || !strength || !experience) {

                    alert(
                        "Please answer all three questions."
                    );

                    return;

                }


                recommendedCareerKey = recommendCareer(
                    interest,
                    strength
                );


                const career = careers[recommendedCareerKey];


                if (!career) {

                    return;

                }


                let experienceAdvice = "";


                if (experience === "beginner") {

                    experienceAdvice =
                        "Start with programming fundamentals and small projects.";

                } else if (experience === "intermediate") {

                    experienceAdvice =
                        "Strengthen your core skills and build practical projects.";

                } else {

                    experienceAdvice =
                        "Focus on advanced projects, a portfolio, and internship opportunities.";

                }


                assessmentMessage.textContent =
                    "Based on your selected interests and strengths, " +
                    career.title +
                    " is a career worth exploring. " +
                    experienceAdvice;


                assessmentResult.hidden = false;


                assessmentResult.scrollIntoView({

                    behavior: "smooth",

                    block: "center"

                });

            }
        );

    }


    // Open the recommended career profile.

    if (viewRecommendedCareer) {

        viewRecommendedCareer.addEventListener(
            "click",
            function () {

                if (recommendedCareerKey) {

                    openCareer(recommendedCareerKey);

                }

            }
        );

    }


    // ========================================
    // 6. INITIALIZE THE WEBSITE
    // ========================================

    filterCareers();


    console.log(
        "CareerPathAI initialized successfully."
    );

});