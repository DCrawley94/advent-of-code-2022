from string import ascii_letters
from functools import reduce


class ElfRucksack:
    def __init__(self, file_path):
        self.priorities = {char: i + 1 for i, char in enumerate(ascii_letters)}
        with open(file_path) as f:
            self.rucksacks = f.read().split('\n')

    def solve_part_one(self):
        common_items = []
        for rucksack_contents in self.rucksacks:
            middle_index = int(len(rucksack_contents)/2)
            compartment_one = rucksack_contents[:middle_index]
            compartment_two = rucksack_contents[middle_index:]

            common_item = list(
                set(compartment_one).intersection(compartment_two))[0]

            common_items.append(common_item)

        return reduce(lambda priority_sum, item: priority_sum + self.priorities[item], common_items, 0)

    def solve_part_two(self):
        elf_groups = [self.rucksacks[i:i+3]
                      for i in range(0, len(self.rucksacks), 3)]
        badges = []
        for elf1, elf2, elf3 in elf_groups:
            badges.extend(list(set(elf1).intersection(elf2, elf3)))

        return reduce(lambda priority_sum, item: priority_sum + self.priorities[item], badges, 0)

    def get_solutions(self):
        return self.solve_part_one(), self.solve_part_two()


part_one_solution, part_two_solution = ElfRucksack(
    'raw_data/day3.txt').get_solutions()

print(f"part 1 solution: {part_one_solution}")
print(f"part 2 solution: {part_two_solution}")
