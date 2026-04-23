import streamlit as st
import random

# ─────────────────────────────────────────────
#  QUESTION BANK  (10 per lesson)
# ─────────────────────────────────────────────
LESSONS = {
    "Lesson 1 – Programming Languages": [
        {
            "q": "What is a programming language?",
            "choices": [
                "A set of rules for communicating an algorithm to a computer",
                "A type of hardware component",
                "A storage device for programs",
                "An operating system interface"
            ],
            "a": 0
        },
        {
            "q": "What are the grammatical rules of a programming language called?",
            "choices": ["Semantics", "Syntax", "Algorithms", "Paradigms"],
            "a": 1
        },
        {
            "q": "Which generation of programming language uses machine code?",
            "choices": ["Second Generation", "Third Generation", "First Generation", "Fourth Generation"],
            "a": 2
        },
        {
            "q": "Assembly language belongs to which generation?",
            "choices": ["First Generation", "Second Generation", "Third Generation", "Fourth Generation"],
            "a": 1
        },
        {
            "q": "A compiler translates source code into:",
            "choices": ["Assembly language", "Pseudocode", "Object (machine) code", "HTML"],
            "a": 2
        },
        {
            "q": "An interpreter reads and executes source code:",
            "choices": [
                "All at once after full translation",
                "One instruction or line at a time",
                "Only after compilation",
                "Using a separate virtual machine"
            ],
            "a": 1
        },
        {
            "q": "Java and C++ are examples of which programming paradigm?",
            "choices": [
                "Functional programming",
                "Logic programming",
                "Object-Oriented programming",
                "Procedural programming"
            ],
            "a": 2
        },
        {
            "q": "Which language was developed at Bell Laboratories in the early 1970s?",
            "choices": ["COBOL", "BASIC", "C", "Java"],
            "a": 2
        },
        {
            "q": "Python is classified as a:",
            "choices": ["Command language", "Markup language", "Scripting language", "Machine language"],
            "a": 2
        },
        {
            "q": "A computer program is best described as:",
            "choices": [
                "A type of computer hardware",
                "A set of instructions following the rules of a chosen language",
                "A graphical user interface",
                "A database management system"
            ],
            "a": 1
        },
    ],

    "Lesson 1 – Block Structure": [
        {
            "q": "What is a block in programming?",
            "choices": [
                "A hardware component",
                "A section of code that executes together, defining variable scope and execution flow",
                "A type of comment",
                "A loop counter variable"
            ],
            "a": 1
        },
        {
            "q": "Block structure was introduced in which programming language in the 1960s?",
            "choices": ["COBOL", "FORTRAN", "ALGOL", "C"],
            "a": 2
        },
        {
            "q": "In Python, blocks are defined using:",
            "choices": ["Curly braces { }", "begin/end keywords", "Indentation", "Square brackets [ ]"],
            "a": 2
        },
        {
            "q": "Scope determines:",
            "choices": [
                "How fast a program runs",
                "Where a variable can be accessed in a program",
                "The number of functions in a program",
                "The size of the executable file"
            ],
            "a": 1
        },
        {
            "q": "A variable declared inside a function has:",
            "choices": ["Global scope", "Static scope", "Local scope", "Dynamic scope"],
            "a": 2
        },
        {
            "q": "What is the key difference between a Procedure and a Function?",
            "choices": [
                "Procedures are faster than functions",
                "Functions return values; procedures do not",
                "Procedures can be recursive; functions cannot",
                "Functions require more parameters"
            ],
            "a": 1
        },
        {
            "q": "In 'Pass by Value', what is passed to the function?",
            "choices": [
                "A memory address of the variable",
                "A reference to the original variable",
                "A copy of the argument",
                "A pointer to the stack"
            ],
            "a": 2
        },
        {
            "q": "Stack memory is used to store:",
            "choices": [
                "Dynamically allocated memory",
                "Local variables and function calls",
                "Global variables only",
                "Database records"
            ],
            "a": 1
        },
        {
            "q": "A recursive function is one that:",
            "choices": [
                "Never terminates",
                "Calls itself during its execution",
                "Only works with global variables",
                "Avoids using loops"
            ],
            "a": 1
        },
        {
            "q": "Which of the following is a best practice in block structuring?",
            "choices": [
                "Write very long functions to reduce file count",
                "Avoid comments to keep code short",
                "Keep functions small and focused with consistent indentation",
                "Use global variables as much as possible"
            ],
            "a": 2
        },
    ],

    "Lesson 2 – Rationale for Studying PL": [
        {
            "q": "Which is the most important language evaluation criterion?",
            "choices": ["Cost", "Writability", "Readability", "Portability"],
            "a": 2
        },
        {
            "q": "Orthogonality in a programming language means:",
            "choices": [
                "The language is object-oriented",
                "A small number of constructs can be combined in many ways with context-independent meaning",
                "The language compiles very fast",
                "The language uses indentation for blocks"
            ],
            "a": 1
        },
        {
            "q": "Writability in a programming language refers to:",
            "choices": [
                "How easy it is to type programs",
                "How well a language supports writing programs for a given domain",
                "The quality of the compiler's output",
                "The speed of program execution"
            ],
            "a": 1
        },
        {
            "q": "Which implementation method translates the entire high-level program to machine code before execution?",
            "choices": ["Pure Interpretation", "Hybrid", "Compilation", "Tokenization"],
            "a": 2
        },
        {
            "q": "Pure interpretation is characterized by:",
            "choices": [
                "Fast execution and slow translation",
                "No translation but slow execution",
                "Medium execution speed",
                "Requires a compiler"
            ],
            "a": 1
        },
        {
            "q": "Reliability in a programming language includes:",
            "choices": [
                "Fast compilation speed",
                "Low cost of development",
                "Type checking, exception handling, and consistent behavior under all conditions",
                "Support for object-oriented programming only"
            ],
            "a": 2
        },
        {
            "q": "Which of the following is NOT a programming domain listed in the lesson?",
            "choices": ["Scientific applications", "Business applications", "Gaming applications", "Artificial intelligence"],
            "a": 2
        },
        {
            "q": "Studying programming language concepts helps programmers to:",
            "choices": [
                "Only learn one language deeply",
                "Increase capacity to express ideas and improve ability to learn new languages",
                "Avoid using high-level languages",
                "Write only machine code"
            ],
            "a": 1
        },
        {
            "q": "A hybrid implementation system offers:",
            "choices": [
                "Fastest execution with no translation cost",
                "Small translation cost and medium execution speed",
                "Slowest execution but best portability",
                "Full compilation to native machine code"
            ],
            "a": 1
        },
        {
            "q": "Which skill involves 'using logic and analysis to identify strengths and weaknesses of different approaches'?",
            "choices": ["Oral Expression", "Critical Thinking", "Written Comprehension", "Mathematics"],
            "a": 1
        },
    ],

    "Lesson 5 – Basic Syntax & Semantics (Python)": [
        {
            "q": "In Python, what does 'syntax' refer to?",
            "choices": [
                "The meaning of the program",
                "The rules for specifying an algorithm in a programming language",
                "The speed of execution",
                "The memory usage of a program"
            ],
            "a": 1
        },
        {
            "q": "Each line of code in a Python program is called a:",
            "choices": ["Function", "Module", "Statement", "Token"],
            "a": 2
        },
        {
            "q": "In Python, the symbol `\\` at the end of a line is used to:",
            "choices": [
                "Start a comment",
                "End the program",
                "Continue a statement onto the next line",
                "Import a module"
            ],
            "a": 2
        },
        {
            "q": "What does the `#` symbol do in Python?",
            "choices": [
                "Starts a string literal",
                "Marks a comment; everything after it on that line is ignored",
                "Defines a function",
                "Imports a library"
            ],
            "a": 1
        },
        {
            "q": "What is a Python module?",
            "choices": [
                "A single variable in a program",
                "A Python file containing elements to help with a certain problem (e.g., math)",
                "A reserved keyword",
                "A type of loop"
            ],
            "a": 1
        },
        {
            "q": "The `input()` built-in function in Python always returns a:",
            "choices": ["Integer", "Float", "String", "Boolean"],
            "a": 2
        },
        {
            "q": "In Python, `=` is called the:",
            "choices": ["Equality operator", "Assignment operator", "Comparison operator", "Logical operator"],
            "a": 1
        },
        {
            "q": "Literals in Python are:",
            "choices": [
                "Reserved keywords",
                "Variable names",
                "Fixed values used directly in a program (e.g., 123, 3.14)",
                "Functions that return values"
            ],
            "a": 2
        },
        {
            "q": "Leading whitespace at the beginning of a Python statement defines its:",
            "choices": ["Comment level", "Indentation", "Module name", "String length"],
            "a": 1
        },
        {
            "q": "What type of error occurs when Python cannot translate malformed code?",
            "choices": ["Runtime Error", "Logic Error", "SyntaxError", "ImportError"],
            "a": 2
        },
    ],
}

