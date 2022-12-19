from src.day1.calories import calculate_elf_calories


def test_it_works():
    '''Incredibly named function that badly tests my code'''
    assert calculate_elf_calories(
        'test/test-inputs/day1.txt') == [6000, 4000, 11000, 24000, 10000]
