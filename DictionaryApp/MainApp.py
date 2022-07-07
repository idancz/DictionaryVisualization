from tkinter import *
from tkinter import messagebox
from Dictionary import *


class GUI:
    def __init__(self, master):
        self.master = master
        self.frames = [Frame(self.master) for _ in range(5)]
        self.create_frames()
        self.dict = Dictionary(Table(self.frames[3:]))
        self.a_b = [StringVar() for _ in range(2)]
        self.key = StringVar()
        self.value = StringVar()
        self.message = StringVar()
        self.radio_butt = StringVar()
        self.widgets = {}
        self.collision_en = True


    def create_frames(self):
        for i, frame in enumerate(self.frames):
            frame.grid(row=i, column=0)

    def create_menu(self):
        main_menu = Menu(self.master)
        self.master.config(menu=main_menu)
        file_menu = Menu(self.master)
        main_menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label="Exit", command=self.exit)
        file_menu.add_separator()


    def create_title(self):
        self.master.title("Dictionary Implementation")


    def create_main_title(self):
        m_title = Label(self.frames[0], text="Dictionary", pady=5, fg="#50659E", font="times 20 bold italic underline")
        m_title.grid(row=0, column=5)


    def check_box(self):
        '''
        Creates radio buttons for 3 collision functions: linear,quadratic,double hashing, custom
        '''
        c = Label(self.frames[0], text="Collision Function: ")
        c.grid(row=3, column=2)

        self.radio_butt.set("linear")
        cc = Radiobutton(self.frames[0], text="Linear", variable=self.radio_butt, value="linear", command=self.hash_function)
        cc.grid(row=3, column=3)
        self.widgets["Linear"] = cc

        c3 = Radiobutton(self.frames[0], text="Quadratic", variable=self.radio_butt, value="quadratic", command=self.hash_function)
        c3.grid(row=3, column=4)
        self.widgets["Quadratic"] = c3

        c4 = Radiobutton(self.frames[0], text="Double Hashing", variable=self.radio_butt, value="double", command=self.hash_function)
        c4.grid(row=3, column=5)
        self.widgets["Double Hashing"] = c4

        c5 = Radiobutton(self.frames[0], text="Custom ------>", variable=self.radio_butt, value="custom", command=self.hash_function)
        c5.grid(row=3, column=6)
        self.widgets["Custom"] = c5

        l_a = Label(self.frames[0], text="A:", pady=5)
        l_a.grid(row=3, column=7, sticky='W')

        a = Entry(self.frames[0], width=7, textvariable=self.a_b[0], justify='center')
        a.grid(row=3, column=8, sticky='W')
        self.widgets["A"] = a
        self.a_b[0].set(2)

        l_b = Label(self.frames[0], text="B:", pady=5)
        l_b.grid(row=3, column=9, sticky='W')

        b = Entry(self.frames[0], width=7, textvariable=self.a_b[1], justify='center')
        b.grid(row=3, column=10, sticky='W')
        self.widgets["B"] = b
        self.a_b[1].set(7)


    def key_box(self):
        '''
        Create label and text box for key
        '''
        k_label = Label(self.frames[0], text="Key:", pady=20, font="none 9 bold")
        k_label.grid(row=5, column=3)
        key = Entry(self.frames[0], width=27, textvariable=self.key, justify='center')
        key.grid(row=5, column=4)
        self.widgets["Key"] = key


    def value_box(self):
        '''
        Create label and text box for value
        '''
        v_label = Label(self.frames[0], text="Value:", pady=20, font="none 9 bold")
        v_label.grid(row=5, column=5)
        value = Entry(self.frames[0], width=27, textvariable=self.value, justify='center')
        value.grid(row=5, column=6)
        self.widgets["Value"] = value


    def create_buttons(self):
        '''
        Create buttons for :insert,get,delete,index,clear,keys,values,items
        '''
        insret_but = Button(self.frames[1], text="Insret", command=self.insret_button, pady=7, padx=10)
        insret_but.grid(row=7, column=2)
        self.widgets["Insret"] = insret_but

        get_but = Button(self.frames[1], text="Get", command=self.get_button, pady=7, padx=10)
        get_but.grid(row=7, column=3)
        self.widgets["Get"] = get_but

        delete_but = Button(self.frames[1], text="Delete", command=self.delete_button, pady=7, padx=10)
        delete_but.grid(row=7, column=4)
        self.widgets["Delete"] = delete_but

        index_but = Button(self.frames[1], text="Index", command=self.index_button, pady=7, padx=10)
        index_but.grid(row=7, column=5)
        self.widgets["Index"] = index_but

        keys_but = Button(self.frames[1], text="Keys", command=self.show_keys, pady=7, padx=10)
        keys_but.grid(row=7, column=6)
        self.widgets["Keys"] = keys_but

        values_but = Button(self.frames[1], text="Values", command=self.show_values, pady=7, padx=10)
        values_but.grid(row=7, column=7)
        self.widgets["Values"] = values_but

        items_but = Button(self.frames[1], text="Items", command=self.print_dictionary, pady=7, padx=10)
        items_but.grid(row=7, column=8)
        self.widgets["Items"] = items_but

        clear_but = Button(self.frames[1], text="Clear", command=self.clean_table, pady=7, padx=10)
        clear_but.grid(row=7, column=9)
        self.widgets["Clear"] = clear_but



    def text_box(self):
        '''
        Creates the Messages Window
        '''
        leb = Label(self.frames[2], text='Output Window', pady=10, font="none 9 bold underline")
        leb.grid(row=0, column=2)
        output = Text(self.frames[2], width=80, height=2, padx=10, fg="white", bg="#404141")
        output.grid(row=1, column=2)
        self.widgets["Messages Window"] = output


    def hash_function(self):
        '''
        Set collision function to dictionary
        '''
        func = self.radio_butt.get()
        try:
            if func == "custom":
                self.dict.set_collision_func(func, int(self.a_b[0].get()), int(self.a_b[1].get()))
            else:
                self.dict.set_collision_func(func)
            self.check_first_hash_func()
        except ValueError:
            self.pop_up_message("You must insert numbers to A nad B")


    def check_first_hash_func(self):
        linear_func = "(hash(key) + i) % size_table"
        quadratic_func = "(hash(key) + i^2) % size_table"
        double_func = "h1 = (hash(key) + i) % size_table\nh2 = prime - (hash(key) %  prime)\n(h1 + i*h2) %  size_table"
        custom_func = "h = (A + h*B) % size_table"
        if self.radio_butt.get() == "linear":
            self.dict.get_table().printing_first_hash_func(linear_func, "Linear Probing Calculation:")
        elif self.radio_butt.get() == "quadratic":
            self.dict.get_table().printing_first_hash_func(quadratic_func, "Quadratic Probing Calculation:")
        elif self.radio_butt.get() == "double":
            self.dict.get_table().printing_first_hash_func(double_func, "Double Hashing Calculation:")
        elif self.radio_butt.get() == "custom":
            self.dict.get_table().printing_first_hash_func(custom_func, "Custom Hashing Calculation:")


    def cheack_arguments(self):
        if not(self.a_b[0].get().isdigit() and self.a_b[1].get().isdigit()):
            raise Exception("Unvalid variables A  B ")


    def insret_button(self):
        '''
        Insert key ,value to dictionary
        '''
        try:
            if self.radio_butt.get() == "custom":
                self.cheack_arguments()
            key = self.input_type(self.key.get())
            value = self.input_type(self.value.get())
            self.dict[key] = value
            if self.collision_en:
                self.lock_collision_func(True)
        except Exception as e:
            self.pop_up_message(e)
        self.clear_entries()


    def get_button(self):
        '''
        Get the value of key from
        '''
        try:
            key = self.input_type(self.key.get())
            self.value.set(self.dict[key])
        except Exception as e:
            self.pop_up_message(e)


    def delete_button(self):
        '''
        Delete the key,value from dictionary
        '''
        try:
            key = self.input_type(self.key.get())
            self.dict.delete(key)
        except Exception as e:
            self.pop_up_message(e)
            self.clear_entries()


    def index_button(self):
        '''
        Check if key in dictionary and return index else show error message
        '''
        try:
            key = self.input_type(self.key.get())
            self.clear_message()
            self.widgets["Messages Window"].insert(END, "The index of key=%s is %s" % (key, self.dict.index(key)))
        except Exception as e:
            self.pop_up_message(e)
            self.clear_entries()


    def lock_collision_func(self, commd):
        if commd:
            self.widgets["Double Hashing"].configure(state=DISABLED)
            self.widgets["Quadratic"].configure(state=DISABLED)
            self.widgets["Linear"].configure(state=DISABLED)
            self.widgets["Custom"].configure(state=DISABLED)
            self.widgets["A"].configure(state=DISABLED)
            self.widgets["B"].configure(state=DISABLED)
            self.collision_en = False
        else:
            self.widgets["Double Hashing"].configure(state=NORMAL)
            self.widgets["Quadratic"].configure(state=NORMAL)
            self.widgets["Linear"].configure(state=NORMAL)
            self.widgets["Custom"].configure(state=NORMAL)
            self.widgets["A"].configure(state=NORMAL)
            self.widgets["B"].configure(state=NORMAL)
            self.collision_en = True


    def input_type(self, inp):
        '''
        Handel input type
        '''
        if not len(inp):
            raise IndexError("The key field is empty !!")
        if inp.isdigit():
            return int(inp)
        elif (inp[0] == "'" and inp[-1] == "'") or (inp[0] == '"' and inp[-1] == '"'):
            return inp[1:-1]
        return inp


    def clear_entries(self):
        self.key.set("")
        self.value.set("")
        self.clear_message()

    def clean_table(self):
        self.dict.get_table().delete_table()
        self.dict.clear()
        self.clear_entries()
        self.clear_message()
        self.lock_collision_func(False)
        self.radio_butt.set("linear")
        self.check_first_hash_func()

    def run_app(self):
        self.dict.get_table().create_titles()
        self.create_main_title()
        self.dict.get_table().create_hash_func_label()
        self.dict.get_table().create_table()

        self.create_title()
        self.create_menu()
        self.key_box()
        self.value_box()

        self.check_box()
        self.create_buttons()
        self.text_box()
        self.check_first_hash_func()


    def pop_up_message(self, e):
        messagebox.showerror("ERROR", e)
        self.clear_entries()


    def show_keys(self):
        self.clear_message()
        self.widgets["Messages Window"].insert(END, "All Keys: %s" % self.dict.keys())


    def show_values(self):
        self.clear_message()
        self.widgets["Messages Window"].insert(END, "All Values: %s" % self.dict.values())

    def print_dictionary(self):
        self.clear_message()
        self.widgets["Messages Window"].insert(END, "All Items: %s" % self.dict.print_dict())

    def clear_message(self):
        self.widgets["Messages Window"].delete(1.0, END)


    def exit(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    gu = GUI(root)
    gu.run_app()
    root.mainloop()


