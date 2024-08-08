# import os
# from typing import List, Tuple, Any, Dict
# import google.generativeai as genai
# from dotenv import load_dotenv
# import tkinter as tk
# from tkinter import ttk

# # Load environment variables
# load_dotenv()

# # Configure Google AI API
# genai.configure(api_key="AIzaSyCTD1IDdOULrsyog7AB_UgRKLxOP6d0Kto")

# # Initialize Gemini model
# model = genai.GenerativeModel('gemini-pro')

# def is_video_game_related(user_input: str) -> bool:
#     """Check if the user input is related to video games."""
#     prompt = f"""
#     Determine if the following text is related to video games. Respond with only 'True' or 'False'.
#     Text: {user_input}
#     """
#     response = model.generate_content(prompt)
#     return response.text.strip().lower() == 'true'

# def generate_response(user_input: str) -> str:
#     """Generate a response to a video game-related query."""
#     prompt = f"""
#     You are a chatbot that only discusses video games. Respond to the following query about video games:
#     {user_input}
#     """
#     response = model.generate_content(prompt)
#     return response.text

# class VideoGameChatbot(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Video Game Chatbot")
#         self.geometry("600x400")

#         # Create the chat history text box
#         self.chat_history = tk.Text(self, height=15, width=60)
#         self.chat_history.pack(pady=10)

#         # Create the input entry and send button
#         self.input_frame = tk.Frame(self)
#         self.input_entry = ttk.Entry(self.input_frame, width=50)
#         self.input_entry.pack(side=tk.LEFT, padx=5)
#         self.send_button = ttk.Button(self.input_frame, text="Send", command=self.send_message)
#         self.send_button.pack(side=tk.LEFT, padx=5)
#         self.input_frame.pack(pady=10)

#         self.chat_history.insert(tk.END, "Video Game Chatbot: Hello! I'm ready to talk about video games. What would you like to discuss?\n")

#     def send_message(self):
#         user_input = self.input_entry.get().strip()
#         self.input_entry.delete(0, tk.END)

#         if user_input.lower() in ['exit', 'quit', 'bye']:
#             self.chat_history.insert(tk.END, "Video Game Chatbot: Goodbye! Thanks for chatting about video games.\n")
#             self.after(2000, self.destroy)  # Close the window after 2 seconds
#         elif is_video_game_related(user_input):
#             response = generate_response(user_input)
#             self.chat_history.insert(tk.END, f"You: {user_input}\n")
#             self.chat_history.insert(tk.END, f"Video Game Chatbot: {response}\n")
#         else:
#             self.chat_history.insert(tk.END, "Video Game Chatbot: I'm sorry, I can only discuss video games. Please ask me something related to video games.\n")

#         self.chat_history.see(tk.END)  # Scroll to the end of the chat history

# if __name__ == "__main__":
#     app = VideoGameChatbot()
#     app.mainloop()



#************************** This code is running +++++++++++++++++++++++++++++++++++++

# import os
# from typing import List, Tuple, Any, Dict
# import google.generativeai as genai
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Configure Google AI API
# genai.configure(api_key="AIzaSyCTD1IDdOULrsyog7AB_UgRKLxOP6d0Kto")

# # Initialize Gemini model
# model = genai.GenerativeModel('gemini-pro')

# def is_video_game_related(user_input: str) -> bool:
#     """Check if the user input is related to video games."""
#     prompt = f"""
#     Determine if the following text is related to video games. Respond with only 'True' or 'False'.
#     Text: {user_input}
#     """
#     response = model.generate_content(prompt)
#     return response.text.strip().lower() == 'true'

# def generate_response(user_input: str) -> str:
#     """Generate a response to a video game-related query."""
#     prompt = f"""
#     You are a chatbot that only discusses video games. Respond to the following query about video games:
#     {user_input}
#     """
#     response = model.generate_content(prompt)
#     return response.text

# def chat():
#     """Run the chatbot."""
#     print("Video Game Chatbot: Hello! I'm ready to talk about video games. What would you like to discuss?")
    
#     while True:
#         user_input = input("You: ")
        
#         if user_input.lower() in ['exit', 'quit', 'bye']:
#             print("Video Game Chatbot: Goodbye! Thanks for chatting about video games.")
#             break
        
#         if is_video_game_related(user_input):
#             response = generate_response(user_input)
#             print(f"Video Game Chatbot: {response}")
#         else:
#             print("Video Game Chatbot: I'm sorry, I can only discuss video games. Please ask me something related to video games.")

# if __name__ == "__main__":
#     chat()


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^New code below ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6

import os
from typing import List, Tuple, Any, Dict
from langgraph.prebuilt import ToolMessage
from langgraph.graph import Graph, END
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google AI API

#AIzaSyCTD1IDdOULrsyog7AB_UgRKLxOP6d0Kto
genai.configure(api_key="AIzaSyCTD1IDdOULrsyog7AB_UgRKLxOP6d0Kto")

# Initialize Gemini model
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

def process_user_input(state: Dict[str, Any]) -> Dict[str, Any]:
    """Process user input and update the state."""
    user_input = state['user_input']
    
    if is_video_game_related(user_input):
        response = generate_response(user_input)
        state['response'] = response
    else:
        state['response'] = "I'm sorry, I can only discuss video games. Please ask me something related to video games."
    
    return state

def should_end(state: Dict[str, Any]) -> Tuple[bool, str]:
    """Determine if the conversation should end."""
    return False, "continue"

# Define the graph
workflow = Graph()

