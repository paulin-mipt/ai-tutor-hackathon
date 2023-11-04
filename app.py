from flask import Flask, render_template, request
from flask_materialize import Material

from anthropic_client import AnthropicClient
from problems import get_problem

import os


app = Flask(__name__)  
Material(app)

API_KEY = os.environ["ANTHROPIC_KEY"]
anthropic_client = AnthropicClient(API_KEY)


@app.route("/", methods=["GET", "POST"])
def problem():
    # todo - add problem uuid and a database, currently hardcoded
    problem = get_problem()

    if request.method == "GET":
        return render_template('problem.html', problem=problem.problem_text, solution=problem.solution_steps, hints=None)

    # some solution was submitted
    student_solution = request.form["student_solution"]
    if anthropic_client.is_answer_complete(problem.solution_steps, student_solution):
        # todo replace with some proper page
        return "<h1>Tada, all good, correct</h1>"
    else:
        # TODO: give options, ask if you need a hint?
        hints = anthropic_client.get_help(problem=problem.problem_text, solution=problem.solution_steps, student_solution=student_solution)
        return render_template('problem.html', problem=problem.problem_text, solution=problem.solution_steps, hints=hints)