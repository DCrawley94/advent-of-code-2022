import re

def get_shift_data(file_path):
    with open(file_path) as f:
        lines = f.read().split('\n')
        pairs_data = [re.split(r"[-,]", line) for line in lines]

        shift_data = []

        for pair_shifts in pairs_data:
            shift_times = [int(time) for time in pair_shifts]

            shift_one_diagram = make_shift_diagram(shift_times[0], shift_times[1])
            shift_two_diagram = make_shift_diagram(shift_times[2], shift_times[3])

            shift_data.append([shift_one_diagram, shift_two_diagram])

    
    return shift_data

def make_shift_diagram(start, end):
    diagram = ""
    for i in range(1,10):
        if i >= start and i <= end:
            diagram += str(i)
        else:
            diagram += '.'
    
    return diagram

def shifts_collide(shift1, shift2):
    # print('test', shift1, shift2)
    shift1_hours = re.findall(r'\d', shift1)
    shift2_hours = re.findall(r'\d', shift2)
    max_shared_hours = len(shift1_hours) + len(shift2_hours) - 1
    # min_shared_hours = min([len(shift1_hours), len(shift2_hours)])
    shared_hours = set(shift1_hours + shift2_hours)
    # print(max_shared_hours)
    # print(min_shared_hours)

    return len(shared_hours) <= max_shared_hours


def shift_check(shift_data):
    innefficient_elf_pairs = [shift for shift in shift_data if shifts_collide(shift[0], shift[1])]
    
    return len(innefficient_elf_pairs)


data = get_shift_data('raw_data/day4.txt')

print(f"answer = {shift_check(data)}")

# print(f"part 2 answer = {count_overlapping_shifts('raw_data/day4.txt')}")