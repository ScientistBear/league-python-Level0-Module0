from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(10):
        # 4. Ask the user for a guess using a pop-up window, and save their response
        guess = simpledialog.askinteger(title='guess',prompt='pick a number 1 through 100')
        # 5. If the guess is correct
            # 6. Win. Use 'sys.exit(0)' to end the program
        if guess == random_num:
            messagebox.showinfo(title='win',message='you won')
            sys.exit(0)
        # 7. if the guess is high
            # 8. Tell them it's too high
        if guess > random_num:
            messagebox.showinfo(title='too high',message='your guess was too high')
        # 9. Else if the guess is low
            # 10. Tell them it's too low
        else:
            messagebox.showinfo(title='too low',message='your guess was too low')
    #11. Outside of the loop, tell the user they lost
    messagebox.showinfo(message='you lost')

    window.mainloop()
