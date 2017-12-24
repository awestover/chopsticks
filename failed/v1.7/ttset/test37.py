from tkinter import *
import threading

root = Tk()
root.wm_state('zoomed')
# no buttons
root.overrideredirect(1)
root.resizable(0,0)

def task():
    print("hello")
    root.after(2000, task)  # reschedule event in 2 seconds

    def callback():
        i = input("what is your purpose in living?")
        if i == "quit":
            root.quit()
        if i == "1":
            pic("testImage.png")
        if i == "2":
            pic("BoxesSimulation.png")

    t = threading.Thread(target=callback)
    t.start()


def pic(file):
    photo = PhotoImage(file=file)
    photo_label = Label(image=photo)
    photo_label.grid()
    photo_label.image = photo


root.after(2000, task)
root.mainloop()
