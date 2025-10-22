print("which do u want to run?")
print("1. cat program")
print("2. Never Gonna Give You Up program")
print("3. blank program")
print("4. infinite loop program")
print("5. hello world program")

choice = input("Enter choice(1/2/3/4/5): ")
if choice == "1": # cat program
    a = input() 
    print(a)
    exit()
if choice == "2": # Never Gonna Give You Up program
    print("We're no strangers to love \n \
You know the rules and so do I (do I) \n \
A full commitment's what I'm thinking of \n \
You wouldn't get this from any other guy \n \
\n \
I just wanna tell you how I'm feeling \n \
Gotta make you understand \n \
\n \
Never gonna give you up \n \
Never gonna let you down \n \
Never gonna run around and desert you \n \
Never gonna make you cry \n \
Never gonna say goodbye \n \
Never gonna tell a lie and hurt you \n \
\n \
\n \
We've known each other for so long\n \
Your heart's been aching, but you're too shy to say it (say it)\n \
Inside, we both know what's been going on (going on) \n \
We know the game and we're gonna play it \n \
\n \
And if you ask me how I'm feeling\n \
Don't tell me you're too blind to see\n \
\n \
Never gonna give you up\n \
Never gonna let you down\n \
Never gonna run around and desert you\n \
Never gonna make you cry\n \
Never gonna say goodbye\n \
Never gonna tell a lie and hurt you\n \
\n \
Never gonna give you up\n \
Never gonna let you down\n \
Never gonna run around and desert you\n \
Never gonna make you cry\n \
Never gonna say goodbye\n \
Never gonna tell a lie and hurt you\n \
\n \
We've known each other for so long\n \
Your heart's been aching, but you're too shy to say it (say it)\n \
Inside, we both know what's been going on (going on)\n \
We know the game and we're gonna play it\n \
\n \
I just wanna tell you how I'm feeling\n \
Gotta make you understand\n \
\n \
Never gonna give you up\n \
Never gonna let you down\n \
Never gonna run around and desert you\n \
Never gonna make you cry\n \
Never gonna say goodbye\n \
Never gonna tell a lie and hurt you\n \
\n \
Never gonna give you up\n \
Never gonna let you down\n \
Never gonna run around and desert you\n \
Never gonna make you cry\n \
Never gonna say goodbye\n \
Never gonna tell a lie and hurt you\n \
\n \
Never gonna give you up\n \
Never gonna let you down\n \
Never gonna run around and desert you\n \
Never gonna make you cry\n \
Never gonna say goodbye\n \
Never gonna tell a lie and hurt you")
    exit()
if choice == "3": # blank program
    exit()
if choice == "4": # infinite loop program
    while True:
        pass
if choice == "5": # hello world program
    print("Hello, World!")
    exit()
