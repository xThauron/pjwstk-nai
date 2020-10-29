# Źródło: https://www.codingame.com/ide/puzzle/winamax-battle
# Autor: Jakub Pilachowski (s17999)

from queue import Queue 

def getValueOfCard(card):
    if len(card) == 3:
        return 10
    else:
        num = card[0]
        if num == "J":
            return 11
        elif num == "Q":
            return 12
        elif num == "K":
            return 13
        elif num == "A":
            return 14
        else:
            return int(num)

def war(deck1, deck2):
    warQueue1 = Queue()
    warQueue2 = Queue()
    c1 = deck1.get()
    c2 = deck2.get()
    warQueue1.put(c1)
    warQueue2.put(c2)
    while c1 == c2 and not deck1.empty() and not deck2.empty():
        for i in range(3):
            warQueue1.put(deck1.get())
            warQueue2.put(deck2.get())
            if deck1.empty() or deck2.empty():
                return False
        c1 = deck1.get()
        c2 = deck2.get()
        warQueue1.put(c1)
        warQueue2.put(c2)
    
    while not warQueue1.empty():
        if c1 > c2:
            deck1.put(warQueue1.get())
        else:
            deck2.put(warQueue1.get())

    while not warQueue2.empty():
        if c1 > c2:
            deck1.put(warQueue2.get())
        else:
            deck2.put(warQueue2.get())
    return True

n = int(input()) 
deck1 = Queue()
for i in range(n):
    cardp_1 = input() 
    deck1.put(getValueOfCard(cardp_1))
m = int(input()) 
deck2 = Queue()
for i in range(m):
    cardp_2 = input() 
    deck2.put(getValueOfCard(cardp_2))

pat = False
round = 0
while not deck1.empty() and not deck2.empty():
    round = round + 1
    if not war(deck1, deck2):
        pat = True
        break
    
if pat or (deck1.empty() and deck2.empty()):
    print("PAT")
elif deck1.empty():
    print(2, round)
else:
    print(1, round)
