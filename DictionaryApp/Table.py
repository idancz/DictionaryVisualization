from tkinter import *
from time import sleep
#################################################################################
#=============================== Class Table ===================================#
#################################################################################
class Table:
    def __init__(self, window):
        self.window = window
        self.hash_map = []
        self.rows = {}
        self.var = [StringVar() for _ in range(2)]

    def initialize_table(self, hash_map):
        self.hash_map = hash_map
		

    def create_titles(self):
        '''
        Create table column titles
        '''
        label2 = Label(self.window[1], text="Index", font="none 11 bold")
        label2.grid(row=1, column=0, padx=5, pady=8, sticky='S')

        label = Label(self.window[1], text="Hash", font="none 11 bold")
        label.grid(row=1, column=1, padx=5, pady=8, sticky='S')

        label3 = Label(self.window[1], text="Key", font="none 11 bold")
        label3.grid(row=1, column=2, padx=5, pady=8, sticky='S')

        label4 = Label(self.window[1], text="Value", font="none 11 bold")
        label4.grid(row=1, column=3, padx=5, pady=8, sticky='S')

        label5 = Label(self.window[1], text="Status", font="none 11 bold")
        label5.grid(row=1, column=4, padx=5, pady=8, sticky='S')

        label6 = Label(self.window[1], text="Jumps Order", font="none 11 bold")
        label6.grid(row=1, column=5, padx=5, pady=8, sticky='S')


    def create_table(self):
        '''
        Creates rows from the dictionary hash_map
        '''
        self.rows = {}
        for i, slots in enumerate(self.hash_map):
            data = self.check_status(slots)
            self.rows[i] = Row(self.window[1], i, data[0], data[1], data[2], '')


    def create_hash_func_label(self):
        label = Label(self.window[0], textvariable=self.var[0], text="", font="none 9 bold")
        label.grid(row=0, column=1, padx=1, pady=8)
        enter = Label(self.window[0], textvariable=self.var[1], padx=1, pady=8, justify='center', font="none 9 bold")
        enter.grid(row=0, column=3)

    def printing_first_hash_func(self, func, st):
        self.var[0].set(st)
        self.var[1].set(func)

    def print_rehashing_message(self):
        for i in range(4):
            self.var[1].set("----------------")
            self.window[0].update()
            sleep(0.4)
            self.var[1].set("REHASHING TABLE")
            self.window[0].update()
            sleep(0.4)

    def check_status(self, slots):
        '''
        Check slot status :occupied , deleted or free
        '''
        if len(slots) > 1:
            return [slots[0], slots[1], "Occupied"]
        elif len(slots) == 1:
            return ["< Dummy >", "< Dummy >", "Deleted"]
        return ['', '', "Free"]


    def jump_number(self, i):
        ls = ['st', 'nd', 'rd', 'th']
        if i % 10 == 0 and i != 10:
            return str(i+1) + ls[0]
        elif i % 10 == 1 and i != 11:
            return str(i+1) + ls[1]
        elif i % 10 == 2 and i != 12:
            return str(i + 1) + ls[2]
        return str(i + 1) + ls[3]


    def mark_spot(self, idx, i, color, st):
        '''
        Mark collision spots
        '''
        self.window[1].update()
        sleep(0.4)
        self.rows[idx].set_jumps_order(self.jump_number(i), color)
        self.show_jump_func(st)
        self.window[1].update()
        sleep(0.4)


    def clean_marks(self):
        for val in self.rows.values():
            val.clean_jumps()


    def insert_row(self, index):
        '''
        Insert new row to table
        '''
        slot = self.hash_map[index]
        self.rows[index] = (Row(self.window[1], index, slot[0], slot[1], "Occupied", bin(hash(slot[0]) & 0xFF)))


    def show_jump_func(self, st):
        self.var[1].set(st)


    def update_table(self , table):
        '''
        Load changes from dictionary to table
        '''
        self.hash_map = table
        for i, slots in enumerate(self.hash_map):
            data = self.check_status(self.hash_map[i])
            temp = data[0]
            if temp != '':
                temp = bin(hash(temp) & 0xFF)
            try:
                self.rows[i].update_row(i, data[0], data[1], data[2], temp)
            except KeyError:
                self.rows[i] = Row(self.window[1], i, data[0], data[1], data[2], temp)
            self.rows[i].clean_jumps()


    def delete_table(self):
        '''
        Clean and initialize table
        '''
        for val in self.rows.values():
            print(val.delete_row())
        self.create_titles()
        self.create_hash_func_label()


