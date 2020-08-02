
class Menu:
    def ui_input(self):
        a = input('Enter the coordinates: ')
        self.mark(a)

    def __init__(self):
        self.state = 'X'
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.qqq = [[(1, 3), (2, 3), (3, 3)], [(1, 2), (2, 2), (3, 2)], [(1, 1), (2, 1), (3, 1)]]
        self.init_print()

    def init_print(self):
        print('---------')
        for i in self.board:
            print('| {} |'.format(' '.join(i)))
        print('---------')
        return self.ui_input()

    def check(self):
        #  check for lines
        match = []
        filter_ = list(filter(lambda x: len(set(x)) == 1, self.board))
        if len(filter_) != 0 and filter_[0] != [' ', ' ', ' ']:
            match.append(filter_[0])
        #  check for columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                match.append(self.board[0][i])
        #  check for diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            match.append(self.board[0][0])
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            match.append(self.board[0][2])
        #  searching for white spaces in all board without looping
        val_list = self.board[0] + self.board[1] + self.board[2]
        if len(match) == 0 and ' ' in val_list:
            return self.ui_input()
        elif len(match) == 0 and ' ' not in val_list:
            print('Draw')
            return None
        elif len(match) == 1:
            print('{} wins'.format(match[0]))
            return None

    def mark(self, coord):
        if coord.count(' ') == 1:
            x, y = coord.split()
            if x.isdigit() and y.isdigit():
                x, y = int(x), int(y)
                if x in range(1, 4) and y in range(1, 4):
                    for i in range(3):
                        if (x, y) in self.qqq[i]:
                            if self.board[i][self.qqq[i].index((x, y))] == ' ':
                                if self.state == 'X':
                                    self.board[i][self.qqq[i].index((x, y))] = 'X'
                                    self.state = 'O'
                                elif self.state == 'O':
                                    self.board[i][self.qqq[i].index((x, y))] = 'O'
                                    self.state = 'X'
                                print('---------')
                                for j in self.board:
                                    print('| {} |'.format(' '.join(j)))
                                print('---------')
                                return self.check()
                            else:
                                print('This cell is occupied! Choose another one!')
                else:
                    print('Coordinates should be from 1 to 3!')
            else:
                print('You should enter numbers!')
        else:
            print("The coordinates must be 2 and separated by space(' ')")    
        return self.ui_input()


tic = Menu()