# ─────────────────────────────────────────────
#  COLOR PALETTE
# ─────────────────────────────────────────────
BG       = "#1E2761"   # navy
CARD     = "#FFFFFF"
ACC      = "#F96167"   # coral accent
TEXT     = "#1E2761"
SUBTEXT  = "#555555"
BTN_BG   = "#1E2761"
BTN_FG   = "#FFFFFF"
CORRECT  = "#2DCB70"
WRONG    = "#F96167"
GOLD     = "#FFD700"
FONT     = "Segoe UI"

# ─────────────────────────────────────────────
#  INITIALIZE SESSION STATE
# ─────────────────────────────────────────────
def init_session_state():
    if "page" not in st.session_state:
        st.session_state.page = "home"
    if "selected_lesson" not in st.session_state:
        st.session_state.selected_lesson = list(LESSONS.keys())[0]
    if "shuffle" not in st.session_state:
        st.session_state.shuffle = True
    if "questions" not in st.session_state:
        st.session_state.questions = []
    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "selected_answer" not in st.session_state:
        st.session_state.selected_answer = None
    if "answered" not in st.session_state:
        st.session_state.answered = False

# ─────────────────────────────────────────────
#  PAGE: HOME
# ─────────────────────────────────────────────
def show_home():
    st.markdown(f"""
    <div style='text-align: center; padding: 40px;'>
        <h1 style='color: {ACC};'>🎓 CSPC-11 Quiz Game</h1>
        <p style='font-size: 18px; color: {SUBTEXT};'>Welcome to the Quiz!</p>
        <p style='color: {SUBTEXT};'>Select a lesson and test your knowledge.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns([2, 1])
    with col1:
        lesson = st.selectbox(
            "Choose a Lesson:",
            options=list(LESSONS.keys()),
            index=list(LESSONS.keys()).index(st.session_state.selected_lesson),
            key="lesson_select"
        )
        st.session_state.selected_lesson = lesson
    
    shuffle = st.checkbox("Shuffle questions", value=True)
    st.session_state.shuffle = shuffle
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("▶ Start Quiz", use_container_width=True, type="primary"):
            st.session_state.page = "quiz"
            st.session_state.questions = list(LESSONS[st.session_state.selected_lesson])
            if st.session_state.shuffle:
                random.shuffle(st.session_state.questions)
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.rerun()
    
    st.markdown(f"""
    <div style='text-align: center; color: {SUBTEXT}; margin-top: 40px;'>
        <p>10 questions per lesson  •  Instant feedback  •  Final score</p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  PAGE: QUIZ
# ─────────────────────────────────────────────
def show_question():
    total = len(st.session_state.questions)
    q_data = st.session_state.questions[st.session_state.q_index]
    
    # Progress bar
    progress_pct = (st.session_state.q_index / total)
    st.progress(progress_pct)
    
    # Header info
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.markdown(f"**Q {st.session_state.q_index + 1}/{total}**")
    with col3:
        st.markdown(f"**Score: {st.session_state.score}/{st.session_state.q_index}**")
    
    st.markdown(f"<p style='color: {SUBTEXT};'>{st.session_state.selected_lesson}</p>", unsafe_allow_html=True)
    st.divider()
    
    # Question
    st.markdown(f"<h3 style='color: {TEXT};'>{q_data['q']}</h3>", unsafe_allow_html=True)
    st.divider()
    
    # Choices
    labels = ["A", "B", "C", "D"]
    correct_idx = q_data["a"]
    
    for i, (lbl, choice_text) in enumerate(zip(labels, q_data["choices"])):
        if st.session_state.answered:
            # Show correct/wrong feedback
            if i == correct_idx:
                col_color = CORRECT
                emoji = "✅"
            elif i == st.session_state.selected_answer and i != correct_idx:
                col_color = WRONG
                emoji = "❌"
            else:
                col_color = TEXT
                emoji = ""
            
            st.markdown(f"""
            <div style='
                background-color: {("white" if col_color == TEXT else ("lightgreen" if col_color == CORRECT else "lightcoral"))};
                border-left: 4px solid {col_color};
                padding: 15px;
                margin: 10px 0;
                border-radius: 5px;
            '>
                <b>{lbl}. {choice_text}</b> {emoji}
            </div>
            """, unsafe_allow_html=True)
        else:
            if st.button(f"**{lbl}.** {choice_text}", key=f"choice_{i}", use_container_width=True):
                st.session_state.selected_answer = i
                st.session_state.answered = True
                if i == correct_idx:
                    st.session_state.score += 1
                st.rerun()
    
    # Feedback
    if st.session_state.answered:
        st.divider()
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.session_state.selected_answer == correct_idx:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Wrong! Answer: {labels[correct_idx]}")
        
        with col2:
            if st.button("Next ▶", use_container_width=True, key="next_btn"):
                st.session_state.q_index += 1
                if st.session_state.q_index < len(st.session_state.questions):
                    st.session_state.answered = False
                    st.session_state.selected_answer = None
                    st.rerun()
                else:
                    st.session_state.page = "results"
                    st.rerun()

# ─────────────────────────────────────────────
#  PAGE: RESULTS
# ─────────────────────────────────────────────
def show_results():
    total = len(st.session_state.questions)
    score = st.session_state.score
    pct = (score / total) * 100
    
    if pct == 100:
        emoji, msg, col = "🏆", "PERFECT SCORE!", GOLD
    elif pct >= 80:
        emoji, msg, col = "🎉", "Excellent Work!", CORRECT
    elif pct >= 60:
        emoji, msg, col = "👍", "Good Job!", "#5B9BD5"
    else:
        emoji, msg, col = "📚", "Keep Studying!", WRONG
    
    st.markdown(f"""
    <div style='text-align: center; padding: 40px;'>
        <h1>{emoji}</h1>
        <h2 style='color: {col};'>{msg}</h2>
        <h3>You scored <span style='color: {col};'>{score} / {total}</span></h3>
        <h4 style='color: {SUBTEXT};'>{pct:.0f}%</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Progress bar for visual representation
    st.progress(score / total)
    
    st.divider()
    
    st.markdown(f"**Lesson:** {st.session_state.selected_lesson}")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("🔄 Retry", use_container_width=True):
            st.session_state.page = "quiz"
            st.session_state.questions = list(LESSONS[st.session_state.selected_lesson])
            if st.session_state.shuffle:
                random.shuffle(st.session_state.questions)
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.rerun()
    
    with col3:
        if st.button("🏠 Home", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()

# ─────────────────────────────────────────────
#  MAIN APP
# ─────────────────────────────────────────────
def main():
    st.set_page_config(
        page_title="CSPC-11 Quiz Game",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS
    st.markdown(f"""
    <style>
        body {{
            background-color: {BG};
            color: {TEXT};
        }}
        .stButton > button {{
            width: 100%;
            background-color: {BTN_BG};
            color: {BTN_FG};
            border-radius: 5px;
            border: none;
            font-size: 16px;
        }}
    </style>
    """, unsafe_allow_html=True)
    
    init_session_state()
    
    # Header
    st.markdown(f"""
    <div style='background-color: {ACC}; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
        <h1 style='color: white; margin: 0;'>🎓 CSPC-11 Programming Languages Quiz</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Page routing
    if st.session_state.page == "home":
        show_home()
    elif st.session_state.page == "quiz":
        show_question()
    elif st.session_state.page == "results":
        show_results()

if __name__ == "__main__":
    main()
