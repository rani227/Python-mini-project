from tkinter import *
from PIL import ImageTk, Image
import random

def show_rules():
    rules_window = Toplevel(main)
    rules_window.title("Game Rules")
    rules_window.geometry("1000x500")
    ruleswindow_width = rules_window.winfo_screenwidth()
    ruleswindow_height = rules_window.winfo_screenheight()
    img = Image.open("bg_intro.jpg")
    img = img.resize((ruleswindow_width, ruleswindow_height))
    img = ImageTk.PhotoImage(img)

    bg_label = Label(rules_window, image=img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    rules_text = '''
    Rules:
    1. There are three stages of the game: Easy, Moderate, and Difficult.
    2. There will be five questions per stage.
    3. The time limit is 30s/question for easy, 45s/question for moderate, and 60s/question for difficult.
    4. For each correct answer, the points are allotted as: Easy-100, Moderate-300, Difficult-500.
    5. To move to the next question, you must choose the correct answer to the current question.
    6. If the option chosen is incorrect, you will lose the game and your score will become 0.
    7. If you are not sure about the answer, you may quit the game without losing your score.
    '''

    rules_label = Label(rules_window, text=rules_text, font=("Arial", 14, "bold"), justify="left", bg="#5a798c", fg="white")
    rules_label.place(x=200, y=150)
    
    rules_window.mainloop()


def start_game_2():
    global bg_image_2

    root_2 = Toplevel(main)
    root_2.title("KBC")
    root_2.geometry("1000x600")
    window_width_2 = root_2.winfo_screenwidth()
    window_height_2 = root_2.winfo_screenheight()
    bg_image_2 = Image.open("bg_questions.jpg")
    bg_image_2 = bg_image_2.resize((window_width_2, window_height_2))
    bg_image_2 = ImageTk.PhotoImage(bg_image_2)

    bg_label_2 = Label(root_2, image=bg_image_2)
    bg_label_2.place(x=0, y=0, relwidth=1, relheight=1)

    hard_2 = open('hard.txt', 'r').readlines()
    hard_answers_2 = open('hardanswers.txt', 'r').readlines()
    hard_answers_2 = [i.strip() for i in hard_answers_2]
    hard_options_2 = open('hardoptions.txt', 'r').readlines()
    hard_options_2 = [str.strip().split(';') for str in hard_options_2]


    window_width_2 = root_2.winfo_screenwidth()
    window_height_2 = root_2.winfo_screenheight()
    root_2.geometry(f"{window_width_2}x{window_height_2}")
    bg_image_2 = Image.open("bg_questions.jpg")
    bg_image_2 = bg_image_2.resize((window_width_2, window_height_2))
    bg_image_2 = ImageTk.PhotoImage(bg_image_2)

    bg_label_2 = Label(root_2, image=bg_image_2)
    bg_label_2.place(x=0, y=0, relwidth=1, relheight=1)

    randomno_2 = random.sample(range(0, 9), 5)
    
    question_number_2 = 0
    score_2 = 0


    def check_answer_2(answer):
        nonlocal question_number_2, score_2
        if answer == hard_answers_2[randomno_2[question_number_2]]:
            score_2 += 500
        question_number_2 += 1
        if question_number_2 < len(randomno_2):
            show_question_2()
        else:
            show_result_2()


    def show_question_2():
        question_label_2.config(text=hard_2[randomno_2[question_number_2]], bg='#062844', fg="white",
                                font=("Arial", 15, "bold"), highlightbackground="white", highlightcolor="white",
                                highlightthickness=2)
        question_label_2.place(relx=0.5, rely=0.45, anchor='center')
        option_btn1_2.config(text=hard_options_2[randomno_2[question_number_2]][0], bg='#C3FEFF', width=30, height=2,
                             font=("Arial", 15, "bold"),
                             command=lambda: check_answer_2(hard_options_2[randomno_2[question_number_2]][0]))
        option_btn1_2.place(relx=0.60, rely=0.55)
        option_btn2_2.config(text=hard_options_2[randomno_2[question_number_2]][1], bg='#C3FEFF', width=30, height=2,
                             font=("Arial", 15, "bold"),
                             command=lambda: check_answer_2(hard_options_2[randomno_2[question_number_2]][1]))
        option_btn2_2.place(relx=0.10, rely=0.55)
        option_btn3_2.config(text=hard_options_2[randomno_2[question_number_2]][2], bg='#C3FEFF', width=30, height=2,
                             font=("Arial", 15, "bold"),
                             command=lambda: check_answer_2(hard_options_2[randomno_2[question_number_2]][2]))
        option_btn3_2.place(relx=0.60, rely=0.70)
        option_btn4_2.config(text=hard_options_2[randomno_2[question_number_2]][3], bg='#C3FEFF', width=30, height=2,
                             font=("Arial", 15, "bold"),
                             command=lambda: check_answer_2(hard_options_2[randomno_2[question_number_2]][3]))
        option_btn4_2.place(relx=0.10, rely=0.70)


    def show_result_2():
        question_label_2.config(text="Your score is: " + str(score_2))
        option_btn1_2.config(text="")
        option_btn2_2.config(text="")
        option_btn3_2.config(text="")
        option_btn4_2.config(text="")
        result_btn_2 = Button(root_2, text='Exit', command=exit)
        result_btn_2.place(relx=0.5, rely=0.55, anchor='center')
        


    center_y_2 = window_height_2 // 2
    question_label_2 = Label(root_2, text="", wraplength=300, width=window_width_2, height=5, fg="white",
                             font=("Arial", 20, "bold"))

    question_label_2.pack()

    option_btn1_2 = Button(root_2, text="")
    option_btn1_2.pack()

    option_btn2_2 = Button(root_2, text="")
    option_btn2_2.pack()

    option_btn3_2 = Button(root_2, text="")
    option_btn3_2.pack()

    option_btn4_2 = Button(root_2, text="")
    option_btn4_2.pack()

    show_question_2()
    


def start_game_1():
    global bg_image
    
    root_1 = Toplevel(main)
    root_1.title("KBC")
    root_1.geometry("1000x600")
    window_width = root_1.winfo_screenwidth()
    window_height = root_1.winfo_screenheight()
    bg_image = Image.open("bg_questions.jpg")
    bg_image = bg_image.resize((window_width, window_height))
    bg_image = ImageTk.PhotoImage(bg_image)
    medium_1 = open('medium.txt', 'r').readlines()
    medium_answers_1 = open('mediumanswers.txt', 'r').readlines()
    medium_answers_1 = [i.strip() for i in medium_answers_1]
    medium_options_1 = open('mediumoptions.txt', 'r').readlines()
    medium_options_1 = [str.strip().split(';') for str in medium_options_1]
    window_width_1 = root_1.winfo_screenwidth()
    window_height_1 = root_1.winfo_screenheight()
    root_1.geometry(f"{window_width_1}x{window_height_1}")

    root_1.title("KBC")  # Set title on the root window

    bg_label_1 = Label(root_1, image=bg_image)  # Place bg_label_1 on root window
    bg_label_1.place(x=0, y=0, relwidth=1, relheight=1)

    def close_root1():
        root_1.destroy()

    def new_window():
        close_root1()
        start_game_2()

    randomno_1 = random.sample(range(0, 9), 5)
    question_number_1 = 0
    score_1 = 0

    def check_answer_1(answer):
        nonlocal question_number_1, score_1
        if answer == medium_answers_1[randomno_1[question_number_1]]:
            score_1 += 300
        question_number_1 += 1
        if question_number_1 < len(randomno_1):
            show_question_1()
        else:
            show_result_1()
    
    def show_question_1():
        question_label_1.config(text=medium_1[randomno_1[question_number_1]], bg='#062844', fg="white", font=("Arial", 15, "bold"), highlightbackground="white", highlightcolor="white", highlightthickness=2)
        question_label_1.place(relx=0.5, rely=0.45, anchor='center')
        option_btn1_1.config(text=medium_options_1[randomno_1[question_number_1]][0], bg='#C3FEFF', width=30, height=2, font=("Arial", 15, "bold"), command=lambda: check_answer_1(medium_options_1[randomno_1[question_number_1]][0]))
        option_btn1_1.place(relx=0.60, rely=0.55)
        option_btn2_1.config(text=medium_options_1[randomno_1[question_number_1]][1], bg='#C3FEFF', width=30, height=2, font=("Arial", 15, "bold"), command=lambda: check_answer_1(medium_options_1[randomno_1[question_number_1]][1]))
        option_btn2_1.place(relx=0.10, rely=0.55)
        option_btn3_1.config(text=medium_options_1[randomno_1[question_number_1]][2], bg='#C3FEFF', width=30, height=2, font=("Arial", 15, "bold"), command=lambda: check_answer_1(medium_options_1[randomno_1[question_number_1]][2]))
        option_btn3_1.place(relx=0.60, rely=0.70)
        option_btn4_1.config(text=medium_options_1[randomno_1[question_number_1]][3], bg='#C3FEFF', width=30, height=2, font=("Arial", 15, "bold"), command=lambda: check_answer_1(medium_options_1[randomno_1[question_number_1]][3]))
        option_btn4_1.place(relx=0.10, rely=0.70)

        
    
    def show_result_1():
        question_label_1.config(text="Your score is: " + str(score_1))
        option_btn1_1.config(text="")
        option_btn2_1.config(text="")
        option_btn3_1.config(text="")
        option_btn4_1.config(text="")
        result_btn_2 = Button(root_1, text='Next', command=new_window)
        result_btn_2.place(relx=0.5, rely=0.55, anchor='center')
    center_y_1 = window_height_1 // 2
    question_label_1 = Label(root_1, text="", wraplength=300, width=window_width_1, height=5, fg="white", font=("Arial", 20, "bold"))
    question_label_1.pack()
    
    option_btn1_1 = Button(root_1, text="")
    option_btn1_1.pack()
    
    option_btn2_1 = Button(root_1, text="")
    option_btn2_1.pack()
    
    option_btn3_1 = Button(root_1, text="")
    option_btn3_1.pack()
    
    option_btn4_1 = Button(root_1, text="")
    option_btn4_1.pack()
    
    show_question_1()
    

def start_game():
    global bg_image
    
    root = Toplevel(main)
    root.title("KBC")
    root.geometry("1000x600")
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    bg_image = Image.open("bg_questions.jpg")
    bg_image = bg_image.resize((window_width, window_height))
    bg_image = ImageTk.PhotoImage(bg_image)
    
    bg_label = Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    easy=open('easy.txt','r').readlines()
    easyanswers=open('easyanswers.txt','r').readlines()
    easyanswers=[i.strip() for i in easyanswers]
    easyoptions=open('easyoptions.txt','r').readlines()
    easyoption=[str.strip().split(';') for str in easyoptions]
   
    
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    root.geometry(f"{window_width}x{window_height}")
    bg_image = Image.open("bg_questions.jpg")
    bg_image = bg_image.resize((window_width, window_height))
    bg_image = ImageTk.PhotoImage(bg_image)
    
    bg_label = Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def close_root():
        root.destroy()

    def new_window():
        close_root()
        start_game_1()
    
    root.title("KBC")
    randomno=random.sample(range(0,9),5)
    
    question_number = 0
    score = 0
    def check_answer(answer):
        nonlocal question_number, score
        if answer == easyanswers[randomno[question_number]]:
            score += 100
        question_number += 1
        if question_number < len(randomno):
            show_question()
        else:
            show_result()
    
    def show_question():
        question_label.config(text=easy[randomno[question_number]],bg='#062844', fg="white", font=("Arial", 15, "bold"),highlightbackground="white",highlightcolor="white",highlightthickness=2)
        question_label.place(relx=0.5,rely=0.45,anchor='center')
        option_btn1.config(text=easyoption[randomno[question_number]][0],bg='#C3FEFF',width=30,height=2,font=("Arial", 15, "bold"),command=lambda: check_answer(easyoption[randomno[question_number]][0]))
        option_btn1.place(relx=0.60, rely=0.55)
        option_btn2.config(text=easyoption[randomno[question_number]][1],bg='#C3FEFF',width=30,height=2,font=("Arial", 15, "bold"),command=lambda: check_answer(easyoption[randomno[question_number]][1]))
        option_btn2.place(relx=0.10, rely=0.55)
        option_btn3.config(text=easyoption[randomno[question_number]][2], bg='#C3FEFF',width=30,height=2,font=("Arial", 15, "bold"),command=lambda: check_answer(easyoption[randomno[question_number]][2]))
        option_btn3.place(relx=0.60, rely=0.70)
        option_btn4.config(text=easyoption[randomno[question_number]][3], bg='#C3FEFF',width=30,height=2,font=("Arial", 15, "bold"),command=lambda: check_answer(easyoption[randomno[question_number]][3]))
        option_btn4.place(relx=0.10, rely=0.70)
    
    def show_result():
        question_label.config(text="Your score is: " + str(score) )
        option_btn1.config(text="")
        option_btn2.config(text="")
        option_btn3.config(text="")
        option_btn4.config(text="")
        result_btn = Button(root, text='Next', command=new_window)
        result_btn.place(relx=0.5, rely=0.55, anchor='center')
    center_y=window_height//2
    question_label = Label(root, text="", wraplength=300,width=window_width,height=5,fg="white",font=("Arial", 20, "bold"))
    
    
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


button_frame = Frame(main)
button_frame.pack(pady=50)


play_button = Button(main, text="PLAY", font=("Comic Sans MS", 24, "bold"), bg="#44868D", fg="white", command=start_game)
play_button.config(width=10, height=0)
play_button.place(x=window_width1//2, y=window_height1//2-25, anchor='center')


rules_button = Button(main, text="RULES", font=("Comic Sans MS", 24, "bold"), bg="#626F71", fg="white", command=show_rules)
rules_button.config(width=10, height=0)
rules_button.place(x=window_width1//2, y=window_height1//2+100, anchor='center')

main.mainloop()