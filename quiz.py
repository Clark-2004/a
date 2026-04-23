import tkinter as tk
from tkinter import ttk, messagebox
import json
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

    "Lesson 1B – Block Structure": [
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
#  APP
# ─────────────────────────────────────────────
class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSPC-11 Programming Languages Quiz")
        self.geometry("820x620")
        self.resizable(False, False)
        self.configure(bg=BG)

        self.lesson_names   = list(LESSONS.keys())
        self.selected_lesson = tk.StringVar(value=self.lesson_names[0])

        # runtime state
        self.questions   = []
        self.q_index     = 0
        self.score       = 0
        self.answered    = False
        self.choice_var  = tk.IntVar()

        self._build_ui()
        self._show_home()

    # ── UI BUILD ─────────────────────────────
    def _build_ui(self):
        # ── HEADER ──
        hdr = tk.Frame(self, bg=ACC, height=60)
        hdr.pack(fill="x")
        tk.Label(hdr, text="🎓  CSPC-11 Quiz Game", bg=ACC, fg="white",
                 font=(FONT, 18, "bold")).pack(side="left", padx=20, pady=10)

        # ── MAIN CANVAS (card area) ──
        self.main_frame = tk.Frame(self, bg=BG)
        self.main_frame.pack(fill="both", expand=True, padx=30, pady=20)

    def _clear(self):
        for w in self.main_frame.winfo_children():
            w.destroy()

    # ── HOME ─────────────────────────────────
    def _show_home(self):
        self._clear()
        card = tk.Frame(self.main_frame, bg=CARD, bd=0, relief="flat")
        card.place(relx=0.5, rely=0.5, anchor="center", width=620, height=460)

        tk.Label(card, text="Welcome to the Quiz!", bg=CARD, fg=BG,
                 font=(FONT, 22, "bold")).pack(pady=(30, 5))
        tk.Label(card, text="Select a lesson and test your knowledge.",
                 bg=CARD, fg=SUBTEXT, font=(FONT, 12)).pack()

        tk.Frame(card, bg=ACC, height=3).pack(fill="x", padx=40, pady=15)

        tk.Label(card, text="Choose a Lesson:", bg=CARD, fg=TEXT,
                 font=(FONT, 12, "bold")).pack(anchor="w", padx=40)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox", fieldbackground=CARD, background=CARD,
                        foreground=TEXT, font=(FONT, 11))

        combo = ttk.Combobox(card, textvariable=self.selected_lesson,
                             values=self.lesson_names,
                             state="readonly", width=54, font=(FONT, 11))
        combo.pack(padx=40, pady=(5, 25))

        # shuffle option
        self.shuffle_var = tk.BooleanVar(value=True)
        tk.Checkbutton(card, text="Shuffle questions", variable=self.shuffle_var,
                       bg=CARD, fg=TEXT, font=(FONT, 11),
                       activebackground=CARD, selectcolor=CARD).pack()

        tk.Button(card, text="▶  Start Quiz", bg=BTN_BG, fg=BTN_FG,
                  font=(FONT, 13, "bold"), relief="flat", cursor="hand2",
                  padx=30, pady=10, command=self._start_quiz).pack(pady=25)

        tk.Label(card, text="10 questions per lesson  •  Instant feedback  •  Final score",
                 bg=CARD, fg=SUBTEXT, font=(FONT, 9)).pack()

    # ── START QUIZ ───────────────────────────
    def _start_quiz(self):
        lesson = self.selected_lesson.get()
        self.questions = list(LESSONS[lesson])
        if self.shuffle_var.get():
            random.shuffle(self.questions)
        self.q_index = 0
        self.score   = 0
        self._show_question()

    # ── QUESTION SCREEN ──────────────────────
    def _show_question(self):
        self._clear()
        q_data = self.questions[self.q_index]
        total  = len(self.questions)

        # progress bar background
        prog_bg = tk.Frame(self.main_frame, bg="#CADCFC", height=8)
        prog_bg.pack(fill="x", pady=(0, 12))
        pct = (self.q_index / total)
        prog_fill = tk.Frame(prog_bg, bg=ACC, height=8)
        prog_fill.place(relwidth=pct, relheight=1)

        # question card
        card = tk.Frame(self.main_frame, bg=CARD, bd=0)
        card.pack(fill="both", expand=True)

        # top bar
        top = tk.Frame(card, bg=BTN_BG)
        top.pack(fill="x")
        tk.Label(top, text=f"Question {self.q_index+1} / {total}",
                 bg=BTN_BG, fg="white", font=(FONT, 11, "bold"),
                 padx=20, pady=8).pack(side="left")
        lname = self.selected_lesson.get()
        tk.Label(top, text=lname, bg=BTN_BG, fg="#CADCFC",
                 font=(FONT, 10), padx=20).pack(side="right", pady=8)

        # question text
        q_frame = tk.Frame(card, bg=CARD)
        q_frame.pack(fill="x", padx=30, pady=(20, 5))
        tk.Label(q_frame, text=q_data["q"], bg=CARD, fg=TEXT,
                 font=(FONT, 13, "bold"), wraplength=700,
                 justify="left").pack(anchor="w")

        tk.Frame(card, bg="#DDDDDD", height=1).pack(fill="x", padx=30, pady=8)

        # choices
        self.choice_var.set(-1)
        self.answered = False
        self.choice_btns = []

        choices = q_data["choices"]
        labels = ["A", "B", "C", "D"]

        choices_frame = tk.Frame(card, bg=CARD)
        choices_frame.pack(fill="x", padx=25, pady=5)

        for i, (lbl, txt) in enumerate(zip(labels, choices)):
            row = tk.Frame(choices_frame, bg=CARD, cursor="hand2")
            row.pack(fill="x", pady=5)

            indicator = tk.Label(row, text=lbl, bg="#CADCFC", fg=BTN_BG,
                                 font=(FONT, 11, "bold"), width=3, height=2)
            indicator.pack(side="left", padx=(5, 10))

            text_lbl = tk.Label(row, text=txt, bg=CARD, fg=TEXT,
                                font=(FONT, 11), wraplength=580,
                                justify="left", anchor="w")
            text_lbl.pack(side="left", fill="x", expand=True)

            for widget in (row, indicator, text_lbl):
                widget.bind("<Button-1>", lambda e, idx=i: self._select(idx))

            self.choice_btns.append((row, indicator, text_lbl))

        # bottom: feedback + next
        self.bottom_frame = tk.Frame(card, bg=CARD)
        self.bottom_frame.pack(fill="x", padx=30, pady=(10, 20))

        self.feedback_lbl = tk.Label(self.bottom_frame, text="", bg=CARD,
                                     font=(FONT, 12, "bold"))
        self.feedback_lbl.pack(side="left", expand=True)

        self.next_btn = tk.Button(self.bottom_frame,
                                  text="Next  ▶",
                                  bg=BTN_BG, fg=BTN_FG,
                                  font=(FONT, 11, "bold"),
                                  relief="flat", cursor="hand2",
                                  padx=20, pady=8,
                                  command=self._next_question,
                                  state="disabled")
        self.next_btn.pack(side="right")

        # score label top right
        self.score_lbl = tk.Label(self.main_frame,
                                  text=f"Score: {self.score}/{self.q_index}",
                                  bg=BG, fg="white", font=(FONT, 10, "bold"))
        self.score_lbl.place(relx=1.0, y=-38, anchor="ne")

    # ── SELECT ANSWER ────────────────────────
    def _select(self, idx):
        if self.answered:
            return
        self.answered = True
        correct = self.questions[self.q_index]["a"]

        for i, (row, ind, txt) in enumerate(self.choice_btns):
            if i == correct:
                ind.config(bg=CORRECT, fg="white")
                row.config(bg="#E8FAF0")
                txt.config(bg="#E8FAF0")
            elif i == idx and idx != correct:
                ind.config(bg=WRONG, fg="white")
                row.config(bg="#FFF0F0")
                txt.config(bg="#FFF0F0")

        if idx == correct:
            self.score += 1
            self.feedback_lbl.config(text="✅  Correct!", fg=CORRECT)
        else:
            self.feedback_lbl.config(
                text=f"❌  Wrong! Answer: {['A','B','C','D'][correct]}", fg=WRONG)

        self.next_btn.config(state="normal")
        self.score_lbl.config(text=f"Score: {self.score}/{self.q_index+1}")

    # ── NEXT ─────────────────────────────────
    def _next_question(self):
        self.q_index += 1
        if self.q_index < len(self.questions):
            self._show_question()
        else:
            self._show_results()

    # ── RESULTS ──────────────────────────────
    def _show_results(self):
        self._clear()
        total = len(self.questions)
        pct   = (self.score / total) * 100

        if pct == 100:
            emoji, msg, col = "🏆", "PERFECT SCORE!", GOLD
        elif pct >= 80:
            emoji, msg, col = "🎉", "Excellent Work!", CORRECT
        elif pct >= 60:
            emoji, msg, col = "👍", "Good Job!", "#5B9BD5"
        else:
            emoji, msg, col = "📚", "Keep Studying!", WRONG

        card = tk.Frame(self.main_frame, bg=CARD)
        card.place(relx=0.5, rely=0.5, anchor="center", width=620, height=460)

        tk.Label(card, text=emoji, bg=CARD, font=(FONT, 48)).pack(pady=(30, 5))
        tk.Label(card, text=msg, bg=CARD, fg=col,
                 font=(FONT, 22, "bold")).pack()

        tk.Label(card, text=f"You scored  {self.score} / {total}",
                 bg=CARD, fg=TEXT, font=(FONT, 16)).pack(pady=10)

        # score bar
        bar_bg = tk.Frame(card, bg="#EEEEEE", height=18)
        bar_bg.pack(fill="x", padx=60, pady=5)
        bar_bg.update_idletasks()
        fill_w = int((self.score / total) * bar_bg.winfo_width())
        tk.Frame(bar_bg, bg=col, height=18, width=fill_w).place(x=0, y=0)

        tk.Label(card, text=f"{pct:.0f}%", bg=CARD, fg=SUBTEXT,
                 font=(FONT, 11)).pack()

        tk.Frame(card, bg="#DDDDDD", height=1).pack(fill="x", padx=60, pady=15)

        lesson = self.selected_lesson.get()
        tk.Label(card, text=f"Lesson: {lesson}", bg=CARD, fg=SUBTEXT,
                 font=(FONT, 10), wraplength=500).pack()

        btn_frame = tk.Frame(card, bg=CARD)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="🔄  Retry", bg=ACC, fg="white",
                  font=(FONT, 11, "bold"), relief="flat", cursor="hand2",
                  padx=20, pady=8, command=self._start_quiz).pack(side="left", padx=10)

        tk.Button(btn_frame, text="🏠  Home", bg=BTN_BG, fg=BTN_FG,
                  font=(FONT, 11, "bold"), relief="flat", cursor="hand2",
                  padx=20, pady=8, command=self._show_home).pack(side="left", padx=10)


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()