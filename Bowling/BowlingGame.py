from Player import Player


class BowlingGame:
    def __init__(self):
        self.players_list = []

    def add_player(self, name):
        player = Player(name)
        self.players_list.append(player)

    @staticmethod
    def throw_validator(pins_knocked_down, player_round_score):
        if pins_knocked_down <= 10 and pins_knocked_down + player_round_score <= 10:
            return True
        else:
            return False

    def play(self):
        for player in self.players_list:
            while player.current_round_throws < 2 or player.current_round_throws == 2 and player.round == 10:

                # Tirar y comprobar validez de la tirada
                throw_validation = False
                while not throw_validation:
                    print(f"{player.name}, ronda: {player.round}, lanzamiento: {player.current_round_throws + 1}")
                    pins_knocked_down = player.throw()
                    throw_validation = BowlingGame.throw_validator(pins_knocked_down, player.round_score)
                    # Tirada invalida
                    if not throw_validation:
                        print("Numero de bolos derribados incorrecto.")

                # Tirada valida
                if throw_validation:
                    player.add_throw()  # Sumo 1 tirada
                    player.round_score += pins_knocked_down

                    # STRIKE (rompe bucle)
                    if player.current_round_throws == 1 and player.round_score == 10:
                        # Comprobar STRIKE previo
                        if player.previous_was_strike_or_spare == "strike":
                            player.temp_score += 20  # Compensar puntos de la tirada 2 que no se hara al ser Strike

                        elif player.previous_was_strike_or_spare == "spare":
                            player.temp_score += 10  # Compensar puntos de la tirada 2 que no se hara al ser Strike

                        if player.round == 10:
                            BowlingGame.bonus_strike(player)
                        else:
                            BowlingGame.is_strike(player)

                        # Imprimir tabla de resultados
                        BowlingGame.score_dashboard(player)
                        BowlingGame.get_total_score(player)
                        print("\n")
                        player.round_score = 0
                        break

                    # SPARE
                    elif player.current_round_throws == 2 and player.round_score == 10:
                        if player.round == 10:
                            if player.previous_was_strike_or_spare == "strike":
                                BowlingGame.bonus_strike(player)
                            else:
                                BowlingGame.bonus_spare(player)
                        else:
                            BowlingGame.is_spare(player)

                        # Imprimir tabla de resultados
                        BowlingGame.score_dashboard(player)
                        BowlingGame.get_total_score(player)
                        print("\n")
                        player.round_score = 0
                        break

                    # 1 o 2 tiradas
                    # Sumar puntos previos
                    if player.current_round_throws == 1 and player.previous_was_strike_or_spare:  # Strike o Spare
                        player.temp_score += pins_knocked_down
                        if player.previous_was_strike_or_spare == "spare":
                            player.previous_was_strike_or_spare = None

                    elif player.current_round_throws == 2 and player.previous_was_strike_or_spare == "strike":  # Strike
                        player.temp_score += pins_knocked_down
                        player.previous_was_strike_or_spare = None

                    #player.round_score += player.temp_score  # Modificar round_score
                    player.round_score_list_updater(pins_knocked_down)
                    player.score_list_updater(player.round_score + player.temp_score) # if player.current_round_throws == 2 else None
                    player.temp_score = 0
                    # Imprimir tabla de resultados
                    BowlingGame.score_dashboard(player)
                    BowlingGame.get_total_score(player)
                    print("\n")

            else:
                # Resetear Jugador y pasar a la siguiente ronda
                player.new_round_settings()





    @staticmethod
    def is_strike(player):
        player.temp_score += 10
        player.score_list_updater("X")
        player.round_score_list_updater("X")
        player.round_score_list_updater(" ")
        player.previous_was_strike_or_spare = "strike"
        player.add_throw()


    @staticmethod
    def is_spare(player):
        player.temp_score += 10
        player.score_list_updater("/")
        player.round_score_list_updater("/")
        player.previous_was_strike_or_spare = "spare"

    @staticmethod
    def bonus_strike(player):
        player.temp_score += 10
        player.score_list_updater("X")
        player.round_score_list_updater("X")
        player.previous_was_strike_or_spare = "strike"

    @staticmethod
    def bonus_spare(player):
        player.temp_score += 10
        player.score_list_updater("/")
        player.round_score_list_updater("/")
        player.previous_was_strike_or_spare = "spare"

    @staticmethod
    def score_dashboard(player):
        counter = 1
        print(f"{player.name}")
        print(""" Round 1 | Round 2 | Round 3 | Round 4 | Round 5 | Round 6 | Round 7 | Round 8 | Round 9 | Round10""")
        for i in player.round_score_list:
            i = str(i)
            if counter % 2 != 0:
                print(" " + i, end="   ")
            else:
                print(" " + i, end="  |")
            counter += 1

    @staticmethod
    def get_total_score(player):
        for number in player.score_list:
            number = str(number)
            if number.isdigit():
                player.total_score += int(number)
            else:
                continue
        print("\nTOTAL: {}".format(player.total_score))

