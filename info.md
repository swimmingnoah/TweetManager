Challenge: Tweet Manager
Description: Create a Tweet Manager in Python according to the requirements specified in this document. Twitter is a social networking service that provides users with a platform to post short messages called tweets. You are to create a menu-driven, Twitter-like program that allows users to make, view, and search through tweets. As an example, the University of Missouri’s official Twitter account is at https://twitter.com/mizzou (Links to an external site.). Unlike Twitter, you will not be publishing tweets to the Internet. You will be storing, saving, and loading tweet-like messages using Python on your computer.

Purpose: The purpose of this challenge is to provide experience working with classes and object-oriented programming (OOP) in Python as well as designing the architecture of an application.

Requirements:

Twitter is a social networking service that provides users with a platform to post short messages called tweets. You are to create a menu-driven, Twitter-like program that allows users to make, view, and search through tweets. As an example, the University of Missouri’s official Twitter account is at https://twitter.com/mizzou (Links to an external site.). Unlike Twitter, you will not be publishing Tweets to the Internet. You will be storing, saving, and loading Tweet-like messages using Python on your computer.

Tweet classes
Write a class named Tweet and save it as a file named Tweet.py. The Tweet class is to have the following data attributes and methods.

Attributes
This attribute stores the name of the person making the tweet.

\_\_author

This attribute stores the text of the tweet contents.

\_\_text

This attribute stores the time when the tweet was created.

\_\_age

Methods
This method is to take two parameters: author and text of the tweet. It is to set **author and **text based on those parameters and it is to set \_\_age based on the current time.

**init**

This method returns the value of the \_\_author field.

get_author

This method returns the value of the \_\_text field.

get_text

This method calculates the difference between the current time and the value of the \_\_age field. It is to return a string based on the age of the tweet.

get_age

For example, this method is to return the following.

30s if the tweet was posted 30 seconds ago
15m if the tweet was posted 15 minutes ago
1h if the tweet was posted 1 hour, 10 minutes, and 42 seconds ago
Note that the string returned from get_age is only concerned with the largest unit of time. If the tweet is 0 to 59 seconds old, the value returned from get_age is to end with an “s” for “seconds”. If the Tweet is some number of minutes old, it will end with an “m” and ignore the seconds. Likewise, if the Tweet is one or more hours old, it will ignore both the minutes and seconds.

To work with time, you’ll need to use Python’s time module. The documentation for that module is available here: https://docs.python.org/3.9/library/time.html (Links to an external site.)

Tweet Manager
Write a program named twitter.py. This program has four functional parts as shown below.

Tweet Menu
-—————

1. Make a Tweet
2. View Recent Tweets
3. Search Tweets
4. Quit

The following describes the four functional parts.

1. Make a Tweet

If the user chooses to make a tweet, they will be asked for their name and what they would like to tweet.

Twitter limits the length of tweets to 140 characters. Likewise, your program is to check the length of the user’s tweet and re-prompt them if it is greater than 140 characters.

Use the user’s input and the Tweet class to create a new Tweet object.

2. View Recent Tweets

If the user chooses to view recent tweets, then display the five most recently created tweets including each tweet’s author, text, and age.

If there are no tweets, display a message indicating so.

3. Search Tweets

Check to make sure there are tweets available to search. If there are no tweets, display a message indicating so.

If there are tweets, ask the user what they would like to search for. Look through the tweets and display only the tweets that contain the search text.

The tweets are to be displayed in chronological order, starting with the most recently created tweet.

If no tweets contain the user’s search, display a message indicating so.

4. Quit

If the user chooses to quit, the program is to exit.

Storing, Saving, and Loading Tweets
In order to view and search through the tweets, they need to be organized in some way. One method for doing that is to use a list. Whenever Tweet objects are created, they are added to the list.

When the program ends, the tweets are not to disappear. The tweets are to persist in file storage. Each time the program is run, it should be possible to go back and view/search past tweets. To accomplish that, the list of tweets need to be saved and loaded.

