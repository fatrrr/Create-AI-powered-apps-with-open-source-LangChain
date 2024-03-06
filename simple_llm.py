import os
'''from langchain_openai import ChatOpenAI
import gradio as gr

# Memasukkan API key
os.environ["OPENAI_API_KEY"] = ["OPENAI_API_KEY"]

gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo" )

def chatbot(prompt):
    return gpt3.invoke(prompt).content

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)
'''
# Menggunakan Hugging FaceHub
from langchain_community.llms import HuggingFaceEndpoint

# Set the Hugging Face API token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = ["HUGGINGFACEHUB_API_TOKEN"]

# Initialize the HuggingFaceEndpoint
llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")

# Define the text to be passed to the model
text = "Beritahu fakta menarik tentang kentang!"

try:
    # Invoke the model and get the result
    result = llm.invoke(text)
    print("Result:", result)
except Exception as e:
    # Print any errors that occur during model invocation
    print("Error:", e)