# -*- coding: cp1252 -*-

'''
Name: Tic Tac Toe
Other names: Noughts and Crosses, Xs and Os
Author: Clercio Guiliche
Special thanks to: Nicole Joaquim
Date: 25.11.2020
Date: 01.12.2020
'''

import random
    
T=[" "," "," "," "," "," "," "," "," "]

easy_level="Easy"
medium_level="Medium"
hard_level="Hard"

level=easy_level

player_mark="X"
computer_mark="O"

x_winner="--> You won!"
o_winner="--> You lost!"

wins=0
losses=0

def is_a_tie():
    for i in range(len(T)):
        if T[i]==" ":
            return False
    print("--> End of game!")
    print("--> No winners!")
    toString()
    return True

def free_indexes():
    indexes=[]
    for i in range(len(T)):
        if T[i]==" ":
            indexes.append(i)
    return indexes

'''
0 1 2
3 4 5
6 7 8
  '''    
def have_a_winner():
    global wins, losses
    matches=[[T[0],T[3],T[6]],[T[1],T[4],T[7]],[T[2],T[5],T[8]],
            [T[0],T[1],T[2]],[T[3],T[4],T[5]],[T[6],T[7],T[8]],
            [T[0],T[4],T[8]],[T[6],T[4],T[2]]]
    if(["X","X","X"] in matches):
        if player_mark=="X":
            wins=wins+1
        else:
            losses=losses+1
        print("--> End of game!")
        print(x_winner)
        return True;
    elif(["O","O","O"] in matches):
        if player_mark=="O":
            wins=wins+1
        else:
            losses=losses+1
        print("--> End of game!")
        print(o_winner)
        return True
    return False

def would_have_a_winner(index, mark):
    A=[]
    A=[T[i] for i in range(len(T))]
    A[index]=mark
    matches=[[A[0],A[3],A[6]],[A[1],A[4],A[7]],[A[2],A[5],A[8]],
            [A[0],A[1],A[2]],[A[3],A[4],A[5]],[A[6],A[7],A[8]],
            [A[0],A[4],A[8]],[A[6],A[4],A[2]]]
    if([mark,mark,mark] in matches):
        return True
    return False

def advantage(index, mark):
    A=[]
    A=[T[i] for i in range(len(T))]
    A[index]="W"
    advantage=0
    matches=[[A[0],A[3],A[6]],[A[1],A[4],A[7]],[A[2],A[5],A[8]],
            [A[0],A[1],A[2]],[A[3],A[4],A[5]],[A[6],A[7],A[8]],
            [A[0],A[4],A[8]],[A[6],A[4],A[2]]]
    for i in range(len(matches)):
        if((["W"," ",mark] == matches[i]) or
           (["W",mark," "] == matches[i]) or
           ([" ","W",mark] == matches[i]) or
           ([" ",mark,"W"] == matches[i]) or
           ([mark,"W"," "] == matches[i]) or
           ([mark," ","W"] == matches[i])):
            advantage=advantage+1
    return advantage

def best_advantage(mark):
    indexes=free_indexes()
    advant=[]
    for i in range(len(indexes)):
        advant.append(advantage(indexes[i],mark))
                    
    maior=0
    for i in range(len(indexes)):
        if maior<advant[i]:
            maior=advant[i]
            index=indexes[i]
    
    if maior==0:
        return -1
    
    indexes2=[]
    for i in range(len(indexes)):
        if maior==advant[i]:
            indexes2.append(indexes[i])

    return random.choice(indexes2)
    
def jogoEmCurso():
    return not (have_a_winner() or is_a_tie())

def toString():
    print ("")
    print ("Positions       Board")
    print ("|1|2|3|         " + "|"+T[0]+"|"+T[1]+"|"+T[2]+"|")
    print ("|4|5|6|         " + "|"+T[3]+"|"+T[4]+"|"+T[5]+"|")
    print ("|7|8|9|         " + "|"+T[6]+"|"+T[7]+"|"+T[8]+"|")

def player_move():
    position=eval(input("--> Your turn (1-9): "))
    index=position-1
    if position<1 or position>9:
        print ("--> Invalid position!")
        player_move();
    elif not T[index]==" ":
        print ("--> Taken position!")
        player_move();
    else:
        T[index]=player_mark

def computer_move():
    index=computer_move_1()
    
    if level==easy_level:
        indexes=free_indexes()
        for i in range(len(indexes)//2):
            indexes.append(index)
        index=random.choice(indexes)
        
    elif level==medium_level:
        indexes=free_indexes()
        for i in range(len(indexes)):
            indexes.append(index)
        index=random.choice(indexes)
        
    T[index]=computer_mark
    print ("--> Computer turn: "+str(index+1))

def computer_move_3():
    index=random.choice(free_indexes())
    return index
    
def computer_move_2():
    index=best_advantage(computer_mark)
    
    if index==-1:
        index=best_advantage(player_mark)
        if index==-1:
            return computer_move_3()

    return index

def computer_move_1():
    indexes=free_indexes();

    for i in range(len(indexes)):
        if would_have_a_winner(indexes[i],computer_mark):
            return indexes[i]
    
    for i in range(len(indexes)):
        if would_have_a_winner(indexes[i],player_mark):
            return indexes[i]
    
    return computer_move_2()

print ("")
print ("Welcome to the Tic Tac Toe game!")
print ("(Also known as noughts and crosses or Xs and Os)")
print ("")
print ("By Clercio Guiliche (2020).")
print ("Special thanks to Nicole Joaquim.")

def menu():

    print ("")
    print ("*. The RULES are simple:")
    print ("1. Each player uses oly one mark (X or O).")
    print ("2. Players switch turns, marking a free position each time.")
    print ("3. Any free position from 1 to 9 can be marked.")
    print ("4. The first player to match three marks in a row wins!")
    print ("5. The game can end with no winners too.")

    global T
    T=[" "," "," "," "," "," "," "," "," "]
    
    print ("")
    global level
    choice=eval(input("Choose a level [1-Easy | 2-Medium | 3-Hard]: "))
    if(choice==3):
        level=hard_level
    elif(choice==2):
        level=medium_level
    else:
        level=easy_level
    print ("--> Level: "+level)

    print ("")
    global player_mark
    global computer_mark
    global x_winner
    global o_winner
    if(eval(input("Choose a mark [1-X | 2-O]: "))==1):
        player_mark="X"
        computer_mark="O"
        x_winner="--> You won!"
        o_winner="--> You lost!"
    else:
        player_mark="O"
        computer_mark="X"
        x_winner="--> You lost!"
        o_winner="--> You won!"
    print ("--> Mark: "+player_mark)
    print ("")

    import random
    toString()
    users_turn=random.choice([True,False])
    while jogoEmCurso():
        if(users_turn):
            player_move()
            users_turn=False
        else:
            computer_move()
            users_turn=True
        toString()
    else:
        print ("")
        print ("--> You: "+str(wins)+" x "+str(losses)+" :Computer")
        print ("")
        if(eval(input("Play again? [1-Yes | 2-No]: "))==1):
            menu()
        else:
            print("Come back soon!")

menu()
