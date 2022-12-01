''' Day 1 functions '''
from heapq import nlargest

# PART 1

def find_most_calorific_elf(path_to_data):
    '''Finds the elf in the group that is packing the most calorific content'''

    with open(path_to_data, encoding='utf8') as f:
        elf_calorie_strings = f.read().split('\n\n')

        formatted_calorie_data = [[int(calorie_count) for calorie_count in elf.split(
            '\n')] for elf in elf_calorie_strings]

        calorie_counts = [sum(calorie_group)
                          for calorie_group in formatted_calorie_data]

    return max(calorie_counts), calorie_counts


part_1_answer, calorie_deets = find_most_calorific_elf('raw_data/day_1.txt')
print(f'Answer to part 1: {part_1_answer}')

#  PART 2

def find_total_calories_of_top_elves(elf_calorie_data):
    '''Finds total calories of top 3 elves'''
    return sum(nlargest(3, elf_calorie_data))


part_2_answer = find_total_calories_of_top_elves(calorie_deets)
print(f'Answer to part 2: {part_2_answer}')
