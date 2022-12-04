from src.day2.rock_paper_scissors import RockPaperScissors

class TestRockPaperScissors:
    test_game = RockPaperScissors('test/test-inputs/day2.txt')

    def test_get_first_part_outcome(self):
        assert self.test_game.get_first_part_outcome("A X") == 4
        assert self.test_game.get_first_part_outcome("A Y") == 8
        assert self.test_game.get_first_part_outcome("A Z") == 3
        assert self.test_game.get_first_part_outcome("B X") == 1
        assert self.test_game.get_first_part_outcome("B Y") == 5
        assert self.test_game.get_first_part_outcome("B Z") == 9
        assert self.test_game.get_first_part_outcome("C X") == 7
        assert self.test_game.get_first_part_outcome("C Y") == 2
        assert self.test_game.get_first_part_outcome("C Z") == 6

    def test_get_second_part_outcome(self):
        assert self.test_game.get_second_part_outcome("A X") == 3
        assert self.test_game.get_second_part_outcome("A Y") == 4
        assert self.test_game.get_second_part_outcome("A Z") == 8
        assert self.test_game.get_second_part_outcome("B X") == 1
        assert self.test_game.get_second_part_outcome("B Y") == 5
        assert self.test_game.get_second_part_outcome("B Z") == 9
        assert self.test_game.get_second_part_outcome("C X") == 2
        assert self.test_game.get_second_part_outcome("C Y") == 6
        assert self.test_game.get_second_part_outcome("C Z") == 7  
        
    
    def test_calculate_scores(self):
        self.test_game.calculate_scores()

        assert self.test_game.get_score(1) == 15
        assert self.test_game.get_score(2) == 12












    