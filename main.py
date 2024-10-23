class Main:
    def read(self, book):
        with open(book) as f:
            file_contents = f.read()
            print(file_contents)




if __name__ == "__main__":
    reading  =  Main()
    reading.read("../books/frankenstein.txt")
