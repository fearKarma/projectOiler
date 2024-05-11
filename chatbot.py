import nltk
nltk.download('punkt')


def chat():
    print("hello")
    
    while True:
        user_input = input("you: ").strip().lower()
        if user_input == "sup bitch":
            print("what up twin")
        elif user_input == "jolly good":
            print("lame af")
        else:
            print("damn bro word")
            break

if __name__ == "__main__":
    chat()
