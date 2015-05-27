from Vigener import Vizhener

def main():
    """
    Main function.
    :return:
        void
    """
    vizhener = Vizhener("lemon", "attackatdawn")
    encryption = vizhener.encryption_vizhener()
    print encryption
    print vizhener.decryption_vizhener(encryption)

if __name__ == '__main__':
    main()
