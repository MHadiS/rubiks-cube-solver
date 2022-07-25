import utils.settings as s


class RubiksCube:
    def __init__(self, state: dict = s.START_STATE) -> None:
        self.state = state
    
    def solved(self) -> bool:
        if self.state == s.START_STATE:
            return True
        return False