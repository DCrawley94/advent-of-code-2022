from src.day4.camp_cleanup import (
    get_shift_data,
    make_shift_diagram,
    shifts_collide,
    shift_check)


def test_get_shift_data():
    expected = [[".234.....", ".....678."],
                [".23......", "...45...."],
                ["....567..", "......789"],
                [".2345678.", "..34567.."],
                [".....6...", "...456..."],
                [".23456...", "...45678."]]
    actual = get_shift_data('test/test-inputs/day4.txt')
    assert actual == expected


def test_shifts_envelope():
    shift1 = ".234....."
    shift2 = ".....678."
    assert shifts_collide(shift1, shift2) is False

    shift1 = ".23...... "
    shift2 = "...45...."
    assert shifts_collide(shift1, shift2) is False

    shift1 = ".2345678."
    shift2 = "..34567.."
    assert shifts_collide(shift1, shift2) is True

    shift1 = ".....6..."
    shift2 = "...456..."
    assert shifts_collide(shift1, shift2) is True


def test_shifts_overlap():
    shift1 = ".....67.."
    shift2 = "...456..."
    assert shifts_collide(shift1, shift2) is True

    shift1 = ".....6..."
    shift2 = "...456..."
    assert shifts_collide(shift1, shift2) is True

    shift1 = ".......89"
    shift2 = "...456..."
    assert shifts_collide(shift1, shift2) is False


def test_shift_check():
    data = get_shift_data('test/test-inputs/day4.txt')
    assert shift_check(data) == 4

# def test_count_enveloping_shifts():
#     assert count_enveloping_shifts('test/test-inputs/day4.txt') == 2

# def test_count_overlapping_shifts():
    # assert count_overlapping_shifts('test/test-inputs/day4.txt') == 4
