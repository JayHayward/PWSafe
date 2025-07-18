# Jay Hayward 2025
# Class implementation


import PWSafe as pws
import tkinter as tk

class my_app(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('400x200')
        self.title('PWSafe')
        
        self.name_var = tk.StringVar()
        self.key_var = tk.StringVar()

        name_label = tk.Label(self, text = 'Username', font = ('calibre', 10, 'bold'))
        name_input = tk.Entry(self, textvariable = self.name_var, font = ('calibre', 10))

        key_label = tk.Label(self, text = 'Key', font = ('calibre', 10, 'bold'))
        key_input = tk.Entry(self, textvariable = self.key_var, font = ('calibre', 10))

        submit_button = tk.Button(self, text = 'Submit', command = self.submit)
        exit_button = tk.Button(self, text = 'EXIT', command = self.destroy)
        # open_new_window_button = tk.Button(self, text = 'new_window', command = self.open_new_window)

        box_spacing = tk.Label(self, text = '\n')


        self.username_label_var = tk.StringVar()
        self.key_label_var = tk.StringVar()

        self.username_label_var.set('hello:')
        self.key_label_var.set('world:')
        self.print_username = tk.Label(self, textvariable=self.username_label_var, font=('calibre', 10, 'bold'))
        self.print_key = tk.Label(self, textvariable=self.key_label_var, font = ('calibre', 10, 'bold'))


        name_label.grid(row = 0, column = 0)
        name_input.grid(row = 0, column = 1)
        key_label.grid(row = 1, column = 0)
        key_input.grid(row = 1,column = 1)
        submit_button.grid(row = 2, column = 1)
        exit_button.grid(row = 3, column = 1)
        box_spacing.grid(row = 4, column = 1)
        self.print_username.grid(row = 5, column = 0)
        self.print_key.grid(row = 6, column = 0)
        # open_new_window_button.grid(row = 4, column = 1)

    def submit(self):
        name = self.name_var.get()
        keyword = self.key_var.get()
        
        # print the given input back out to text box
        # self.username_label_var.set(f'hello: {name}')
        # self.key_label_var.set(f'world: {keyword}')

        print(f'Username : {name}')
        print(f'keyword: {keyword}')

        self.pws_handling(name, keyword)  # collect the input to pass to backend

        self.name_var.set('')
        self.key_var.set('')

    # def open_new_window(self):
    #     new_window = tk.Toplevel(self)
    #     new_window.title('secondary window')

    def pws_handling(self, plaintext, keyword):
        get_pws_rule = pws.create_rule(keyword)
        print(f'rule: {get_pws_rule}')
        print(f'plain: {plaintext}\tkeyword: {keyword}')

        ciphertext = pws.generate_ciphertext(plaintext, get_pws_rule)
        print(f'ciphertext: {ciphertext}')

        self.username_label_var.set(f'hello: {plaintext}')  
        self.key_label_var.set(f'world: {ciphertext}')

        return()


if __name__ == '__main__':
    app_instance = my_app()
    app_instance.mainloop()