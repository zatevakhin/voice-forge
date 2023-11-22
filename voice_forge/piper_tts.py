import operator as op
from functools import reduce
from pathlib import Path
from typing import Tuple

import numpy as np


class PiperTts:
    def __init__(self, model_name: str, model_dir: str, use_cuda: bool = False) -> None:
        from piper import PiperVoice

        model_location = Path(model_dir) / model_name
        model = f"{model_location}.onnx"
        model_config = f"{model}.json"

        self.tts = PiperVoice.load(model, config_path=model_config, use_cuda=use_cuda)

    # TODO: Make `Protocol` with list of methods, when other tts engines will be added
    def synthesize_stream(self, text: str) -> Tuple[np.ndarray[np.int16], int]:
        data = self.tts.synthesize_stream_raw(text)
        data = np.frombuffer(reduce(op.add, data), dtype=np.int16)

        return data, self.tts.config.sample_rate
