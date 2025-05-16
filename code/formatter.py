import gradio as gr
import os

def greet(name):
    updated = ""
    capitalize = True
    spaced = False
    for i in name:
        if(i == ' ' and spaced == False):
            spaced = True
            capitalize = True
            updated += i
        elif(i == ' ' and spaced == True):
            capitalize = True
            pass
        elif(i.isalpha() == False):
            updated += i
            spaced = False
        elif(capitalize == True):
            updated += i.upper()
            capitalize = False
            spaced = False
        else:
            updated += i.lower()
            spaced = False
    
    return updated

demo = gr.Interface(
    fn=greet,
    inputs=["text"],
    outputs=["text"],
)

proxy_prefix = os.environ.get("PROXY_PREFIX")
demo.launch(server_name="0.0.0.0", server_port=8080, root_path=proxy_prefix)