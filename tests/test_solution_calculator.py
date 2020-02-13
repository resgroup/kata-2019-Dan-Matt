
def test_should_return_answer_when_the_solution_is_requested():
    solution_calculator = SolutionCalculator()
    expected_solution = solution_calculator.calculate(7)
    assert expected_solution == 7