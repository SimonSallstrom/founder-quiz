# founder_fit_questions_final.py
# ------------------------------------------------------------------
# COMPLETE QUESTION BANK  (60 Likert items)  +  WEIGHTS
#
# * Customer‑empathy, leadership, finance, vision, frugality, and
#   aware‑bad‑motivation dimensions have been removed.
# * Time‑ and duration‑commitment have been merged into an “obsession”
#   dimension (3 items).
# * New dimensions added: initiative_under_uncertainty,
#   ownership_proactivity, strategic_thinking.
# * Intelligence + Creativity + Independent‑Thought together = 25 %
# * Communication = 15 %   •   Execution‑Speed = 15 %
# * Remaining 45 % is shared equally by all other dimensions at runtime.
# ------------------------------------------------------------------

QUESTIONS = [
    # --- Adaptability (4) ----------------------------------------------------
    ("I maintain healthy routines (sleep, exercise) even during crunch time.",
        "adaptability", False),
    ("Unexpected crises leave me overwhelmed and indecisive.",
        "adaptability", True),
    ("I re‑prioritize quickly when data disproves my assumptions.",
        "adaptability", False),
    ("Rapidly changing environments keep me engaged and creative.",
        "adaptability", False),

    # --- Risk Tolerance (5) --------------------------------------------------
    ("I remain calm and focused when facing the possibility of total financial loss.",
        "risk_tolerance", False),
    ("Volatile, untested markets energize rather than scare me.",
        "risk_tolerance", False),
    ("I’m willing to place bold, high‑stakes bets—but only after modelling worst‑case burn scenarios.",
        "risk_tolerance", False),
    ("I actively seek uncertain, high‑variance opportunities that could 10× the business.",
        "risk_tolerance", False),
    ("I’m emotionally and financially prepared to go another 6–12 months without salary or certainty.",
        "risk_tolerance", False),

    # --- Execution (4) -------------------------------------------------------
    ("I routinely ship minimum viable versions rather than wait for perfection.",
        "execution", False),
    ("Limited resources push me to creative solutions rather than excuses.",
        "execution", False),
    ("When plans hit obstacles, I often freeze instead of improvising.",
        "execution", True),
    ("I rapidly hack together novel work‑arounds to launch faster than competitors.",
        "execution", False),

    # --- Magnetism / Communication / Evangelism (5) -------------------------------------
 ("I can easily get people I just meet to volunteer their time to help me out with favours.",
        "communication", False),
    ("I usually convince high‑stakes stakeholders (e.g., investors, key partners) to back me despite initial hesitation.",
        "communication", False),
    ("People often describe my speaking or writing style as charismatic or magnetic.",
        "communication", False),
    ("People tend to tune out when I present my ideas or updates.",  # inverse check
        "communication", True),

    # --- Ethics & Integrity (3) ---------------------------------------------
    ("I refuse shortcuts that could harm users or reputation, even if they boost short‑term metrics.",
        "ethics", False),
    ("I think in decades when evaluating the impact of my company.",
        "ethics", False),
    ("I’d consider bending rules if it accelerates growth and seems unlikely to be caught.",
        "ethics", True),


    # --- Learning Agility (3) -----------------------------------------------
    ("I quickly teach myself unfamiliar concepts well enough to brief others.",
        "learning", False),
    ("I avoid launching projects until I feel 100 % expert.",
        "learning", True),
    ("My decisions are grounded in both expertise and continuous experimentation.",
        "learning", False),

    # --- Learning & Self‑Awareness (2) --------------------------------------
    ("I actively seek feedback and iterate quickly, viewing every experiment as a learning opportunity.",
        "learning_adaptability", False),
    ("I regularly reflect on my blind spots and seek mentors to fill them.",
        "learning_adaptability", False),

    # --- Obsession / Commitment (3) -----------------------------------------
    ("I treat this venture with the urgency and time investment of a founder—not a side project or advisory role.",
        "obsession", False),
    ("Building this company is my #1 priority, above any other family, professional, and personal pursuit.",
        "obsession", False),
    ("If this startup fails, I’ll still feel proud because I gave it everything; I showed up like it was mine.",
        "obsession", False),

    # --- Perseverance / Grit (2) --------------------------------------------
    ("I keep pushing a critical task even when progress is painfully slow.",
        "perseverance", False),
    ("I complete key objectives even after multiple failures or rejections.",
        "perseverance", False),

    # --- Focus (2) -----------------------------------------------------------
    ("I can concentrate on one top priority for hours without distraction.",
        "focus", False),
    ("I rarely multitask during deep work sessions.",
        "focus", False),

    # --- Initiative under Uncertainty (1) -----------------------------------
    ("When things are ambiguous or undefined, I take action without needing permission or guidance.",
        "initiative_under_uncertainty", False),

    # --- Ownership without Prompts (1) --------------------------------------
    ("I’ve independently taken full ownership of at least one core part of the business and pushed it forward proactively.",
        "ownership_proactivity", False),

    # --- Problem‑Solver & Inventor (3) --------------------------------------
    ("I quickly devise innovative solutions when faced with a difficult problem.",
        "problem_solver_inventor", False),
    ("I routinely build or prototype new tools or processes to improve efficiency.",
        "problem_solver_inventor", False),
    ("When we hit friction or blockers, I step in, research options, and propose solutions without waiting.",
        "problem_solver_inventor", False),

    # --- Strategic Thinking (1) ---------------------------------------------
    ("I lead or advance conversations on vision, direction, or tough prioritization calls—not just execution.",
        "strategic_thinking", False),

    # --- Execution Speed (3) -------------------------------------------------
    ("I move fast—I set ambitious deadlines and hit them, or communicate delays early and clearly.",
        "execution_speed", False),
    ("I can turn a new idea into a live test or prototype within days.",
        "execution_speed", False),
    ("I prefer launching imperfect versions quickly to learn, rather than perfecting them for months.",
        "execution_speed", False),

    # --- Rate of Improvement (2) --------------------------------------------
    ("I deliberately track my performance and set weekly improvement goals.",
        "rate_of_improvement", False),
    ("Each month I can point to a concrete skill I've measurably improved.",
        "rate_of_improvement", False),


    # --- Shapeshifter Elasticity (4) ----------------------------------------
    ("I effortlessly switch between high‑level strategy and hands‑on tasks several times a day.",
        "shapeshifter", False),
    ("I often sense unspoken organisational needs and tackle them before anyone asks.",
        "shapeshifter", False),
    ("I know exactly when to pause and gather consensus, preventing slow‑downs without blindsiding teammates.",
        "shapeshifter", False),
    ("I push ahead without consulting others even when alignment is critical.",
        "shapeshifter", True),

    # --- Intelligence (2) ----------------------------------------------------
    ("I enjoy dissecting complex problems most people avoid.",
        "intelligence", False),
    ("I consider unconventional ideas that don’t yet exist in the market.",
        "intelligence", False),

    # --- Creativity (4) ------------------------------------------------------
    ("I regularly generate multiple distinct approaches to a single problem.",
        "creativity", False),
    ("I blend ideas from unrelated fields to create novel solutions.",
        "creativity", False),
    ("I rarely come up with original ideas and stick to proven methods.",
        "creativity", True),
    ("During brainstorming I produce a high volume of ideas.",
        "creativity", False),

    # --- Independent Thought (2) --------------------------------------------
    ("I often generate ideas that challenge conventional wisdom.",
        "independent_thought", False),
    ("I am comfortable pursuing a path even when the majority disagrees.",
        "independent_thought", False)
]

# ------------------------------------------------------------------
# WEIGHTS  (sum = 1.0)
# ------------------------------------------------------------------
WEIGHTS = {
    # 25 % for intelligence‑creativity‑independent_thought
    "intelligence":        0.0833,
    "creativity":          0.0833,
    "independent_thought": 0.0834,
    # High‑importance dimensions
    "communication":       0.15,
    "execution_speed":     0.15
    # Remaining 0.45 is distributed equally across ALL other
    # dimensions at runtime by the scoring script.
}