#################################################################################
#================================== Class Row ==================================#
#################################################################################
class Row:
    def __init__(self, window, index, key, value, status, _hash):
        self.window = window
        self.index = index
        self.key = key
        self.value = value
        self.status = status
        self.hash = _hash
        self.entries = {}
        self.variables = {}
        self.create_row()


    def create_row(self):
        v1 = StringVar()
        e1 = Entry(self.window, textvariable=v1, state='readonly', justify='center')
        v1.set('')
        e1.grid(row=2+self.index, column=5, padx=5, pady=3, sticky='S')
        self.variables["Jumps"] = v1
        self.entries["Jumps"] = e1

        v2 = StringVar()
        color = self.status_color(self.status)
        e2 = Entry(self.window, textvariable=v2, state='readonly', justify='center', fg=color)
        v2.set(self.status)
        e2.grid(row=2+self.index, column=4, padx=5, pady=3, sticky='S')
        self.variables["Status"] = v2
        self.entries["Status"] = e2

        v3 = StringVar()
        e3 = Entry(self.window, textvariable=v3, state='readonly', justify='center')
        v3.set(self.value)
        e3.grid(row=2+self.index, column=3, padx=5, pady=3, sticky='S')
        self.variables["Value"] = v3
        self.entries["Value"] = e3

        v4 = StringVar()
        e4 = Entry(self.window, textvariable=v4, state='readonly', justify='center')
        v4.set(self.key)
        e4.grid(row=2+self.index, column=2, padx=5, pady=3, sticky='S')
        self.variables["Key"] = v4
        self.entries["Key"] = e4

        v5 = StringVar()
        e5 = Entry(self.window, textvariable=v5, state='readonly', justify='center')
        v5.set(self.hash)
        e5.grid(row=2+self.index, column=1, padx=5, pady=3, sticky='S')
        self.variables["Hash"] = v5
        self.entries["Hash"] = e5

        v6 = StringVar()
        e6 = Entry(self.window, textvariable=v6, state='readonly', justify='center')
        v6.set(self.index)
        e6.grid(row=2+self.index, column=0, padx=5, pady=3, sticky='S')
        self.variables["Index"] = v6
        self.entries["Index"] = e6


    def update_row(self, index, key, value, status, _hash):
        '''
        Update all row variables (index, key, value, status, _hash)
        '''
        self.index = index
        self.key = key
        self.value = value
        self.status = status
        self.hash = _hash
        color = self.status_color(self.status)
        self.variables["Index"].set(self.index)
        self.variables["Hash"].set(self.conv_to_bits(self.hash))
        self.variables["Key"].set(self.key)
        self.variables["Value"].set(self.value)
        self.entries["Status"].configure(fg=color)
        self.variables["Status"].set(self.status)
        self.clean_jumps()


    def set_jumps_order(self, order, color):
        self.entries["Jumps"].configure(state="normal", background=color)
        self.variables["Jumps"].set("<----        " + str(order))


    def clean_jumps(self):
        self.entries["Jumps"].configure(background='SystemButtonFace')
        self.variables["Jumps"].set('')


    def status_color(self, status):
        '''
        Return status color: free-green , occupied-red,deleted-orange
        '''
        if status == "Free":
            return "green"
        elif status == "Occupied":
            return "red"
        return "orange"


    def conv_to_bits(self, binr):
        '''
        Convert hash to bits
        '''
        if binr != '':
            bb = binr.split('b')[1]
            return '0' * (8 - len(bb)) + bb
        return ''


    def delete_row(self):
        '''
        Delete all
        '''
        lis = self.window.grid_slaves()
        for l in lis:
            l.destroy()