# Add nodes to the graph
workflow.add_node("process_input", process_user_input)
workflow.add_node("should_end", should_end)

# Add edges to the graph
workflow.set_entry_point("process_input")
workflow.add_edge("process_input", "should_end")

# Compile the graph
app = workflow.compile()

def chat():
    """Run the chatbot."""
    print("Video Game Chatbot: Hello! I'm ready to talk about video games. What would you like to discuss?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Video Game Chatbot: Goodbye! Thanks for chatting about video games.")
            break
        
        state = {"user_input": user_input}
        result = app(state)
        
        print(f"Video Game Chatbot: {result['response']}")

if __name__ == "__main__":
    chat()

#***********************************88New code *******************************


# import os
# from typing import List, Tuple, Any, Dict
# from langgraph.graph import Graph, END
# import google.generativeai as genai
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Configure Google AI API
# genai.configure(api_key="AIzaSyCTD1IDdOULrsyog7AB_UgRKLxOP6d0Kto")

# # Initialize Gemini model
# model = genai.GenerativeModel('gemini-pro')

# def is_video_game_related(user_input: str) -> bool:
#     """Check if the user input is related to video games."""
#     prompt = f"""
#     Determine if the following text is related to video games. Respond with only 'True' or 'False'.
#     Text: {user_input}
#     """
#     response = model.generate_content(prompt)
#     return response.text.strip().lower() == 'true'

# def generate_response(user_input: str) -> str:
#     """Generate a response to a video game-related query."""
#     prompt = f"""
#     You are a chatbot that only discusses video games. Respond to the following query about video games:
#     {user_input}
#     """
#     response = model.generate_content(prompt)
#     return response.text

# def process_user_input(state: Dict[str, Any]) -> Dict[str, Any]:
#     """Process user input and update the state."""
#     user_input = state['user_input']
    
#     if is_video_game_related(user_input):
#         response = generate_response(user_input)
#         state['response'] = response
#     else:
#         state['response'] = "I'm sorry, I can only discuss video games. Please ask me something related to video games."
    
#     return state

# def should_end(state: Dict[str, Any]) -> Tuple[bool, str]:
#     """Determine if the conversation should end."""
#     return False, "continue"

# # Define the graph
# workflow = Graph()

# # Add nodes to the graph
# workflow.add_node("process_input", process_user_input)

# # Add edges to the graph
# workflow.set_entry_point("process_input")
# workflow.add_edge("process_input", should_end)

# # Compile the graph
# app = workflow.compile()

# def chat():
#     """Run the chatbot."""
#     print("Video Game Chatbot: Hello! I'm ready to talk about video games. What would you like to discuss?")
    
#     while True:
#         user_input = input("You: ")
        
#         if user_input.lower() in ['exit', 'quit', 'bye']:
#             print("Video Game Chatbot: Goodbye! Thanks for chatting about video games.")
#             break
        
#         state = {"user_input": user_input}
#         result = app(state)
        
#         print(f"Video Game Chatbot: {result['response']}")

# if __name__ == "__main__":
#     chat()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4

# import os
# from typing import List, Tuple, Any, Dict
# from langgraph.prebuilt import ToolMessage
# from langgraph.graph import Graph, END
# import google.generativeai as genai
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Configure Google AI API

# GOOGLE_AI_API_KEY="AIzaSyCTD1IDdOULrsyog7AB_UgRKLxOP6d0Kto"
# genai.configure(api_key=os.getenv("GOOGLE_AI_API_KEY"))

# # Initialize Gemini model
# model = genai.GenerativeModel('gemini-pro')

# def is_video_game_related(user_input: str) -> bool:
#     """Check if the user input is related to video games."""
#     prompt = f"""
#     Determine if the following text is related to video games. Respond with only 'True' or 'False'.
#     Text: {user_input}
#     """
#     response = model.generate_content(prompt)
#     return response.text.strip().lower() == 'true'

# def generate_response(user_input: str) -> str:
#     """Generate a response to a video game-related query."""
#     prompt = f"""
#     You are a chatbot that only discusses video games. Respond to the following query about video games:
#     {user_input}
#     """
#     response = model.generate_content(prompt)
#     return response.text

# def process_user_input(state: Dict[str, Any]) -> Dict[str, Any]:
#     """Process user input and update the state."""
#     user_input = state['user_input']
    
#     if is_video_game_related(user_input):
#         response = generate_response(user_input)
#         state['response'] = response
#     else:
#         state['response'] = "I'm sorry, I can only discuss video games. Please ask me something related to video games."
    
#     return state

# def should_end(state: Dict[str, Any]) -> Tuple[bool, str]:
#     """Determine if the conversation should end."""
#     return False, "continue"

# # Define the graph
# workflow = Graph()

# # Add nodes to the graph
# workflow.add_node("process_input", process_user_input)

# # Add edges to the graph
# workflow.set_entry_point("process_input")
# workflow.add_edge("process_input", should_end)

# # Compile the graph
# app = workflow.compile()

# def chat():
#     """Run the chatbot."""
#     print("Video Game Chatbot: Hello! I'm ready to talk about video games. What would you like to discuss?")
    
#     while True:
#         user_input = input("You: ")
        
#         if user_input.lower() in ['exit', 'quit', 'bye']:
#             print("Video Game Chatbot: Goodbye! Thanks for chatting about video games.")
#             break
        
#         state = {"user_input": user_input}
#         result = app(state)
        
#         print(f"Video Game Chatbot: {result['response']}")

# if __name__ == "__main__":
#     chat()