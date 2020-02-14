import problem_sovler.solution_calculator as sc

testtime = '12:56:01'

def test_should_return_answer_when_the_solution_is_requested():
    solution_calculator = sc.BerlinClock(7)
    expected_solution = solution_calculator.calculate()
    assert expected_solution == 7

def test_should_return_O_when_seconds_are_odd(testtime):
    solution_calculator = sc.BerlinClock(testtime)
    expected_solution = solution_calculator.calculate()
    assert expected_solution == 'O'