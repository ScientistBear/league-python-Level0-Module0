from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block 
if __name__ == '__main__':
    window = Tk()

    window.withdraw()

    name = simpledialog.askstring(title='Greeter', prompt="What is your name?")

    # Show a message box with your message using the .showinfo() method
    messagebox.showinfo()
    # Print your message to the console using the print() function
    print()
    # Show an error message using messagebox.showerror()
    for i in range(100):
        messagebox.showerror()
    # Run the window's .mainloop() method
    window.mainloop()
    pass
