import time
import random

start = time.time()


def brutus():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    guess = ''
    holder = ''
    i = 0
    print(alphabet)
    solution = input("What word/sentence would you like to test: ")
    while guess != solution:
        holder = random.choice(alphabet)
        if holder != solution[i]:
            alphabet.remove(holder)
            print(guess + holder)
        else:
            alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            guess = guess + holder
            print(guess)
            i = i+1
            time.sleep(0.2)
    return guess


brutus()
print('---------------')
print("End of program")

end = time.time()
elapsedtime = end - start

print("Time elapsed: " + str(round(elapsedtime, 2)), "Seconds")
