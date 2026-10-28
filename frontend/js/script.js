"use strict";

// =====================================================
// CONFIGURATION
// =====================================================

const API_BASE_URL = "http://127.0.0.1:8000";

let activeCategory = "all";
let activeSearch = "";


// =====================================================
// GENERAL HELPERS
// =====================================================

function getElement(id) {
    return document.getElementById(id);
}


function createElement(tag, className = "", text = "") {
    const element = document.createElement(tag);

    if (className) {
        element.className = className;
    }

    if (text !== undefined && text !== null) {
        element.textContent = text;
    }

    return element;
}


async function fetchJSON(url, options = {}) {
    const response = await fetch(url, options);

    let data;

    try {
        data = await response.json();
    } catch {
        throw new Error("The server returned an invalid response.");
    }

    if (!response.ok) {
        throw new Error(
            typeof data.detail === "string"
                ? data.detail
                : `Request failed with status ${response.status}.`
        );
    }

    return data;
}


// =====================================================
// SKILLS RENDERING
// =====================================================

function renderSkills(container, skills) {
    if (!container) {
        return;
    }

    container.replaceChildren();

    if (!Array.isArray(skills) || skills.length === 0) {
        container.appendChild(
            createElement("p", "", "Skills will be added soon.")
        );

        return;
    }

    const list = createElement("ul", "career-skills-list");

    skills.forEach((skill) => {
        list.appendChild(
            createElement("li", "career-skill", skill)
        );
    });

    container.appendChild(list);
}


// =====================================================
// LEARNING RESOURCES
// =====================================================

function renderResources(container, resources) {
    if (!container) {
        return;
    }

    container.replaceChildren();

    if (!Array.isArray(resources) || resources.length === 0) {
        container.appendChild(
            createElement(
                "p",
                "",
                "Learning resources will be added soon."
            )
        );

        return;
    }

    const list = createElement("ul", "career-resources-list");

    resources.forEach((resource) => {
        if (!resource || !resource.url) {
            return;
        }

        const link = createElement(
            "a",
            "resource-link",
            resource.title || resource.url
        );

        link.href = resource.url;
        link.target = "_blank";
        link.rel = "noopener noreferrer";

        const item = createElement("li");

        item.appendChild(link);
        list.appendChild(item);
    });

    container.appendChild(list);
}


// =====================================================
// ROADMAP PROGRESS
// Progress is stored separately for each career.
// =====================================================

function getCompletedStages(careerId) {
    try {
        const value = JSON.parse(
            localStorage.getItem(
                `careerpathai-progress-${careerId}`
            ) || "[]"
        );

        return Array.isArray(value) ? value : [];
    } catch {
        return [];
    }
}


function updateProgress(container, careerId, total) {
    const completed = getCompletedStages(careerId);

    const percent = total
        ? Math.round((completed.length / total) * 100)
        : 0;

    const text = container.querySelector(
        ".roadmap-progress-text"
    );

    const bar = container.querySelector(
        ".roadmap-progress-bar"
    );

    const track = container.querySelector(
        ".roadmap-progress-track"
    );

    if (text) {
        text.textContent =
            `${completed.length} of ${total} stages completed (${percent}%)`;
    }

    if (bar) {
        bar.style.width = `${percent}%`;

        bar.setAttribute(
            "aria-valuenow",
            String(percent)
        );
    }

    if (track) {
        track.setAttribute(
            "aria-valuenow",
            String(completed.length)
        );
    }
}


// =====================================================
// COMPLETE LEARNING ROADMAP
// Works for every career returned by the backend.
// =====================================================

