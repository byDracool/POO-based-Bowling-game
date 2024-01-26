class Player:
    def __init__(self, name):
        self.name = name
        self.score_list = []
        self.round_score_list = []
        self.round_score = 0
        self.current_round_throws = 0
        self.round = 1
        self.temp_score = 0
        self.previous_was_strike_or_spare = None
        self.total_score = 0

    def throw(self):
        pins_knocked_down = int(input(f"\n{self.name} Introduzca los bolos que ha derribado: "))
        return pins_knocked_down

    def score_calculator(self, pins_knocked_down):
        self.round_score += pins_knocked_down

    def add_throw(self):
        self.current_round_throws += 1

    def score_list_updater(self, score):
        self.score_list.append(score)

    def round_score_list_updater(self, score):
        self.round_score_list.append(score)

    def new_round_settings(self):
        self.round_score = 0
        self.current_round_throws = 0
        self.round += 1



