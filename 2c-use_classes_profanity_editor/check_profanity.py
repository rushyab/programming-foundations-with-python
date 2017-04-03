import urllib.request
import urllib.parse

def read_text():
    quotes = open(r"E:\programming-foundations-with-python\2c-use_classes_profanity_editor\movie_quotes.txt")
    contents_of_file = quotes.read();
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    text = urllib.parse.quote(text_to_check)
    url = "http://www.wdylike.appspot.com/?q=" + text
    connection = urllib.request.urlopen(url)
    output = connection.read()
    output_string = output.decode("utf-8")
    connection.close()
    if "true" in output_string:
        print("Profanity Alert!!")
    elif "false" in output_string:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")

read_text()
