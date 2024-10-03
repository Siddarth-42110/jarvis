import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "i am"  :"you arere",
    "i was"  :"you were",
    "i"  :"you",
    "i'm"  :"you are",
    "i'd"  :"you would",
    "i've"  :"you have",
    "i'll"  :"you will",
    "my"  :"your",
    "you are"  :"i am",
    "you were"  :"i was",
    "you've"  :"i have",
    "you'll"  :"i will ",
    "your"  :"my",
    "yours"  :"mine",
    "you"  :"me",
    "me"  :"you"
}

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello","Hey there"]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?"]
    ],
    [
        r"what is your name?",
        ["I am a bot created by Siddarth. You can call me Jarvis!"]
    ],
    [
        r"sorry(.*)",
        ["It's alright", "It's OK, nevermind"]
    ],
    [
        r"I am fine",
        ["Great to hear that. how can I help you?"]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude. Seriously, you are asking me this?"]
    ],
    [
        r"what (.*) want?",
        ["Make me an offer I can't refuse"]
    ],
    [
        r"(.*) created?",
        ["Siddarth created me using Python's NLTK library", "Top secret ;)"]
    ],
    [
        r"(.*) (location|city)?",
        ["Scotland, dunfermline"]
    ],
    [
        r"how is the weather in (.*)",
        ["the weather in %1 is awesome like always", "Too hot her in %1", "Too cold here in %1"]
    ],
    [
        r"i work in (.*)",
        ["%1 is an amazing company, though I've heard they are facing some challenges lately."]
    ],
    [
        r"(.*) raining in (.*)",
        ["No rain since last week here in %2", "Damn, it's raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy"]
    ],
]

def  chat():
    print("Hi! I am a chatbot created by Siddarth, for your service.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chat()