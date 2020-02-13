import problem_sovler.solution_calculator as sc

def test_should_return_answer_when_the_solution_is_requested():
    solution_calculator = sc.SolutionCalculator(7)
    expected_solution = solution_calculator.calculate()
    assert expected_solution == 7