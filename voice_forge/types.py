from pathlib import Path
from typing import Any, Dict, List, Tuple

from pydantic import BaseModel


class Language(BaseModel):
    code: str
    family: str
    region: str
    name_native: str
    name_english: str
    country_english: str


class File(BaseModel):
    size_bytes: int
    md5_digest: str


class SpeakerData(BaseModel):
    key: str
    name: str
    language: Language
    quality: str
    num_speakers: int
    speaker_id_map: Dict[str, Any]
    files: Dict[str, File]
    aliases: List[str] = []

    def get_path(self) -> str:
        return f"{self.language.family}/{self.language.code}/{self.name}/{self.quality}/{self.key}"

    def get_onnx(self) -> Tuple[Path, File]:
        path = f"{self.get_path()}.onnx"
        return Path(path), self.files[path]

    def get_json(self) -> Tuple[Path, File]:
        path = f"{self.get_path()}.onnx.json"
        return Path(path), self.files[path]
