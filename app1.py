import streamlit as st
import pandas as pd
import joblib

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CSE Placement Roadmap & Mentorship Portal",
    page_icon="🎓",
    layout="wide"
)

# ============================================================
# LOAD ML MODEL
# ============================================================

@st.cache_resource
def load_model():

    model = joblib.load("placement_model.pkl")
    encoder = joblib.load("label_encoder.pkl")

    return model, encoder


model, encoder = load_model()

# ============================================================
# SESSION STATE
# ============================================================

if "task_status" not in st.session_state:
    st.session_state.task_status = {}

if "mentor_question" not in st.session_state:
    st.session_state.mentor_question = ""

# ============================================================
# TITLE
# ============================================================

st.title("🎓 CSE Placement Roadmap & Mentorship Portal")

st.write(
    "A structured platform to help CSE students prepare for "
    "skills, DSA, projects, internships and placements."
)

st.markdown("---")


# ============================================================
# 1. STUDENT PROFILE
# ============================================================

st.header("👤 Student Profile")

col1, col2, col3 = st.columns(3)

with col1:
    student_name = st.text_input(
        "Student Name",
        placeholder="Enter your name"
    )

with col2:
    academic_year = st.selectbox(
        "Academic Year",
        [
            "First Year",
            "Second Year",
            "Third Year",
            "Final Year"
        ]
    )

with col3:
    student_branch = st.text_input(
        "Branch",
        value="Computer Science & Engineering"
    )

st.markdown("---")


# ============================================================
# YEAR NUMBER
# ============================================================

year_number = {
    "First Year": 1,
    "Second Year": 2,
    "Third Year": 3,
    "Final Year": 4
}[academic_year]


# ============================================================
# 2. YEAR-WISE ROADMAP
# ============================================================

st.header("🛣️ Year-wise Placement Roadmap")

st.subheader(f"📌 {academic_year}")

# ------------------------------------------------------------
# ROADMAP DATA
# ------------------------------------------------------------

roadmaps = {

    1: {
        "Skills": [
            "Programming Fundamentals",
            "C / Python Basics",
            "HTML & CSS",
            "Git & GitHub Basics"
        ],

        "DSA": [
            "Arrays",
            "Strings",
            "Basic Searching",
            "Basic Sorting"
        ],

        "Projects": [
            "Simple Calculator",
            "Personal Portfolio",
            "Basic Student Management System"
        ],

        "Internship": [
            "Understand internship opportunities",
            "Create GitHub profile",
            "Start building technical skills"
        ],

        "Placement": [
            "Understand placement process",
            "Start aptitude preparation",
            "Improve communication skills"
        ]
    },

    2: {
        "Skills": [
            "Object-Oriented Programming",
            "Database & SQL",
            "Web Development",
            "Problem Solving"
        ],

        "DSA": [
            "Linked List",
            "Stack",
            "Queue",
            "Recursion",
            "Hashing"
        ],

        "Projects": [
            "CRUD Web Application",
            "Database Project",
            "Mini Full Stack Project"
        ],

        "Internship": [
            "Prepare internship resume",
            "Build GitHub projects",
            "Apply for beginner internships"
        ],

        "Placement": [
            "Start aptitude practice",
            "Practice coding questions",
            "Improve technical communication"
        ]
    },

    3: {
        "Skills": [
            "Advanced Programming",
            "Data Structures",
            "Database Management",
            "Software Development"
        ],

        "DSA": [
            "Trees",
            "Graphs",
            "Dynamic Programming",
            "Greedy Algorithms"
        ],

        "Projects": [
            "Major Academic Project",
            "Full Stack Application",
            "Machine Learning Project"
        ],

        "Internship": [
            "Apply for technical internships",
            "Complete internship projects",
            "Gain industry experience"
        ],

        "Placement": [
            "Regular aptitude practice",
            "Technical interview preparation",
            "Mock coding tests",
            "Resume preparation"
        ]
    },

    4: {
        "Skills": [
            "Advanced Technical Skills",
            "Interview Preparation",
            "System Design Basics",
            "Industry Knowledge"
        ],

        "DSA": [
            "Advanced DSA",
            "Interview Coding",
            "Competitive Programming",
            "Problem Solving"
        ],

        "Projects": [
            "Final Year Project",
            "Industry-oriented Project",
            "Project Documentation"
        ],

        "Internship": [
            "Apply for internships",
            "Use internship experience in interviews",
            "Build professional network"
        ],

        "Placement": [
            "Company-specific preparation",
            "Technical interviews",
            "HR interviews",
            "Mock interviews",
            "Placement applications"
        ]
    }
}

