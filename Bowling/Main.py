from BowlingGame import BowlingGame


def main():
    bowling_game = BowlingGame()

    # Crear jugadores y anadirlos a una lista de jugadores
    number_of_players = int(input("¿Cuántos jugadores participarán? "))
    for i in range(number_of_players):
        player_name = input("Introduzca el nombre del jugador: ")
        bowling_game.add_player(player_name)

    while bowling_game.players_list[-1].round <= 10:
        bowling_game.play()
    else:
        print("Juego finalizado. Este es el marcador final:\n")
        for player in bowling_game.players_list:
            bowling_game.score_dashboard(player)
            bowling_game.get_total_score(player)


if __name__ == "__main__":
    main()