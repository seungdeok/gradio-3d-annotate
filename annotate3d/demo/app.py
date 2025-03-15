
import gradio as gr
from gradio_annotate3d import annotate3d

with gr.Blocks() as demo:
    gr.Markdown(
        "# Hello world")

if __name__ == "__main__":
    demo.launch(debug=True)
