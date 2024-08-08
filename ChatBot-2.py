
import os
import pyttsx3 
import speech_recognition as sr
import pyaudio
import datetime
from typing import List, Tuple, Any, Dict
import google.generativeai as genai
from dotenv import load_dotenv
import tkinter as tk
from tkinter import ttk


load_dotenv()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Video Game Chatbot , ready to talk about video games. What would you like to discuss?")
    speak(" Thankyou")             




# Google AI API
genai.configure(api_key="AIzaSyCTD1IDdOULrsyog7AB_UgRKLxOP6d0Kto")

model = genai.GenerativeModel('gemini-pro')

def is_video_game_related(user_input: str) -> bool:
    """Check if the user input is related to video games."""
    prompt = f"""
    Determine if the following text is related to video games. Respond with only 'True' or 'False'.
    Text: {user_input}
    """
    response = model.generate_content(prompt)
    return response.text.strip().lower() == 'true'

def generate_response(user_input: str) -> str:
    """Generate a response to a video game-related query."""
    prompt = f"""
    You are a chatbot that only discusses video games. Respond to the following query about video games:
    {user_input}
    """
    response = model.generate_content(prompt)
    return response.text

class VideoGameChatbot(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Video Game Chatbot")
        self.geometry("600x400")

        # color theme
        self.configure(bg="#1a1a2e")
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#1a1a2e")
        self.style.configure("TButton", background="#0f3460", foreground="#ffffff")
        self.style.configure("TEntry", fieldbackground="#0f3460", foreground="#2C3E50")
        self.style.configure("TText", background="#16213e", foreground="#ffffff")
        
        # Chat history 
        self.chat_history = tk.Text(self, height=15, width=60, bg="#16213e", fg="#ffffff", bd=0, padx=10, pady=10, wrap=tk.WORD)
        self.chat_history.config(state=tk.DISABLED)
        self.chat_history.pack(pady=10, padx=10)

        # Frame for input field and send button
        self.input_frame = ttk.Frame(self)

        self.input_entry = ttk.Entry(self.input_frame, width=30, font=("Arial", 14))  # Slightly smaller font
        #self.input_entry.pack(side=tk.LEFT, padx=10)

        #self.input_entry = ttk.Entry(self.input_frame, font=("Arial", 15))
        self.input_entry.pack(side=tk.LEFT, padx=5)
        self.send_button = ttk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button = tk.Button(self.input_frame, text="Send", bg="#1ABC9C", fg="#FFFFFF", font=("Arial", 16), relief=tk.FLAT, command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=5)
        #self.send_button = tk.Button(self.input_frame, text="Send", bg="#1ABC9C", fg="#FFFFFF", font=("Arial", 16), relief=tk.FLAT, command=self.send_message)
        self.input_frame.pack(pady=10)
        

        self.display_message("Video Game Chatbot: Hello! I'm ready to talk about video games. What would you like to discuss?")
        wishMe() 
    
    
    def display_message(self, message: str):
        """Display a message in the chat history."""
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, f"{message}\n")
        self.chat_history.config(state=tk.DISABLED)
        self.chat_history.see(tk.END)

    def send_message(self):
        user_input = self.input_entry.get().strip()
        self.input_entry.delete(0, tk.END)

        if user_input.lower() in ['exit', 'quit', 'bye']:
            self.display_message("Video Game Chatbot: Goodbye! Thanks for chatting about video games.")
            self.after(2000, self.destroy)
        elif is_video_game_related(user_input):
            response = generate_response(user_input)
            self.display_message(f"You: {user_input}")
            self.display_message(f"Video Game Chatbot: {response}")
        else:
    
            self.display_message("Video Game Chatbot: I'm sorry, I can only discuss video games. Please ask me something related to video games.")
            speak("I'm sorry, I can only discuss video games. Please ask me something related to video games")
        
if __name__ == "__main__":
      
    app = VideoGameChatbot()
       
    app.mainloop()
     





