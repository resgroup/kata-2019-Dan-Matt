import berlin_clock.light_calculator

testtime = '12:56:01'

def test_should_return_O_when_seconds_are_odd(testtime = '12:56:01'):
    clock = berlin_clock.light_calculator.BerlinClock(testtime)
    expected_solution = clock.calculate_row_1_light()
    assert expected_solution == 'O'

def test_should_return_RROO_when_2x_full_5_hours(testtime = '12:56:01'):
    clock = berlin_clock.light_calculator.BerlinClock(testtime)
    expected_solution = clock.calculate_row_2_lights()
    assert expected_solution == 'RROO'