roadmap = roadmaps[year_number]


# ============================================================
# ROADMAP DISPLAY
# ============================================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("💻 Skills")

    for item in roadmap["Skills"]:
        st.write("•", item)

    st.subheader("🧠 DSA")

    for item in roadmap["DSA"]:
        st.write("•", item)

    st.subheader("🛠️ Projects")

    for item in roadmap["Projects"]:
        st.write("•", item)


with col2:

    st.subheader("💼 Internship")

    for item in roadmap["Internship"]:
        st.write("•", item)

    st.subheader("🎯 Placement")

    for item in roadmap["Placement"]:
        st.write("•", item)


st.markdown("---")


# ============================================================
# 3. RESOURCES & TASKS
# ============================================================

st.header("📚 Resources & Tasks")

st.write(
    f"Resources and tasks for **{academic_year}**"
)

resources = {

    "Programming": [
        "Programming fundamentals",
        "Python / Java programming practice",
        "Basic coding problems"
    ],

    "DSA": [
        "Arrays and Strings practice",
        "Linked List problems",
        "Stack and Queue problems",
        "Trees and Graphs practice"
    ],

    "Projects": [
        "Project documentation",
        "GitHub project development",
        "Mini project implementation"
    ],

    "Aptitude": [
        "Quantitative aptitude",
        "Logical reasoning",
        "Verbal ability"
    ],

    "Communication": [
        "Communication practice",
        "Group discussion preparation",
        "Interview introduction practice"
    ],

    "Placement": [
        "Resume preparation",
        "Technical interview preparation",
        "HR interview preparation",
        "Mock interview practice"
    ]
}


for category, items in resources.items():

    st.subheader(f"📌 {category}")

    for i, item in enumerate(items):

        task_key = f"{academic_year}_{category}_{i}"

        st.checkbox(
            item,
            key=task_key
        )

        st.session_state.task_status[task_key] = st.session_state[task_key]


st.markdown("---")


# ============================================================
# 4. PROGRESS TRACKING
# ============================================================

st.header("📈 My Progress")

total_tasks = 0
completed_tasks = 0

for category, items in resources.items():

    for i, item in enumerate(items):

        task_key = f"{academic_year}_{category}_{i}"

        total_tasks += 1

        if st.session_state.task_status.get(
            task_key,
            False
        ):
            completed_tasks += 1


if total_tasks > 0:

    progress = completed_tasks / total_tasks

else:

    progress = 0


st.progress(progress)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Tasks",
        total_tasks
    )

with col2:
    st.metric(
        "Completed Tasks",
        completed_tasks
    )

with col3:
    st.metric(
        "Progress",
        f"{progress * 100:.1f}%"
    )


if progress == 0:

    st.info(
        "Start completing your tasks to track your placement preparation."
    )

elif progress < 0.5:

    st.warning(
        "You have started your preparation. Keep improving your skills."
    )

elif progress < 1:

    st.success(
        "Good progress! Continue completing the remaining tasks."
    )

else:

    st.success(
        "🎉 All available tasks are completed!"
    )


st.markdown("---")


# ============================================================
# 5. ML PLACEMENT READINESS
# ============================================================

st.header("🤖 Placement Readiness Prediction")

st.write(
    "Enter your current preparation level to predict your placement readiness."
)

col1, col2 = st.columns(2)


with col1:

    coding_score = st.slider(
        "Coding Score",
        0,
        100,
        50
    )

    dsa_score = st.slider(
        "DSA Score",
        0,
        100,
        50
    )

    technical_score = st.slider(
        "Technical Skills",
        0,
        100,
        50
    )

    projects_score = st.slider(
        "Projects Score",
        0,
        100,
        50
    )

    communication_score = st.slider(
        "Communication Score",
        0,
        100,
        50
    )


