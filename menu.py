import subprocess

from tkinter import *
from tkinter import messagebox
from n_euclidean_ray1 import *
from n_euclidean_ray2 import *

colors = ["#CBBDF0", "#2B2933", "#42317A"]

root = Tk()
root.title('Non-Euclidean Environment With Ray Casting (Python)')
root.geometry("800x260")
root.resizable(False, False)
root.configure(bg=colors[0])


# Frame
frame = Frame(root, bg=colors[0])
frame.pack()

# Main Function
def exec_main(number):
    if number == 1:
        try:
            main = "./n_euclidean_ray1/main.py"
            resultado = subprocess.run(["python", main], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            messagebox.showerror(title='Error', message='Unable to run first program')
    else:
        try:
            main = "./n_euclidean_ray2/main.py"
            resultado = subprocess.run(["python", main], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            messagebox.showerror(title='Error', message='Unable to run second program')

# Labels Config
label1 = Label(frame,text="Non-Euclidean Environment in a Ray Casting World (Python)", font="Times 22", fg=colors[1], bg=colors[0])
credits_label_one = Label(frame,text="Made by Luan de Souza Ferreira Marques", font="Times 15", fg=colors[1], bg=colors[0])
credits_label_two = Label(frame,text="Github: https://github.com/LuanSFMarques", font="Times 15", fg=colors[1], bg=colors[0])

# Button Config
main1_button = Button(frame, text="First-Person Only",command = lambda: exec_main(1), bg=colors[2], font="Times 20", fg=colors[0], relief='sunken')
main2_button = Button(frame, text="Debug View Mode",command = lambda: exec_main(2), bg=colors[2], font="Times 20", fg=colors[0], relief='sunken')

# Labels Display
label1.grid(row=0,column=0,columnspan=2, pady=28)
credits_label_one.grid(row=2,column=0, columnspan=2, pady=(30,0))
credits_label_two.grid(row=3,column=0, columnspan=2)

# Button Display
main1_button.grid(row=1,column=0, sticky=EW)
main2_button.grid(row=1,column=1, sticky=EW)

root.mainloop()
