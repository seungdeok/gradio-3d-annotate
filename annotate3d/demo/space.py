
import gradio as gr
from app import demo as app
import os

_docs = {'annotate3d': {'description': 'A base class for defining methods that all input/output components should have.', 'members': {'__init__': {'interactive': {'type': 'bool | None', 'default': 'None', 'description': None}}, 'postprocess': {}, 'preprocess': {}}, 'events': {}}, '__meta__': {'additional_interfaces': {}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_annotate3d`

<div style="display: flex; gap: 7px;">
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange">  
</div>

annotate3d
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_annotate3d
```

## Usage

```python

import gradio as gr
from gradio_annotate3d import annotate3d
import numpy as np


def load_point_cloud(point_cloud_url):
    '''
    TODO pointcloud parsing
    '''
    return np.random.rand(1000, 3) * 2 - 1


def update_config_annotate3d(tool, point_cloud_url):
    if not point_cloud_url:
        raise ValueError('URL을 입력해주세요')
    if not tool:
        raise ValueError('Tool을 선택해주세요')

    data = {
        "tool": tool,
        "points": load_point_cloud(point_cloud_url).tolist()
    }

    return data


with gr.Blocks() as demo:
    gr.Markdown(
        "# 3D Point Cloud Annotation")

    with gr.Row():
        with gr.Column(scale=1):
            tool_combo = gr.Dropdown(
                choices=["BoundingBox"],
                value="BoundingBox",
                label="Annotation Tool",
                interactive=True
            )
            point_url = gr.Textbox(
                label="Point Cloud URL",
                placeholder="URL을 입력해주세요(.bin, .pcd)"
            )
            update_btn = gr.Button("Submit")

        with gr.Column(scale=4):
            annotate_component = annotate3d(
                label="3D Point Cloud Annotation",
                interactive=True
            )

    with gr.Row():
        result_json = gr.JSON(label="Annotation3D 결과")

    '''
    annotate_component:value로 주입
    '''
    update_btn.click(
        fn=update_config_annotate3d,
        inputs=[tool_combo, point_url],
        outputs=annotate_component
    )

if __name__ == "__main__":
    demo.launch(debug=True, share=False)

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `annotate3d`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["annotate3d"]["members"]["__init__"], linkify=[])







    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {};
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
