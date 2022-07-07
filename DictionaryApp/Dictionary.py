from Table import Table

class Dictionary:
    def __init__(self, table=None, a=None, b=None):
        self._size = 8                                                                #size of dict
        self.hash_map = [[] for _ in range(self._size)]                               #create hash map at size 8
        self.stored_items = 0                                                         #number of stored items
        self.deleted_items = 0                                                        #number of deleted items
        self.load_factor = 0.0                                                        #Occupancy indicator
        self._prime = 7                                                               #set first prime number
        self.quadratic_factor = 3                                                     #set quadratic factor to 3
        self.collision_func = "linear" 									              # set collision function to linear
        self.a = a
        self.b = b
        self.table = table
        if isinstance(table, Table):
            self.table.initialize_table(self.hash_map)
	

    def is_full(self):
        '''
        check if dict is full
        '''
        self.load_factor = (self.stored_items / self._size)
        return int(self.load_factor)


    def slot_empty(self, slot):
        '''
        check if solt empty
        '''
        return not len(slot)



    def hash_functions(self, key, control):
        '''
        Search free space in the hash table
        Find keys in the hash table
        Handel collisions by 4 deferent functions:
        "linear, quadratic, double hashing, custom"
        Displays a dynamic interface action
        '''
        temp_key = hash(key)
        hash_index = temp_key
        if self.collision_func == "double":
            h1 = temp_key % self._size
            h2 = self._prime - (temp_key % self._prime)
            h1 += not h1 % 2
            h2 += not h2 % 2
        for i in range(self.number_of_jumps()):
            if self.collision_func == "linear":
                hash_index = (temp_key + i) % self._size
                ss = "(h + %s) %% %s" % (i, self._size)
            elif self.collision_func == "quadratic":
                hash_index = (temp_key + i ** 2) % self._size
                ss = "(h + %s) %% %s" % (i, self._size)
            elif self.collision_func == 'double':
                hash_index = (h1 + (i * h2)) % self._size
                ss = "(h1 + (%s * h2)) %% %s" % (i, self._size)
            else:
                hash_index = (self.a + (hash_index * self.b)) % self._size
                ss = "(%s + (h * %s)) %% %s" % (self.a, self.b, self._size)
            if control:
                if self.slot_empty(self.hash_map[hash_index]):
                    self.mark_interface_spot(hash_index, i, "green", ss)
                    return hash_index
                elif key == self.hash_map[hash_index][0]:
                    self.mark_interface_spot(hash_index, i, "green", ss)
                    self.stored_items -= 1
                    return hash_index
            else:
                if not self.slot_empty(self.hash_map[hash_index]):
                    if key == self.hash_map[hash_index][0]:
                        self.mark_interface_spot(hash_index, i, "green", ss)
                        return hash_index
                else:
                    self.mark_interface_spot(hash_index, i, "red", ss)
                    break
            self.mark_interface_spot(hash_index, i, "red", ss)
        if not control:
            self.update_interface()
            raise KeyError("Key %s does not exist !!" % key)
        self.rehashing()
        return self.hash_functions(key, control)

	

    def index(self, key):
        '''
        return idx of key according to hash table
        '''
        return self.hash_functions(key, 0)



    def insert(self, key, value):
        '''
        save key,value at hash map(dict)
        '''
        if self.is_full():                                      #if dict is full
            self.rehashing()                                    #increases the dict size
            self.update_interface()                             
        idx = self.hash_functions(key, 1)                       #get index of hash
        self.hash_map[idx] = (key, value)                       #save key,value at hash map
        self.stored_items += 1                                  #increase stored items
        self.update_interface()                                 #update gui table
                                                                

    def rehashing(self):
        '''
        increases dict size(x2) and copy all slots
        implement the new hash function on all slots
        '''
        self._size *= 2                                         #increase size
        self.deleted_items = 0                                  #reset deleted items
        self.stored_items = 0                                   #reset stored items
        self.max_prime_num()                                    #set new prime number
        old_hash_map = self.hash_map                            #save old hash map
        self.hash_map = [[] for _ in range(self._size)]
        self.quadratic_jump_factor()
        self.update_interface()
        self.rehashing_interface()
        for slots in old_hash_map:
            if len(slots):
                if slots[0] is not None:
                    self.insert(slots[0], slots[1])             #insert keys,values to hash map
        self.load_factor = (self.stored_items / self._size)



    def set_collision_func(self, func, a=None, b=None):
        '''
        set collision function: linear / quadratic / double hashing / custom
        '''
        if func == "custom":
            self.a = a
            self.b = b
        self.collision_func = func

	
    def number_of_jumps(self):
        if self.collision_func == "quadratic":
            return self.quadratic_factor
        return self._size


    def quadratic_jump_factor(self):
        '''
        Calculate number of jumps for quadratic collision handling function
        '''
        self.quadratic_factor = 2*self.quadratic_factor - (1 + (self.quadratic_factor % 2))


    def is_prime(self, num):
        '''
        Check if number is prime
        '''
        i = 2
        flag = 0
        while i < num:
            if num % i == 0:
                flag = 1
                break
            else:
                i += 1
        if flag == 0:
            return True
        return False


    def max_prime_num(self):
        '''
        Find the biggest prime number that smaller then size of the hash table
        '''
        for i in range(self._size - 1, 1, -1):
            if self.is_prime(i):
                self._prime = i
                break


    def get_prime(self):
        return self._prime


    def get(self, key):
        '''
        Return value from the dictionary
        '''
        val = self.hash_map[self.hash_functions(key, 0)][1]
        self.clean_interface_marks()
        return val


    def delete(self, key):
        '''
        Delete key and value from the dictionary
        '''
        self.hash_map[self.hash_functions(key, 0)] = [None]
        self.deleted_items += 1
        self.update_interface()


    def show_slots(self):
        '''
        Print all hash map slots
        '''
        for slot in self.hash_map:
            print(slot, end='')
        print("\n")


    def print_dict(self):
        '''
        Print dictionary
        '''
        dictionary = "{"
        for slot in self.hash_map:
            if len(slot) > 1:
                dictionary += "%s: %s, " % self.check_type(slot[0], slot[1])
        return dictionary[:-2] + '}'

	

    def check_type(self, key, val):
        '''
        Check type(str or integer) of key and value
        '''
        if type(key) is str:
            k = "'" + key + "'"
        else:
            k = key
        if type(val) is str:
            v = "'" + val + "'"
        else:
            v = val
        return k, v


    def get_hash_map(self):
        return self.hash_map


    def keys(self):
        '''
        Return all keys
        '''
        k = []
        for slots in self.hash_map:
            if len(slots) > 1:
                k.append(slots[0])
        return k


    def values(self):
        '''
        Return all values
        '''
        v = []
        for slots in self.hash_map:
            if len(slots) > 1:
                v.append(slots[1])
        return v


    def clear(self):
        '''
        Clean all dictionary parameters
        Clean interface and reset
        '''
        self._size = 8
        self.hash_map = [[] for _ in range(self._size)]
        self.stored_items = 0
        self.deleted_items = 0
        self.load_factor = 0.0
        self._prime = 7
        self.quadratic_factor = 3
        self.collision_func = "linear"
        self.initialize_interface()
        self.clear_interface()



    def get_table(self):
        return self.table


    def number_of_items(self):
        return self.stored_items - self.deleted_items


    def get_size(self):
        return self._size


    def __setitem__(self, key, value):
        return self.insert(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __str__(self):
        return self.print_dict()

    def __len__(self):
        return self.number_of_items()

    def __contains__(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __delitem__(self, key):
        self.delete(key)

    def __eq__(self, obj):
        if not isinstance(obj, Dictionary):
            try:
                obj = Dictionary(obj)
            except TypeError:
                return NotImplemented
        if self.stored_items != obj.stored_items:
            return False
        for slot in self.hash_map:
            if len(slot) > 1:
                try:
                    value = obj[slot[0]]
                except KeyError:
                    return False
                if value != slot[1]:
                    return False
        return True
		

	# Graphical interface functions for dictionary implementation
    def update_interface(self):
        if isinstance(self.table, Table):
            self.table.update_table(self.hash_map)


    def initialize_interface(self):
        if isinstance(self.table, Table):
            self.table.initialize_table(self.hash_map)


    def mark_interface_spot(self, hash_index, i, color, ss):
        if isinstance(self.table, Table):
            self.table.mark_spot(hash_index, i, color, ss)

    def rehashing_interface(self):
        if isinstance(self.table, Table):
            self.table.print_rehashing_message()


    def clean_interface_marks(self):
        if isinstance(self.table, Table):
            self.table.clean_marks()


    def clear_interface(self):
        if isinstance(self.table, Table):
            self.table.create_table()

