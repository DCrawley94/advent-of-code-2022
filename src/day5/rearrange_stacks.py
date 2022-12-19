from src.day5.helpers import (
    format_input,
    format_diagram,
    format_instructions,
    reorganise_stacks
)


def rearrange_crates(diagram, instructions, move_multiple):
    working_diagram = diagram
    for instruction in instructions:
        working_diagram = reorganise_stacks(
            instruction, working_diagram, move_multiple)
    return working_diagram


with open('raw_data/day5.txt') as f:
    file = f.read()
    raw_diagram, raw_instructions = format_input(file)

diagram = format_diagram(raw_diagram)
instructions = format_instructions(raw_instructions)
# First part answer
# reorganised_crates = rearrange_crates(
#     diagram, instructions, False)

# Second part answer
reorganised_crates = rearrange_crates(
    diagram, instructions, True)

stacks = reorganised_crates.values()
top_items = [stack[-1] for stack in stacks]
print('Top items:', ''.join(top_items))
