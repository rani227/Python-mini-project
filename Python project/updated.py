from tkinter import *
from PIL import ImageTk, Image


def show_rules():
    rules_window = Toplevel(main)
    rules_window.title("Game Rules")
    rules_window.geometry("1000x500")
    ruleswindow_width = rules_window.winfo_screenwidth()
    ruleswindow_height = rules_window.winfo_screenheight()
    img=Image.open("bg_intro.jpg")
    img=img.resize((ruleswindow_width,ruleswindow_height))
    img = ImageTk.PhotoImage(img)

    bg_label = Label(rules_window, image=img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    rules_label = Label(rules_window, text='''Rules:\n
    1. There are three stages of the game: Easy, Moderate, and Difficult.\n
    2. There will be five questions per stage.\n
    3. The time limit is 30s/question for easy, 45s/question for moderate, and 60s/question for difficult.\n
    4. For each correct answer, the points are allotted as: Easy-100, Moderate-300, Difficult-500.\n
    5. To move to the next question, you must choose the correct answer to the current question.\n
    6. If the option chosen is incorrect, you will lose the game and your score will become 0.\n
    7. If you are not sure about the answer, you may quit the game without losing your score.''')

    rules_label.config(font=("Arial",14,"bold"), justify="left", bg="#5a798c", fg="white")

    rules_label.place(x=200,y=150)
    
    rules_window.mainloop()


def start_game():
    global bg_image
    
    root = Toplevel(main)
    easy = open('easy.txt', 'r').readlines()
    easyanswers = open('easyanswers.txt', 'r').readlines()
    easyanswers = [i.strip() for i in easyanswers]
    easyoptions = open('easyoptions.txt', 'r').readlines()
    easyoption = [str.strip().split(';') for str in easyoptions]

    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    root.geometry(f"{window_width}x{window_height}")
    bg_image = Image.open("bg_questions.jpg")
    bg_image = bg_image.resize((window_width, window_height))
    bg_image = ImageTk.PhotoImage(bg_image)

    bg_label = Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    root.title("Geeky Trivia")
    question_number = 0
    score = 0

    def check_answer(answer):
        nonlocal question_number, score
        if answer == easyanswers[question_number]:
            score += 1
        question_number += 1
        if question_number < len(easy):
            show_question()
        else:
            show_result()                               

    def show_question():
        question_label.config(text=easy[question_number], bg='#062844', fg="white", font=("Arial", 15, "bold"),highlightbackground="white",highlightcolor="white",highlightthickness=2)
        question_label.place(relx=0.5, rely=0.4, anchor='center')
        option_btn1.config(text=easyoption[question_number][0], bg='#C3FEFF', command=lambda: check_answer(easyoption[question_number][0]), width=30,height=2,font=("Arial", 15, "bold"))
        option_btn1.place(relx=0.60, rely=0.55)
        option_btn2.config(text=easyoption[question_number][1], bg='#C3FEFF', command=lambda: check_answer(easyoption[question_number][1]), width=30,height=2,font=("Arial", 15, "bold"))
        option_btn2.place(relx=0.10, rely=0.55)
        option_btn3.config(text=easyoption[question_number][2], bg='#C3FEFF', command=lambda: check_answer(easyoption[question_number][2]), width=30,height=2,font=("Arial", 15, "bold"))
        option_btn3.place(relx=0.60, rely=0.70)
        option_btn4.config(text=easyoption[question_number][3], bg='#C3FEFF', command=lambda: check_answer(easyoption[question_number][3]), width=30,height=2,font=("Arial", 15, "bold"))
        option_btn4.place(relx=0.10, rely=0.70)

    def show_result():
        question_label.config(text="Your score is: " + str(score) + "/" + str(len(easy)))
        option_btn1.config(text="")
        option_btn2.config(text="")
        option_btn3.config(text="")
        option_btn4.config(text="")

    center_y = window_height // 2
    question_label = Label(root, text="", wraplength=300, width=window_width, height=5)
    question_label.pack()

    option_btn1 = Button(root, text="")
    option_btn1.pack()

    option_btn2 = Button(root, text="")
    option_btn2.pack()

    option_btn3 = Button(root, text="")
    option_btn3.pack()

    option_btn4 = Button(root, text="")
    option_btn4.pack()

    show_question()


# Create the main window
main = Tk()
main.title("Main Window")
main.geometry("1525x900")
window_width1 = main.winfo_screenwidth()
window_height1 = main.winfo_screenheight()
bg_image1 = Image.open("bg_int1.jpg")
bg_image1 = bg_image1.resize((window_width1, window_height1))
bg_image1 = ImageTk.PhotoImage(bg_image1)

bg_label1 = Label(main, image=bg_image1)
bg_label1.place(x=0, y=0, relwidth=1, relheight=1)



# Create a frame to hold the buttons
button_frame = Frame(main)
button_frame.pack(pady=50)

# Create a play button

play_button = Button(main, text="PLAY", font=("Comic Sans MS", 24,"bold"), bg="#44868D", fg="white", command=start_game)
play_button.config(width=10, height=0)
play_button.place(x=window_width1//2, y=window_height1//2-25, anchor='center')

# Create a rules button
rules_button = Button(main, text="RULES", font=("Comic Sans MS", 24,"bold"), bg="#626F71", fg="white", command=show_rules)
rules_button.config(width=10, height=0)
rules_button.place(x=window_width1//2, y=window_height1//2+100, anchor='center')
#626F71
main.mainloop()
