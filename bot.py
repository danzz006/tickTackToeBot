''' Bot logic implemented here '''


class Bot:

    def __init__(self):
        self.played = []

    def assess_choices(self, choices):
        x = choices


        for i in choices:
            if i not in self.played:
                self.played.append(i)

        print(self.played)


        win_move = self.is_winning(x)

        pattern_move = self.pattern_finding(x)

        if pattern_move:
            print('pattern move', pattern_move)
            return pattern_move

        if win_move:
            print('move = ', win_move)
            return win_move
       
        # print(self.played)


       

        # for y in range(1,10):
        #     if y in x:
        #         if (y+1) in x:
        #             if y-1 >= 1 and y-1 not in self.played:
        #                 self.played.append(y-1)
        #                 return y-1
        #             elif y+2 <= 9 and y+2 not in self.played:
        #                 self.played.append(y+2)
        #                 return y+2



        if 4 in x:
            if 5 in x:
                if 6 not in self.played:
                    self.played.append(6)
                    print('1')
                    return 6

        


        if 7 in x:
            if 8 in x:
                if 9 not in self.played:
                    self.played.append(9)
                    print('2')
                    return 9
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

        if 9 in x:
            if 7 in x:
                if 8 not in self.played:
                    self.played.append(8)
                    print('3')
                    return 8
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1
                                    
                    
        if 1 in x:
            if 4 in x:
                if 7 not in self.played:
                    self.played.append(7)
                    print('4')
                    return 7
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

        if 1 in x:
            if 7 in x:
                if 4 not in self.played:
                    self.played.append(4)
                    print('5')
                    return 4
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1
        if 4 in x:
            if 1 in x:
                if 7 not in self.played:
                    self.played.append(7)
                    print('6')
                    return 7
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1
        
        if 4 in x:
            if 7 in x:
                if 1 not in self.played:
                    self.played.append(1)
                    print('7')
                    return 1
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

        if 7 in x:
            if 1 in x:
                if 4 not in self.played:
                    self.played.append(4)
                    print('8')
                    return 4
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

        if 7 in x:
            if 4 in x:
                if 1 not in self.played:
                    self.played.append(1)
                    print('9')
                    return 1
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

        if 2 in x:
            if 5 in x:
                if 8 not in self.played:
                    self.played.append(8)
                    print('10')
                    return 8
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

        if 2 in x:
            if 8 in x:
                if 5 not in self.played:
                    self.played.append(5)
                    print('11')
                    return 5
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1
        
        if 8 in x:
            if 2 in x:
                if 5 not in self.played:
                        self.played.append(5)
                        print('12')
                        return 5
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

        if 8 in x:
            if 5 in x:
                if 2 not in self.played:
                    self.played.append(2)
                    print('13')
                    return 2
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

        if 5 in x:
            if 8 in x:
                if 2 not in self.played:
                    self.played.append(2)
                    print('14')
                    return 2
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

        if 5 in x:
            if 2 in x:
                if 8 not in self.played:
                    self.played.append(8)
                    print('15')
                    return 8
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1
        
        if 3 in x:
            if 6 in x:
                if 9 not in self.played:
                    self.played.append(9)
                    print('16')
                    return 9
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

        if 3 in x:
            if 9 in x:
                if 6 not in self.played:
                    self.played.append(6)
                    print('17')
                    return 6
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

        if 6 in x:
            if 3 in x:
                if 9 not in self.played:
                    self.played.append(9)
                    print('18')
                    return 9
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

        if 6 in x:
            if 9 in x:
                if 3 not in self.played:
                    self.played.append(3)
                    print('19')
                    return 3
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

        if 9 in x:
            if 3 in x:
                if 6 not in self.played:
                    self.played.append(6)
                    print('20')
                    return 6
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

        if 9 in x:
            if 6 in x:
                if 3 not in self.played:
                    self.played.append(3)
                    print('21')
                    return 3
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

        


        


        if 1 in x:
            if 5 in x:
                # print(x)
                if 9 not in x:
                    # print('t')
                # if 9 in self.played:
                #     self.played.remove(9)
                    if 9 not in self.played:
                        self.played.append(9)
                        print('22')
                        return 9
                    # else:
                    #     if 7 in x:
                    #         print('t')
                    #         if 5 in x:
                    #             print('t')
                    #             if 3 not in self.played:
                    #                 self.played.append(3)
                    #                 return 3
                    #             else:
                    #                 last = x[-1]
                    #                 if last-1 >= 1 and last-1 not in self.played:
                    #                     self.played.append(last-1)
                    #                     return last-1
                                    
                    #                 if last+1 <= 9 and last+1 not in self.played:
                    #                     self.played.append(last+1)
                    #                     return last+1
                    # last = x[-1]
                    # if last-1 >= 1 and last-1 not in self.played:
                    #     self.played.append(last-1)
                    #     return last-1

                    # if last+1 <= 9 and last+1 not in self.played:
                    #     self.played.append(last+1)
                    #     return last+1
                    

        if 1 in x:
            if 9 in x:
                if 5 not in self.played:
                    self.played.append(5)
                    print('23')
                    return 5
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

                #     if last+1 <= 9 and last+1 not in self.played:
                #         self.played.append(last+1)
                #         return last+1
                    
        if 5 in x:
            if 1 in x:
                if 9 not in self.played:
                    self.played.append(9)
                    print('24')
                    return 9
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

                #     if last+1 <= 9 and last+1 not in self.played:
                #         self.played.append(last+1)
                #         return last+1
                    

        if 5 in x:
            if 9 in x:
                if 1 not in self.played:
                    self.played.append(1)
                    print('25')
                    return 1
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

                #     if last+1 <= 9 and last+1 not in self.played:
                #         self.played.append(last+1)
                #         return last+1
                    

        if 9 in x:
            if 1 in x:
                if 5 not in self.played:
                    self.played.append(5)
                    print('26')
                    return 5
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

                #     if last+1 <= 9 and last+1 not in self.played:
                #         self.played.append(last+1)
                #         return last+1
                    

        if 9 in x:
            if 5 in x:
                if 1 not in self.played:
                    self.played.append(1)
                    print('27')
                    return 1
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

                #     if last+1 <= 9 and last+1 not in self.played:
                #         self.played.append(last+1)
                #         return last+1
                    

        if 3 in x:
            if 5 in x:
                # if 7 in self.played:
                #     self.played.remove(7)
                if 7 not in x:
                    if 7 not in self.played:
                        self.played.append(7)
                        print('28')
                        return 7
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1
                #     if last+1 <= 9 and last+1 not in self.played:
                #         self.played.append(last+1)
                #         return last+1
                    

        if 3 in x:
            if 7 in x:
                if 5 not in self.played:
                    self.played.append(5)
                    print('29')
                    return 5
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

                #     if last+1 <= 9 and last+1 not in self.played:
                #         self.played.append(last+1)
                #         return last+1
                    

        if 5 in x:
            if 3 in x:
                if 7 not in self.played:
                    self.played.append(7)
                    print('30')
                    return 7
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

                #     if last+1 <= 9 and last+1 not in self.played:
                #         self.played.append(last+1)
                #         return last+1
                    

        if 5 in x:
            if 7 in x:
                if 3 not in self.played:
                    self.played.append(3)
                    print('31')
                    return 3
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

                #     if last+1 <= 9 and last+1 not in self.played:
                #         self.played.append(last+1)
                #         return last+1
                    

        if 7 in x:
            if 3 in x:
                if 5 not in self.played:
                    self.played.append(5)
                    print('32')
                    return 5
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1

                #     if last+1 <= 9 and last+1 not in self.played:
                #         self.played.append(last+1)
                #         return last+1
                    

        
        if 7 in x:
            if 5 in x:
                if 3 not in self.played:
                    self.played.append(3)
                    print('33')
                    return 3
                # else:
                #     last = x[-1]
                #     if last-1 >= 1 and last-1 not in self.played:
                #         self.played.append(last-1)
                #         return last-1
                    
                #     if last+1 <= 9 and last+1 not in self.played:
                #         self.played.append(last+1)
                #         return last+1
                    

        # if win_move:
        #     print('move = ', win_move)
        #     return win_move


        if 5 not in x and 5 not in self.played:
            self.played.append(5)
            print('34')
            return 5

        for y in range(1,10):
            if y in x:
                if (y+1) in x:
                    if y-1 >= 1 and y-1 not in self.played:
                        self.played.append(y-1)
                        print('35')
                        return y-1
                    elif y+2 <= 9 and y+2 not in self.played:
                        self.played.append(y+2)
                        print('36')
                        return y+2


        if len(x) <= 1:
            if 5 in x:
                self.played.append(1)
                print('37')
                return 1
        
        # if 5 not in x and 5 not in self.played:
        #     self.played.append(5)
        #     return 5

        else:
            last = x[-1]
            
            if last-1 not in self.played and last-1 >= 1:
                self.played.append(last-1)
                print('38')
                return last-1

            if last+1 not in self.played:
                self.played.append(last+1)
                print('39')
                return last+1
            
            for i in range(1,10):
                if i not in x:
                    if i not in self.played:
                        self.played.append(i)
                        print('40')
                        return i


            
        


    def reset_bot(self):
        self.played.clear()



    def is_winning(self, choices):

        print(choices)

         # horizontal
        winsA = [1,2,3]
        winsB = [4,5,6]
        winsC = [7,8,9]
        # vertical
        winsD = [1,4,7]
        winsE = [2,5,8]
        winsF = [3,6,9]
        # diagonals
        winsG = [1,5,9]
        winsH = [3,5,7]

        wins = [winsA, winsB, winsC, winsD, winsE, winsF, winsG, winsH]


        # if len(choices) == 3:
        #     for i in range(len(wins)):
        #         for j in range(len(wins[i])):
        #             if wins[i][j] in self.played:
        #                 if wins[i][j] not in choices:
        #                     if j == 0:
        #                         # for k in wins[i]:
        #                         #     if k not in self.played:
        #                         if wins[i][-1] not in choices:
        #                             self.played.append(wins[i][-1])
        #                             return wins[i][-1]

        count = 0
        compared = []

        for x in range(len(wins)):
            for val in wins[x]:
                if val in self.played:
                    if val not in choices:
                        if val not in compared:
                            compared.append(val)
                            if compared[0] in wins[x]:
                                count += 1
                            # if count == 3:
                            #     count = 0
                            else:
                                compared.clear()
                                count = 0
                            if count >= 2:
                                for y in wins[x]:
                                    if y not in self.played:
                                        self.played.append(y)
                                        count = 0
                                        return y
                                    # else:
                                    #     count = 0
                    
                        else:
                            compared.clear()
                            count = 0

                    
                    # else:
                    #     count += 1


        

    def pattern_finding(self, choices):

        o_moves = []

        for item in self.played:
            if item not in choices:
                o_moves.append(item)

        patterns = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

        missing = 0

        for i in range(len(o_moves)):
            for sett in patterns:
                for x in sett:
                    if o_moves[i] == x:
                        for y in o_moves:
                            if y != o_moves[i]:
                                if y in sett:
                                    missing = sett


        
        if missing:
            print('\n', missing)

            for i in missing:
                if i not in o_moves:
                    if i not in self.played:
                        return i


             
