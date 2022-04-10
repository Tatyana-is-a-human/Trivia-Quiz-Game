from tkinter import *
from quiz_brain import QuizBrain
import html

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quizBrain:QuizBrain):

        self.quiz=quizBrain

        self.window=Tk()
        self.window.title("Quizzler")
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)

        self.score=0
        self.total=0
        self.scorebox=Label(text=f"Score: {self.score} / {self.total}", bg=THEME_COLOR, fg="White")

        self.canvas=Canvas(height=250, width=300)
        self.questionHolder = self.canvas.create_text(150, 125,
                                                      text="lorem ipsi",
                                                      font=("Arial", 15, "italic"),
                                                      fill=THEME_COLOR,
                                                      width=280)

        check_img=PhotoImage(file=".\images\\true.png")
        self.check=Button(self.window, image=check_img, command=self.check_right)

        ex_img=PhotoImage(file=".\images\\false.png")
        self.ex=Button(self.window, image=ex_img, command=self.check_wrong)

        self.scorebox.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.check.grid(row=2, column=0)
        self.ex.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):

        self.scorebox.config(text=f"Score: {self.score} / {self.total}")
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():

            q_text = html.unescape(self.quiz.next_question())
            self.canvas.itemconfig(self.questionHolder, text=q_text)
            self.total += 1

        else:
            self.canvas.itemconfig(self.questionHolder, text="Quiz completed")
            self.ex.state="disabled"
            self.check.state="disabled"




    def check_wrong(self):
        is_right=self.quiz.check_answer("false")
        self.give_feedback(is_right)

        self.get_next_question()

    def check_right(self):
        is_right=self.quiz.check_answer("true")

        self.give_feedback(is_right)


    def give_feedback(self, is_right):

        if is_right==True:
            self.canvas.config(bg="green")
            self.score+=1

        else:
            self.canvas.config(bg="red")
           S
        self.window.after(1000, self.get_next_question)