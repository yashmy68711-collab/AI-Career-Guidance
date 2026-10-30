(() => {
    "use strict";

    /*
     * CAREERPATHAI — LEARNING ACADEMY
     *
     * Features:
     * 1. Load careers from the FastAPI backend.
     * 2. Display career modules and topics.
     * 3. Generate learning objectives and study notes.
     * 4. Provide YouTube search links.
     * 5. Track completed topics.
     * 6. Save progress in localStorage.
     * 7. Navigate between topics.
     * 8. Print notes or save them as PDF.
     */

    const API_BASE_URL = "http://127.0.0.1:8000";

    const STORAGE_PREFIX = "careerpathai_academy_progress_v1";

    const $ = (selector, root = document) =>
        root.querySelector(selector);

    const state = {
        careers: [],
        career: null,
        modules: [],
        moduleIndex: 0,
        topicIndex: 0,
        completed: new Set(),
        loading: false
    };

    const elements = {};

    /* ==========================================
       INITIALIZE HTML ELEMENT REFERENCES
    ========================================== */

    function getElements() {
        elements.careerSelect = $("#academyCareer");
        elements.loadButton = $("#loadCurriculum");
        elements.status = $("#academyStatus");
        elements.content = $("#academyContent");

        elements.careerTitle = $("#academyCareerTitle");
        elements.description = $("#academyDescription");

        elements.moduleList = $("#academyModuleList");
        elements.moduleContent = $("#academyModuleContent");

        elements.progressText = $("#academyProgressText");
        elements.progressBar = $("#academyProgressBar");
        elements.progressDetails = $("#academyProgressDetails");
    }

    /* ==========================================
       SAFE HTML OUTPUT
    ========================================== */

    function escapeHTML(value) {
        return String(value ?? "").replace(/[&<>"']/g, (character) => {
            const replacements = {
                "&": "&amp;",
                "<": "&lt;",
                ">": "&gt;",
                '"': "&quot;",
                "'": "&#39;"
            };

            return replacements[character];
        });
    }

    function slugify(value) {
        return String(value ?? "")
            .toLowerCase()
            .trim()
            .replace(/[^a-z0-9]+/g, "-")
            .replace(/^-|-$/g, "");
    }

    /* ==========================================
       STATUS MESSAGES
    ========================================== */

    function setStatus(message, isError = false) {
        if (!elements.status) {
            return;
        }

        elements.status.textContent = message;

        elements.status.classList.toggle(
            "is-error",
            isError
        );
    }

    /* ==========================================
       BACKEND API REQUESTS
    ========================================== */

    async function fetchJSON(url) {
        const response = await fetch(url, {
            method: "GET",
            headers: {
                Accept: "application/json"
            }
        });

        if (!response.ok) {
            let message = `HTTP error ${response.status}`;

            try {
                const data = await response.json();

                if (data.detail) {
                    message = typeof data.detail === "string"
                        ? data.detail
                        : JSON.stringify(data.detail);
                }
            } catch (_) {
                // Use the HTTP status if no JSON error is available.
            }

            throw new Error(message);
        }

        return response.json();
    }

    /* ==========================================
       CAREER IDENTIFICATION
    ========================================== */

    function getCareerId(career = state.career) {
        return career?.id || "unknown";
    }

    function getStorageKey() {
        return `${STORAGE_PREFIX}_${getCareerId()}`;
    }

    function getTopicKey(topic) {
        return `${getCareerId()}:${topic.id}`;
    }

    /* ==========================================
       SAVE AND RESTORE PROGRESS
    ========================================== */

    function loadSavedProgress() {
        state.completed = new Set();

        try {
            const stored = localStorage.getItem(getStorageKey());

            const saved = JSON.parse(stored || "[]");

            if (Array.isArray(saved)) {
                saved.forEach((topicId) => {
                    if (typeof topicId === "string") {
                        state.completed.add(topicId);
                    }
                });
            }
        } catch (error) {
            console.warn(
                "Unable to restore Academy progress:",
                error
            );
        }
    }

    function saveProgress() {
        try {
            localStorage.setItem(
                getStorageKey(),
                JSON.stringify(Array.from(state.completed))
            );

            return true;
        } catch (error) {
            console.error(
                "Unable to save Academy progress:",
                error
            );

            setStatus(
                "Progress could not be saved in this browser.",
                true
            );

            return false;
        }
    }

    /* ==========================================
       YOUTUBE SEARCH LINKS
    ========================================== */

    function youtubeSearchURL(query) {
        return (
            "https://www.youtube.com/results?search_query=" +
            encodeURIComponent(query)
        );
    }

    /* ==========================================
       LEARNING OBJECTIVES
    ========================================== */

    function buildObjectives(topic) {
        return [
            `Understand the fundamental concepts of ${topic}.`,
            `Identify important terminology related to ${topic}.`,
            `Explain how ${topic} works using a simple example.`,
            `Apply the concept in a small practical exercise.`
        ];
    }

    /* ==========================================
       TOPIC SUBTOPICS
    ========================================== */

    function buildSubtopics(topic) {
        const normalized = String(topic)
            .toLowerCase()
            .trim();

        const curriculum = [
            {
                keywords: [
                    "variable",
                    "data type",
                    "operator"
                ],
                topics: [
                    "Variables and naming rules",
                    "Integers, floats, strings, and booleans",
                    "Type conversion",
                    "Arithmetic, comparison, and logical operators"
                ]
            },
            {
                keywords: [
                    "condition",
                    "loop",
                    "iteration"
                ],
                topics: [
                    "Conditional statements",
                    "Comparison and logical operators",
                    "For loops and while loops",
                    "Break, continue, and loop tracing"
                ]
            },
            {
                keywords: [
                    "function",
                    "module"
                ],
                topics: [
                    "Defining and calling functions",
                    "Parameters, arguments, and return values",
                    "Local and global scope",
                    "Importing and organising modules"
                ]
            },
            {
                keywords: [
                    "class",
                    "object",
                    "oop",
                    "object-oriented"
                ],
                topics: [
                    "Classes and objects",
                    "Attributes and methods",
                    "Constructors and initialisation",
                    "Encapsulation, inheritance, and polymorphism"
                ]
            },
            {
                keywords: [
                    "forward kinematic"
                ],
                topics: [
                    "Coordinate frames and joint variables",
                    "Link transformations",
                    "Homogeneous transformation matrices",
                    "Calculating end-effector position and orientation"
                ]
            },
            {
                keywords: [
                    "inverse kinematic"
                ],
                topics: [
                    "Target position and orientation",
                    "Joint variables and robot configuration",
                    "Geometric and analytical methods",
                    "Reachability and multiple solutions"
                ]
            },
            {
                keywords: [
                    "denavit",
                    "dh parameter"
                ],
                topics: [
                    "Link length a",
                    "Link twist alpha",
                    "Link offset d",
                    "Joint angle theta and DH transformation"
                ]
            },
            {
                keywords: [
                    "ros 2 workspace",
                    "ros2 workspace",
                    "ros 2 package",
                    "ros2 package"
                ],
                topics: [
                    "Workspace structure",
                    "Creating a ROS 2 package",
                    "Building packages using colcon",
                    "Sourcing the workspace setup file"
                ]
            },
            {
                keywords: [
                    "node",
                    "topic",
                    "message"
                ],
                topics: [
                    "Understanding nodes",
                    "Topic-based communication",
                    "Message types",
                    "Inspecting nodes and topics from the terminal"
                ]
            },
            {
                keywords: [
                    "opencv",
                    "image processing"
                ],
                topics: [
                    "Reading and displaying images",
                    "Image colour spaces and channels",
                    "Resizing, cropping, and filtering",
                    "Thresholding and contour detection"
                ]
            },
            {
                keywords: [
                    "dataframe",
                    "series"
                ],
                topics: [
                    "Creating Series and DataFrames",
                    "Selecting rows and columns",
                    "Filtering records",
                    "Inspecting data types and dimensions"
                ]
            },
            {
                keywords: [
                    "missing value",
                    "duplicate",
                    "data cleaning"
                ],
                topics: [
                    "Detecting missing values",
                    "Dropping or imputing missing data",
                    "Finding duplicate records",
                    "Validating cleaned data"
                ]
            },
            {
                keywords: [
                    "regression",
                    "classification"
                ],
                topics: [
                    "Features and target variables",
                    "Regression for numerical predictions",
                    "Classification for categorical predictions",
                    "Choosing evaluation metrics"
                ]
            },
            {
                keywords: [
                    "semantic html",
                    "html structure"
                ],
                topics: [
                    "HTML document structure",
                    "Header, nav, main, section, and footer",
                    "Headings and document outline",
                    "Accessible and meaningful markup"
                ]
            },
            {
                keywords: [
                    "flexbox",
                    "css grid"
                ],
                topics: [
                    "Flexbox axes and alignment",
                    "Spacing and distribution",
                    "Grid rows and columns",
                    "Responsive layouts"
                ]
            },
            {
                keywords: [
                    "dom manipulation",
                    "document object model"
                ],
                topics: [
                    "Selecting HTML elements",
                    "Changing text and attributes",
                    "Creating and removing elements",
                    "Responding to browser events"
                ]
            },
            {
                keywords: [
                    "rest api",
                    "restful api"
                ],
                topics: [
                    "Resources and endpoints",
                    "GET, POST, PUT, PATCH, and DELETE",
                    "JSON request and response bodies",
                    "HTTP status codes and error handling"
                ]
            },
            {
                keywords: [
                    "subnet",
                    "ip address"
                ],
                topics: [
                    "IPv4 address structure",
                    "Private and public IP addresses",
                    "Subnet masks and CIDR notation",
                    "Network and host portions"
                ]
            },
            {
                keywords: [
                    "confidentiality",
                    "integrity",
                    "availability"
                ],
                topics: [
                    "Confidentiality",
                    "Integrity",
                    "Availability",
                    "Applying the CIA triad to examples"
                ]
            },
            {
                keywords: [
                    "minimum viable product",
                    "mvp"
                ],
                topics: [
                    "Identifying the problem",
                    "Selecting essential features",
                    "Building a basic prototype",
                    "Testing assumptions with user feedback"
                ]
            }
        ];

        const match = curriculum.find((entry) =>
            entry.keywords.some((keyword) =>
                normalized.includes(keyword)
            )
        );

        if (match) {
            return [...match.topics];
        }

        return [
            `Core concepts and terminology of ${topic}`,
            `How ${topic} works and where it is used`,
            `Methods, tools, and workflows related to ${topic}`,
            `Examples, limitations, and common mistakes`,
            `Practical applications of ${topic}`
        ];
    }

    /* ==========================================
       STUDY NOTES
    ========================================== */

    function buildStudyNotes(topic, moduleTitle, careerTitle) {
        const subtopics = buildSubtopics(topic);

        const numberedSubtopics = subtopics
            .map((item, index) => `${index + 1}. ${item}`)
            .join("\n");

        return [
            `OVERVIEW\n${topic} is part of the "${moduleTitle}" module in the ${careerTitle} learning path. Begin by understanding what the concept means, why it is useful, and which problem it helps solve.`,

            `KEY AREAS TO STUDY\n${numberedSubtopics}`,

            `STUDY METHOD\n1. Learn the definition and basic terminology.\n2. Follow a beginner tutorial.\n3. Write down unfamiliar terms.\n4. Work through a small example yourself.\n5. Modify the example and predict the result.\n6. Explain the concept without looking at your notes.`,

            `SELF-ASSESSMENT\nCan you explain ${topic} in your own words? Can you give an example? Can you identify a common mistake or limitation? Revisit the relevant subtopic if you need more practice.`,

            `IMPORTANT\nThese are generated study notes and learning prompts, not a complete textbook chapter. Use the tutorial links and practical exercises to develop a deeper understanding.`
        ].join("\n\n");
    }

    /* ==========================================
       PRACTICE TASKS
    ========================================== */

    function buildPracticeTasks(topic) {
        return [
            `Write a short explanation of ${topic} in your own words.`,
            `Find or create a beginner example related to ${topic}.`,
            "Modify the example and explain what changes.",
            "Record your observations and key takeaways."
        ];
    }

    /* ==========================================
       NORMALIZE BACKEND CAREER DATA
    ========================================== */

    function normalizeCareer(career) {
        const stages = Array.isArray(career?.roadmap?.stages)
            ? career.roadmap.stages
            : [];

        const modules = stages.map((stage, moduleIndex) => {
            const rawTopics = Array.isArray(stage.topics)
                ? stage.topics
                : [];

            const topics = rawTopics.map((rawTopic, topicIndex) => {
                const title = typeof rawTopic === "string"
                    ? rawTopic
                    : String(
                        rawTopic?.title ||
                        rawTopic?.name ||
                        "Learning topic"
                    );

                const subtopics = buildSubtopics(title);

                return {
                    id: [
                        slugify(career.id),
                        moduleIndex + 1,
                        topicIndex + 1,
                        slugify(title)
                    ].join("-"),

                    title,

                    objectives: buildObjectives(title),

                    subtopics,

                    notes: buildStudyNotes(
                        title,
                        stage.title || `Module ${moduleIndex + 1}`,
                        career.title || career.id
                    ),

                    practiceTasks: buildPracticeTasks(title),

                    videoUrl: youtubeSearchURL(
                        `${career.title || career.id} ${title} tutorial`
                    ),

                    subtopicVideos: subtopics.map((subtopic) => ({
                        title: `${subtopic} tutorial`,

                        url: youtubeSearchURL(
                            `${career.title || career.id} ${title} ${subtopic} tutorial`
                        )
                    }))
                };
            });

            return {
                id: `${slugify(career.id)}-module-${moduleIndex + 1}`,

                title: stage.title || `Module ${moduleIndex + 1}`,

                duration: stage.duration || "Self-paced",

                completionGoal: stage.completion_goal || "",

                topics
            };
        });

        return {
            id: career.id,

            title: career.title || career.id,

            description: career.description || "",

            duration:
                career.roadmap?.estimated_duration ||
                "Self-paced",

            weeklyHours:
                career.roadmap?.weekly_study_hours ||
                "",

            skills: Array.isArray(career.skills)
                ? career.skills
                : [],

            resources: Array.isArray(career.resources)
                ? career.resources
                : [],

            modules
        };
    }

    /* ==========================================
       FLATTEN TOPICS FOR NAVIGATION
    ========================================== */

    function getAllTopics() {
        return state.modules.flatMap((module, moduleIndex) =>
            module.topics.map((topic, topicIndex) => ({
                moduleIndex,
                topicIndex,
                topic
            }))
        );
    }

    /* ==========================================
       UPDATE LEARNING PROGRESS
    ========================================== */

    function updateProgress() {
        const topics = getAllTopics();

        const total = topics.length;

        const completedCount = topics.filter(({ topic }) =>
            state.completed.has(getTopicKey(topic))
        ).length;

        const percentage = total
            ? Math.round((completedCount / total) * 100)
            : 0;

        if (elements.progressText) {
            elements.progressText.textContent = `${percentage}%`;
        }

        if (elements.progressBar) {
            elements.progressBar.style.width = `${percentage}%`;

            elements.progressBar.setAttribute(
                "role",
                "progressbar"
            );

            elements.progressBar.setAttribute(
                "aria-valuemin",
                "0"
            );

            elements.progressBar.setAttribute(
                "aria-valuemax",
                "100"
            );

            elements.progressBar.setAttribute(
                "aria-valuenow",
                String(percentage)
            );
        }

        if (elements.progressDetails) {
            elements.progressDetails.textContent =
                `${completedCount} of ${total} topics completed`;
        }
    }

    /* ==========================================
       RENDER MODULE SIDEBAR
    ========================================== */

    function renderModules() {
        if (!elements.moduleList) {
            return;
        }

        if (!state.modules.length) {
            elements.moduleList.innerHTML = `
                <div class="academy-empty">
                    No curriculum modules are available.
                </div>
            `;

            return;
        }

        elements.moduleList.innerHTML = state.modules
            .map((module, index) => {
                const total = module.topics.length;

                const completed = module.topics.filter((topic) =>
                    state.completed.has(getTopicKey(topic))
                ).length;

                const active = index === state.moduleIndex;

                return `
                    <button
                        type="button"
                        class="academy-module-button ${active ? "active" : ""}"
                        data-module-index="${index}"
                        aria-pressed="${active}"
                    >
                        <span class="academy-module-number">
                            ${String(index + 1).padStart(2, "0")}
                        </span>

                        <span class="academy-module-info">
                            <strong>
                                ${escapeHTML(module.title)}
                            </strong>

                            <small>
                                ${escapeHTML(module.duration)}
                                · ${completed}/${total} topics
                            </small>
                        </span>
                    </button>
                `;
            })
            .join("");

        elements.moduleList
            .querySelectorAll("[data-module-index]")
            .forEach((button) => {
                button.addEventListener("click", () => {
                    state.moduleIndex = Number(
                        button.dataset.moduleIndex
                    );

                    state.topicIndex = 0;

                    renderModules();
                    renderLesson();
                });
            });
    }

    /* ==========================================
       RENDER REUSABLE LISTS
    ========================================== */

    function renderStringList(items, className) {
        if (!Array.isArray(items) || items.length === 0) {
            return `
                <p class="academy-muted">
                    No items are available for this section.
                </p>
            `;
        }

        return `
            <ul class="${className}">
                ${items.map((item) => `
                    <li>${escapeHTML(item)}</li>
                `).join("")}
            </ul>
        `;
    }

    /* ==========================================
       RENDER CURRENT LESSON
    ========================================== */

    function renderLesson() {
        if (!elements.moduleContent) {
            return;
        }

        const module = state.modules[state.moduleIndex];

        const topic = module?.topics?.[state.topicIndex];

        if (!module || !topic) {
            elements.moduleContent.innerHTML = `
                <div class="academy-empty">
                    <h3>No topics available</h3>
                    <p>
                        This module does not currently contain
                        any learning topics.
                    </p>
                </div>
            `;

            return;
        }

        const allTopics = getAllTopics();

        const globalIndex = allTopics.findIndex(
            (entry) => entry.topic.id === topic.id
        );

        const isCompleted = state.completed.has(
            getTopicKey(topic)
        );

        const isFirstTopic = globalIndex <= 0;

        const isLastTopic =
            globalIndex >= allTopics.length - 1;

        const resources = state.career.resources.slice(0, 4);

        const resourceHTML = resources
            .filter((resource) => resource.url)
            .map((resource) => `
                <a
                    class="academy-video-link"
                    href="${escapeHTML(resource.url)}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    <span aria-hidden="true">↗</span>

                    <span>
                        ${escapeHTML(resource.title || resource.name || "Learning resource")}
                    </span>
                </a>
            `)
            .join("");

        elements.moduleContent.innerHTML = `
            <article class="academy-lesson">

                <div class="academy-lesson-meta">
                    <span>${escapeHTML(module.title)}</span>
                    <span>${escapeHTML(module.duration)}</span>
                </div>

                <h2>${escapeHTML(topic.title)}</h2>

                <p class="academy-lesson-intro">
                    ${escapeHTML(state.career.title)}
                    · Topic ${globalIndex + 1} of ${allTopics.length}
                </p>

                <section class="academy-lesson-section">
                    <h3>Learning objectives</h3>

                    ${renderStringList(
                        topic.objectives,
                        "academy-objectives"
                    )}
                </section>

                <section class="academy-lesson-section">
                    <h3>Subtopics</h3>

                    ${renderStringList(
                        topic.subtopics,
                        "academy-subtopics"
                    )}
                </section>

                <section class="academy-notes">
                    <div class="academy-notes-heading">
                        <span aria-hidden="true">✦</span>
                        <h3>Study notes</h3>
                    </div>

                    <p>${escapeHTML(topic.notes)}</p>
                </section>

                <section class="academy-lesson-section">
                    <h3>Practice tasks</h3>

                    ${renderStringList(
                        topic.practiceTasks,
                        "academy-practice"
                    )}
                </section>

                <section class="academy-lesson-section">
                    <h3>YouTube tutorial</h3>

                    <a
                        class="academy-video-link academy-primary-video"
                        href="${escapeHTML(topic.videoUrl)}"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        <span aria-hidden="true">▶</span>

                        <span>
                            Search for ${escapeHTML(topic.title)} tutorials
                        </span>

                        <span aria-hidden="true">↗</span>
                    </a>

                    <p class="academy-muted">
                        This opens YouTube search results.
                        Individual videos have not been verified
                        by CareerPathAI.
                    </p>
                </section>

                <section class="academy-lesson-section">
                    <h3>YouTube tutorials for subtopics</h3>

                    <div class="academy-video-list">
                        ${topic.subtopicVideos.map((video) => `
                            <a
                                class="academy-video-link"
                                href="${escapeHTML(video.url)}"
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                <span aria-hidden="true">▶</span>

                                <span>
                                    ${escapeHTML(video.title)}
                                </span>

                                <span aria-hidden="true">↗</span>
                            </a>
                        `).join("")}
                    </div>
                </section>

                ${resourceHTML ? `
                    <section class="academy-lesson-section">
                        <h3>Additional career resources</h3>

                        <div class="academy-video-list">
                            ${resourceHTML}
                        </div>
                    </section>
                ` : ""}

                ${module.completionGoal ? `
                    <section class="academy-lesson-section">
                        <h3>Module completion goal</h3>

                        <p class="academy-muted">
                            ${escapeHTML(module.completionGoal)}
                        </p>
                    </section>
                ` : ""}

                <div class="academy-lesson-actions">

                    <button
                        type="button"
                        class="academy-button ${isCompleted ? "academy-button-completed" : ""}"
                        id="academyToggleComplete"
                    >
                        ${isCompleted
                            ? "✓ Mark as incomplete"
                            : "✓ Mark as completed"}
                    </button>

                    <button
                        type="button"
                        class="academy-button academy-print-button"
                        id="academyPrintNotes"
                    >
                        Print / Save as PDF
                    </button>

                </div>

                <nav
                    class="academy-topic-navigation"
                    aria-label="Lesson navigation"
                >
                    <button
                        type="button"
                        class="academy-navigation-button"
                        id="academyPrevious"
                        ${isFirstTopic ? "disabled" : ""}
                    >
                        ← Previous topic
                    </button>

                    <span>
                        Topic ${globalIndex + 1} of ${allTopics.length}
                    </span>

                    <button
                        type="button"
                        class="academy-navigation-button"
                        id="academyNext"
                        ${isLastTopic ? "disabled" : ""}
                    >
                        Next topic →
                    </button>
                </nav>

            </article>
        `;

        /* Mark topic complete or incomplete. */

        $("#academyToggleComplete", elements.moduleContent)
            .addEventListener("click", () => {
                const key = getTopicKey(topic);

                if (state.completed.has(key)) {
                    state.completed.delete(key);
                } else {
                    state.completed.add(key);
                }

                saveProgress();

                renderModules();
                renderLesson();
                updateProgress();
            });

        /* Print notes or save as PDF. */

        $("#academyPrintNotes", elements.moduleContent)
            .addEventListener("click", () => {
                window.print();
            });

        /* Topic navigation. */

        $("#academyPrevious", elements.moduleContent)
            .addEventListener("click", () => {
                moveTopic(-1);
            });

        $("#academyNext", elements.moduleContent)
            .addEventListener("click", () => {
                moveTopic(1);
            });
    }

    /* ==========================================
       PREVIOUS / NEXT TOPIC
    ========================================== */

    function moveTopic(direction) {
        const topics = getAllTopics();

        const currentModule = state.modules[state.moduleIndex];

        const currentTopic =
            currentModule?.topics?.[state.topicIndex];

        const currentIndex = topics.findIndex(
            (entry) => entry.topic.id === currentTopic?.id
        );

        const nextEntry = topics[currentIndex + direction];

        if (!nextEntry) {
            return;
        }

        state.moduleIndex = nextEntry.moduleIndex;

        state.topicIndex = nextEntry.topicIndex;

        renderModules();
        renderLesson();

        if (elements.moduleContent) {
            elements.moduleContent.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        }
    }

    /* ==========================================
       LOAD A SELECTED CAREER
    ========================================== */

    async function loadSelectedCareer() {
        if (
            !elements.careerSelect ||
            !elements.content ||
            state.loading
        ) {
            return;
        }

        const careerId = elements.careerSelect.value;

        if (!careerId) {
            setStatus(
                "Choose a career to view its curriculum.",
                true
            );

            return;
        }

        state.loading = true;

        if (elements.loadButton) {
            elements.loadButton.disabled = true;
        }

        elements.content.hidden = true;

        setStatus("Loading curriculum from CareerPathAI...");

        try {
            const data = await fetchJSON(
                `${API_BASE_URL}/api/careers/${encodeURIComponent(careerId)}`
            );

            if (!data || !data.id) {
                throw new Error(
                    "The backend returned invalid career data."
                );
            }

            state.career = normalizeCareer(data);

            state.modules = state.career.modules;

            state.moduleIndex = 0;

            state.topicIndex = 0;

            loadSavedProgress();

            if (elements.careerTitle) {
                elements.careerTitle.textContent =
                    state.career.title;
            }

            if (elements.description) {
                const extraDetails = [];

                if (state.career.duration) {
                    extraDetails.push(
                        `Estimated duration: ${state.career.duration}.`
                    );
                }

                if (state.career.weeklyHours) {
                    extraDetails.push(
                        `Suggested study time: ${state.career.weeklyHours} per week.`
                    );
                }

                elements.description.textContent = [
                    state.career.description,
                    ...extraDetails
                ]
                    .filter(Boolean)
                    .join(" ");
            }

            elements.content.hidden = false;

            renderModules();
            renderLesson();
            updateProgress();

            const totalTopics = getAllTopics().length;

            setStatus(
                `Curriculum loaded successfully: ${state.modules.length} modules and ${totalTopics} topics.`
            );

        } catch (error) {
            console.error(
                "Learning Academy loading error:",
                error
            );

            state.career = null;
            state.modules = [];

            elements.content.hidden = true;

            setStatus(
                `Could not load the curriculum: ${error.message}. Check that your backend is running at ${API_BASE_URL}.`,
                true
            );

        } finally {
            state.loading = false;

            if (elements.loadButton) {
                elements.loadButton.disabled = false;
            }
        }
    }

    /* ==========================================
       POPULATE CAREER DROPDOWN
    ========================================== */

    function populateCareerDropdown(careers) {
        if (!elements.careerSelect) {
            return;
        }

        if (!careers.length) {
            elements.careerSelect.innerHTML = `
                <option value="">
                    No careers available
                </option>
            `;

            return;
        }

        const previousValue = elements.careerSelect.value;

        elements.careerSelect.innerHTML = careers
            .map((career) => `
                <option value="${escapeHTML(career.id)}">
                    ${escapeHTML(career.title || career.id)}
                </option>
            `)
            .join("");

        const previousCareerExists = careers.some(
            (career) => career.id === previousValue
        );

        if (previousCareerExists) {
            elements.careerSelect.value = previousValue;
            return;
        }

        const roboticsCareer = careers.find(
            (career) => career.id === "robotics"
        );

        elements.careerSelect.value = roboticsCareer
            ? roboticsCareer.id
            : careers[0].id;
    }

    /* ==========================================
       INITIALIZE LEARNING ACADEMY
    ========================================== */

    async function initialize() {
        getElements();

        const requiredElements = [
            elements.careerSelect,
            elements.loadButton,
            elements.status,
            elements.content,
            elements.moduleList,
            elements.moduleContent
        ];

        if (requiredElements.some((element) => !element)) {
            console.error(
                "Learning Academy HTML elements are missing. Check the Academy section in index.html."
            );

            return;
        }

        elements.loadButton.addEventListener(
            "click",
            loadSelectedCareer
        );

        elements.careerSelect.addEventListener(
            "change",
            loadSelectedCareer
        );

        try {
            setStatus("Connecting to the CareerPathAI backend...");

            const response = await fetchJSON(
                `${API_BASE_URL}/api/careers`
            );

            state.careers = Array.isArray(response.careers)
                ? response.careers
                : [];

            populateCareerDropdown(state.careers);

            if (!state.careers.length) {
                setStatus(
                    "The backend is running, but no careers were returned.",
                    true
                );

                return;
            }

            await loadSelectedCareer();

        } catch (error) {
            console.error(
                "Learning Academy initialization failed:",
                error
            );

            setStatus(
                `Could not connect to the backend. Start FastAPI and reload the page. Details: ${error.message}`,
                true
            );
        }
    }

    /* ==========================================
       START WHEN THE DOCUMENT IS READY
    ========================================== */

    if (document.readyState === "loading") {
        document.addEventListener(
            "DOMContentLoaded",
            initialize
        );
    } else {
        initialize();
    }

})();

/* Notify the quiz system that a new lesson has loaded. */

document.dispatchEvent(
    new CustomEvent("academy:lesson-loaded", {
        detail: {
            careerId: state.career.id,
            career: state.career,
            module: module,
            topic: topic
        }
    })
);