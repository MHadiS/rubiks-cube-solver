import settings as s


class RubiksCube:
    def __init__(self, state: list = s.START_STATE) -> None:
        self.state = state