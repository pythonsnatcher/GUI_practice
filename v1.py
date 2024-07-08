import tkinter as tk
from tkinter import messagebox


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.menu_bar = tk.Menu(self.root)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='Close', command=self.on_closing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Close without question', command=exit)

        self.action_menu = tk.Menu(tearoff=0)
        self.action_menu.add_command(label='Show Message', command=self.show_message)

        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.menu_bar.add_cascade(label='Action', menu=self.action_menu)

        self.root.config(menu=self.menu_bar)

        self.label = tk.Label(self.root, text="Hello Tuco bear!", font=("Arial", 24))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, )
        self.textbox.bind('<KeyPress>',self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar(value=1)

        self.check = tk.Checkbutton(self.root, text='Show Messagebox', font=('Arial', 12), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Show Message', font=('Arial', 12), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clear_button = tk.Button(self.root, text ='Claer', font=('Arial', 12), command=self.clear)
        self.clear_button.pack(padx=10, pady=10)

        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo('Message', message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        print(event.state,event.keysym)

        if event.state == 4 and event.keysym == 'Return':
            self.show_message()
        elif event.state == 4 and event.keysym == 'BackSpace':
            self.clear()
        elif event.state == 4 and event.keysym == 'Escape':
            self.root.destroy()

    def on_closing(self):
        if messagebox.askyesno('Exit', 'Are you sure you want to exit?'):
            self.label.config(text='Window closed')
            self.root.after(1000, self.root.destroy)  # Wait 1 second before destroying the window

    def clear(self):
        self.textbox.delete('1.0', tk.END)

MyGUI()

