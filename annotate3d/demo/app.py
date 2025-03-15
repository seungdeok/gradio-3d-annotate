
import gradio as gr
from gradio_annotate3d import annotate3d


with gr.Blocks() as demo:
    gr.Markdown(
        "# Change the value (keep it JSON) and the front-end will update automatically.")
    annotate3d(value={"message": "Hello from Gradio!"}, label="Static")


if __name__ == "__main__":
    demo.launch(debug=True)
