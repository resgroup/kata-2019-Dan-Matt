import berlin_clock.light_calculator

testtime = '12:56:01'

def test_O_when_seconds_are_odd(testtime = '12:56:01'):
    clock = berlin_clock.light_calculator.BerlinClock(testtime)
    expected_solution = clock.calculate_seconds_light()
    assert expected_solution == 'O'

def test_RROO_when_2x_full_5_hours(testtime = '12:56:01'):
    clock = berlin_clock.light_calculator.BerlinClock(testtime)
    expected_solution = clock.calculate_5_hour_lights()
    assert expected_solution == 'RROO'

def test_RROO_when_2x_full_1_hours_remainder(testtime = '12:56:01'):
    clock = berlin_clock.light_calculator.BerlinClock(testtime)
    expected_solution = clock.calculate_1_hour_lights()
    assert expected_solution == 'RROO'

def test_YYYYYYYYYYY_when_11x_5_minutes(testtime = '12:56:01'):
    clock = berlin_clock.light_calculator.BerlinClock(testtime)
    expected_solution = clock.calculate_5_minute_lights()
    assert expected_solution == 'YYYYYYYYYYY'


def test_YOOO_when_1x_1_minutes_remainder(testtime = '12:56:01'):
    clock = berlin_clock.light_calculator.BerlinClock(testtime)
    expected_solution = clock.calculate_1_minute_lights()
    assert expected_solution == 'YOOO'