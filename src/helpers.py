from pathlib import Path

class helpers:

    @staticmethod
    def parse_input(file: Path) -> list[str]:
        fp = Path.open(file)
        return [line for line in fp.readlines()]