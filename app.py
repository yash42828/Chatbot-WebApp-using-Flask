from chatbot import chatbot
import win32com.client
from flask import Flask, render_template, request
#speaker = win32com.client.Dispatch("SAPI.SpVoice")
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    #speaker.Speak(userText)    
    resp = str(chatbot.get_response(userText))
    #print(resp)
    #tts.Speak("Hello, fellow Python programmer")
    #speaker.Speak("Hello, fellow Python programmer")    
    #speak(resp)
    return (resp)

if __name__ == "__main__":
    app.run()