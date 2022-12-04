class RockPaperScissors:
    def __init__(self, file_path):
        self.FAKE_STRAT_POINTS = {
            "A X": 4,
            "A Y": 8,
            "A Z": 3,
            "B X": 1,
            "B Y": 5,
            "B Z": 9,
            "C X": 7,
            "C Y": 2,
            "C Z": 6
        }
        self.REAL_STRAT_POINTS = {
            "A X": 3,
            "A Y": 4,
            "A Z": 8,
            "B X": 1,
            "B Y": 5,
            "B Z": 9,
            "C X": 2,
            "C Y": 6,
            "C Z": 7
        }
        self.first_score = 0
        self.second_score = 0

        with open(file_path) as f:
            self.strategy = f.read().split("\n")

    def get_first_part_outcome(self, round):
        return self.FAKE_STRAT_POINTS[round]

    def get_second_part_outcome(self, round):
        return self.REAL_STRAT_POINTS[round]

    def calculate_scores(self):
        self.first_score = sum([self.get_first_part_outcome(round) for round in self.strategy])
        self.second_score = sum([self.get_second_part_outcome(round) for round in self.strategy])

    def get_score(self, part):
        if part == 1:
            return self.first_score
        else:
            return self.second_score



solution = RockPaperScissors("raw_data/day2.txt")


print(f'part 1 answer is: {solution.get_score(1)}')
print(f'part 2 answer is: {solution.get_score(2)}')
