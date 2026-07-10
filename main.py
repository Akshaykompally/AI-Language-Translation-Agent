import os
from typing import TypedDict
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
import pyttsx3

class State(TypedDict):
    User_input : str
    Language_entry : str
    Grammar_check : str
    Meaning_Tone : str
    Translate_Text : str


load_dotenv()

model = ChatMistralAI(model="mistral-small-2506")



def Grammar_check(state:State) -> dict:

    prompt = (
        "You are a Grammar Check Agent"
        "Correct only grammar or spelling if needed."
        "Return ONLY the corrected translated text."
        "Do not explain anything."
        f"Text:{state['Meaning_Tone']}"
    )

    response = model.invoke(prompt)

    return {"Grammar_check": response.content.strip()}

def Meaning_Tone(state:State) -> dict:


    prompt = (
        """
        Compare the original text and the translated text.
        If the translation is correct, return ONLY the translated text.
        If it is incorrect, correct it and return ONLY the corrected translated text.
        Do not explain anything.
        """
        f"Text:{state['User_input']}"
        f"Language:{state['Language_entry']}"

    )

    response = model.invoke(prompt)

    return {"Meaning_Tone":response.content.strip()}




def Translate_Text(state:State) -> dict:

    prompt =(
        "You are a Translation Agent."
        "Translate the given text from the source language to the target language."
        "Preserve the original meaning and context."
        "Return only the translated text."
        """"
        Rules:
        - Return ONLY the translated text.
        - No explanation.
        - No notes.
        - No markdown.
        - No quotes.
        - No extra words
        """
        f"Text:{state['User_input']}"
        f"Language:{state['Language_entry']}"

    )

    response = model.invoke(prompt)

    return {"Translate_Text":response.content.strip()}

graph = StateGraph(State)

graph.add_node("Grammar",Grammar_check)
graph.add_node("Meaning",Meaning_Tone)
graph.add_node("Translate",Translate_Text)


graph.add_edge(START,"Translate")
graph.add_edge("Translate","Meaning")
graph.add_edge("Meaning","Grammar")
graph.add_edge("Grammar",END)


app = graph.compile()

def translate(user_input, language):
    result = app.invoke({
        "User_input": user_input,
        "Language_entry": language
    })
    return result["Grammar_check"]

def speak(text):
    engine = pyttsx3.init()
    engine.stop()
    text = text.strip().split("\n")[-1]
    engine.say(text)
    engine.runAndWait()
