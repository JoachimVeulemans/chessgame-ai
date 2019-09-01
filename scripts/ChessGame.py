class ChessGame:
    def __init__(self, event="", site="", date="", round="", white="", black="",
                 white_elo="", black_elo="", eco="", moves=[], result=""):
        self.event = event
        self.site = site
        self.date = date
        self.round = round
        self.white = white
        self.black = black
        self.white_elo = white_elo
        self.black_elo = black_elo
        self.eco = eco
        self.moves = moves
        self.result = result

    def __iter__(self):
        return iter([self.event, self.site, self.date, self.round, self.white, self.black, self.white_elo, self.black_elo, self.eco, self.moves, self.result])

    def __str__(self):
        return "Event: " + self.event + ", Site: " + self.site + ", Date: " + self.date + ", Round: " + self.round + \
            ", White: " + self.white + ", Black: " + self.black + ", White Elo: " + self.white_elo + ", Black Elo: " + \
            self.black_elo + ", ECO: " + self.eco + ", Result: " + self.result

    def __repr__(self):
        return repr(self.__str__())
