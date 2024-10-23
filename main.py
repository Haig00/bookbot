class Main:
    def read(self, book):
        with open(book) as f:
            file_contents = f.read()
        
        return file_contents

    def count(self, book_text):
        words = book_text.split()
        return len(words)

    def countCharacters(self, text):
        dict = {}
        lowertext = text.lower()
        for character in lowertext:
            if character in dict:
                dict[character] += 1
            else:
                dict[character] = 1
        
        return dict
    
    def print_report(self, count, dictio):
        temp = sorted(dictio.items(), key=lambda x:x[1], reverse=True)
        sorted_dict = dict(temp)
        print("----------- Start of report -----------")
        print(f"{count} words were in the book")
        for letter in sorted_dict:
            if letter.isalpha():
                print(f"the letter '{letter}' appears {sorted_dict[letter]} times in the book")
        return "-------- End of report --------"

            




if __name__ == "__main__":
    reading  =  Main()
    book = "books/frankenstein.txt"
    full_text = reading.read(book)
    #print(reading.count(full_text))
    dictio = (reading.countCharacters(full_text))
    print(reading.print_report(reading.count(full_text), dictio))

    
        