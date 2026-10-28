from copy import deepcopy
from urllib.parse import quote_plus

from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/api/curriculum",
    tags=["Learning Curriculum"],
)


# ============================================================
# CAREERPATHAI LEARNING ACADEMY
# Structured curricula: modules, topics, subtopics, notes,
# objectives, practice tasks, and YouTube search suggestions.
# ============================================================

CURRICULUM = {
    "robotics": {
        "career": "AI & Robotics Engineer",
        "description": (
            "Learn programming, mathematics, electronics, computer vision, "
            "robot kinematics, ROS 2, simulation, and autonomous robotics."
        ),
        "level": "Beginner to Advanced",
        "modules": [
            {
                "id": "robotics-python",
                "title": "Module 1: Python Programming",
                "level": "Beginner",
                "estimated_hours": 25,
                "topics": [
                    {
                        "id": "python-variables",
                        "title": "Variables and Data Types",
                        "subtopics": [
                            "Variables and naming rules",
                            "Integers, floats, strings, and booleans",
                            "Lists, tuples, dictionaries, and sets",
                            "Type conversion",
                            "User input and output",
                        ],
                        "objectives": [
                            "Understand Python's basic data types.",
                            "Store and manipulate sensor readings.",
                            "Use collections to organize robot data.",
                        ],
                        "notes": (
                            "A variable stores a value under a name. "
                            "Python provides numeric types such as int and float, "
                            "text values using str, and logical values using bool. "
                            "Lists store ordered collections, dictionaries store "
                            "key-value pairs, and tuples represent ordered "
                            "collections that are not normally modified."
                        ),
                        "practice_tasks": [
                            "Store a robot's name, battery percentage, and speed.",
                            "Create a list containing five sensor readings.",
                            "Use a dictionary to store a robot's configuration.",
                        ],
                    },
                    {
                        "id": "python-control-flow",
                        "title": "Conditions and Loops",
                        "subtopics": [
                            "if, elif, and else",
                            "Comparison and logical operators",
                            "for loops",
                            "while loops",
                            "break and continue",
                        ],
                        "objectives": [
                            "Write programs that make decisions.",
                            "Repeat operations using loops.",
                            "Implement simple robot control logic.",
                        ],
                        "notes": (
                            "Conditional statements select an action based on "
                            "a condition. Loops repeat instructions. For example, "
                            "a robot might stop when its battery is low or "
                            "continue checking a distance sensor while moving."
                        ),
                        "practice_tasks": [
                            "Print a warning when battery level falls below 20%.",
                            "Loop through a list of distance readings.",
                            "Stop a simulated robot when an obstacle is detected.",
                        ],
                    },
                    {
                        "id": "python-functions",
                        "title": "Functions and Modules",
                        "subtopics": [
                            "Defining functions with def",
                            "Parameters and return values",
                            "Scope and local variables",
                            "Importing modules",
                            "Exceptions and error handling",
                        ],
                        "objectives": [
                            "Break programs into reusable functions.",
                            "Return calculated sensor values.",
                            "Handle common runtime errors.",
                        ],
                        "notes": (
                            "Functions organize reusable logic. Parameters pass "
                            "data into a function, and return sends a result back. "
                            "Modules let you separate code into files. Exception "
                            "handling with try and except can help a program "
                            "respond to invalid input or unavailable resources."
                        ),
                        "practice_tasks": [
                            "Write a function that converts centimetres to metres.",
                            "Create a function that calculates average sensor readings.",
                            "Handle invalid numeric input using try and except.",
                        ],
                    },
                    {
                        "id": "python-oop",
                        "title": "Object-Oriented Programming",
                        "subtopics": [
                            "Classes and objects",
                            "Constructors and __init__",
                            "Instance attributes and methods",
                            "Inheritance",
                            "Encapsulation and composition",
                        ],
                        "objectives": [
                            "Represent robots as software objects.",
                            "Organize related data and behaviours.",
                            "Design reusable classes for robotics projects.",
                        ],
                        "notes": (
                            "A class defines the attributes and methods an object "
                            "can have. An object is an instance of a class. A Robot "
                            "class could store its name and battery level and "
                            "provide methods such as move(), stop(), and status(). "
                            "Composition allows one object to use other objects."
                        ),
                        "practice_tasks": [
                            "Create a Robot class with name and battery attributes.",
                            "Add move(), stop(), and display_status() methods.",
                            "Create two robot objects with different properties.",
                        ],
                    },
                    {
                        "id": "python-libraries",
                        "title": "Python Libraries and NumPy",
                        "subtopics": [
                            "Installing packages with pip",
                            "Importing libraries",
                            "NumPy arrays",
                            "Array indexing and slicing",
                            "Vector and matrix operations",
                        ],
                        "objectives": [
                            "Install and import Python packages.",
                            "Use arrays for numerical data.",
                            "Perform basic matrix calculations.",
                        ],
                        "notes": (
                            "Libraries provide reusable functionality. NumPy "
                            "supports efficient numerical arrays and mathematical "
                            "operations. Arrays are useful for sensor data, "
                            "coordinate vectors, transformations, and numerical "
                            "calculations in robotics."
                        ),
                        "practice_tasks": [
                            "Create a NumPy array containing sensor readings.",
                            "Calculate its mean, minimum, and maximum.",
                            "Multiply two compatible matrices.",
                        ],
                    },
                ],
            },
            {
                "id": "robotics-math",
                "title": "Module 2: Mathematics for Robotics",
                "level": "Beginner to Intermediate",
                "estimated_hours": 30,
                "topics": [
                    {
                        "id": "robotics-linear-algebra",
                        "title": "Linear Algebra",
                        "subtopics": [
                            "Scalars, vectors, and matrices",
                            "Vector addition and subtraction",
                            "Dot product and cross product",
                            "Matrix multiplication",
                            "Identity and inverse matrices",
                        ],
                        "objectives": [
                            "Understand vectors and matrices.",
                            "Represent positions and directions mathematically.",
                            "Prepare for coordinate transformations.",
                        ],
                        "notes": (
                            "A vector can represent position, direction, or "
                            "velocity. Matrices can transform vectors between "
                            "coordinate systems. The dot product is useful for "
                            "measuring alignment, while the cross product gives "
                            "a vector perpendicular to two 3D vectors."
                        ),
                        "practice_tasks": [
                            "Add two 3D position vectors.",
                            "Calculate the dot product of two vectors.",
                            "Multiply two 2x2 matrices by hand and with NumPy.",
                        ],
                    },
                    {
                        "id": "robotics-trigonometry",
                        "title": "Trigonometry for Robot Motion",
                        "subtopics": [
                            "Degrees and radians",
                            "Sine, cosine, and tangent",
                            "Right-triangle calculations",
                            "2D coordinate geometry",
                            "Angles and rotation",
                        ],
                        "objectives": [
                            "Convert degrees to radians.",
                            "Calculate positions using angles and lengths.",
                            "Understand the geometry of robot arms.",
                        ],
                        "notes": (
                            "Robotics frequently uses radians in software. "
                            "For a link of length L at angle theta, its planar "
                            "coordinates relative to the joint are x = L cos(theta) "
                            "and y = L sin(theta). Coordinate conventions and "
                            "angle reference directions must be kept consistent."
                        ),
                        "practice_tasks": [
                            "Convert 90 degrees into radians.",
                            "Calculate a 100 mm link's endpoint at 30 degrees.",
                            "Plot a point calculated from an angle and length.",
                        ],
                    },
                    {
                        "id": "robotics-calculus",
                        "title": "Calculus and Motion",
                        "subtopics": [
                            "Functions and graphs",
                            "Limits and derivatives",
                            "Position, velocity, and acceleration",
                            "Basic integration",
                            "Numerical approximation",
                        ],
                        "objectives": [
                            "Understand how position changes over time.",
                            "Relate velocity and acceleration to motion.",
                            "Recognize the role of calculus in control.",
                        ],
                        "notes": (
                            "Velocity describes the rate of change of position, "
                            "and acceleration describes the rate of change of "
                            "velocity. Derivatives express these relationships "
                            "mathematically. Integration can be used to estimate "
                            "position from velocity, although measurement errors "
                            "can accumulate."
                        ),
                        "practice_tasks": [
                            "Calculate average velocity from two positions and times.",
                            "Plot position against time.",
                            "Explain how constant acceleration changes velocity.",
                        ],
                    },
                ],
            },
            {
                "id": "robotics-kinematics",
                "title": "Module 3: Robot Kinematics",
                "level": "Intermediate",
                "estimated_hours": 35,
                "topics": [
                    {
                        "id": "robotics-coordinate-frames",
                        "title": "Coordinate Frames and Transformations",
                        "subtopics": [
                            "World and robot coordinate frames",
                            "Joint and end-effector frames",
                            "Homogeneous transformation matrices",
                            "Rotation matrices",
                            "Translation and rotation composition",
                        ],
                        "objectives": [
                            "Identify coordinate frames in a robot arm.",
                            "Represent position and orientation.",
                            "Understand transformations between frames.",
                        ],
                        "notes": (
                            "A coordinate frame defines an origin and axes. "
                            "Robots use multiple frames, such as the world, base, "
                            "joint, and tool frames. A homogeneous transformation "
                            "matrix combines rotation and translation in a 4x4 "
                            "matrix. The order of matrix multiplication matters."
                        ),
                        "practice_tasks": [
                            "Draw the base and end-effector frames of a robot arm.",
                            "Write a 4x4 transformation matrix for a translation.",
                            "Explain why transformation order matters.",
                        ],
                    },
                    {
                        "id": "robotics-forward-kinematics",
                        "title": "Forward Kinematics",
                        "subtopics": [
                            "Joint variables and link lengths",
                            "Serial manipulator geometry",
                            "Transformation matrices",
                            "Combining transformations",
                            "Calculating end-effector position",
                        ],
                        "objectives": [
                            "Calculate an end-effector pose from joint values.",
                            "Understand the relationship between joints and position.",
                            "Implement a basic forward-kinematics calculation.",
                        ],
                        "notes": (
                            "Forward kinematics calculates the position and "
                            "orientation of a robot's end-effector from known "
                            "joint values and robot geometry. For a planar two-link "
                            "arm, x = L1 cos(q1) + L2 cos(q1 + q2), and "
                            "y = L1 sin(q1) + L2 sin(q1 + q2)."
                        ),
                        "practice_tasks": [
                            "Calculate the endpoint of a two-link planar arm.",
                            "Change joint angles and compare the endpoint positions.",
                            "Implement the planar equations in Python.",
                        ],
                    },
                    {
                        "id": "robotics-inverse-kinematics",
                        "title": "Inverse Kinematics",
                        "subtopics": [
                            "Target position and pose",
                            "Geometric inverse kinematics",
                            "Multiple possible solutions",
                            "Reachability and singular configurations",
                            "Numerical inverse kinematics",
                        ],
                        "objectives": [
                            "Understand how target positions determine joint angles.",
                            "Identify reachable and unreachable targets.",
                            "Compare geometric and numerical approaches.",
                        ],
                        "notes": (
                            "Inverse kinematics determines joint values that "
                            "place an end-effector at a desired target. A target "
                            "may have multiple solutions or no solution. Reachability "
                            "depends on link lengths and joint limits. Numerical "
                            "methods may be used for more complex manipulators."
                        ),
                        "practice_tasks": [
                            "Draw reachable and unreachable targets for a two-link arm.",
                            "Solve a simple planar two-link example.",
                            "Explain why one target may have two configurations.",
                        ],
                    },
                    {
                        "id": "robotics-dh",
                        "title": "Denavit–Hartenberg Parameters",
                        "subtopics": [
                            "Assigning coordinate frames",
                            "Link length a",
                            "Link twist alpha",
                            "Link offset d",
                            "Joint angle theta",
                            "Building the DH transformation matrix",
                        ],
                        "objectives": [
                            "Understand the four DH parameters.",
                            "Build a DH table for a serial manipulator.",
                            "Use DH matrices in forward kinematics.",
                        ],
                        "notes": (
                            "The Denavit–Hartenberg convention describes the "
                            "relative geometry of adjacent joint frames using "
                            "a, alpha, d, and theta. Parameter definitions depend "
                            "on the chosen convention. Once frames are assigned "
                            "consistently, each row produces a transformation "
                            "matrix that can be multiplied to obtain the final pose."
                        ),
                        "practice_tasks": [
                            "Draw frames for a simple two-joint arm.",
                            "Create a DH table with clearly stated units.",
                            "Calculate and multiply the corresponding matrices.",
                        ],
                    },
                ],
            },
            {
                "id": "robotics-computer-vision",
                "title": "Module 4: Computer Vision with OpenCV",
                "level": "Intermediate",
                "estimated_hours": 30,
                "topics": [
                    {
                        "id": "opencv-basics",
                        "title": "Image Processing Fundamentals",
                        "subtopics": [
                            "Images, pixels, and colour channels",
                            "Reading and displaying images",
                            "Resizing and cropping",
                            "Grayscale conversion",
                            "Thresholding and image filtering",
                        ],
                        "objectives": [
                            "Load and display images in Python.",
                            "Understand image arrays and colour channels.",
                            "Apply basic image-processing operations.",
                        ],
                        "notes": (
                            "An image is represented as a grid of pixels. "
                            "Colour images commonly use multiple channels, while "
                            "grayscale images represent intensity. OpenCV provides "
                            "functions to load, resize, convert, filter, and "
                            "threshold images. OpenCV commonly uses BGR ordering "
                            "for colour images read through its standard image API."
                        ),
                        "practice_tasks": [
                            "Load an image using cv2.imread().",
                            "Convert an image to grayscale.",
                            "Resize an image and apply a threshold.",
                        ],
                    },
                    {
                        "id": "opencv-detection",
                        "title": "Object and Feature Detection",
                        "subtopics": [
                            "Image contours",
                            "Colour-based segmentation",
                            "Edge detection",
                            "Feature detection basics",
                            "Object detection concepts",
                        ],
                        "objectives": [
                            "Extract useful visual information.",
                            "Detect simple objects using image processing.",
                            "Understand the difference between classical and learned detection.",
                        ],
                        "notes": (
                            "Classical computer vision methods use image properties "
                            "such as colour, edges, and contours. These methods can "
                            "work well in controlled environments. Learned object "
                            "detectors use training data to identify object classes "
                            "and locations, but their performance depends on the "
                            "model, data, and operating conditions."
                        ),
                        "practice_tasks": [
                            "Detect a coloured object using an HSV mask.",
                            "Find contours in a thresholded image.",
                            "Test detection under different lighting conditions.",
                        ],
                    },
                ],
            },
            {
                "id": "robotics-ros2",
                "title": "Module 5: ROS 2 and Simulation",
                "level": "Intermediate to Advanced",
                "estimated_hours": 40,
                "topics": [
                    {
                        "id": "ros2-fundamentals",
                        "title": "ROS 2 Fundamentals",
                        "subtopics": [
                            "Nodes and packages",
                            "Topics and messages",
                            "Publishers and subscribers",
                            "Services and actions",
                            "Parameters and launch files",
                        ],
                        "objectives": [
                            "Understand ROS 2 communication concepts.",
                            "Create and run a basic ROS 2 node.",
                            "Inspect topics and nodes from the terminal.",
                        ],
                        "notes": (
                            "ROS 2 is a robotics middleware framework. Nodes "
                            "are separate programs, topics carry streamed messages, "
                            "services support request-response interactions, and "
                            "actions support longer-running tasks with feedback. "
                            "Packages organize code and resources. Commands and "
                            "APIs can vary slightly between ROS 2 distributions."
                        ),
                        "practice_tasks": [
                            "Create a Python ROS 2 package.",
                            "Write a publisher and subscriber.",
                            "Inspect running nodes with ros2 node list.",
                        ],
                    },
                    {
                        "id": "ros2-robot-description",
                        "title": "URDF and Robot Models",
                        "subtopics": [
                            "Links and joints",
                            "URDF structure",
                            "Fixed, revolute, and prismatic joints",
                            "Visual and collision geometry",
                            "Robot state publishing",
                        ],
                        "objectives": [
                            "Describe a robot using URDF.",
                            "Understand links, joints, and joint limits.",
                            "Visualize a robot model in a compatible ROS 2 setup.",
                        ],
                        "notes": (
                            "URDF describes a robot as links connected by joints. "
                            "Links can define visual and collision geometry, while "
                            "joints specify motion and relationships between links. "
                            "Accurate origins, axes, and joint limits are important "
                            "for simulation and robot visualization."
                        ),
                        "practice_tasks": [
                            "Create a URDF for a simple two-link robot.",
                            "Define one revolute joint and its limits.",
                            "Check the model in a compatible visualization tool.",
                        ],
                    },
                    {
                        "id": "robotics-gazebo",
                        "title": "Robot Simulation with Gazebo",
                        "subtopics": [
                            "Worlds and physics",
                            "Models and simulation entities",
                            "Robot spawning",
                            "Simulated sensors",
                            "Connecting simulation to ROS 2",
                        ],
                        "objectives": [
                            "Understand the role of physics simulation.",
                            "Load a robot model into a simulated world.",
                            "Recognize how simulated sensors support testing.",
                        ],
                        "notes": (
                            "Gazebo simulates robot motion, physics, environments, "
                            "and sensors. A simulation can help test navigation "
                            "and control before using physical hardware. Integration "
                            "details depend on the Gazebo version, ROS 2 distribution, "
                            "and installed bridge or simulation packages."
                        ),
                        "practice_tasks": [
                            "Launch a simple simulation world.",
                            "Spawn a robot model.",
                            "Inspect a simulated sensor topic.",
                        ],
                    },
                ],
            },
        ],
    },

    "software": {
        "career": "Software Developer",
        "description": (
            "Learn programming fundamentals, data structures, algorithms, "
            "software design, Git, testing, and backend development."
        ),
        "level": "Beginner to Advanced",
        "modules": [
            {
                "id": "software-programming",
                "title": "Module 1: Programming Foundations",
                "level": "Beginner",
                "estimated_hours": 30,
                "topics": [
                    {
                        "id": "software-fundamentals",
                        "title": "Programming Fundamentals",
                        "subtopics": [
                            "Variables and data types",
                            "Operators and expressions",
                            "Conditions and loops",
                            "Functions",
                            "Input, output, and error handling",
                        ],
                        "objectives": [
                            "Write small programs to solve problems.",
                            "Use conditions and loops correctly.",
                            "Break programs into reusable functions.",
                        ],
                        "notes": (
                            "Programming expresses a solution as instructions "
                            "that a computer can execute. Variables hold data, "
                            "conditions select execution paths, loops repeat work, "
                            "and functions organize reusable operations. Clear "
                            "names and small functions improve readability."
                        ),
                        "practice_tasks": [
                            "Build a calculator.",
                            "Write a number-guessing game.",
                            "Create a program that validates user input.",
                        ],
                    },
                    {
                        "id": "software-oop",
                        "title": "Object-Oriented Programming",
                        "subtopics": [
                            "Classes and objects",
                            "Constructors",
                            "Encapsulation",
                            "Inheritance",
                            "Polymorphism and composition",
                        ],
                        "objectives": [
                            "Model a problem using classes and objects.",
                            "Understand the major OOP concepts.",
                            "Design reusable components.",
                        ],
                        "notes": (
                            "Object-oriented programming groups data and related "
                            "behaviour into objects. Encapsulation controls how "
                            "state is accessed, inheritance reuses or specializes "
                            "behaviour, and polymorphism allows different objects "
                            "to be used through a common interface. Composition "
                            "is often a flexible alternative to deep inheritance."
                        ),
                        "practice_tasks": [
                            "Create a Student class.",
                            "Build a small library-management model.",
                            "Compare inheritance and composition in an example.",
                        ],
                    },
                ],
            },
            {
                "id": "software-dsa",
                "title": "Module 2: Data Structures and Algorithms",
                "level": "Beginner to Intermediate",
                "estimated_hours": 45,
                "topics": [
                    {
                        "id": "software-complexity",
                        "title": "Algorithm Analysis and Big-O",
                        "subtopics": [
                            "Input size",
                            "Time complexity",
                            "Space complexity",
                            "Big-O, Big-Theta, and Big-Omega",
                            "Best, average, and worst cases",
                        ],
                        "objectives": [
                            "Estimate algorithm efficiency.",
                            "Compare common growth rates.",
                            "Explain complexity using input size.",
                        ],
                        "notes": (
                            "Algorithm analysis studies how resource use grows "
                            "with input size. Big-O describes an asymptotic upper "
                            "bound, Big-Omega a lower bound, and Big-Theta a tight "
                            "bound. Common growth rates include constant, logarithmic, "
                            "linear, linearithmic, quadratic, and exponential."
                        ),
                        "practice_tasks": [
                            "Find the complexity of a single loop.",
                            "Analyse a nested loop.",
                            "Compare linear search and binary search.",
                        ],
                    },
                    {
                        "id": "software-data-structures",
                        "title": "Core Data Structures",
                        "subtopics": [
                            "Arrays and strings",
                            "Linked lists",
                            "Stacks and queues",
                            "Hash tables",
                            "Trees and binary search trees",
                            "Graphs and heaps",
                        ],
                        "objectives": [
                            "Choose an appropriate data structure.",
                            "Understand common operations and their costs.",
                            "Implement basic data structures.",
                        ],
                        "notes": (
                            "Data structures organize information for efficient "
                            "access and modification. Arrays provide indexed access, "
                            "stacks use last-in-first-out order, queues use "
                            "first-in-first-out order, and hash tables support "
                            "efficient average-case key lookup. Trees and graphs "
                            "represent hierarchical and network relationships."
                        ),
                        "practice_tasks": [
                            "Implement a stack using a Python list.",
                            "Implement a queue.",
                            "Count word frequencies using a dictionary.",
                        ],
                    },
                    {
                        "id": "software-algorithms",
                        "title": "Searching and Sorting",
                        "subtopics": [
                            "Linear search",
                            "Binary search",
                            "Bubble and insertion sort",
                            "Merge sort",
                            "Quick sort",
                            "Sorting stability and trade-offs",
                        ],
                        "objectives": [
                            "Implement fundamental algorithms.",
                            "Compare algorithm complexity.",
                            "Recognize when binary search is applicable.",
                        ],
                        "notes": (
                            "Linear search checks items one by one. Binary search "
                            "repeatedly halves the search range and requires sorted "
                            "data. Merge sort has O(n log n) time complexity, while "
                            "quick sort typically has O(n log n) average time but "
                            "can degrade to O(n²) with poor pivot behaviour."
                        ),
                        "practice_tasks": [
                            "Implement linear search.",
                            "Implement binary search on sorted data.",
                            "Compare insertion sort and merge sort.",
                        ],
                    },
                ],
            },
            {
                "id": "software-tools",
                "title": "Module 3: Professional Development Tools",
                "level": "Beginner to Intermediate",
                "estimated_hours": 20,
                "topics": [
                    {
                        "id": "software-git",
                        "title": "Git and GitHub",
                        "subtopics": [
                            "Repositories and commits",
                            "git status, add, and commit",
                            "Branches and merging",
                            "Remote repositories and push",
                            "Pull requests and code reviews",
                        ],
                        "objectives": [
                            "Track code changes.",
                            "Use branches for isolated development.",
                            "Publish projects in a remote repository.",
                        ],
                        "notes": (
                            "Git records a project's change history. A commit "
                            "stores a snapshot, a branch provides an independent "
                            "line of development, and a remote repository allows "
                            "collaboration. Review changes before committing and "
                            "never commit passwords or secret API keys."
                        ),
                        "practice_tasks": [
                            "Create a Git repository for a small project.",
                            "Make three meaningful commits.",
                            "Create a branch and merge a change.",
                        ],
                    },
                    {
                        "id": "software-testing",
                        "title": "Debugging and Software Testing",
                        "subtopics": [
                            "Reading error messages",
                            "Breakpoints and debugging",
                            "Unit testing",
                            "Integration testing",
                            "Assertions and edge cases",
                        ],
                        "objectives": [
                            "Find and fix common bugs.",
                            "Write tests for expected behaviour.",
                            "Check edge cases and invalid inputs.",
                        ],
                        "notes": (
                            "Testing checks whether software behaves as expected. "
                            "Unit tests focus on small components, while integration "
                            "tests check how components work together. Debugging "
                            "uses evidence, logs, breakpoints, and repeatable test "
                            "cases to locate faults."
                        ),
                        "practice_tasks": [
                            "Write tests for a calculator function.",
                            "Test empty input and invalid values.",
                            "Debug a deliberately introduced error.",
                        ],
                    },
                ],
            },
        ],
    },

    "web": {
        "career": "Web Developer",
        "description": (
            "Learn HTML, CSS, JavaScript, responsive design, APIs, "
            "backend development, databases, and deployment."
        ),
        "level": "Beginner to Advanced",
        "modules": [
            {
                "id": "web-html",
                "title": "Module 1: HTML and Web Foundations",
                "level": "Beginner",
                "estimated_hours": 15,
                "topics": [
                    {
                        "id": "web-html-basics",
                        "title": "HTML Structure and Semantics",
                        "subtopics": [
                            "HTML document structure",
                            "Headings and paragraphs",
                            "Links and images",
                            "Lists and tables",
                            "Forms and input elements",
                            "Semantic elements",
                        ],
                        "objectives": [
                            "Create a valid HTML page.",
                            "Structure content meaningfully.",
                            "Build basic user-input forms.",
                        ],
                        "notes": (
                            "HTML describes the structure and meaning of web "
                            "content. Semantic elements such as header, nav, main, "
                            "section, article, and footer help organize a page. "
                            "Forms collect user input, but client-side validation "
                            "does not replace server-side validation."
                        ),
                        "practice_tasks": [
                            "Create a personal profile page.",
                            "Build a contact form.",
                            "Use semantic elements to structure a landing page.",
                        ],
                    },
                ],
            },
            {
                "id": "web-css",
                "title": "Module 2: CSS and Responsive Design",
                "level": "Beginner to Intermediate",
                "estimated_hours": 25,
                "topics": [
                    {
                        "id": "web-css-basics",
                        "title": "CSS Fundamentals",
                        "subtopics": [
                            "Selectors and specificity",
                            "Colours, fonts, and typography",
                            "Box model",
                            "Margin, padding, and borders",
                            "Pseudo-classes and transitions",
                        ],
                        "objectives": [
                            "Style web pages consistently.",
                            "Understand layout spacing.",
                            "Build reusable visual styles.",
                        ],
                        "notes": (
                            "CSS controls the presentation of HTML. The box model "
                            "includes content, padding, border, and margin. "
                            "Specificity and the cascade determine which rule "
                            "applies when multiple rules target an element. "
                            "Reusable classes help maintain consistent styling."
                        ),
                        "practice_tasks": [
                            "Create a styled profile card.",
                            "Design a navigation bar.",
                            "Build a consistent colour and typography system.",
                        ],
                    },
                    {
                        "id": "web-responsive",
                        "title": "Flexbox, Grid, and Responsive Layouts",
                        "subtopics": [
                            "Flexbox alignment",
                            "CSS Grid",
                            "Media queries",
                            "Relative units",
                            "Mobile-first design",
                            "Accessible responsive navigation",
                        ],
                        "objectives": [
                            "Build layouts that adapt to screen sizes.",
                            "Choose between Flexbox and Grid.",
                            "Improve mobile usability.",
                        ],
                        "notes": (
                            "Flexbox is useful for arranging items along one "
                            "primary axis, while CSS Grid supports two-dimensional "
                            "layouts. Media queries apply styles at selected "
                            "conditions. Responsive design should preserve readable "
                            "text, usable controls, and accessible navigation."
                        ),
                        "practice_tasks": [
                            "Make a three-column card layout responsive.",
                            "Create a Flexbox navigation bar.",
                            "Build a Grid-based dashboard.",
                        ],
                    },
                ],
            },
            {
                "id": "web-javascript",
                "title": "Module 3: JavaScript",
                "level": "Beginner to Intermediate",
                "estimated_hours": 35,
                "topics": [
                    {
                        "id": "web-js-fundamentals",
                        "title": "JavaScript Fundamentals",
                        "subtopics": [
                            "let, const, and data types",
                            "Functions and arrow functions",
                            "Arrays and objects",
                            "Conditions and loops",
                            "Scope and closures",
                            "Modules and error handling",
                        ],
                        "objectives": [
                            "Write interactive browser logic.",
                            "Manipulate arrays and objects.",
                            "Organize JavaScript code into functions.",
                        ],
                        "notes": (
                            "JavaScript adds behaviour to web pages. Use const "
                            "for bindings that will not be reassigned and let "
                            "when reassignment is needed. Arrays store ordered "
                            "values, and objects store named properties. Functions "
                            "make logic reusable and easier to test."
                        ),
                        "practice_tasks": [
                            "Create a form validator.",
                            "Filter a list of products.",
                            "Build a simple interactive counter.",
                        ],
                    },
                    {
                        "id": "web-dom",
                        "title": "DOM and Browser Events",
                        "subtopics": [
                            "Selecting DOM elements",
                            "Changing text and attributes",
                            "Event listeners",
                            "Form submission",
                            "Creating and removing elements",
                        ],
                        "objectives": [
                            "Update page content dynamically.",
                            "Handle user interactions.",
                            "Respond to form submissions safely.",
                        ],
                        "notes": (
                            "The Document Object Model represents the page as "
                            "objects. JavaScript can select elements, update their "
                            "properties, and listen for events. Avoid inserting "
                            "untrusted input with innerHTML; use textContent or "
                            "properly sanitize content when appropriate."
                        ),
                        "practice_tasks": [
                            "Build a to-do list.",
                            "Show form validation messages.",
                            "Add filtering to a list of cards.",
                        ],
                    },
                    {
                        "id": "web-api",
                        "title": "HTTP and REST APIs",
                        "subtopics": [
                            "Client-server architecture",
                            "HTTP methods",
                            "Status codes",
                            "JSON",
                            "fetch and asynchronous JavaScript",
                            "Handling loading and error states",
                        ],
                        "objectives": [
                            "Understand how a frontend communicates with a backend.",
                            "Make HTTP requests from JavaScript.",
                            "Handle API responses and failures.",
                        ],
                        "notes": (
                            "A frontend can request data from a backend over HTTP. "
                            "REST-style APIs commonly use GET to read resources, "
                            "POST to create or submit data, PUT or PATCH to update, "
                            "and DELETE to remove. JSON is a common data format. "
                            "A successful network request does not always mean "
                            "the application operation succeeded, so check status "
                            "codes and handle errors."
                        ),
                        "practice_tasks": [
                            "Fetch data from a public API.",
                            "Display a loading indicator while waiting.",
                            "Show a useful message when a request fails.",
                        ],
                    },
                ],
            },
            {
                "id": "web-backend",
                "title": "Module 4: Backend and Databases",
                "level": "Intermediate",
                "estimated_hours": 35,
                "topics": [
                    {
                        "id": "web-backend-basics",
                        "title": "Backend Development with FastAPI",
                        "subtopics": [
                            "Routes and HTTP methods",
                            "Path and query parameters",
                            "Request and response models",
                            "Validation and error responses",
                            "Environment variables",
                            "API documentation",
                        ],
                        "objectives": [
                            "Create API endpoints in Python.",
                            "Validate incoming request data.",
                            "Expose and test backend routes.",
                        ],
                        "notes": (
                            "FastAPI is a Python framework for building APIs. "
                            "Routes connect URLs and HTTP methods to Python "
                            "functions. Request models validate incoming data, "
                            "while response models help define output structure. "
                            "Environment variables can keep configuration outside "
                            "source code. Never expose credentials in public code."
                        ),
                        "practice_tasks": [
                            "Create a health-check endpoint.",
                            "Build a CRUD API for tasks.",
                            "Test endpoints through the generated API docs.",
                        ],
                    },
                    {
                        "id": "web-database",
                        "title": "SQL and Database Fundamentals",
                        "subtopics": [
                            "Tables, rows, and columns",
                            "Primary and foreign keys",
                            "SELECT, INSERT, UPDATE, and DELETE",
                            "Filtering, sorting, and joins",
                            "Database relationships",
                            "Normalization and constraints",
                        ],
                        "objectives": [
                            "Design basic relational tables.",
                            "Write SQL queries.",
                            "Understand relationships and data integrity.",
                        ],
                        "notes": (
                            "Relational databases store structured data in tables. "
                            "Primary keys identify rows, and foreign keys link "
                            "related tables. SQL supports querying and modifying "
                            "data. Constraints help maintain valid data, while "
                            "normalization reduces unnecessary duplication."
                        ),
                        "practice_tasks": [
                            "Create a students table.",
                            "Write a query using WHERE and ORDER BY.",
                            "Join two related tables.",
                        ],
                    },
                ],
            },
        ],
    },

    "data": {
        "career": "Data Scientist",
        "description": (
            "Learn Python, data cleaning, statistics, visualization, "
            "machine learning, model evaluation, and responsible data use."
        ),
        "level": "Beginner to Advanced",
        "modules": [
            {
                "id": "data-python",
                "title": "Module 1: Python for Data Science",
                "level": "Beginner",
                "estimated_hours": 25,
                "topics": [
                    {
                        "id": "data-python-basics",
                        "title": "Python for Data Analysis",
                        "subtopics": [
                            "Variables and collections",
                            "Functions and comprehensions",
                            "Reading CSV files",
                            "NumPy arrays",
                            "Pandas Series and DataFrames",
                        ],
                        "objectives": [
                            "Load tabular data.",
                            "Manipulate data with Pandas.",
                            "Perform basic numerical analysis.",
                        ],
                        "notes": (
                            "Pandas provides Series and DataFrame structures for "
                            "working with tabular data. NumPy provides numerical "
                            "arrays and mathematical operations. A typical analysis "
                            "loads data, inspects its shape and types, checks "
                            "missing values, and then transforms or summarizes it."
                        ),
                        "practice_tasks": [
                            "Read a CSV file with Pandas.",
                            "Inspect columns and data types.",
                            "Calculate summary statistics for numeric columns.",
                        ],
                    },
                    {
                        "id": "data-cleaning",
                        "title": "Data Cleaning and Preparation",
                        "subtopics": [
                            "Missing values",
                            "Duplicate records",
                            "Incorrect data types",
                            "Outlier investigation",
                            "String and date cleaning",
                            "Data validation",
                        ],
                        "objectives": [
                            "Identify common data quality issues.",
                            "Prepare data for analysis.",
                            "Document cleaning decisions.",
                        ],
                        "notes": (
                            "Real-world data may contain missing values, duplicates, "
                            "inconsistent formats, and incorrect entries. Cleaning "
                            "should be guided by the meaning of the data. Outliers "
                            "should be investigated rather than automatically "
                            "removed, and transformations should be documented."
                        ),
                        "practice_tasks": [
                            "Remove duplicate records from a sample dataset.",
                            "Handle missing values using justified rules.",
                            "Convert a date column to datetime format.",
                        ],
                    },
                ],
            },
            {
                "id": "data-statistics",
                "title": "Module 2: Statistics and Visualization",
                "level": "Beginner to Intermediate",
                "estimated_hours": 30,
                "topics": [
                    {
                        "id": "data-statistics-basics",
                        "title": "Statistics Fundamentals",
                        "subtopics": [
                            "Mean, median, and mode",
                            "Variance and standard deviation",
                            "Probability basics",
                            "Distributions",
                            "Sampling and bias",
                            "Correlation versus causation",
                        ],
                        "objectives": [
                            "Summarize data distributions.",
                            "Understand variability and probability.",
                            "Avoid common statistical interpretation errors.",
                        ],
                        "notes": (
                            "Descriptive statistics summarize data. The mean can "
                            "be affected by extreme values, while the median is "
                            "often more robust. Standard deviation describes "
                            "spread around the mean. Correlation describes an "
                            "association and does not by itself establish causation."
                        ),
                        "practice_tasks": [
                            "Calculate mean and median for a dataset.",
                            "Compare two distributions.",
                            "Explain why correlation does not prove causation.",
                        ],
                    },
                    {
                        "id": "data-visualization",
                        "title": "Data Visualization",
                        "subtopics": [
                            "Bar and line charts",
                            "Histograms",
                            "Scatter plots",
                            "Matplotlib fundamentals",
                            "Choosing appropriate chart types",
                            "Labelling and interpreting charts",
                        ],
                        "objectives": [
                            "Choose suitable visualizations.",
                            "Create readable plots.",
                            "Communicate data patterns clearly.",
                        ],
                        "notes": (
                            "Visualizations help reveal patterns and communicate "
                            "results. Bar charts compare categories, line charts "
                            "show trends over ordered values, histograms show "
                            "distributions, and scatter plots show relationships "
                            "between numerical variables. Clear labels and honest "
                            "scales are essential."
                        ),
                        "practice_tasks": [
                            "Plot monthly sales as a line chart.",
                            "Create a histogram of numerical values.",
                            "Use a scatter plot to examine two variables.",
                        ],
                    },
                ],
            },
            {
                "id": "data-machine-learning",
                "title": "Module 3: Machine Learning",
                "level": "Intermediate",
                "estimated_hours": 45,
                "topics": [
                    {
                        "id": "data-ml-basics",
                        "title": "Machine Learning Fundamentals",
                        "subtopics": [
                            "Supervised and unsupervised learning",
                            "Features and target variables",
                            "Training, validation, and test sets",
                            "Data leakage",
                            "Model baselines",
                            "Scikit-learn workflows",
                        ],
                        "objectives": [
                            "Understand common ML problem types.",
                            "Prepare data for model training.",
                            "Establish a baseline model.",
                        ],
                        "notes": (
                            "Machine learning uses data to fit a model for a task. "
                            "Supervised learning uses labelled examples, while "
                            "unsupervised learning looks for structure without "
                            "target labels. A test set estimates performance on "
                            "unseen data. Information from the test set must not "
                            "leak into training or model selection."
                        ),
                        "practice_tasks": [
                            "Train a basic classifier using Scikit-learn.",
                            "Split a dataset into training and test sets.",
                            "Compare a model against a simple baseline.",
                        ],
                    },
                    {
                        "id": "data-model-evaluation",
                        "title": "Model Evaluation",
                        "subtopics": [
                            "Classification and regression metrics",
                            "Accuracy and precision",
                            "Recall and F1 score",
                            "Confusion matrices",
                            "Mean absolute and squared error",
                            "Cross-validation",
                        ],
                        "objectives": [
                            "Select metrics appropriate to a task.",
                            "Interpret model errors.",
                            "Compare model performance responsibly.",
                        ],
                        "notes": (
                            "Evaluation metrics measure different aspects of "
                            "performance. Accuracy can be misleading on imbalanced "
                            "classification tasks. Precision measures the fraction "
                            "of predicted positives that are correct, while recall "
                            "measures the fraction of actual positives found. "
                            "Regression tasks use metrics such as MAE and MSE."
                        ),
                        "practice_tasks": [
                            "Calculate precision and recall from a confusion matrix.",
                            "Compare MAE and MSE.",
                            "Evaluate a classifier on a held-out test set.",
                        ],
                    },
                ],
            },
        ],
    },

    "cybersecurity": {
        "career": "Cybersecurity Engineer",
        "description": (
            "Learn networking, Linux, security principles, system hardening, "
            "defensive monitoring, incident response, and secure development."
        ),
        "level": "Beginner to Advanced",
        "modules": [
            {
                "id": "cyber-networking",
                "title": "Module 1: Networking Fundamentals",
                "level": "Beginner",
                "estimated_hours": 25,
                "topics": [
                    {
                        "id": "cyber-network-basics",
                        "title": "Computer Networking Basics",
                        "subtopics": [
                            "IP addresses and subnet masks",
                            "MAC addresses",
                            "DNS and DHCP",
                            "TCP and UDP",
                            "Common ports and services",
                            "HTTP and HTTPS",
                        ],
                        "objectives": [
                            "Understand how devices communicate.",
                            "Recognize common network protocols.",
                            "Read basic network configuration.",
                        ],
                        "notes": (
                            "Networking connects systems and allows them to "
                            "exchange data. IP addresses identify network interfaces "
                            "at the IP layer, DNS maps names to records, and DHCP "
                            "can assign network configuration automatically. TCP "
                            "provides an ordered reliable byte stream, while UDP "
                            "provides datagrams without the same delivery guarantees."
                        ),
                        "practice_tasks": [
                            "Inspect your machine's IP configuration.",
                            "Resolve a domain name using a DNS lookup tool.",
                            "Explain the difference between TCP and UDP.",
                        ],
                    },
                    {
                        "id": "cyber-subnets",
                        "title": "Subnetting and Network Design",
                        "subtopics": [
                            "Binary representation of IP addresses",
                            "CIDR notation",
                            "Network and host portions",
                            "Private and public address ranges",
                            "Default gateways",
                            "Basic routing concepts",
                        ],
                        "objectives": [
                            "Read CIDR notation.",
                            "Understand network boundaries.",
                            "Interpret simple network diagrams.",
                        ],
                        "notes": (
                            "Subnetting divides an IP address space into smaller "
                            "networks. CIDR notation such as /24 indicates how many "
                            "leading bits form the network prefix. The number of "
                            "available host addresses depends on the address family "
                            "and subnet size."
                        ),
                        "practice_tasks": [
                            "Identify the prefix length in a CIDR address.",
                            "Draw a small network with two subnets.",
                            "Explain the role of a default gateway.",
                        ],
                    },
                ],
            },
            {
                "id": "cyber-linux",
                "title": "Module 2: Linux and System Security",
                "level": "Beginner to Intermediate",
                "estimated_hours": 30,
                "topics": [
                    {
                        "id": "cyber-linux-basics",
                        "title": "Linux Command Line",
                        "subtopics": [
                            "Filesystem navigation",
                            "Files and directories",
                            "Permissions and ownership",
                            "Processes and services",
                            "Package management",
                            "Logs and system information",
                        ],
                        "objectives": [
                            "Navigate a Linux terminal.",
                            "Inspect files, processes, and permissions.",
                            "Understand basic system administration.",
                        ],
                        "notes": (
                            "The Linux command line provides tools to inspect "
                            "and manage a system. File permissions control access "
                            "for owners, groups, and others. Processes and services "
                            "can be inspected to understand system activity. Use "
                            "administrative privileges only when necessary."
                        ),
                        "practice_tasks": [
                            "Navigate directories using pwd, ls, and cd.",
                            "Inspect permissions with ls -l.",
                            "Review system logs in a lab environment.",
                        ],
                    },
                    {
                        "id": "cyber-hardening",
                        "title": "System Hardening",
                        "subtopics": [
                            "Updates and patch management",
                            "Least privilege",
                            "Strong authentication",
                            "Firewall concepts",
                            "Service minimization",
                            "Backups and recovery",
                        ],
                        "objectives": [
                            "Recognize common system security controls.",
                            "Reduce unnecessary attack surface.",
                            "Understand the importance of patching and backups.",
                        ],
                        "notes": (
                            "System hardening reduces unnecessary exposure. "
                            "Useful measures include applying security updates, "
                            "disabling unused services, enforcing least privilege, "
                            "using strong authentication, configuring firewalls, "
                            "and testing backups. Controls should be documented "
                            "and verified after changes."
                        ),
                        "practice_tasks": [
                            "Review available system updates.",
                            "List enabled services on a test machine.",
                            "Write a basic hardening checklist for a personal system.",
                        ],
                    },
                ],
            },
            {
                "id": "cyber-defence",
                "title": "Module 3: Defensive Security",
                "level": "Intermediate",
                "estimated_hours": 35,
                "topics": [
                    {
                        "id": "cyber-monitoring",
                        "title": "Logs and Security Monitoring",
                        "subtopics": [
                            "Authentication logs",
                            "System and application logs",
                            "Indicators of suspicious activity",
                            "Time correlation",
                            "Alert triage",
                            "False positives and false negatives",
                        ],
                        "objectives": [
                            "Understand the purpose of security logs.",
                            "Recognize suspicious patterns in sample logs.",
                            "Document investigation findings.",
                        ],
                        "notes": (
                            "Logs record events from operating systems, applications, "
                            "and network services. Defensive monitoring looks for "
                            "patterns that may indicate misuse or compromise. A "
                            "single event rarely proves an incident; analysts "
                            "correlate evidence, validate context, and record "
                            "decisions."
                        ),
                        "practice_tasks": [
                            "Inspect authentication logs on your own test system.",
                            "Create a timeline from a supplied sample log.",
                            "Write a short incident triage report.",
                        ],
                    },
                    {
                        "id": "cyber-incident-response",
                        "title": "Incident Response Fundamentals",
                        "subtopics": [
                            "Preparation",
                            "Identification and analysis",
                            "Containment",
                            "Eradication and recovery",
                            "Evidence preservation",
                            "Lessons learned",
                        ],
                        "objectives": [
                            "Understand the stages of incident response.",
                            "Preserve useful evidence.",
                            "Create a clear incident report.",
                        ],
                        "notes": (
                            "Incident response provides a structured approach "
                            "to handling security events. Teams prepare in advance, "
                            "identify and analyse incidents, contain their impact, "
                            "remove causes, recover systems, and document lessons "
                            "learned. Follow organizational procedures and legal "
                            "requirements when handling evidence."
                        ),
                        "practice_tasks": [
                            "Write a response checklist for a compromised test account.",
                            "Build a timeline from a fictional incident.",
                            "Draft an incident summary with impact and remediation.",
                        ],
                    },
                ],
            },
        ],
    },

    "entrepreneur": {
        "career": "Entrepreneur",
        "description": (
            "Learn problem discovery, customer research, MVP design, "
            "business models, budgeting, marketing, and product validation."
        ),
        "level": "Beginner to Advanced",
        "modules": [
            {
                "id": "entrepreneur-discovery",
                "title": "Module 1: Problem Discovery",
                "level": "Beginner",
                "estimated_hours": 15,
                "topics": [
                    {
                        "id": "entrepreneur-problems",
                        "title": "Finding and Validating Problems",
                        "subtopics": [
                            "Identifying customer pain points",
                            "Defining a target audience",
                            "Customer interviews",
                            "Separating assumptions from evidence",
                            "Competitor research",
                            "Problem statements",
                        ],
                        "objectives": [
                            "Identify a specific customer problem.",
                            "Collect evidence before building a solution.",
                            "Define an initial target audience.",
                        ],
                        "notes": (
                            "A business idea should begin with a problem worth "
                            "solving. Customer interviews can reveal needs, current "
                            "workarounds, and purchasing behaviour. Avoid asking "
                            "leading questions. Distinguish what people actually "
                            "do from what they say they might do."
                        ),
                        "practice_tasks": [
                            "Interview five potential users about one problem.",
                            "Write a one-sentence problem statement.",
                            "List competing products and existing alternatives.",
                        ],
                    },
                    {
                        "id": "entrepreneur-persona",
                        "title": "Customer Personas and Journey Mapping",
                        "subtopics": [
                            "Customer segments",
                            "User goals and frustrations",
                            "Customer journey stages",
                            "Pain points and opportunities",
                            "Value propositions",
                        ],
                        "objectives": [
                            "Describe an initial customer segment.",
                            "Map the customer's current journey.",
                            "Connect product benefits to user needs.",
                        ],
                        "notes": (
                            "A customer persona is a research-informed summary "
                            "of a user segment, not a fictional stereotype. Journey "
                            "mapping records the steps a person takes, their goals, "
                            "frustrations, and opportunities for improvement. A "
                            "value proposition explains why a customer might choose "
                            "your product over alternatives."
                        ),
                        "practice_tasks": [
                            "Create one evidence-based customer persona.",
                            "Map the steps from problem recognition to solution.",
                            "Write a concise value proposition.",
                        ],
                    },
                ],
            },
            {
                "id": "entrepreneur-product",
                "title": "Module 2: Product and MVP",
                "level": "Beginner to Intermediate",
                "estimated_hours": 25,
                "topics": [
                    {
                        "id": "entrepreneur-mvp",
                        "title": "Minimum Viable Product",
                        "subtopics": [
                            "MVP definition",
                            "Core versus optional features",
                            "Prototype and wireframe",
                            "Build-measure-learn cycle",
                            "User feedback",
                            "Defining success metrics",
                        ],
                        "objectives": [
                            "Scope a small testable product.",
                            "Choose the most important initial features.",
                            "Plan a measurable experiment.",
                        ],
                        "notes": (
                            "An MVP is the smallest practical product or experiment "
                            "that tests important assumptions with real users. It "
                            "is not simply a low-quality product. Define the "
                            "hypothesis, audience, success metric, and learning goal "
                            "before investing heavily in development."
                        ),
                        "practice_tasks": [
                            "Write an MVP feature list with priorities.",
                            "Sketch a three-screen wireframe.",
                            "Define one measurable product experiment.",
                        ],
                    },
                    {
                        "id": "entrepreneur-feedback",
                        "title": "Product Testing and Iteration",
                        "subtopics": [
                            "Usability testing",
                            "Feedback collection",
                            "Qualitative and quantitative evidence",
                            "Prioritizing improvements",
                            "Product iteration",
                        ],
                        "objectives": [
                            "Test an early product with users.",
                            "Organize feedback into actionable findings.",
                            "Choose improvements based on evidence.",
                        ],
                        "notes": (
                            "Product testing checks whether people can use a "
                            "solution and whether it addresses the intended problem. "
                            "Observe real behaviour rather than relying only on "
                            "opinions. Prioritize changes by user impact, effort, "
                            "risk, and the evidence supporting the change."
                        ),
                        "practice_tasks": [
                            "Run a usability test with three participants.",
                            "Summarize recurring usability problems.",
                            "Prioritize the top three improvements.",
                        ],
                    },
                ],
            },
            {
                "id": "entrepreneur-business",
                "title": "Module 3: Business and Growth",
                "level": "Intermediate",
                "estimated_hours": 30,
                "topics": [
                    {
                        "id": "entrepreneur-business-model",
                        "title": "Business Models and Revenue",
                        "subtopics": [
                            "Value proposition",
                            "Customer segments",
                            "Revenue streams",
                            "Cost structure",
                            "Channels and partnerships",
                            "Business Model Canvas",
                        ],
                        "objectives": [
                            "Describe how a business creates value.",
                            "Identify possible revenue streams.",
                            "Recognize major costs and assumptions.",
                        ],
                        "notes": (
                            "A business model explains how a company creates, "
                            "delivers, and captures value. It includes customers, "
                            "value propositions, channels, revenue, costs, and "
                            "key activities. A proposed model is a set of "
                            "hypotheses that must be tested with market evidence."
                        ),
                        "practice_tasks": [
                            "Complete a one-page Business Model Canvas.",
                            "List likely fixed and variable costs.",
                            "Compare two possible pricing models.",
                        ],
                    },
                    {
                        "id": "entrepreneur-marketing",
                        "title": "Marketing and Customer Acquisition",
                        "subtopics": [
                            "Brand positioning",
                            "Content marketing",
                            "Search engine basics",
                            "Social media strategy",
                            "Customer acquisition cost",
                            "Conversion and retention",
                        ],
                        "objectives": [
                            "Choose appropriate channels for a target audience.",
                            "Understand basic marketing metrics.",
                            "Plan a small marketing experiment.",
                        ],
                        "notes": (
                            "Marketing helps potential customers discover and "
                            "understand a product. Channel selection should match "
                            "customer behaviour and available resources. Metrics "
                            "such as conversion rate, customer acquisition cost, "
                            "and retention help evaluate whether a channel is "
                            "working, but should be interpreted in context."
                        ),
                        "practice_tasks": [
                            "Draft a one-week content plan.",
                            "Define a conversion event for your product.",
                            "Design a small, measurable acquisition experiment.",
                        ],
                    },
                ],
            },
        ],
    },
}


