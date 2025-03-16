
import gradio as gr
from gradio_annotate3d import annotate3d


def update_config_annotate3d(tool, point_cloud_url):
    if not point_cloud_url:
        raise gr.Error('URL을 입력해주세요')
    if not str(point_cloud_url).endswith(('.ply', '.splat', '.bin')):
        raise gr.Error('.ply, .splat, .bin파일이 아닙니다.')
    if not tool:
        raise gr.Error('Tool을 선택해주세요')

    data = {
        "tool": tool,
        "point_cloud_url": point_cloud_url,
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
            point_cloud_url = gr.Textbox(
                label="Point Cloud URL",
                placeholder="URL을 입력해주세요(.bin, .ply, .splat)"
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
        inputs=[tool_combo, point_cloud_url],
        outputs=annotate_component
    )

if __name__ == "__main__":
    demo.launch(debug=True, share=False)
