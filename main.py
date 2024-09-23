import speech_recognition as sr;
import webbrowser;
import pyttsx3;
import musicLibrary;
import requests;
from hugchat import hugchat;

recognizer = sr.Recognizer();
engine = pyttsx3.init();

def speak(text):
    engine.say(text);
    engine.runAndWait();
    
def ai_process(command):
    
    user_input = command.lower()
    chatbot = hugchat.ChatBot(cookie_path="cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    # speak(response)
    return response


def processComand(c):
    # print(c);
    if "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif c.lower().startswith('play'):
        song = c.lower().split(" ")[1];
        link = musicLibrary.music[song];
        webbrowser.open(link);
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=0266969321104e50a6113ed3917c0974");
        if r.status_code == 200:
            data = r.json();
            articcles = data.get('articles', []);
            
            for article in articcles:
                speak(article['title']);
    else:
        output = ai_process(c);
        speak(output);                
    pass;

if __name__ == "__main__":
    speak('initializing Jarvis...');
    while True:
        print("reocgnizeing");
        try:
            with sr.Microphone() as source:
                print('Listening.....');
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2);
            word = recognizer.recognize_google(audio);
            if(word.lower() == "jarvis"):
                speak('yes');
                with sr.Microphone() as source:
                    print('jarvis active.....');
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=5);
                    command = recognizer.recognize_google(audio);
                    
                    processComand(command);
                
        except Exception as e:
            print("sphinx error ; (0)".format(e));