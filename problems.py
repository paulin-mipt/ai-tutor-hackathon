from dataclasses import dataclass
from typing import List

"""
Can contain problem/solution related utilities.

At the moment has a hardcoded problem and solution.
"""

PROBLEM = "Solve me 2 + 2 * 2"
SOLUTION_STEPS = ["2 * 2 = 4", "2 + 4 = 6"]

@dataclass
class Problem:
    problem_text: str
    solution_steps: List[str]

def get_problem() -> Problem:
    return Problem(problem_text=PROBLEM, solution_steps=SOLUTION_STEPS)
