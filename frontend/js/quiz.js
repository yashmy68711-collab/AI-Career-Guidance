/* ==========================================
   CAREERPATHAI — QUIZ ENGINE
========================================== */

(() => {
    "use strict";

    const PASS_PERCENTAGE = 70;

    const BANK = window.CAREERPATHAI_QUIZ_BANK || {
        topics: {},
        subtopics: {}
    };

    const STORAGE_KEY = "careerpathai_quiz_results_v1";

    const normalize = (value) =>
        String(value || "")
            .toLowerCase()
            .trim()
            .replace(/[^a-z0-9]+/g, " ")
            .replace(/\s+/g, " ");

    let currentQuiz = null;

    let currentQuestionIndex = 0;

    let selectedAnswers = [];

    let quizSubmitted = false;

    let currentContext = null;

    function loadResults() {
        try {
            return JSON.parse(
                localStorage.getItem(STORAGE_KEY) || "{}"
            );
        } catch (error) {
            console.error("Could not load quiz results:", error);
            return {};
        }
    }

    function saveResults(results) {
        try {
            localStorage.setItem(
                STORAGE_KEY,
                JSON.stringify(results)
            );
        } catch (error) {
            console.error("Could not save quiz results:", error);
        }
    }

    function saveQuizResult(quizId, result) {
        const results = loadResults();

        results[quizId] = {
            ...result,
            updatedAt: new Date().toISOString()
        };

        saveResults(results);
    }

    function findQuestions(collection, name) {
        const key = normalize(name);

        const matchingKey = Object.keys(collection || {}).find(
            (item) => normalize(item) === key
        );

        return matchingKey
            ? collection[matchingKey]
            : [];
    }

    function getTopicQuestions(topic) {
        return findQuestions(BANK.topics, topic.title);
    }

    function getSubtopicQuestions(subtopic) {
        return findQuestions(BANK.subtopics, subtopic);
    }

    function createQuizId(type, careerId, topic, subtopic = "") {
        return [
            careerId,
            normalize(topic),
            type,
            normalize(subtopic)
        ].join("::");
    }

    function createQuizPanel() {
        const lesson = document.querySelector(
            "#academyModuleContent .academy-lesson"
        );

        if (!lesson) {
            return null;
        }

        const oldPanel = lesson.querySelector("#academyQuizPanel");

        if (oldPanel) {
            oldPanel.remove();
        }

        const panel = document.createElement("section");

        panel.id = "academyQuizPanel";
        panel.className = "academy-quiz-panel";

        panel.innerHTML = `
            <div class="academy-quiz-header">

                <span class="academy-small-label">
                    TEST YOUR KNOWLEDGE
                </span>

                <h3>Topic &amp; Subtopic Assessments</h3>

                <p>
                    Test your understanding after studying this lesson.
                </p>

            </div>

            <div class="academy-quiz-options">

                <button
                    type="button"
                    class="academy-quiz-option active"
                    data-quiz-type="topic"
                >
                    Topic-wise Test
                </button>

                <button
                    type="button"
                    class="academy-quiz-option"
                    data-quiz-type="subtopic"
                >
                    Subtopic-wise Test
                </button>

            </div>

            <div
                id="academySubtopicSelect"
                class="academy-subtopic-select"
                hidden
            >
                <label for="academyQuizSubtopic">
                    Select a subtopic
                </label>

                <select id="academyQuizSubtopic"></select>
            </div>

            <div id="academyQuizContent">

                <div class="academy-quiz-empty">
                    Choose an assessment to begin.
                </div>

            </div>
        `;

        lesson.appendChild(panel);

        return panel;
    }

    function renderSubtopicOptions(topic) {
        const select = document.querySelector(
            "#academyQuizSubtopic"
        );

        if (!select) {
            return;
        }

        select.innerHTML = topic.subtopics.map(
            (subtopic, index) => `
                <option value="${index}">
                    ${escapeHTML(subtopic)}
                </option>
            `
        ).join("");
    }

    function escapeHTML(value) {
        return String(value ?? "").replace(/[&<>"']/g, (char) => ({
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#39;"
        })[char]);
    }

    function showQuizMessage(message) {
        const content = document.querySelector(
            "#academyQuizContent"
        );

        if (!content) {
            return;
        }

        content.innerHTML = `
            <div class="academy-quiz-empty">
                ${escapeHTML(message)}
            </div>
        `;
    }

    function startTopicQuiz(context) {
        const questions = getTopicQuestions(context.topic);

        if (!questions.length) {
            showQuizMessage(
                "No topic-wise questions have been added for this topic yet. Add MCQs to quiz-data.js."
            );

            return;
        }

        startQuiz({
            type: "topic",
            title: context.topic.title,
            questions,
            context
        });
    }

    function startSubtopicQuiz(context, subtopic) {
        const questions = getSubtopicQuestions(subtopic);

        if (!questions.length) {
            showQuizMessage(
                "No questions have been added for this subtopic yet. Add MCQs to quiz-data.js."
            );

            return;
        }

        startQuiz({
            type: "subtopic",
            title: subtopic,
            questions,
            context
        });
    }

    function startQuiz(quiz) {
        currentQuiz = quiz;

        currentQuestionIndex = 0;

        selectedAnswers = new Array(
            quiz.questions.length
        ).fill(null);

        quizSubmitted = false;

        renderQuestion();
    }

    function renderQuestion() {
        const content = document.querySelector(
            "#academyQuizContent"
        );

        if (!content || !currentQuiz) {
            return;
        }

        const question =
            currentQuiz.questions[currentQuestionIndex];

        const total = currentQuiz.questions.length;

        const percentage = Math.round(
            ((currentQuestionIndex + 1) / total) * 100
        );

        content.innerHTML = `
            <div class="academy-quiz-progress">

                <div class="academy-quiz-progress-heading">
                    <span>
                        Question ${currentQuestionIndex + 1} of ${total}
                    </span>

                    <strong>${percentage}%</strong>
                </div>

                <div class="academy-quiz-progress-track">
                    <div
                        class="academy-quiz-progress-fill"
                        style="width: ${percentage}%"
                    ></div>
                </div>

            </div>

            <div class="academy-quiz-question">

                <h4>
                    ${escapeHTML(question.question)}
                </h4>

                <div class="academy-quiz-answers">

                    ${question.options.map((option, index) => `
                        <button
                            type="button"
                            class="academy-quiz-answer"
                            data-answer="${index}"
                        >
                            <span class="academy-answer-letter">
                                ${String.fromCharCode(65 + index)}
                            </span>

                            <span>
                                ${escapeHTML(option)}
                            </span>
                        </button>
                    `).join("")}

                </div>

            </div>

            <div class="academy-quiz-navigation">

                <button
                    type="button"
                    id="academyQuizPrevious"
                    ${currentQuestionIndex === 0 ? "disabled" : ""}
                >
                    ← Previous
                </button>

                <button
                    type="button"
                    id="academyQuizNext"
                    disabled
                >
                    ${currentQuestionIndex === total - 1
                        ? "Submit Test"
                        : "Next Question →"}
                </button>

            </div>
        `;

        const answerButtons = content.querySelectorAll(
            ".academy-quiz-answer"
        );

        answerButtons.forEach((button) => {
            button.addEventListener("click", () => {
                if (quizSubmitted) {
                    return;
                }

                const answer = Number(
                    button.dataset.answer
                );

                selectedAnswers[currentQuestionIndex] = answer;

                answerButtons.forEach((item) => {
                    item.classList.remove("selected");
                });

                button.classList.add("selected");

                const nextButton = document.querySelector(
                    "#academyQuizNext"
                );

                if (nextButton) {
                    nextButton.disabled = false;
                }
            });
        });

        const previousButton = document.querySelector(
            "#academyQuizPrevious"
        );

        previousButton.addEventListener("click", () => {
            if (currentQuestionIndex > 0) {
                currentQuestionIndex--;
                renderQuestion();
            }
        });

        const nextButton = document.querySelector(
            "#academyQuizNext"
        );

        nextButton.addEventListener("click", () => {
            if (selectedAnswers[currentQuestionIndex] === null) {
                return;
            }

            if (currentQuestionIndex < total - 1) {
                currentQuestionIndex++;
                renderQuestion();
            } else {
                submitQuiz();
            }
        });

        const selected = selectedAnswers[currentQuestionIndex];

        if (selected !== null) {
            answerButtons[selected]?.classList.add("selected");
            nextButton.disabled = false;
        }
    }

    function submitQuiz() {
        if (!currentQuiz) {
            return;
        }

        quizSubmitted = true;

        const questions = currentQuiz.questions;

        let correct = 0;

        questions.forEach((question, index) => {
            if (selectedAnswers[index] === question.answer) {
                correct++;
            }
        });

        const total = questions.length;

        const percentage = Math.round(
            (correct / total) * 100
        );

        const passed = percentage >= PASS_PERCENTAGE;

        const quizId = createQuizId(
            currentQuiz.type,
            currentContext.careerId,
            currentContext.topic.title,
            currentQuiz.type === "subtopic"
                ? currentQuiz.title
                : ""
        );

        const result = {
            type: currentQuiz.type,
            title: currentQuiz.title,
            correct,
            total,
            percentage,
            passed
        };

        saveQuizResult(quizId, result);

        renderResults(result);
    }

    function renderResults(result) {
        const content = document.querySelector(
            "#academyQuizContent"
        );

        if (!content) {
            return;
        }

        const questions = currentQuiz.questions;

        content.innerHTML = `
            <div class="academy-quiz-result">

                <div class="academy-quiz-score">
                    <span>Your Score</span>

                    <strong>
                        ${result.percentage}%
                    </strong>

                    <small>
                        ${result.correct} out of ${result.total} correct
                    </small>
                </div>

                <h4 class="${result.passed ? "quiz-passed" : "quiz-failed"}">
                    ${result.passed
                        ? "Congratulations! You passed the test."
                        : "Keep practising! You can try again."}
                </h4>

                <p>
                    Passing score: ${PASS_PERCENTAGE}%
                </p>

                <div class="academy-quiz-review">

                    <h4>Answer Review</h4>

                    ${questions.map((question, index) => {
                        const isCorrect =
                            selectedAnswers[index] === question.answer;

                        return `
                            <div class="academy-review-item">

                                <strong>
                                    ${index + 1}. ${escapeHTML(question.question)}
                                </strong>

                                <p class="${isCorrect ? "quiz-correct" : "quiz-incorrect"}">
                                    Your answer:
                                    ${selectedAnswers[index] === null
                                        ? "Not answered"
                                        : escapeHTML(
                                            question.options[selectedAnswers[index]]
                                        )}
                                </p>

                                <p>
                                    Correct answer:
                                    ${escapeHTML(
                                        question.options[question.answer]
                                    )}
                                </p>

                                <p class="academy-explanation">
                                    ${escapeHTML(question.explanation)}
                                </p>

                            </div>
                        `;
                    }).join("")}

                </div>

                <button
                    type="button"
                    class="academy-button"
                    id="academyQuizRetake"
                >
                    Retake Test
                </button>

            </div>
        `;

        $("#academyQuizRetake").addEventListener(
            "click",
            () => startQuiz(currentQuiz)
        );
    }

    function renderQuiz(context) {
        currentContext = context;

        const panel = createQuizPanel();

        if (!panel) {
            return;
        }

        currentQuiz = null;

        currentQuestionIndex = 0;

        selectedAnswers = [];

        const topicButton = panel.querySelector(
            '[data-quiz-type="topic"]'
        );

        const subtopicButton = panel.querySelector(
            '[data-quiz-type="subtopic"]'
        );

        const subtopicSelect = panel.querySelector(
            "#academySubtopicSelect"
        );

        const select = panel.querySelector(
            "#academyQuizSubtopic"
        );

        renderSubtopicOptions(context.topic);

        topicButton.addEventListener("click", () => {
            topicButton.classList.add("active");

            subtopicButton.classList.remove("active");

            subtopicSelect.hidden = true;

            startTopicQuiz(context);
        });

        subtopicButton.addEventListener("click", () => {
            subtopicButton.classList.add("active");

            topicButton.classList.remove("active");

            subtopicSelect.hidden = false;

            const selectedSubtopic =
                context.topic.subtopics[Number(select.value)];

            startSubtopicQuiz(
                context,
                selectedSubtopic
            );
        });

        select.addEventListener("change", () => {
            const selectedSubtopic =
                context.topic.subtopics[Number(select.value)];

            startSubtopicQuiz(
                context,
                selectedSubtopic
            );
        });

        startTopicQuiz(context);
    }

    function init() {
        document.addEventListener(
            "academy:lesson-loaded",
            (event) => {
                renderQuiz(event.detail);
            }
        );
    }

    if (document.readyState === "loading") {
        document.addEventListener(
            "DOMContentLoaded",
            init
        );
    } else {
        init();
    }

})();