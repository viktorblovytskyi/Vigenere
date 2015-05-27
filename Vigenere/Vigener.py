class Vizhener:
    """
        Class Vizhener
        Methods:
            create_vizhener_array();
            encryption_vizhener(data);
            decryption(data);
            key_maker();
            print_vigener_array(vigener_array);

    """
    __private_alf = "abcdefghijklmnopqrstuvwxyz"
    __private_key = ""
    __private_data = ""

    def __init__(self, key, data):
        self.__private_key = key
        self.__private_data = data

    def create_vizhner_array(self):
        """
        This function creates Vizhener's array.
        :return vizhener_arr: Array
        """
        vizhener_arr = []
        temp_vizhener_arr = []
        i, j = 0, 0
        while i < 26:
            while j < 26:
                shift = i + j
                if shift >= 26:
                    shift %= 26
                temp_vizhener_arr.append(self.__private_alf[shift])
                j += 1
            vizhener_arr.append(temp_vizhener_arr)
            temp_vizhener_arr = []
            j = 0
            i += 1
        return vizhener_arr

    def encryption_vizhener(self):
        """
        This function encrypts data by Vizhener's method.
        :return:
            encrypted_data - String
        """
        self.key_maker()
        vigener_arr = self.create_vizhner_array()
        encryption_data = ""
        i = 0
        while i < len(self.__private_data):
            index_of_input = self.find_char_in_row(self.__private_data[i], vigener_arr)
            index_of_key = self.find_char_in_col(self.__private_key[i], vigener_arr)
            encryption_data += vigener_arr[index_of_input][index_of_key]
            i += 1
        return encryption_data

    def decryption_vizhener(self, encryption_data):
        """
        This function decrypts data by Vizhener's methods.
        :param:
            encryption_data - String
        :return:
            decryption_data - String
        """
        self.key_maker()
        vigener_arr = self.create_vizhner_array()
        decryption_data = ""
        i = 0
        while i < len(encryption_data):
            index_of_key = self.find_char_in_row(self.__private_key[i],vigener_arr)
            index_of_data = self.find_char_in_col(encryption_data[i],vigener_arr,index_of_key)
            decryption_data += vigener_arr[index_of_data][0]
            i += 1
        return decryption_data

    def key_maker(self, ):
        """
        This function makes the key length of the input row.
        :return:
            __private_key - String
        """
        new_key = self.__private_key
        i, j = 0, 0
        key_len = len(self.__private_key)
        while i < len(self.__private_data):
            if key_len <= i:
                new_key += self.__private_key[j]
                j += 1
                if j == key_len:
                    j = 0
            i += 1
        self.__private_key = new_key
        return 0

    def print_vigener_array(self, vigener_array):
        """
        This function displays Vigener's array;
        :return:
            void
        """
        i = 0
        while i < len(vigener_array):
            print vigener_array[i]
            i += 1
        return 0

    def find_char_in_row(self, symbol, vigener_array):
        """
        This function looks for a symbol in the row and returns index of this symbol.
        If the symbol is found: return index of symbol
        Else: return -1 as error;
        :param:
            symbol - character of the input data
            vigener_array - Array

        :return:
            index - index of the symbol.
        """
        j = 0
        while j < len(vigener_array[0]):
            if vigener_array[0][j] == symbol:
                return j
            j += 1
        return -1

    def find_char_in_col(self, symbol, vigener_array, row_index=0):
        """
        This function looks for a symbol in the column and returns index of this symbol.
        If the symbol is found: return index of symbol
        Else: return -1 as error;
        :param:
            symbol - character of the input data
            vigener_array - Array
        :return:
            index - index of the symbol
        """
        i = 0
        while i < len(vigener_array):
            if vigener_array[i][row_index] == symbol:
                return i
            i += 1
        return -1

