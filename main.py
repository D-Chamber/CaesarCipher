import sys
import Cryptoboy


class Main:
    def __init__(self, arg, var1, var2, var3):
        self.arg = arg
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def run(self):
        if self.arg == '-e':
            Cryptoboy.encrypt(self.var1, int(self.var2), self.var3)
        elif self.arg == '-d':
            Cryptoboy.decrypt(self.var1, int(self.var2), self.var3)
        elif self.arg == '-c':
            if self.var2 == '-t' and 0 < float(self.var3) < 1:
                Cryptoboy.crack(self.var1, float(self.var3))
            else:
                print(f'{self.var2} is an invalid input. Possibly the number you input is too high or low '
                      f'of a number make sure to use a number (float) between 0 and 1.')
        else:
            print(f'{self.arg} is not a valid argument input.')


def main():
    args = sys.argv
    m = Main(args[1], args[2], args[3], args[4])
    m.run()


if __name__ == '__main__':
    main()
