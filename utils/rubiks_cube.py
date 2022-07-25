import utils.settings as s


class RubiksCube:
    def __init__(self, state: dict = s.START_STATE) -> None:
        self.state = state
    
    def solved(self) -> bool:
        if self.state == s.START_STATE:
            return True
        return False

    def up(self, inverse: bool = False):
        blue = state['b'][0]
        green = state['g'][0]
        yellow = state['y'][0]
        white = state['w'][0]
        new_value = None

        if inverse:
            new_values = (green, yellow, blue, white)
        else:
            new_value = (blue, white, green, yellow)

        state = self.state.copy()
        (state['w'][0], state['g'][0], state['y'][0], state['b'][0]) = new_values

        return RubiksCube(state)
