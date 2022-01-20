n=18
i=1
print("wlecome!...to guess the no. game")
while i<=9:
    s=int(input("guess the no."))
    if s<18:
        print("leaser")
    elif s>18:
        print("greater")
    else:
        print("correct guess!..you won!!")
        print(i,"you took guesses to complete")
        break
    print(9-i,"no.of guesse left")
    i=i+1
if i>9:
    print("your game is over")