You can develop your own strategy for doing that if you’d like. The following are a few suggestions to get you started. Whenever a new Tweet object is created, add it to the list of tweets. Then, serialize the list and save it to a file. Section 9.3 in the textbook provides information on serializing objects. “Serializing an object is the process of converting the object to a stream of bytes that can be saved to a file for later retrieval.”

Then, each time the program starts, check for the file of tweets. If it does not exist, start with a new, empty list. If it does exist, read that file and de-serialize it back into a list of Tweet objects.

Study 9.3 Serializing Objects to learn how serialization works. Also, refer to 10.3 Working with Instances for examples on how to serialize objects.

The tweets are to be saved in a file named tweets.dat

Sample Program Operation
Tweet Menu
-—————

1. Make a Tweet
2. View Recent Tweets
3. Search Tweets
4. Quit

What would you like to do? 1

What is your name? Sally
What would you like to tweet? This is my first tweet!
Sally, your tweet has been saved.

Tweet Menu
-—————

1. Make a Tweet
2. View Recent Tweets
3. Search Tweets
4. Quit

What would you like to do? 2

Recent Tweets
-——————
Sally - 6s
This is my first tweet!

Tweet Menu
-—————

1. Make a Tweet
2. View Recent Tweets
3. Search Tweets
4. Quit

What would you like to do? 1
What is your name? David
What would you like to tweet? I also like to tweet. This is #fun
David, your tweet has been saved.

Tweet Menu
-—————

1. Make a Tweet
2. View Recent Tweets
3. Search Tweets
4. Quit

What would you like to do? 2

Recent Tweets
-——————
David - 2s
I also like to tweet. This is #fun

Sally - 3m
This is my first tweet!

Tweet Menu
-—————

1. Make a Tweet
2. View Recent Tweets
3. Search Tweets
4. Quit

What would you like to do? 3
What would you like to search for? fun

Search Results
-——————
David - 1m
I also like to tweet. This is #fun

Tweet Menu
-—————

1. Make a Tweet
2. View Recent Tweets
3. Search Tweets
4. Quit

What would you like to do? 4
Thank you for using the Tweet Manager!

Notes
The output of your program should match the format of the sample program operation above.

If no tweets exist, the view and search options should display appropriate feedback.

Tweet Menu
-—————

1. Make a Tweet
2. View Recent Tweets
3. Search Tweets
4. Quit

What would you like to do? 2

Recent Tweets
-——————
There are no recent tweets.

Tweet Menu
-—————

1. Make a Tweet
2. View Recent Tweets
3. Search Tweets
4. Quit

What would you like to do? 3

There are no tweets to search

Tweet Menu
-—————

1. Make a Tweet
2. View Recent Tweets
3. Search Tweets
4. Quit

What would you like to do? 4
Thank you for using the Tweet Manager!

If a search yields no results, display an appropriate message like the following.

Tweet Menu
-—————

1. Make a Tweet
2. View Recent Tweets
3. Search Tweets
4. Quit

What would you like to do? 3

What would you like to search for? Python

Search Results
-——————
No tweets contained Python

Tweet Menu
-—————

1. Make a Tweet
2. View Recent Tweets
3. Search Tweets
4. Quit

What would you like to do? 4
Thank you for using the Tweet Manager!

Errors resulting from a user providing invalid input are to be handled. Exceptions are not to cause the program to crash. The following is an example of handling a user’s invalid entry.

Tweet Menu
-—————

1. Make a Tweet
2. View Recent Tweets
3. Search Tweets
4. Quit

What would you like to do? one
Please enter a numeric value.

What would you like to do? –1
Please select a valid option

What would you like to do? 5
Please select a valid option

Remember to check the length of each tweet. Tweets cannot be longer than 140 characters. The following is an example involving a tweet that is too long.

Tweet Menu
-—————

1. Make a Tweet
2. View Recent Tweets
3. Search Tweets
4. Quit

What would you like to do? 1

What is your name? Julie
What would you like to tweet? This is a very long tweet #toolong. The program should prevent me from posting this because it is longer than one hundred and forty characters. Thanks!

Tweets can only be 140 characters!

Testing
Make sure you have thoroughly tested your program!

Submission
Put your Tweet.py and twitter.py files in a folder named TweetManager and zip the folder. The zip file is to be submitted for this assignment.
