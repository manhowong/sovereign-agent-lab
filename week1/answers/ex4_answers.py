"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "It seems there are no Edinburgh venues currently available that can accommodate 300 guests with vegan options. Would you like me to:\n1. Search for venues with lower capacity requirements?\n2. Look for venues without strict vegan requirements?\n3. Check availability at specific venues by name?\n\nLet me know how you'd like to proceed!"

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
I changed The Albanach's status from "available" to "full" in
sovereign_agent/tools/mcp_venue_server.py, reran the MCP client, and then
reverted the change. The discovered tool list did not change, and no client
code needed updating. Query 1 still returned The Haymarket Vaults at
1 Dalry Road, Edinburgh, because that venue already matched the request exactly
for 160 vegan guests, so removing The Albanach as an option did not change the
best match.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 0   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 0   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
With MCP you can share tools across different AI systems. This makes developing 
new systems that need the same tools easier without changing the existing AI 
systems or tool code for integration. It is also easier to update or add new 
tools to the server as long as they are MCP-compatible.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
- Planner: This plans the sub-actions to take based on the given task using a strong reasoning model and lives upstream of the autonomous loop so that the system can plan ahead before excuting any actions.
- Executor: This is a faster worker that execute the action plan using an efficient model. It lives in the autonomous loop and functions without relying on human guidance.
- Memory store: This stores the data that needs to be tracked during or between agent sessions. It lives outside the agentic components but is accessible to the agents.
- Vector store: This stores the pre-defined knowledge that the agent needs for answering questions the flows.yml doesn't cover. It lives inside the structured agent where it can be easily accessed by the agent.
- Handoff bridge: This bridges the two major components (structured and autonomous), allowing the components to communicate and delegate tasks to each other during the task.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
For research: The autonomous agent. This is because the task (user prompt) is 
described in an unstructured format, making the task open-ended. The agent needs 
to reason about what the task is and what it has to do to achieve the user 
intent. For example, during the run, it went through the user's request step by 
step and extracted the relevant information for the task. It planned its own 
action loop using the available tools, e.g. it used the get weather tool to 
check if one of the user's requests (outdoor drinks), then reasoned about the 
returned weather status (partly cloudy), and decided that outdoor drinks are 
feasible.

For the call: The structured agent. This is because confirming booking is a 
high-stake event and should follow strict business rules. For example, if the 
user has a limited budget, the deposit should never exceed it. In my run, the 
agent successfully escalated the call when £500 was entered as it exceeded the 
authorised £300 limit.

The structured flow of the conversation with the structured agent ensures that 
the agent gets what input it needs from the user and that the actions taken 
will follow the pre-defined rules. Swapping the two agents feels wrong because 
you will lose the control of the agent's actions for high-stake events and lose
the flexibility of the autonomous agent for reasoning about open-ended requests.
"""
