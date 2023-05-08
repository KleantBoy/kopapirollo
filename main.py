import tkinter as tk
import random
from PIL import Image, ImageTk


def player_choice(choice):
    global player_score, computer_score, result_label, player_choice_label, computer_choice_label

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    
    if (choice == 'rock' and computer_choice == 'scissors') or \
            (choice == 'paper' and computer_choice == 'rock') or \
            (choice == 'scissors' and computer_choice == 'paper'):
        player_score += 1
        result_label.config(text="Nyertél! Játékos: {}, Gép: {}".format(player_score, computer_score))
    elif choice == computer_choice:
        result_label.config(text="Döntetlen! Játékos: {}, Gép: {}".format(player_score, computer_score))
    else:
        computer_score += 1
        result_label.config(text="Vesztettél! Játékos: {}, Gép: {}".format(player_score, computer_score))

    player_choice_image = Image.open(f"images/{choice}.png").resize((150, 150))
    player_choice_photo = ImageTk.PhotoImage(player_choice_image)
    player_choice_label.config(image=player_choice_photo)
    player_choice_label.image = player_choice_photo

    computer_choice_image = Image.open(f"images/{computer_choice}.png").resize((150, 150))
    computer_choice_photo = ImageTk.PhotoImage(computer_choice_image)
    computer_choice_label.config(image=computer_choice_photo)
    computer_choice_label.image = computer_choice_photo


player_score = 0
computer_score = 0


window = tk.Tk()
window.title("Kő-papír-olló játék")

window.geometry("700x500")
window.configure(bg="#8DDBE0")


rock_button = tk.Button(window, text="Kő", font=("Arial", 20), fg="#2B2D42", bg="#E4E4E4", bd=0, padx=30, pady=20,
                        command=lambda: player_choice('rock'))
rock_button.place(x=50, y=300)

paper_button = tk.Button(window, text="Papír", font=("Arial", 20), fg="#2B2D42", bg="#E4E4E4", bd=0, padx=30, pady=20,
                         command=lambda: player_choice('paper'))
paper_button.place(x=250, y=300)

scissors_button = tk.Button(window, text="Olló", font=("Arial", 20), fg="#2B2D42", bg="#E4E4E4", bd=0, padx=30,
                            pady=20, command=lambda: player_choice('scissors'))
scissors_button.place(x=450, y=300)


player_choice_label = tk.Label(window)
player_choice_label.place(x=150, y=100)

computer_choice_label = tk.Label(window)
computer_choice_label.place(x=400, y=100)


result_label = tk.Label(window, text="Játékos: {}, Gép: {}".format(player_score, computer_score),
                        font=("Arial", 24), fg="#2B2D42", bg="#8DDBE0")
result_label.place(x=200, y=30)

window.mainloop()
