/* ==========================================
   CAREERPATHAI — QUIZ QUESTION BANK
========================================== */

window.CAREERPATHAI_QUIZ_BANK = {

    topics: {

        "variables, data types, and operators": [
            {
                question: "Which Python data type is used to store True or False?",
                options: ["int", "str", "bool", "float"],
                answer: 2,
                explanation: "The bool data type stores Boolean values: True and False."
            },
            {
                question: "What is the output of 10 // 3 in Python?",
                options: ["3.33", "3", "1", "4"],
                answer: 1,
                explanation: "The // operator performs floor division and returns the integer quotient."
            },
            {
                question: "Which operator checks whether two values are equal?",
                options: ["=", "==", "!=", ">="],
                answer: 1,
                explanation: "The == operator compares two values for equality."
            }
        ],

        "conditions and loops": [
            {
                question: "Which statement is used to execute code when a condition is true?",
                options: ["for", "if", "break", "import"],
                answer: 1,
                explanation: "The if statement executes its block when its condition evaluates to True."
            },
            {
                question: "Which loop is commonly used to iterate over a sequence?",
                options: ["for", "if", "class", "return"],
                answer: 0,
                explanation: "A for loop iterates over items in a sequence or other iterable."
            },
            {
                question: "What does the break statement do?",
                options: [
                    "Skips one iteration",
                    "Restarts the loop",
                    "Terminates the loop",
                    "Pauses the program"
                ],
                answer: 2,
                explanation: "break immediately terminates the nearest enclosing loop."
            }
        ],

        "functions and modules": [
            {
                question: "Which keyword is used to define a function in Python?",
                options: ["function", "define", "def", "func"],
                answer: 2,
                explanation: "Python uses the def keyword to define a function."
            },
            {
                question: "What does a return statement do?",
                options: [
                    "Repeats a function",
                    "Sends a result back to the caller",
                    "Imports a module",
                    "Creates a class"
                ],
                answer: 1,
                explanation: "return sends a value back to the code that called the function."
            }
        ],

        "forward kinematics": [
            {
                question: "What does forward kinematics calculate?",
                options: [
                    "Joint angles from a target position",
                    "End-effector position from joint variables",
                    "Motor torque only",
                    "Robot mass"
                ],
                answer: 1,
                explanation: "Forward kinematics calculates the end-effector pose using known joint variables and robot geometry."
            },
            {
                question: "What is a homogeneous transformation matrix used for in robotics?",
                options: [
                    "Representing position and orientation transformations",
                    "Measuring battery voltage",
                    "Calculating motor temperature",
                    "Storing camera images"
                ],
                answer: 0,
                explanation: "A homogeneous transformation matrix represents rotation and translation between coordinate frames."
            }
        ],

        "inverse kinematics concepts": [
            {
                question: "What is the main objective of inverse kinematics?",
                options: [
                    "Calculate end-effector position from joint angles",
                    "Find joint variables for a desired end-effector pose",
                    "Calculate robot weight",
                    "Measure motor speed"
                ],
                answer: 1,
                explanation: "Inverse kinematics finds joint variables that achieve a desired end-effector pose."
            },
            {
                question: "Why can inverse kinematics have multiple solutions?",
                options: [
                    "A robot configuration can sometimes reach the same target in different ways",
                    "The robot has no joints",
                    "The target position is always fixed",
                    "The motors are disconnected"
                ],
                answer: 0,
                explanation: "Different joint configurations can sometimes produce the same end-effector pose."
            }
        ],

        "nodes, topics, and messages": [
            {
                question: "What is a node in ROS 2?",
                options: [
                    "A physical robot wheel",
                    "An executable process that performs a specific task",
                    "A battery controller",
                    "A type of sensor"
                ],
                answer: 1,
                explanation: "A ROS 2 node is an executable process that performs a specific function in a robotic system."
            },
            {
                question: "What is the purpose of a ROS 2 topic?",
                options: [
                    "Store source code",
                    "Enable publisher-subscriber communication",
                    "Install packages",
                    "Control the operating system"
                ],
                answer: 1,
                explanation: "Topics provide a communication channel for publishers and subscribers."
            }
        ],

        "denavit–hartenberg parameters": [
            {
                question: "What does the DH parameter a represent?",
                options: [
                    "Link length",
                    "Joint angle",
                    "Link twist",
                    "Link offset"
                ],
                answer: 0,
                explanation: "In the standard DH convention, a represents the link length measured along the x-axis."
            },
            {
                question: "What does alpha represent in a standard DH table?",
                options: [
                    "Link length",
                    "Link twist",
                    "Joint offset",
                    "End-effector speed"
                ],
                answer: 1,
                explanation: "Alpha represents the link twist angle between adjacent joint axes."
            }
        ]
    },

    subtopics: {

        "variables and naming rules": [
            {
                question: "Which is a valid Python variable name?",
                options: [
                    "2value",
                    "my-value",
                    "my_value",
                    "class"
                ],
                answer: 2,
                explanation: "my_value is valid. Python variable names cannot start with a digit or contain a hyphen, and keywords cannot be used as names."
            }
        ],

        "integers, floats, strings, and booleans": [
            {
                question: "Which Python type represents decimal numbers?",
                options: ["int", "float", "str", "bool"],
                answer: 1,
                explanation: "float represents numbers with a fractional or decimal component."
            }
        ],

        "arithmetic, comparison, and logical operators": [
            {
                question: "What is the result of 5 > 3 and 2 < 4?",
                options: ["True", "False", "5", "Error"],
                answer: 0,
                explanation: "Both comparisons are True, so the and expression evaluates to True."
            }
        ],

        "conditional statements": [
            {
                question: "Which keyword checks another condition after an if statement?",
                options: ["else if", "elif", "then", "switch"],
                answer: 1,
                explanation: "Python uses elif to check another condition when the preceding if or elif condition is False."
            }
        ],

        "for loops and while loops": [
            {
                question: "How many times does range(5) iterate in a standard for loop?",
                options: ["4", "5", "6", "Infinite"],
                answer: 1,
                explanation: "range(5) produces 0, 1, 2, 3, and 4: five values."
            }
        ],

        "break, continue, and loop tracing": [
            {
                question: "What does continue do inside a loop?",
                options: [
                    "Terminates the entire program",
                    "Skips to the next iteration",
                    "Ends the loop permanently",
                    "Restarts the computer"
                ],
                answer: 1,
                explanation: "continue skips the remaining statements in the current iteration and moves to the next iteration."
            }
        ],

        "coordinate frames and joint variables": [
            {
                question: "Why are coordinate frames used in robotics?",
                options: [
                    "To describe positions and orientations relative to reference frames",
                    "To store program passwords",
                    "To increase battery capacity",
                    "To measure temperature"
                ],
                answer: 0,
                explanation: "Coordinate frames provide reference systems for describing robot links, joints, and end-effectors."
            }
        ],

        "homogeneous transformation matrices": [
            {
                question: "What is the usual size of a 3D homogeneous transformation matrix?",
                options: ["2 × 2", "3 × 3", "3 × 4", "4 × 4"],
                answer: 3,
                explanation: "A 3D homogeneous transformation matrix is commonly represented as a 4 × 4 matrix."
            }
        ],

        "understanding nodes": [
            {
                question: "Which command lists active ROS 2 nodes?",
                options: [
                    "ros2 topic list",
                    "ros2 node list",
                    "ros2 pkg list",
                    "ros2 run list"
                ],
                answer: 1,
                explanation: "ros2 node list displays the currently active ROS 2 nodes."
            }
        ],

        "topic-based communication": [
            {
                question: "Which ROS 2 command lists available topics?",
                options: [
                    "ros2 node list",
                    "ros2 topic list",
                    "ros2 service list",
                    "ros2 launch list"
                ],
                answer: 1,
                explanation: "ros2 topic list displays the topics currently available in the ROS 2 graph."
            }
        ]

    }
};