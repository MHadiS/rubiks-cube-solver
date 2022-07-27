import utils.settings as s


class RubiksCube:
    def __init__(self, state: dict = s.START_STATE) -> None:
        self.state = state
    
    def solved(self) -> bool:
        if self.state == s.START_STATE:
            return True
        return False

    def up_down(self, command: str, inverse: bool = False):
        state = self.state.copy()

        if command.lower == "up":
            row = 0
        
        elif command.lower == "down":
            row = 2

        blue = state['b'][row]
        green = state['g'][row]
        yellow = state['y'][row]
        white = state['w'][row]
        new_values = None

        if inverse:
            new_values = (green, yellow, blue, white)
        else:
            new_values = (blue, white, green, yellow)

        (state['w'][row], state['g'][row], state['y'][row], state['b'][row]) = new_values

        return RubiksCube(state)