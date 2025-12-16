from pathlib import Path
# Notes
# Define positive as right
# Define negative as left
# Mod by 100 since it cannot be 100
# maybe make a rotation builder that generates a list, then just iterate through it, add and add and counting each time it becomes zero

class RotationParser:
    def __init__(self):
        self._rotations = []

    def parse_rotation(self, rotation_string: str):
        direction = rotation_string[0]
        distance = int(rotation_string[1:])
        value = distance if direction == "R" else -distance
        self._rotations.append(value)
        return self

    def get_rotations(self) -> list[int]:
        return self._rotations


class RotationFileReader:
    def __init__(self, filepath: Path):
        self._filepath = filepath

    def read(self) -> list[int]:
        parser = RotationParser()
        with open(self._filepath) as file:
            for line in file:
                parser.parse_rotation(line.strip())
        return parser.get_rotations()


class PasswordSolver:
    def __init__(self, rotation_reader: RotationFileReader):
        self._rotations = rotation_reader.read()

    def solve(self) -> int:
        position = 50
        zero_count = 0
        
        for rotation in self._rotations:
            position = (position + rotation) % 100
            if position == 0:
                zero_count += 1
        
        return zero_count


def main():
    reader = RotationFileReader(Path("day_1/puzzle_input.txt"))
    solver = PasswordSolver(reader)
    print(solver.solve())


if __name__ == "__main__":
    main()