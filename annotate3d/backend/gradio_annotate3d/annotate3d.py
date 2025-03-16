from gradio.components.base import Component
import json
import numpy as np


class annotate3d(Component):
    def __init__(
        self,
        value=None,
        label=None,
        interactive: bool | None = None,
    ):
        """
        Args:
            value: data(points, tool)
            label: component label
        """
        self.value = value or {"points": [], "tool": None}
        super().__init__(label=label, interactive=interactive)

    def preprocess(self, payload):
        """
        frontend(JSON 문자열) -> backend(Python 객체)
        """
        if payload is not None and isinstance(payload, str):
            payload = json.loads(payload)
        print('preprocess', payload)
        return payload

    def postprocess(self, value):
        """
        backend(Python 객체) -> frontend(JSON 문자열)
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
        points = np.random.rand(100, 3) * 2 - 1
        return {"points": points.tolist(), "tools": "BoundingBox"}
