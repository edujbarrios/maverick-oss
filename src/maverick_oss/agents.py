from __future__ import annotations

from dataclasses import dataclass

from PIL import Image

from maverick_oss.clients import OpenAICompatibleClient
from maverick_oss.config import AgentConfig


@dataclass
class VisionAgent:
    name: str
    role: str
    prompt: str
    config: AgentConfig

    def __post_init__(self) -> None:
        self.client = OpenAICompatibleClient(self.config)

    def run_with_image(self, user_prompt: str, image: Image.Image) -> str:
        return self.client.vision_chat(self.prompt, user_prompt, image)

    def run_text(self, user_prompt: str) -> str:
        return self.client.text_chat(self.prompt, user_prompt)
