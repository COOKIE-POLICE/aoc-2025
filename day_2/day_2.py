from abc import ABC, abstractmethod

class RepeatingStrategy(ABC):
    @abstractmethod
    def is_repeating(self, number_string: str) -> bool:
        pass

class TwiceRepeatingStrategy(RepeatingStrategy):
    def is_repeating(self, number_string: str) -> bool:
        n = len(number_string)
        if n % 2 != 0:
            return False
        half = n // 2
        return number_string[:half] == number_string[half:]

class CompleteRepeatingStrategy(RepeatingStrategy):
    def is_repeating(self, number_string: str) -> bool:
        return number_string in (number_string + number_string)[1:-1]

class RepeatingNumberChecker:
    def __init__(self, strategy: RepeatingStrategy = TwiceRepeatingStrategy()):
        self.strategy = strategy

    def is_repeating(self, number_string: str) -> bool:
        return self.strategy.is_repeating(number_string)

class RangeBuilder:
    def __init__(self):
        self.ranges = []
    def parse_range(self, range_string: str):
        parts = range_string.split("-")
        self._start = int(parts[0])
        self._end = int(parts[1])
        self.ranges.append(list(range(self._start, self._end + 1)))
        return self

    def build(self) -> list[int]:
        return self.ranges


class PuzzleSolver:
    def __init__(self, repeating_number_checker: RepeatingNumberChecker, range_builder: RangeBuilder, filepath: str):
        self.repeating_number_checker = repeating_number_checker
        self.range_builder = range_builder
        self._filepath = filepath

    def solve(self) -> list[int]:
        sum = 0
        with open(self._filepath) as file:
            for range_string in file.read().split(","):
                self.range_builder.parse_range(range_string.strip())
        for range in self.range_builder.build():
            for number in range:
                if self.repeating_number_checker.is_repeating(str(number)):
                    sum += number
        return sum
        
def main():
    builder1 = RangeBuilder()
    checker = RepeatingNumberChecker(TwiceRepeatingStrategy())
    solver1 = PuzzleSolver(checker, builder1, "day_2/puzzle_input.txt")
    print("Twice: " + str(solver1.solve()))

    builder2 = RangeBuilder()
    checker.strategy = CompleteRepeatingStrategy()
    solver2 = PuzzleSolver(checker, builder2, "day_2/puzzle_input.txt")
    print("Complete: " + str(solver2.solve()))

if __name__ == "__main__":
    main()

