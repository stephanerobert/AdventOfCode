class Move:
    def check_position(self):
        location = '%s_%s' % (self.x, self.y)
        if location in self.coord:
            self.been_there = True
        else:
            self.coord[location] = True

    def nord(self, distance):
        self.y = self.y + distance
        self.check_position()

        self.R = self.est
        self.L = self.ouest

    def sud(self, distance):
        self.y = self.y - distance
        self.check_position()

        self.L = self.est
        self.R = self.ouest

    def est(self, distance):
        self.x = self.x + distance
        self.check_position()

        self.R = self.sud
        self.L = self.nord

    def ouest(self, distance):
        self.x = self.x - distance
        self.check_position()

        self.R = self.nord
        self.L = self.sud

    def __init__(self):
        self.coord = {'0_0': True}
        self.x = 0
        self.y = 0
        self.R = self.est
        self.L = self.ouest
        self.been_there = False

def main():
    move = Move()
    l = 'L3, R2, L5, R1, L1, L2, L2, R1, R5, R1, L1, L2, R2, R4, L4, L3, L3, R5, L1, R3, L5, L2, R4, L5, R4, R2, L2, L1, R1, L3, L3, R2, R1, L4, L1, L1, R4, R5, R1, L2, L1, R188, R4, L3, R54, L4, R4, R74, R2, L4, R185, R1, R3, R5, L2, L3, R1, L1, L3, R3, R2, L3, L4, R1, L3, L5, L2, R2, L1, R2, R1, L4, R5, R4, L5, L5, L4, R5, R4, L5, L3, R4, R1, L5, L4, L3, R5, L5, L2, L4, R4, R4, R2, L1, L3, L2, R5, R4, L5, R1, R2, R5, L2, R4, R5, L2, L3, R3, L4, R3, L2, R1, R4, L5, R1, L5, L3, R4, L2, L2, L5, L5, R5, R2, L5, R1, L3, L2, L2, R3, L3, L4, R2, R3, L1, R2, L5, L3, R4, L4, R4, R3, L3, R1, L3, R5, L5, R1, R5, R3, L1'
    #import pdb;pdb.set_trace()
    for i in l.split(', '):
        if i[0] is 'R':
            move.R(int(i[1:]))
        if i[0] is 'L':
            move.L(int(i[1:]))
        if move.been_there:
            print(move.coord)
            break

if __name__ == "__main__":
    main()

    print(move.x, move.y)
    print('distance', abs(move.x)+abs(move.y))

def test_distance_2():
    l="R8, R4, R4, R8"

