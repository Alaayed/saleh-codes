"""Build 5 moderncv theme variants of the one-page resume. Same content, native moderncv commands.
Tries 11pt, then 10pt, then tighter margins until the PDF is one page."""
import re, subprocess, pathlib, shutil

OUT = pathlib.Path(__file__).parent
XELATEX = "xelatex"

VARIANTS = [
    # name,            style,          color,      font
    ("classic-blue",      "classic",      "blue",     "sans"),
    ("casual-green",      "casual",       "green",    "sans"),
    ("oldstyle-burgundy", "oldstyle",     "burgundy", "roman"),
    ("fancy-purple",      "fancy",        "purple",   "sans"),
    ("banking-cerulean",   "banking",      "cerulean", "sans"),
]

PREAMBLE = r"""\documentclass[FONTSIZE,a4paper,FONT]{moderncv}
\moderncvstyle{STYLE}
\moderncvcolor{COLOR}
\nopagenumbers{}
\usepackage[utf8]{inputenc}
\usepackage{fontspec}
\usepackage[top=TOP, bottom=TOP, left=SIDE, right=SIDE]{geometry}
\setlength{\hintscolumnwidth}{HINT}
\usepackage{hyperref}
\hypersetup{colorlinks=true, urlcolor=blue}
\name{Saleh}{Alaayed}
\title{Software Engineer}
\phone[mobile]{+966 59 266 6761}
\email{saleh.alaayed@kaust.edu.sa}
\social[linkedin]{salaayed}
\social[github]{Alaayed}
\begin{document}
\makecvtitle
"""

BODY = r"""
\section{Summary}
\cvitem{}{Software engineer at Darb, a Saudi spend-management fintech, where I led the redesign of the platform's user model and built its approval workflow engine. MS student in Computer Science at KAUST and Purdue CS graduate (top-20 US program) with a specialization in AI.}

\section{Education}
\cventry{Aug 2026 -- Present}{MS in Computer Science}{King Abdullah University of Science and Technology (KAUST)}{Thuwal, Saudi Arabia}{}{}
\cventry{May 2026}{BS in Computer Science, Specialization in AI}{Purdue University}{West Lafayette, IN}{GPA 3.65/4.0}{}

\section{Experience}
\cventry{Jun 2026 -- Present}{Software Engineer}{Darb (Darbpay)}{Riyadh, Saudi Arabia}{Corporate cards \& spend management}{%
\begin{itemize}
\item Led the redesign of the platform's \textbf{user and roles model}: merged five overlapping identity tables into one, then migrated production data to it with zero downtime, behind feature flags, with nightly checks comparing old and new data.
\item Designed and built the \textbf{approval workflow engine}: admins define who approves card and limit-increase requests, with rules by amount, multi-step approval chains and automatic fallbacks.
\item Fixed a \textbf{security issue} that let group managers see full card numbers, and rebuilt transaction search to run on the server so it covers full history.
\item Shipped \textbf{100+ tickets} across the web portal, admin portal and mobile app, and led 4 projects end to end, from spec to production.
\end{itemize}}

\section{Projects}
\cventry{Aug 2024 -- Dec 2024}{Sports Fantasy Website}{Go, Next.js, MongoDB}{}{}{Collaborated with a six-member team over 3 sprints to deliver a full-stack fantasy sports platform using a Go backend, Next.js frontend and MongoDB.}
\cventry{Jun 2025 -- Aug 2025}{IMU-Based HAR}{KAUST Information Lab, Intern}{}{}{%
\begin{itemize}
\item Built an IMU-based model classifying prayer transitions with ~90\% accuracy across 100 runs, for research using prayer motion as an early indicator of motor decline.
\item Processed quaternion data for world-frame rotation, denoising, and L2-norm peak detection; applied data augmentation (SMP, ATD) to improve temporal model generalization.
\end{itemize}}
\cventry{Jan 2025 -- Present}{\href{https://github.com/Alaayed/baloot_engine}{Baloot Card Game Engine}}{Rust}{}{}{%
\begin{itemize}
\item Engineered a Baloot card game engine in Rust, implementing game state management and trick representation across ``Sun'' and ``Hokom'' game modes.
\item Built rule-compliant legal move validation enforcing suit-following, trump logic, and Baloot-specific scoring, verified by 40+ unit tests.
\item Implemented a parallelized Alpha-Beta pruning AI using Rayon, searching 16 moves ahead and completing a full game traversal in 5.5 seconds.
\end{itemize}}

\section{Skills}
\cvitem{Coursework}{Software Engineering, Information Systems (SQL), Data Mining \& Machine Learning, Analysis of Algorithms}
\cvitem{Languages}{TypeScript, Go, Java, Python, C, C++, Rust}
\cvitem{Spoken}{English, Arabic}

\section{Awards}
\cventry{2021 -- 2026}{KAUST Gifted Student Program Recipient}{King Abdullah University of Science and Technology}{Thuwal, Saudi Arabia}{}{Competitively selected for KAUST's national undergraduate scholarship for academic and extracurricular excellence.}

\end{document}
"""

# (fontsize, top margin, side margin, hint column) tried in order until one page
ATTEMPTS = [("11pt", "0.7in", "0.75in", "2.6cm"),
            ("10pt", "0.7in", "0.75in", "2.5cm"),
            ("10pt", "0.5in", "0.6in", "2.3cm")]

def build(name, style, color, font):
    d = OUT / name; d.mkdir(exist_ok=True)
    for fs, top, side, hint in ATTEMPTS:
        tex = (PREAMBLE.replace("FONTSIZE", fs).replace("FONT", font).replace("STYLE", style)
               .replace("COLOR", color).replace("TOP", top).replace("SIDE", side).replace("HINT", hint))
        # oldstyle/fancy put the contact block in the hint column: it needs ~4cm or it runs into the text
        if style in ("oldstyle", "fancy"):
            tex = tex.replace("\\setlength{\\hintscolumnwidth}{" + hint + "}", "\\setlength{\\hintscolumnwidth}{4cm}")
        body = BODY
        # banking's \cventry prints arg 3 bold and arg 2 italic, so project title and tech stack swap places
        if style == "banking":
            body = re.sub(r"\\cventry\{([^}]*)\}\{(Sports Fantasy Website|IMU-Based HAR|\\href\{[^}]*\}\{Baloot Card Game Engine\})\}\{([^}]*)\}",
                          r"\\cventry{\1}{\3}{\2}", body)
        tex += body
        (d / "resume.tex").write_text(tex, encoding="utf-8")
        r = subprocess.run([XELATEX, "-interaction=nonstopmode", "-halt-on-error", "resume.tex"],
                           cwd=d, capture_output=True, text=True, timeout=300, errors="replace")
        m = re.search(r"Output written on resume\.pdf \((\d+) page", r.stdout)
        if not m:
            err = [l for l in r.stdout.splitlines() if l.startswith("!")][:3]
            return f"{name}: FAILED {err}"
        if m.group(1) == "1":
            return f"{name}: 1 page at {fs}, margins {top}/{side}"
    return f"{name}: still {m.group(1)} pages after all attempts"

for v in VARIANTS:
    print(build(*v), flush=True)
