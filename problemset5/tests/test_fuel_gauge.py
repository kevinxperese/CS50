from problemset5 import fuel_gauge


def test_convert_fraction():
    assert fuel_gauge.convert_fraction('1/4') == (1, 4)
    assert fuel_gauge.convert_fraction('4/4') == (4, 4)


def test_calc_fuel_level():
    assert fuel_gauge.calc_fuel_level(1, 4) == '25%'
    assert fuel_gauge.calc_fuel_level(4, 4) == 'F'
    assert fuel_gauge.calc_fuel_level(99.1, 100) == 'F'
    assert fuel_gauge.calc_fuel_level(0.9, 100) == 'E'