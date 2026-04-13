"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
The model was able to find the correct answers in the context regardless of the 
structure of the prompt. This is because the given context is already "clean" 
(contains only relevant data; no redundant or irrelevant data that "distract" 
the model), making it straightforward for the model to locate the relevant 
information in the data without relying of structured data.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = True

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
None of the distractors misled the model, but if I have to pick one, I would say 
"The New Town Vault: capacity=162, vegan=no, status=available". Both 
distractors fail one condition, but "The New Town Vault" sounds very similar to 
one of the correct answers that it could mislead the model when it considers the 
entire context as one text block without a structure (e.g. pub names and their
properties could weigh similarly important to the model).
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
All answers under different conditions were correct, but the answer under the 
first condition (plain format) did not match the exact official name ("Haymarket 
Vaults" instead of "The Haymarket Vaults"). This is likely because the plain 
format presented the context a a text block without defining the boundary of the 
name of the pub, while in the other two conditions, the xml tags tell the model 
which chunk of tokens is the name of the pub explicitly. Smaller models often 
rely more on data structure than larger models where they can just deduce latent 
information from the context. Therefore, this name matching issue only appears 
in Part C where a small model was used.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the context contains noisy or ambiguous data 
that could distract the model, and when precision in the output is required. In 
this exercise, while all three formats produced correct answers, the plain 
format showed a lower precision in Part C with the smaller model, suggesting 
that structured formatting like XML tags helps the model identify exact 
boundaries of entities in the data, especially when the model is less capable 
of deducing such information from the context.
"""