function renderRoadmap(container, career) {
    if (!container) {
        return;
    }

    container.replaceChildren();

    const roadmap = career.roadmap;

    if (
        !roadmap ||
        !Array.isArray(roadmap.stages) ||
        roadmap.stages.length === 0
    ) {
        container.appendChild(
            createElement(
                "p",
                "roadmap-empty",
                "A learning roadmap is not available yet."
            )
        );

        return;
    }

    // Roadmap summary.

    const summary = createElement(
        "div",
        "roadmap-summary"
    );

    const duration = createElement(
        "span",
        "roadmap-duration",
        `Estimated duration: ${roadmap.estimated_duration || "Varies"}`
    );

    const studyHours = createElement(
        "span",
        "roadmap-hours",
        `Recommended study time: ${roadmap.weekly_study_hours || "Flexible"} per week`
    );

    summary.append(duration, studyHours);

    container.appendChild(summary);

    // Explain that estimates are flexible.

    container.appendChild(
        createElement(
            "p",
            "roadmap-note",
            "Use this as a flexible guide. Move forward when you can complete the stage goal; your pace may differ."
        )
    );

    // Progress display.

    const progressWrapper = createElement(
        "div",
        "roadmap-progress"
    );

    const progressText = createElement(
        "p",
        "roadmap-progress-text",
        ""
    );

    const track = createElement(
        "div",
        "roadmap-progress-track"
    );

    track.setAttribute("role", "progressbar");

    track.setAttribute(
        "aria-label",
        `${career.title} learning progress`
    );

    track.setAttribute("aria-valuemin", "0");

    track.setAttribute(
        "aria-valuemax",
        String(roadmap.stages.length)
    );

    const bar = createElement(
        "div",
        "roadmap-progress-bar"
    );

    track.appendChild(bar);

    progressWrapper.append(progressText, track);

    container.appendChild(progressWrapper);

    // Roadmap stages.

    const timeline = createElement(
        "div",
        "roadmap-timeline"
    );

    const completedStages = getCompletedStages(career.id);

    roadmap.stages.forEach((stage, index) => {
        const card = createElement(
            "article",
            "roadmap-stage"
        );

        const header = createElement(
            "div",
            "roadmap-stage-header"
        );

        const number = createElement(
            "span",
            "roadmap-stage-number",
            String(index + 1).padStart(2, "0")
        );

        const heading = createElement(
            "div",
            "roadmap-stage-heading"
        );

        const stageTitle = createElement(
            "h4",
            "roadmap-stage-title",
            stage.title || `Stage ${index + 1}`
        );

        const stageDuration = createElement(
            "span",
            "roadmap-stage-duration",
            stage.duration || "Duration varies"
        );

        heading.append(stageTitle, stageDuration);

        header.append(number, heading);

        // Topics.

        const topicsHeading = createElement(
            "h5",
            "roadmap-subheading",
            "Topics to learn"
        );

        const topicsList = createElement(
            "ul",
            "roadmap-topics"
        );

        (stage.topics || []).forEach((topic) => {
            topicsList.appendChild(
                createElement("li", "", topic)
            );
        });

        // Completion goal.

        const goal = createElement(
            "div",
            "roadmap-completion-goal"
        );

        goal.append(
            createElement(
                "h5",
                "roadmap-subheading",
                "Completion goal"
            ),
            createElement(
                "p",
                "",
                stage.completion_goal ||
                    "Complete a practical exercise and review the topics."
            )
        );

        // Checkbox.

        const checkboxLabel = createElement(
            "label",
            "roadmap-checkbox-label"
        );

        const checkbox = createElement("input");

        checkbox.type = "checkbox";

        checkbox.className = "roadmap-stage-checkbox";

        checkbox.checked = completedStages.includes(index);

        checkbox.setAttribute(
            "aria-label",
            `Mark ${stage.title} completed`
        );

        const checkboxText = createElement(
            "span",
            "",
            "Mark stage as completed"
        );

        checkboxLabel.append(checkbox, checkboxText);

        if (checkbox.checked) {
            card.classList.add("completed");
        }

        checkbox.addEventListener("change", () => {
            let indexes = getCompletedStages(career.id);

            if (checkbox.checked) {
                if (!indexes.includes(index)) {
                    indexes.push(index);
                }

                card.classList.add("completed");
            } else {
                indexes = indexes.filter(
                    (value) => value !== index
                );

                card.classList.remove("completed");
            }

            indexes.sort((a, b) => a - b);

            localStorage.setItem(
                `careerpathai-progress-${career.id}`,
                JSON.stringify(indexes)
            );

            updateProgress(
                container,
                career.id,
                roadmap.stages.length
            );
        });

        card.append(
            header,
            topicsHeading,
            topicsList,
            goal,
            checkboxLabel
        );

        timeline.appendChild(card);
    });

    container.appendChild(timeline);

    updateProgress(
        container,
        career.id,
        roadmap.stages.length
    );
}


// =====================================================
// CAREER SEARCH AND FILTERS
// =====================================================

function filterCareers() {
    const cards = document.querySelectorAll(
        ".career-card"
    );

    const count = getElement("careerCount");

    const emptyMessage = getElement(
        "noCareersMessage"
    );

    let visible = 0;

    cards.forEach((card) => {
        const category = (
            card.dataset.category || ""
        ).toLowerCase();

        const text = card.textContent.toLowerCase();

        const matchesCategory =
            activeCategory === "all" ||
            category === activeCategory;

        const matchesSearch =
            text.includes(activeSearch);

        card.hidden = !(
            matchesCategory && matchesSearch
        );

        if (!card.hidden) {
            visible += 1;
        }
    });

    if (count) {
        count.textContent =
            `${visible} career${visible === 1 ? "" : "s"} found.`;
    }

    if (emptyMessage) {
        emptyMessage.hidden = visible !== 0;
    }
}


