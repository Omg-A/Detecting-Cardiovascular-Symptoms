from tkinter import *
from tkinter import messagebox as tkmb

root = Tk()
root.title("Detecting Cardiovascular Symptoms")
root.geometry("600x700")

question1 = StringVar(value = "0")
label_question1 = Label(root, text="Do you experience shortness of breath during routine activities??")
label_question1.pack()
question1_radio1 = Radiobutton(root, text="Yes", variable=question1, value="yes")
question1_radio1.pack()
question1_radio2 = Radiobutton(root, text="No", variable=question1, value="no")
question1_radio2.pack()


question2 = StringVar(value = "0")
label_question2 = Label(root, text="Do you experience shortness of breath while at rest/lying down?")
label_question2.pack()
question2_radio1 = Radiobutton(root, text="Yes", variable=question2, value="yes")
question2_radio1.pack()
question2_radio2 = Radiobutton(root, text="No", variable=question2, value="no")
question2_radio2.pack()

question3 = StringVar(value = "0")
label_question3 = Label(root, text="Do you feel short of breath while lying flat and feel the need to stack multiple pillows to sleep well?")
label_question3.pack()
question3_radio1 = Radiobutton(root, text="Yes", variable=question3, value="yes")
question3_radio1.pack()
question3_radio2 = Radiobutton(root, text="No", variable=question3, value="no")
question3_radio2.pack()

question4 = StringVar(value = "0")
label_question4 = Label(root, text="Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?")
label_question4.pack()
question4_radio1 = Radiobutton(root, text="Yes", variable=question4, value="yes")
question4_radio1.pack()
question4_radio2 = Radiobutton(root, text="No", variable=question4, value="no")
question4_radio2.pack()

question5 = StringVar(value = "0")
label_question5 = Label(root, text="Do you have swelling in the feet/ ankles/legs (shoes feel tighter) or abdomen?")
label_question5.pack()
question5_radio1 = Radiobutton(root, text="Yes", variable=question5, value="yes")
question5_radio1.pack()
question5_radio2 = Radiobutton(root, text="No", variable=question5, value="no")
question5_radio2.pack()

question6 = StringVar(value = "0")
label_question6 = Label(root, text="Do you feel tired while doing routine activities such as shopping, climbing stairs, carrying groceries or walking?")
label_question6.pack()
question6_radio1 = Radiobutton(root, text="Yes", variable=question6, value="yes")
question6_radio1.pack()
question6_radio2 = Radiobutton(root, text="No", variable=question6, value="no")
question6_radio2.pack()

question7 = StringVar(value = "0")
label_question7 = Label(root, text="Have you experienced loss of appetite (frequent feeling of being full) or nausea recently?")
label_question7.pack()
question7_radio1 = Radiobutton(root, text="Yes", variable=question7, value="yes")
question7_radio1.pack()
question7_radio2 = Radiobutton(root, text="No", variable=question7, value="no")
question7_radio2.pack()

question8 = StringVar(value = "0")
label_question8 = Label(root, text="Do you feel any of these symptoms - confusion, disorientation or loss of memory?")
label_question8.pack()
question8_radio1 = Radiobutton(root, text="Yes", variable=question8, value="yes")
question8_radio1.pack()
question8_radio2 = Radiobutton(root, text="No", variable=question8, value="no")
question8_radio2.pack()

question9 = StringVar(value = "0")
label_question9 = Label(root, text="Do you often feel that you are having a racing heartbeat and experience palpitations?")
label_question9.pack()
question9_radio1 = Radiobutton(root, text="Yes", variable=question9, value="yes")
question9_radio1.pack()
question9_radio2 = Radiobutton(root, text="No", variable=question9, value="no")
question9_radio2.pack()

def check():
    score = 0
    
    if question1.get() == "yes":
        score = score + 20
        print(score)
    if question2.get() == "yes":
        score = score + 20
        print(score)
    if question3.get() == "yes":
        score = score + 20
        print(score)
    
    if score <= 20:
        tkmb.showinfo("Report", "You don't need to visit a doctor")
    elif score > 20 and score <= 40:
        tkmb.showinfo("Report", "You might perhaps have to visit a doctor")
    else:
        tkmb.showinfo("Report", "You have to visit a doctor")

btn_check = Button(root, text="Done", command = check)
btn_check.pack()

root.mainloop()