from src.day5.helpers import (
    format_input,
    create_rows,
    format_diagram,
    format_instructions,
    reorganise_stacks
)
from src.day5.rearrange_stacks import rearrange_crates


class TestFormattingHelpers:

    with open('test/test-inputs/day5.txt') as f:
        raw_input = f.read()

    raw_diagram, raw_instructions = format_input(raw_input)

    def test_format_input(self):
        raw_diagram, raw_instructions = format_input(self.raw_input)
        expected_diagram = '    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 '
        expected_instructions = 'move 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2'

        assert raw_diagram == expected_diagram
        assert raw_instructions == expected_instructions

    def test_create_rows(self):
        actual = create_rows(self.raw_diagram)
        expected = [['Z', 'M', 'P'], ['N', 'C', 'X'], ['X', 'D', 'X']]
        assert actual == expected

    def test_format_diagram(self):
        actual = format_diagram(self.raw_diagram)
        expected = {1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}

        assert actual == expected

    def test_formats_raw_instructions(self):
        actual = format_instructions(self.raw_instructions)
        expected = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]
        assert actual == expected


class TestReorganiseStack:

    def test_reogarnise_stacks_single_item_move_single_crate(self):
        instr = [1, 2, 1]
        stacks = {1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}

        actual = reorganise_stacks(instr, stacks, False)
        expected = {1: ['Z', 'N', 'D'], 2: ['M', 'C'], 3: ['P']}

        assert actual == expected

    def test_reogarnise_stacks_multi_item_move_single_crate(self):

        instr = [3, 1, 3]
        stacks = {1: ['Z', 'N', 'D'], 2: ['M', 'C'], 3: ['P']}

        actual = reorganise_stacks(instr, stacks, False)
        expected = {1: [], 2: ['M', 'C'], 3: ['P', 'D', 'N', 'Z']}
        assert actual == expected

    def test_reorganise_stacks_move_multiple_crates(self):
        instr = [1, 2, 1]
        stacks = {1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}

        actual = reorganise_stacks(instr, stacks, True)
        expected = {1: ['Z', 'N', 'D'], 2: ['M', 'C'], 3: ['P']}
        assert actual == expected

        instr = [3, 1, 3]
        stacks = {1: ['Z', 'N', 'D'], 2: ['M', 'C'], 3: ['P']}

        actual = reorganise_stacks(instr, stacks, True)
        expected = {1: [], 2: ['M', 'C'], 3: ['P', 'Z', 'N', 'D']}
        assert actual == expected

        instr = [2, 2, 1]
        stacks = {1: [], 2: ['M', 'C'], 3: ['P', 'Z', 'N', 'D']}

        actual = reorganise_stacks(instr, stacks, True)
        expected = {1: ['M', 'C'], 2: [], 3: ['P', 'Z', 'N', 'D']}
        assert actual == expected


def test_rearrange_crates():
    stacks = {1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}
    instructions = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]
    actual = rearrange_crates(stacks, instructions, False)
    expected = {1: ['C'], 2: ['M'], 3: ['P', 'D', 'N', 'Z']}
    assert actual == expected