function initializeCareerFilters() {
    const search = getElement("careerSearch");

    if (search) {
        search.addEventListener("input", () => {
            activeSearch = search.value
                .trim()
                .toLowerCase();

            filterCareers();
        });
    }

    document.querySelectorAll(
        ".filter-btn"
    ).forEach((button) => {
        button.addEventListener("click", () => {
            activeCategory = (
                button.dataset.category || "all"
            ).toLowerCase();

            document.querySelectorAll(
                ".filter-btn"
            ).forEach((item) => {
                item.classList.remove("active");

                item.setAttribute(
                    "aria-pressed",
                    "false"
                );
            });

            button.classList.add("active");

            button.setAttribute(
                "aria-pressed",
                "true"
            );

            filterCareers();
        });
    });

    filterCareers();
}


// =====================================================
// CAREER DETAILS
// =====================================================

async function openCareerDetails(careerId) {
    const section = getElement("career-details");

    const title = getElement("detailTitle");

    const description = getElement(
        "detailDescription"
    );

    const skills = getElement("detailSkills");

    const roadmap = getElement("detailRoadmap");

    const resources = getElement("detailResources");

    if (!section) {
        console.error(
            "Missing HTML section: #career-details"
        );

        return;
    }

    section.hidden = false;

    section.scrollIntoView({
        behavior: "smooth",
        block: "start",
    });

    if (title) {
        title.textContent = "Loading career...";
    }

    if (description) {
        description.textContent =
            "Loading skills, roadmap, and learning resources...";
    }

    try {
        const career = await fetchJSON(
            `${API_BASE_URL}/api/careers/${encodeURIComponent(careerId)}`
        );

        if (title) {
            title.textContent = career.title;
        }

        if (description) {
            description.textContent = career.description;
        }

        renderSkills(skills, career.skills);

        renderRoadmap(roadmap, career);

        renderResources(resources, career.resources);

        history.replaceState(
            null,
            "",
            "#career-details"
        );

    } catch (error) {
        console.error(
            "Could not load career:",
            error
        );

        if (title) {
            title.textContent =
                "Unable to load career details";
        }

        if (description) {
            description.textContent =
                `${error.message} Ensure FastAPI is running at ${API_BASE_URL}.`;
        }

        if (roadmap) {
            roadmap.replaceChildren();
        }

        if (resources) {
            resources.replaceChildren();
        }
    }
}


function closeCareerDetails() {
    const details = getElement("career-details");

    const careers = getElement("careers");

    if (details) {
        details.hidden = true;
    }

    if (careers) {
        careers.scrollIntoView({
            behavior: "smooth",
            block: "start",
        });
    }

    history.replaceState(
        null,
        "",
        "#careers"
    );
}


function initializeCareerDetails() {
    const section = getElement("career-details");

    const backButton = getElement(
        "backToCareers"
    );

    if (section) {
        section.hidden = true;
    }

    if (backButton) {
        backButton.addEventListener(
            "click",
            (event) => {
                event.preventDefault();
                closeCareerDetails();
            }
        );
    }

    document.querySelectorAll(
        ".career-link"
    ).forEach((link) => {
        link.addEventListener(
            "click",
            (event) => {
                event.preventDefault();

                const card = link.closest(
                    ".career-card"
                );

                const careerId =
                    link.dataset.career ||
                    (card && card.dataset.career);

                if (careerId) {
                    openCareerDetails(careerId);
                }
            }
        );
    });

    const requestedCareer =
        new URLSearchParams(
            window.location.search
        ).get("career");

    if (requestedCareer) {
        openCareerDetails(requestedCareer);
    }
}


// =====================================================
// ASSESSMENT RESULT
// =====================================================

