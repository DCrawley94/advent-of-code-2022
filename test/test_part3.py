from src.day3.rucksack_reorganisation import ElfRucksack

class TestElfRucksack:
    test_rucksack = ElfRucksack("test/test-inputs/day3.txt")
    part_one_solution, part_two_solution = test_rucksack.get_solutions()

    def test_solution(self):
        assert self.part_one_solution == 157

    def test_part_two_solution(self):
        assert self.part_two_solution == 70