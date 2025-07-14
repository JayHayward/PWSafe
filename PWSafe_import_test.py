# Class implementation


import tkinter as tk

class my_app(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('400x200')

        self.title('PWSafe')
        
        self.name_var = tk.StringVar()
        self.pw_var = tk.StringVar()

        name_label = tk.Label(self, text = 'Username', font = ('calibre', 10, 'bold'))
        name_input = tk.Entry(self, textvariable = self.name_var, font = ('calibre', 10))

        pw_label = tk.Label(self, text = 'Password', font = ('calibre', 10, 'bold'))
        pw_input = tk.Entry(self, textvariable = self.pw_var, font = ('calibre', 10))

        submit_button = tk.Button(self, text = 'Submit', command = self.submit)
        exit_button = tk.Button(self, text = 'EXIT', command = self.destroy)
        # open_new_window_button = tk.Button(self, text = 'new_window', command = self.open_new_window)

        box_spacing = tk.Label(self, text = '\n')

        name_label.grid(row = 0, column = 0)
        name_input.grid(row = 0, column = 1)
        pw_label.grid(row = 1, column = 0)
        pw_input.grid(row = 1,column = 1)
        submit_button.grid(row = 2, column = 1)
        exit_button.grid(row = 3, column = 1)
        box_spacing.grid(row = 4, column = 1)
        # open_new_window_button.grid(row = 4, column = 1)

    def submit(self):
        name = self.name_var.get()
        password = self.pw_var.get()
        
        print(f'Username : {name}')
        print(f'Password: {password}')

        self.name_var.set('')
        self.pw_var.set('')

    # def open_new_window(self):
    #     new_window = tk.Toplevel(self)
    #     new_window.title('secondary window')



if __name__ == '__main__':
    app_instance = my_app()
    app_instance.mainloop()