function renderAssessmentResult(career) {
    const result = getElement(
        "assessmentResult"
    );

    const title = getElement(
        "resultTitle"
    );

    const description = getElement(
        "resultDescription"
    );

    const content = getElement(
        "resultCareers"
    );

    if (result) {
        result.hidden = false;
    }

    if (title) {
        title.textContent =
            `Your Recommended Career: ${career.title}`;
    }

    if (description) {
        description.textContent =
            career.description;
    }

    if (!content) {
        return;
    }

    content.replaceChildren();

    // Career overview.

    const overview = createElement(
        "div",
        "assessment-career-overview"
    );

    overview.append(
        createElement(
            "p",
            "assessment-category",
            `Category: ${career.category || "General"}`
        ),

        createElement(
            "p",
            "assessment-duration",
            `Estimated learning time: ${career.roadmap?.estimated_duration || "Varies"}`
        ),

        createElement(
            "p",
            "assessment-hours",
            `Study time: ${career.roadmap?.weekly_study_hours || "Flexible"} per week`
        )
    );

    content.appendChild(overview);

    // Skills.

    content.appendChild(
        createElement(
            "h3",
            "",
            "Skills to Develop"
        )
    );

    const skillsContainer = createElement(
        "div",
        "assessment-skills"
    );

    renderSkills(
        skillsContainer,
        career.skills
    );

    content.appendChild(skillsContainer);

    // Full roadmap.

    content.appendChild(
        createElement(
            "h3",
            "assessment-roadmap-heading",
            "Complete Learning Roadmap"
        )
    );

    const roadmapContainer = createElement(
        "div",
        "assessment-roadmap"
    );

    renderRoadmap(
        roadmapContainer,
        career
    );

    content.appendChild(roadmapContainer);

    // Learning resources.

    content.appendChild(
        createElement(
            "h3",
            "",
            "Recommended Learning Resources"
        )
    );

    const resourcesContainer = createElement(
        "div",
        "assessment-resources"
    );

    renderResources(
        resourcesContainer,
        career.resources
    );

    content.appendChild(resourcesContainer);

    // Open full career details button.

    const detailsButton = createElement(
        "button",
        "assessment-details-button",
        `Open Full ${career.title} Details`
    );

    detailsButton.type = "button";

    detailsButton.addEventListener(
        "click",
        () => {
            openCareerDetails(career.id);
        }
    );

    content.appendChild(detailsButton);

    // Disclaimer.

    content.appendChild(
        createElement(
            "p",
            "assessment-disclaimer",
            "This is a preliminary rules-based recommendation, not a professional career diagnosis. Roadmap durations are estimates and can be adjusted to your pace."
        )
    );

    content.scrollIntoView({
        behavior: "smooth",
        block: "start",
    });
}


// =====================================================
// CAREER ASSESSMENT — CONNECT TO FASTAPI
// =====================================================

function initializeAssessment() {
    const form = getElement(
        "assessmentForm"
    );

    if (!form) {
        return;
    }

    const submitButton = form.querySelector(
        'button[type="submit"], input[type="submit"]'
    );

    form.addEventListener(
        "submit",
        async (event) => {
            event.preventDefault();

            const formData = new FormData(form);

            const answers = {
                interest: String(
                    formData.get("interest") || ""
                ).trim(),

                strength: String(
                    formData.get("strength") || ""
                ).trim(),

                experience: String(
                    formData.get("experience") || ""
                ).trim(),
            };

            const result = getElement(
                "assessmentResult"
            );

            const title = getElement(
                "resultTitle"
            );

            const description = getElement(
                "resultDescription"
            );

            const content = getElement(
                "resultCareers"
            );

            // Validate the form.

            if (
                !answers.interest ||
                !answers.strength ||
                !answers.experience
            ) {
                if (result) {
                    result.hidden = false;
                }

                if (title) {
                    title.textContent =
                        "Please Complete the Assessment";
                }

                if (description) {
                    description.textContent =
                        "Choose an answer for all three questions.";
                }

                if (content) {
                    content.replaceChildren();
                }

                return;
            }

            // Show loading state.

            if (submitButton) {
                submitButton.disabled = true;

                submitButton.textContent =
                    "Building Your Roadmap...";
            }

            if (result) {
                result.hidden = false;
            }

            if (title) {
                title.textContent =
                    "Preparing Your Recommendation...";
            }

            if (description) {
                description.textContent =
                    "Matching your answers and loading the full learning roadmap.";
            }

            if (content) {
                content.replaceChildren();
            }

            try {
                const response = await fetchJSON(
                    `${API_BASE_URL}/api/recommend`,
                    {
                        method: "POST",

                        headers: {
                            "Content-Type": "application/json",
                        },

                        body: JSON.stringify(answers),
                    }
                );

                if (
                    !response.recommended_career ||
                    !response.recommended_career.id
                ) {
                    throw new Error(
                        "The backend response did not include a valid career."
                    );
                }

                let career =
                    response.recommended_career;

                // If the backend returns only basic details,
                // fetch the complete roadmap separately.

                if (
                    !career.roadmap ||
                    !Array.isArray(
                        career.roadmap.stages
                    )
                ) {
                    career = await fetchJSON(
                        `${API_BASE_URL}/api/careers/${encodeURIComponent(career.id)}`
                    );
                }

                renderAssessmentResult(career);

            } catch (error) {
                console.error(
                    "Assessment error:",
                    error
                );

                if (title) {
                    title.textContent =
                        "Unable to Generate Recommendation";
                }

                if (description) {
                    description.textContent =
                        `${error.message} Check that FastAPI is running at ${API_BASE_URL}.`;
                }

                if (content) {
                    content.replaceChildren();
                }

            } finally {
                if (submitButton) {
                    submitButton.disabled = false;

                    submitButton.textContent =
                        "Find My Career";
                }
            }
        }
    );
}


// =====================================================
// INITIALIZE PAGE
// =====================================================

document.addEventListener(
    "DOMContentLoaded",
    () => {
        initializeCareerFilters();

        initializeCareerDetails();

        initializeAssessment();

        console.log(
            "CareerPathAI frontend initialized."
        );
    }
);