## Set up a test box for input

import tkinter as tk

# Default empty box
def default_box():
    root = tk.Tk()
    w = tk.Label(root, text='bingus')
    w.pack()
    root.mainloop()


# Padded box with buttons
def button_box():
    root = tk.Tk()
    root.geometry('250x170')

    label1 = tk.Label(root, text = 'Label 1')
    label1.pack(side = tk.TOP, pady = 10)

    button1 = tk.Button(root, text='Button 1')
    button1.pack(side = tk.LEFT , padx = 20)

    button2 = tk.Button(root, text = 'Button 2')
    button2.pack(side = tk.RIGHT, padx = 20)

    root.mainloop()


# Box for text
def text_box():
    root = tk.Tk()
    root.geometry('250x170')

    L = tk.Label(root, text = 'Here is some text')
    my_text = 'lorem impsum dolor'
    L.config(font =("Courier", 14))

    T = tk.Text(root, height = 5, width = 50)

    B1 = tk.Button(root, text = 'KEKW')
    B2 = tk.Button(root, text = 'EXIT', command = root.destroy)

    L.pack()
    T.pack()
    B1.pack(side = tk.LEFT, padx = 20)
    B2.pack(side = tk.RIGHT, padx = 20)

    T.insert(tk.END, my_text)

    root.mainloop()


# box for input
def input_box():
    root = tk.Tk()
    root.geometry('600x400')

    name_var = tk.StringVar()
    pw_var = tk.StringVar()

    # get input, and remove input when submitted
    def submit():
        name=  name_var.get()
        password = pw_var.get()
        
        print(f'Username : {name}')
        print(f'Password: {password}')
        
        name_var.set('')
        pw_var.set('')

    name_label = tk.Label(root, text = 'Username', font = ('calibre', 10, 'bold'))
    name_input = tk.Entry(root, textvariable = name_var, font = ('calibre', 10, 'bold'))

    pw_label = tk.Label(root, text = 'Password', font = ('calibre', 10, 'bold'))
    pw_input = tk.Entry(root, textvariable = pw_var, font = ('calibre', 10, 'bold'))

    submit_button = tk.Button(root, text = 'Submit', command = submit)
    exit_button = tk.Button(root, text = 'EXIT', command = root.destroy)

    name_label.grid(row = 0, column = 0)
    name_input.grid(row = 0, column = 1)
    pw_label.grid(row = 1, column = 0)
    pw_input.grid(row = 1,column = 1)
    submit_button.grid(row = 2, column = 1)
    exit_button.grid(row = 3, column = 1)

    root.mainloop()




def main():
    # button_box()
    # text_box()
    input_box()
    return




if __name__ == '__main__':
    main()