class GameEntry:
    total_player = 0
    def __init__(self, name, score, timeg):
        self.name = name
        self.score = score
        self.timeg = timeg

        GameEntry.total_player += 1

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def set_time(self, timeg):
        self.timeg = timeg

    def get_time(self):
        return self.timeg
    
    def getTotal():
        return GameEntry.total_player

class ScoreBoard:
    def __init__(self, capacity):
        self.capacity = capacity
        self.board = [None] * self.capacity
        # [None, None, None, None, ...]
        self.n = 0
        
    def getCapacity(self):
        return self.capacity

    def sumEntries(self):
        return self.n

    def addItem(self, game_entry):
        score = game_entry.get_score()

        good = len(self.board) > self.n or score > self.board[self.capacity - 1].get_score()

        if good:
            if self.n < self.capacity:
                self.n = self.n + 1 # self.n += 1

            j = self.n - 1

            while j > 0 and self.board[j-1].get_score() < score:
                self.board[j] = self.board[j-1]
                j -= 1
            self.board[j] = game_entry
            print(f"Entry ditambahkan")

    def listEntries(self):
        for i in range (0, self.n):
            print(i+1,":", getattr(self.board[i], 'name'), getattr(self.board[i], 'score'))
        

#rina_score = GameEntry("Rina", 89, 4)
#rina_score2 = GameEntry("Rina", 89, 4)
#rina_score3 = GameEntry("Rina", 79, 4)

score_board = ScoreBoard(10)
#score_board.addItem(rina_score)
#score_board.addItem(rina_score2)
#score_board.addItem(rina_score3)

active = True

while active:
    print("")
    print("""Menu:
    1. Tambah Entry Baru
    2. Tampilkan List Score Board
    3. Keluar""")
    start = input("Pilih Menu = ")
    print("")
    if start == '2':
        score_board.listEntries()
    elif start == '1':
        name = input("Masukan nama pemain : ")
        skor = int(input("Masukan skor        : "))
        waktu = int(input("Masukan waktu       : "))

        in_score = GameEntry(name, skor, waktu)
        set_board = score_board.addItem(in_score)
        print(f"Entri baru ditambahkan: {in_score.get_name()} {in_score.get_score()} {in_score.get_time()}")
    else:
        break
