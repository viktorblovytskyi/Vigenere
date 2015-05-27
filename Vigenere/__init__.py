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
        :param data: - String
        :return:
            encrypted_data - String
        """
        data_char = ''
        self.key_maker()
        arr = self.create_vizhner_array()
        print self.__private_key
        self.print_vigener_array(arr)
        encryption_data = ""
        return encryption_data

    def decryption_vizhener(self):
        """
        This function decrypts data by Vizhener's methods.
        :param data: - String
        :return:
            decryption_data - String
        """
        decryption_data = ""
        return decryption_data

    def key_maker(self, ):
        """
        This function makes the key length of the input row.
        :param data:
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


def main():
    """
    Main function.
    :return:
        void
    """
    vizhener = Vizhener("abcd", "helloworld")
    vizhener.encryption_vizhener()
    #arr = vizhener.create_vizhner_array()
    #vizhener.key_maker()

if __name__ == '__main__':
    main()
