import random
top_rng = input("Enter a number you want to guess between: ")
try:
    top_rng = int(top_rng)
except:
    print("Please enter a number!\nThank you.")
    quit()
if top_rng <= 0:
    print("Please enter a positive nonzero value!")
    quit()

comp_guess = random.randrange(top_rng)
print(comp_guess)

while True:
    your_guess = input("Choose a number between your top range: ")
    try:
        your_guess = int(your_guess)
        if comp_guess == your_guess:
            print("Yeah.....Your guess is correct.")
            break
        else:
            print("Try again.\nBetter luck next time! ")
    except:
        print("Please enter a number!")
        break


#print("Thank you")
