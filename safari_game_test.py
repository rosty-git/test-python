from animal import Lion, Wolf, Tiger, Deer
from safari_game import create_random_map, get_random_cell


def create_mock_map():
    return [[Tiger(), Lion(), Lion(), Wolf(), Tiger(), Lion(), Wolf(), Lion(), Deer(), Lion()],
            [Tiger(), Wolf(), Tiger(), Deer(), Deer(), Deer(), Deer(), Lion(), Lion(), Tiger()],
            [Wolf(), Lion(), Tiger(), Deer(), Deer(), Wolf(), Tiger(), Tiger(), Deer(), Lion()],
            [Wolf(), Deer(), Tiger(), Deer(), Wolf(), Deer(), Lion(), Deer(), Tiger(), Lion()],
            [Wolf(), Lion(), Deer(), Wolf(), Deer(), Wolf(), Wolf(), Wolf(), Deer(), Wolf()],
            [Deer(), Deer(), Deer(), Wolf(), Tiger(), Wolf(), Wolf(), Lion(), Wolf(), Wolf()],
            [Wolf(), Lion(), Wolf(), Deer(), Tiger(), Wolf(), Lion(), Lion(), Deer(), Deer()],
            [Tiger(), Wolf(), Deer(), Wolf(), Wolf(), Lion(), Wolf(), Wolf(), Wolf(), Tiger()],
            [Deer(), Wolf(), Tiger(), Tiger(), Tiger(), Tiger(), Wolf(), Tiger(), Tiger(), Deer()],
            [Lion(), Lion(), Deer(), Tiger(), Lion(), Deer(), Wolf(), Deer(), Tiger(), Wolf()]]


def get_expected_result():
    ex = """T L L - T L - L D L
            T - T - - - - L L T
            - L T - - - T T - L
            - - T - - - L - T L
            - L - - - - - - - -
            - - - - T - - L - -
            - L - - T - L L - -
            T - - - - L - - - T
            - - T T T T - T T -
            L L - T L - - - - -"""
    return ex.replace(" ", "")


def test_50():
    # 1
    safari_map = create_random_map(50)
    start_cell = get_random_cell(safari_map)

    # 2
    from safari_game import Safari
    safari = Safari(safari_map, start_cell)

    # 3
    safari.print_map()

    # 4
    safari.print_start()

    safari.play()

    # 5
    print("end")
    safari.print_map()
    assert True


def test_expected_result():
    safari_map = create_mock_map()
    start_cell = (9, 8)  # one based =(10,9)
    from safari_game import Safari
    safari = Safari(safari_map, start_cell)
    safari.play()
    final = safari.print_map()
    expected_str_representation = get_expected_result()
    assert expected_str_representation == final.replace(" ", "")


if __name__ == "__main__":
    test_expected_result()
    # test_50()
    print("Everything passed")
