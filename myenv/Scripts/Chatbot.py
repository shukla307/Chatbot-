import os
from typing import List, Tuple, Any, Dict
from langgraph.prebuilt import ToolMessage
from langgraph.graph import Graph, END
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
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