def add_video_links(curriculum: dict) -> dict:
    """
    Return a copy of the curriculum with YouTube search suggestions.

    These are search-result links, not verified individual video selections.
    """
    result = deepcopy(curriculum)

    for module in result.get("modules", []):
        for topic in module.get("topics", []):
            topic_title = topic.get("title", "")
            career = result.get("career", "")

            topic_query = quote_plus(
                f"{career} {topic_title} tutorial for beginners"
            )
            topic["video_url"] = (
                f"https://www.youtube.com/results?search_query={topic_query}"
            )

            topic["subtopic_videos"] = []

            for subtopic in topic.get("subtopics", []):
                subtopic_query = quote_plus(
                    f"{career} {subtopic} tutorial"
                )
                topic["subtopic_videos"].append(
                    {
                        "title": subtopic,
                        "url": (
                            "https://www.youtube.com/results?search_query="
                            f"{subtopic_query}"
                        ),
                    }
                )

    return result


@router.get("/")
def get_curricula():
    """Return all available career curricula and their module counts."""
    careers = []

    for career_id, curriculum in CURRICULUM.items():
        topic_count = sum(
            len(module.get("topics", []))
            for module in curriculum.get("modules", [])
        )

        careers.append(
            {
                "id": career_id,
                "career": curriculum["career"],
                "description": curriculum["description"],
                "level": curriculum["level"],
                "module_count": len(curriculum.get("modules", [])),
                "topic_count": topic_count,
            }
        )

    return {
        "total_careers": len(careers),
        "careers": careers,
    }


@router.get("/{career_id}")
def get_curriculum(career_id: str):
    """Return a complete curriculum for one career."""
    curriculum = CURRICULUM.get(career_id.lower())

    if curriculum is None:
        raise HTTPException(
            status_code=404,
            detail=(
                f"Curriculum '{career_id}' was not found. "
                f"Available careers: {', '.join(CURRICULUM.keys())}"
            ),
        )

    return add_video_links(curriculum)