''' Day 1 functions '''
from heapq import nlargest

# PART 1
# def create_summed_calories_list(file_path):
#     with open(file_path) as f:
#         elf_calorie_strings = f.read().split('\n\n')

#     elf_inventory = [elf_data.split('\n') for elf_data in elf_calorie_strings]

#     elf_calories = [sum(list(map(int, inventory)))
#                     for inventory in elf_inventory]

#     return elf_calories

def calculate_elf_calories(path_to_data):
    '''
    Finds the elf in the group that is packing the most calorific content.
    Returns value: Total calories of most calorific elf, list of calori sums for each elf
    '''

    with open(path_to_data, encoding='utf8') as f:
        elf_calorie_strings = f.read().split('\n\n')

    formatted_calorie_data = [[int(calorie_count) for calorie_count in elf.split(
        '\n')] for elf in elf_calorie_strings]

    calorie_counts = [sum(calorie_group)
                      for calorie_group in formatted_calorie_data]

    return calorie_counts

    

#  PART 2


def find_total_calories_of_top_elves(elf_calorie_data):
    '''Finds total calories of top 3 elves'''
    return sum(nlargest(3, elf_calorie_data))


calorie_data = calculate_elf_calories('raw_data/day1.txt')
print(f'Answer to part 1: {max(calorie_data)}')

part_2_answer = find_total_calories_of_top_elves(calorie_data)
print(f'Answer to part 2: {part_2_answer}')
