import re


def format_input(raw_input):
    diagram, instructions = raw_input.split('\n\n')
    return [diagram, instructions]


def create_rows(raw_diagram):
    new_str = ''

    for i, char in enumerate(raw_diagram):
        if i % 4 == 0:
            new_str = new_str + '['
        elif i % 2 == 0:
            new_str = new_str + ']'
        else:
            new_str = new_str + char

    diagram_with_empty_slots = re.sub(r'\[( )\]', "[X]", new_str).split("\n")
    diagram_with_boxes_removed = [
        re.sub(
            r'[\[\]]',
            '',
            row) for row in diagram_with_empty_slots]
    diagram_with_column_labels_removed = diagram_with_boxes_removed[:-1]
    diagram_rows = [row.split(' ')
                    for row in diagram_with_column_labels_removed]
    reversed_rows = diagram_rows[::-1]
    return reversed_rows


def format_diagram(raw_rows):
    diagram = create_rows(raw_rows)
    col_count = len(diagram[0])
    stacks = {i + 1: list() for i in range(col_count)}

    for row in diagram:
        for i, slot in enumerate(row):
            if slot != 'X':
                stacks[i + 1].append(slot)

    return stacks


def format_instructions(raw_instructions):
    '''
    Args:
        raw_instructions: raw string representing the list of instructions

    Returns:
        list of dictionaries representing the key information
        from each instruction
    '''
    try:
        lines = raw_instructions.split('\n')

        # This finds the integers in each instruction string
        matches = [re.findall(r'\d', line) for line in lines]

        # Creates a dictionary representing each instruction
        instructions = []
        for match in matches:
            if (len(match) > 3):
                a, b, c, d = match
                instruction = [int(a + b), int(c), int(d)]
                instructions.append(instruction)
            else:
                a, b, c = match
                instruction = [int(a), int(b), int(c)]
                instructions.append(instruction)
        return instructions
    except Exception as e:
        print("oh no u fucked it\n")
        raise e


def reorganise_stacks(instruction, stack_diagram, move_multiple):
    amount, origin, destination = instruction
    print(amount, origin, destination, '!!!!!')

    if move_multiple is True:
        items = stack_diagram[origin][-amount:]
        stack_diagram[origin] = stack_diagram[origin][:len(
            stack_diagram[origin]) - amount]
        stack_diagram[destination].extend(items)
    else:
        while amount > 0:
            item = stack_diagram[origin].pop()
            stack_diagram[destination].append(item)
            amount = amount - 1

    return stack_diagram
