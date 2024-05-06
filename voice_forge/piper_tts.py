import operator as op
from functools import reduce
from pathlib import Path
from typing import Tuple
import json
import os

import numpy as np
import logging
import httpx

from huggingface_hub import hf_hub_download

from voice_forge.config import (
    PIPER_VOICES_MAP_URL,
    PIPER_VOICES_VERSION,
    PIPER_VOICES_REPO_ID,
    PIPER_VOICES_JSON,
    PIPER_VOICES_MODELS_DIR_GITIGNORE,
)
from voice_forge.types import SpeakerData

logger = logging.getLogger(__name__)


class PiperTts:
    def __init__(self, model_name: str, model_dir: str, use_cuda: bool = False) -> None:
        from piper import PiperVoice

        model, config = self.get_or_download(model_name, model_dir)
        self.tts = PiperVoice.load(model, config_path=config, use_cuda=use_cuda)

    @staticmethod
    def get_or_download(model_name: str, model_dir: str) -> Tuple[Path, Path]:
        if not Path(model_dir).exists():
            os.makedirs(model_dir)

        gitignore = Path(model_dir) / PIPER_VOICES_MODELS_DIR_GITIGNORE
        with open(gitignore, "w") as f:
            f.writelines(["*", ""])

        voices_json = Path(model_dir) / PIPER_VOICES_JSON
        if not voices_json.exists():
            r = httpx.get(PIPER_VOICES_MAP_URL)
            voices_map = r.json()

            with open(voices_json, "w") as f:
                json.dump(voices_map, f, indent=2)
        else:
            with open(voices_json, "r") as f:
                voices_map = json.load(f)

        if model_name not in voices_map:
            logger.warn(f"The `{model_name}` is not present in '{PIPER_VOICES_MAP_URL}'.")

        voice = voices_map[model_name]

        spk = SpeakerData(**voice)
        model_path, _ = spk.get_onnx()
        config_path, _ = spk.get_json()

        model = hf_hub_download(
            repo_id=PIPER_VOICES_REPO_ID,
            filename=str(model_path),
            revision=f"{PIPER_VOICES_VERSION}",
            local_dir=model_dir,
        )
        config = hf_hub_download(
            repo_id=PIPER_VOICES_REPO_ID,
            filename=str(config_path),
            revision=f"{PIPER_VOICES_VERSION}",
            local_dir=model_dir,
        )

        return Path(model), Path(config)

    # TODO: Make `Protocol` with list of methods, when other tts engines will be added
    def synthesize_stream(self, text: str) -> Tuple[np.ndarray[np.int16], int]:
        data = self.tts.synthesize_stream_raw(text)
        data = np.frombuffer(reduce(op.add, data), dtype=np.int16)

        return data, self.tts.config.sample_rate
