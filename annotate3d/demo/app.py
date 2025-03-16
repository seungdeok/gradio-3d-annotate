
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
                label="3D Point Cloud Annotation"
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
