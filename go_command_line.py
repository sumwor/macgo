# -*- coding: utf-8 -*-
#import copy


__metaclass__ = type
class CrossPoint:

    def __init__(self, color, pos):
        self.color = color
        #self.qi = 0
        self.value = "·"
        #color refers to the current condition of a CrossPoint
        #0: empty  1: black stone   2: white stone
        #qi is a slogan of Go. when one stone's qi goes to 0, the stone dies.
        self.pos = pos

    def set_point(self):
        """print the crosspoint"""
        star_list = [ ["D", '16'], ["K", '16'], ["Q", '16'],
                      ["D", '10'], ["K", '10'], ["Q", '10'],
                      ["D", '4'], ["K", '4'], ["Q", '4'] ]
        if self.color == 0 and self.pos not in star_list:
            self.value = "·"
        elif self.color == 0 and self.pos in star_list:
            self.value = "+"
        elif self.color == 1:
            self.value = "●"
        else:
            self.value =  "○"




class Game:

    global char_list
    char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L',
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

    def __init__(self):



        self.stage = 0   #stage refers to current condition of the game  0: white loose  1: black loose
        self.board = [ [CrossPoint(0, ['', '']) for i in range(19)] for j in range(19) ] # define the go board
        for i in range(19):
            for j in range(19):
                self.board[i][j].pos = [char_list[j], str(19-i)]
                #print 19-i
                #print self.board[i][j].pos
                self.board[i][j].set_point()
                #print self.board[i][j].value
        self.number_of_move = 0


    def count(self):
        """this method is designed to decide who wins"""
        pass

    def print_board(self):
        """print the board after every move"""
        char1 = "   "
        for i in range(19):
            char1 += char_list[i] + " "
        char1 += "  "
        print char1
        num = 0
        for x in self.board:
            if num < 10:
                char = str(19 - num) + " "
            else:
                char = str(19 - num) + "  "
            for y in x:
                char = char + y.value + " "
                #print y, y.pos
                #print self.board[m][n].value, self.board[m][n].pos
            print char + str(19 - num)
            num += 1
        print char1
        #print self.board[3][3].value

    def move(self):
        move_pos = ""
        #print "if you want to stop, type 0"
        if self.number_of_move % 2 == 0:
            move_pos = raw_input("black" + "(" + str(self.number_of_move + 1) + "):")
            char = "●"
            color = 1
        else:
            move_pos = raw_input("white" + "(" + str(self.number_of_move + 1) + "):")
            char = "○"
            color = 2
        #print "move_pos", move_pos
        input_list = list(move_pos)
        #print "input_list", input_list
        #print input_list, input_list[0], input_list[2]

        #print input_list, input_list[0], input_list[2]

        if (input_list[0] in char_list and input_list[1] == " " and input_list[2]):
            if len(input_list) == 4 and input_list[3]:
                input_list[2] = input_list[2] + input_list[3]
            move_position = [input_list[0], input_list[2]]
            #print "move position", move_position
            if self.board[19 - int(move_position[1])][char_list.index(move_position[0])].color != 0:
                print "illegal move, the position has been possessed!"
                self.move()
            else:
                self.board[19 - int(move_position[1])][char_list.index(move_position[0])].value = char
                self.board[19 - int(move_position[1])][char_list.index(move_position[0])].color = color

                self.number_of_move += 1
        else:
            print "illegal move, please enter again"
            self.move()

    def find_block(self, color, crosspoint):

        """color refers to the color of the stones, 1:black, 2:white
           actually this function also determine the very block is alive or not
        """

        #find stone blocks, crosspoint is the start position
        x, y = crosspoint.pos

        #print "x, y",  x, y

        #initiate four neighbering crosspoint
        if y == "19":
            up = None
        else:
            up = self.board[18 - int(y)][char_list.index(x)]
        if y == "1":
            down = None
        else:
            down = self.board[20 - int(y)][char_list.index(x)]
        if x == "A":
            left = None
        else:
            left = self.board[19 - int(y)][char_list.index(x) - 1]
        if x == "T":
            right = None
        else:
            right = self.board[19 - int(y)][char_list.index(x) + 1]


        #print "up", up.pos
        #print "down", down.pos
        #print "left", left.pos
        #print "right", right.pos

        #print "up.color", up.color
        #print "down.color", down.color
        #print "right.color", right.color
        #print "left.color", left.color

        area = [crosspoint, crosspoint] # the extra point functs to prevent the loop from stop in the first loop
        area_record = [crosspoint]   #area_record contains the whole block
        area_pos = [crosspoint.pos]

        if (up.color == 0 or down.color == 0 or right.color == 0 or left.color == 0) and up.color != color and down.color != color and right.color != color and left.color != color:
            not_surrounded = True
            return area_record, not_surrounded
        #elif up.color == 2 and down.color == 2 and right.color == 2 and left.color == 2:
        #    not_surrounded = False
        #    return area_record, not_surrounded
        else:
            not_surrounded = False              # if all the elements in is_surrounded is true, the block is dead
            while (up.color == color and (up not in area_record)) or (down.color == color and (down not in area_record)) or (right.color == color and (right not in area_record)) or (left.color == color and (left not in area_record)):
                for cross in area:
                    #print "now working on: ", cross.pos
                    if cross.pos[1] == "19":
                        up = None
                    else:
                        up = self.board[18 - int(cross.pos[1])][char_list.index(cross.pos[0])]
                    #print "in the loop up", up.pos, up.color
                    if up.color == color and (up not in area_record) and (up != None):
                        area.append(up)
                        area_record.append(up)
                        area_pos.append(up.pos)
                    elif up.color == 0:
                        not_surrounded += True


                    if cross.pos[1] == "1":
                        down = None
                    else:
                        down = self.board[20 - int(cross.pos[1])][char_list.index(cross.pos[0])]
                    #print "down", down.pos, down.color
                    if down.color == color and (down not in area_record) and (down != None):
                        area.append(down)
                        area_record.append(down)
                        area_pos.append(down.pos)
                    elif down.color == 0:
                        not_surrounded += True
                    if cross.pos[0] == "T":
                        right = None
                    else:
                        right = self.board[19 - int(cross.pos[1])][char_list.index(cross.pos[0]) + 1]
                    print "right", right.pos, right.color
                    if right.color == color and (right not in area_record) and (right != None):
                        area.append(right)
                        area_record.append(right)
                        area_pos.append(right.pos)
                    elif right.color == 0:
                        not_surrounded += True

                    if cross.pos[0] == "A":
                        left = None
                    else:
                        left = self.board[19 - int(cross.pos[1])][char_list.index(cross.pos[0]) - 1]
                    print "left", left.pos, left.color
                    if left.color == color and (left not in area_record) and (left != None):
                        area.append(left)
                        area_record.append(left)
                        area_pos.append(left.pos)
                    elif left.color == 0:
                        not_surrounded += True

                    #print "area", area
                    area.remove(cross)
                    #print "area after deletion", area

            return area_record, not_surrounded

    def is_alive(self, color):
        for row in self.board:
            for cross in row:
                #print "now the point is", cross.pos
                #print self.find_block(1, cross)
                if cross.color != 0:
                    block, not_surrounded = self.find_block(color, cross)
                    print block, not_surrounded
                    if not_surrounded == False:
                        for point in block:
                            point.color = 0
                            point.value = "·"
"""
    def is_white_alive(self):
        for row in self.board:
            for cross in row:
                if cross.color == 2:
                    print "not the point is",cross.pos
                    print self.find_block(1, cross)

"""





x = Game()
#print x.board
#print x.board[3][3].value, x.board[3][3].pos
x.print_board()
#print len(x.board)
#print len(x.board)
for i in range(30):
    x.move()
    x.print_board()
    x.is_alive(1)
    x.is_alive(2)
