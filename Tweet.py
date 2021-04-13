class Tweet:
    def __init__(self, author, text):
        self.__author = author
        self.__text = text
        self.__age = time.time()

    def get_author(self):
        return self.__author

    def get_text(self):
        return self.__text

    def get_age(self):
        current_time = time.time()
        ticks_diff = int(current_time-self.__age)

        if(ticks_diff >= 0 and ticks_diff < 60):
            return str(ticks_diff)+'s'
        elif(ticks_diff >= 60 and ticks_diff < 3600):
            ticks_diff = int(ticks_diff/60)
            return str(ticks_diff)+'m'
        elif(ticks_diff >= 3600 and ticks_diff < 86, 400):
            ticks_diff = int(ticks_diff/3600)
            return str(ticks_diff) + 'h'