with col2:

    aptitude_score = st.slider(
        "Aptitude Score",
        0,
        100,
        50
    )

    internship = st.selectbox(
        "Internship Experience",
        [
            "No",
            "Yes"
        ]
    )

    resume_score = st.slider(
        "Resume Score",
        0,
        100,
        50
    )


internship_value = 1 if internship == "Yes" else 0


if st.button(
    "🔮 Predict Placement Readiness",
    use_container_width=True
):

    input_data = pd.DataFrame(
        [[
            year_number,
            coding_score,
            dsa_score,
            technical_score,
            projects_score,
            communication_score,
            aptitude_score,
            internship_value,
            resume_score
        ]],

        columns=[
            "Year",
            "Coding_Score",
            "DSA_Score",
            "Technical_Skills",
            "Projects_Score",
            "Communication_Score",
            "Aptitude_Score",
            "Internship_Experience",
            "Resume_Score"
        ]
    )


    prediction = model.predict(input_data)

    prediction_label = encoder.inverse_transform(
        prediction
    )[0]


    probabilities = model.predict_proba(
        input_data
    )[0]

    confidence = max(probabilities) * 100


    st.markdown("---")

    st.subheader("📊 Prediction Result")


    if prediction_label == "Placement Ready":

        st.success(
            f"🎉 Placement Status: **{prediction_label}**"
        )

    elif prediction_label == "Developing":

        st.warning(
            f"📚 Placement Status: **{prediction_label}**"
        )

    else:

        st.error(
            f"⚠️ Placement Status: **{prediction_label}**"
        )


    st.write(
        f"Prediction Confidence: **{confidence:.2f}%**"
    )


    # --------------------------------------------------------
    # RECOMMENDATIONS
    # --------------------------------------------------------

    st.subheader("💡 Recommended Areas")


    scores = {

        "Coding": coding_score,

        "DSA": dsa_score,

        "Technical Skills": technical_score,

        "Projects": projects_score,

        "Communication": communication_score,

        "Aptitude": aptitude_score,

        "Resume": resume_score

    }


    weak_areas = []

    for area, score in scores.items():

        if score < 60:

            weak_areas.append(area)


    if weak_areas:

        st.write(
            "Focus on the following areas:"
        )

        for area in weak_areas:

            st.write(
                "•",
                area
            )

    else:

        st.success(
            "Your preparation is balanced across the entered areas."
        )


st.markdown("---")


# ============================================================
# 6. MENTOR GUIDANCE
# ============================================================

st.header("👨‍🏫 Mentor Guidance")

st.write(
    "Students can submit their placement-related questions "
    "and receive mentor guidance."
)

col1, col2 = st.columns(2)


with col1:

    guidance_topic = st.selectbox(
        "Guidance Topic",
        [
            "Coding",
            "DSA",
            "Projects",
            "Internship",
            "Resume",
            "Aptitude",
            "Technical Interview",
            "HR Interview"
        ]
    )


with col2:

    student_question = st.text_input(
        "Student Question",
        placeholder="Enter your question..."
    )


if st.button(
    "📩 Submit Question",
    use_container_width=True
):

    if student_question.strip():

        st.session_state.mentor_question = student_question

        st.success(
            "Question submitted successfully to the mentor."
        )

    else:

        st.warning(
            "Please enter your question first."
        )


# ------------------------------------------------------------
# MENTOR RESPONSE
# ------------------------------------------------------------

if st.session_state.mentor_question:

    st.markdown("---")

    st.subheader("👨‍🏫 Mentor Response")

    st.info(
        f"Student Question: "
        f"{st.session_state.mentor_question}"
    )

    mentor_response = st.text_area(
        "Enter Mentor Guidance",
        placeholder="Write guidance for the student..."
    )

    if st.button(
        "📤 Send Mentor Guidance",
        use_container_width=True
    ):

        if mentor_response.strip():

            st.success(
                "Mentor guidance submitted successfully."
            )

            st.write(
                "**Guidance:**",
                mentor_response
            )

        else:

            st.warning(
                "Please enter mentor guidance."
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "CSE Placement Roadmap & Mentorship Portal | "
    "Python • Machine Learning • Streamlit"
)