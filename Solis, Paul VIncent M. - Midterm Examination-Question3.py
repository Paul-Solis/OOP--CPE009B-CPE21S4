from tkinter import *

class MyWindow:
    
    def __init__(self, window):
        # Set window title and size
        window.title("Midterm Exam in OOP")
        window.geometry("400x300+10+10")
        
        # Label for fullname input
        self.fullname_label = Label(window, fg="red", text="Enter your fullname:")
        self.fullname_label.place(x=20, y=100)
        
        # Entry for fullname input
        self.fullname_entry = Entry(window, bd=2)
        self.fullname_entry.place(x=220, y=100)
        
        # Button to display fullname
        self.display_button = Button(window, fg="red", text="Click to display your Fullname", command=self.display_fullname)
        self.display_button.place(x=20, y=150)
        
        # Entry to display the fullname
        self.result_entry = Entry(window, bd=2)
        self.result_entry.place(x=220, y=150)
        
    def display_fullname(self):
        # Clear the result entry and insert the fullname from the input entry
        self.result_entry.delete(0, "end")
        self.result_entry.insert(END, self.fullname_entry.get())

# Create the main window
if __name__ == "__main__":
    root = Tk()
    app = MyWindow(root)
    root.mainloop()
