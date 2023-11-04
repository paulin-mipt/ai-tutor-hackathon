import anthropic
from anthropic import Anthropic


# TODO: stub!
SOLUTION_EXPLANATION_TEMPLATE = "Help me with problem {problem} to understand bullet point {solution_explanation_index} of this {solution}"
SOLUTION_HELP_TEMPLATE = "Help solve the problem {problem}. Correct is this: {solution}, human did this: {student_solution}"


class AnthropicClient:
    def __init__(self, api_key: str):
        self.client = Anthropic(api_key=api_key)


    # TODO: draft/stub!!!
    def get_explanation(self, problem, solution, solution_explanation_index) -> str:
        """
        Explain a part of the solution in depth.
        """
        
        prompt = SOLUTION_EXPLANATION_TEMPLATE.format(solution=solution, problem=problem, solution_explanation_index=solution_explanation_index)

        res = self.client.completions.create(
            model="claude-2",
            prompt=f"{anthropic.HUMAN_PROMPT}{prompt}{anthropic.AI_PROMPT}",
            max_tokens_to_sample=1000,
        )
        return res.completion

    # TODO: draft/stub!!!
    def get_help(self, problem, solution, student_solution) -> str:
        """
        Get help and guidsnce with a partial solution.
        """
        prompt = SOLUTION_HELP_TEMPLATE.format(solution=solution, problem=problem, student_solution=student_solution)

        res = self.client.completions.create(
            model="claude-2",
            prompt=f"{anthropic.HUMAN_PROMPT}{prompt}{anthropic.AI_PROMPT}",
            max_tokens_to_sample=1000,
        )
        return res.completion
    
    # TODO: draft/stub!!!
    def is_answer_complete(self, solution, student_solution) -> bool:
        """
        Evaluates if the solution needs more work.
        """
        # TODO: replace debugging stub
        return False