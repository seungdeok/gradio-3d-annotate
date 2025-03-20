from gradio.components.base import Component
import json


class annotate3d(Component):
    def __init__(
        self,
        value=None,
        label=None,
        interactive: bool | None = None,
    ):
        """
        Args:
            value: { point_cloud_url, tool }
            label: component label
        """
        self.value = value or {"point_cloud_url": None, "tool": None}
        super().__init__(label=label, interactive=interactive)

    def preprocess(self, payload):
        """
        frontend:value -> backend(Python 객체) -> gradio
        """
        if payload is not None and isinstance(payload, str):
            payload = json.loads(payload)
        print('preprocess', payload)
        return payload

    def postprocess(self, value):
        """
        gradio -> backend(Python 객체) -> frontend:value
        """
        if value is not None:
            value = json.dumps(value)
        print('postprocess', value)
        return value

    def example_payload(self):
        return {}

    def example_value(self):
        return {}

    def example_inputs(self):
        return {}

    def api_info(self):
        """
        document example
        """
        return {"point_cloud_url": 'https://example.com/test.pcd', "tools": "BoundingBox"}
