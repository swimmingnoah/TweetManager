import time
from Tweet import Tweet


def main():
    tweets = []
    choice = '0'

    while(choice != '4'):
        print("Tweet Menu\n-----------------\n1. Make a Tweet\n2. View Recent Tweets\n3. Search Tweets\n4. Quit\n")
        print("What would you like to do?")
        choice = input()

        if(choice.isalpha()):
            print("Please enter a numeric value.")
        elif(int(choice) not in range(1, 5)):
            print("please enter a valid option.")

        if(choice == '1'):
            author = input("What is your name?")
            text = input("What woudl you like to tweet?")

            while(len(text) > 140):
                print("Tweet limit exceeded...please enter less than 140 character")
                text = input("What would you like to tweet?")
            tweet_obj = Tweet(author, text)
            tweets.append(tweet_obj)
            print(author, "your tweet has been saved.\n")

        elif(choice == '2'):
            print("Recent Tweets\n----------------")
            if(len(tweets) == 0):
                print("No tweets availible")
            else:
                min_index = -1
                min_index = len(tweets)-6
                for i in range(len(tweets)-1, min_index, -1):
                    print(tweets[i].get_author(), " - ",
                          tweets[i].get_age(), "\n")
                    print(tweets[i].get_text())
        elif(choice == '3'):
            key = input("What would you like to search for?")
            flag = 0

            for i in range(len(tweets)-1, -1, -1):
                if key in tweets[i].get_text():
                    flag = 1
                    print(tweets[i].get_author(), " - ",
                          tweets[i].get_age(), "\n")
                    print(tweets[i].get_text())
                if(flag == 0):
                    print("No tweet contained ", key)
        elif(choice == "4"):
            print("Thanks for using the tweet manager!")
