from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UserInterface: 
 
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width= 300, height=300, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        self.question_text = self.canvas.create_text(150,150,width=280, text="Question", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        
        wrong = PhotoImage(file=r"C:\Users\FANARA\OneDrive - Pfizer\Desktop\Python\Intermediate+\Day34\images\false.png") 
        correct = PhotoImage(file=r"C:\Users\FANARA\OneDrive - Pfizer\Desktop\Python\Intermediate+\Day34\images\true.png")
        
        self.true_button = Button(image=correct, highlightthickness=0, command=self.right_answer)
        self.false_button = Button(image=wrong, highlightthickness=0,command=self.wrong_answer)
        
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()

        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
            self.score_label.config(text=f"score: {self.quiz.score}")
        else: 
            self.canvas.itemconfig(self.question_text, text = "You answered to all the questions")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")
            
    def wrong_answer(self):
        self.answer = "false"
        is_right = self.quiz.check_answer(self.answer)
        self.give_feedback(is_right)
        self.score_label.config(text=f"Score:{self.score}")
        self.canvas.config(bg="red")
        self.get_next_question()
        
    def right_answer(self):
        self.answer = "true"
        is_right = self.quiz.check_answer(self.answer)
        self.give_feedback(is_right)
        self.score_label.config(text=f"Score:{self.score}/10")
        self.get_next_question()
        
    def give_feedback(self, is_right):
        if is_right:
           self.canvas.config(bg="green") 
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
       