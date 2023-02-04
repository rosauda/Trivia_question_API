from tkinter import *
from quiz_brain import QuizBrain


# ---------------------------- CONSTANTS ------------------------------- #

THEME_COLOR = "#375362"
WINDOW_TITLE = "Trivia"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain ):

        # Creating window
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title(WINDOW_TITLE)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(width=200, height=200)

        # Creating Canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="Some question will be displayed here",
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Labels
        self.score = Label(text=f"Score: {self.quiz.score}", fg="White", bg=THEME_COLOR, font=("Ariel", 12, "bold"))
        self.score.grid(row=0, column=1)

        # Buttons
        false_png = PhotoImage(file="false.png")
        self.button_wrong = Button(image=false_png, highlightthickness=0, bg=THEME_COLOR) #, command=next_word
        self.button_wrong.grid(row=3, column=0)

        true_png = PhotoImage(file="true.png")
        button_right = Button(image=true_png, highlightthickness=0, bg=THEME_COLOR) #, command=is_known
        button_right.grid(row=3, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)





