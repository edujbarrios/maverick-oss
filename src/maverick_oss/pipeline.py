from __future__ import annotations

from PIL import Image

from maverick_oss.agents import VisionAgent
from maverick_oss.config import AgentConfig
from maverick_oss.prompts import (
    A1_IDENTIFIER_PROMPT,
    A2_DESCRIPTOR_PROMPT,
    A3_CRITIC_PROMPT,
    A4_REFINER_PROMPT,
)


class MaverickPipeline:
    """Reference-free maverick-oss pipeline with four cognitive-inspired agents."""

    def __init__(self, config: dict[str, AgentConfig]) -> None:
        required_agents = {"A1", "A2", "A3", "A4"}
        missing = required_agents.difference(config)
        if missing:
            raise ValueError(f"Missing agent configuration for: {', '.join(sorted(missing))}")

        self.a1 = VisionAgent("A1", "Identifier", A1_IDENTIFIER_PROMPT, config["A1"])
        self.a2 = VisionAgent("A2", "Descriptor", A2_DESCRIPTOR_PROMPT, config["A2"])
        self.a3 = VisionAgent("A3", "Critic", A3_CRITIC_PROMPT, config["A3"])
        self.a4 = VisionAgent("A4", "Refiner", A4_REFINER_PROMPT, config["A4"])

    def run(self, image: Image.Image) -> dict[str, str]:
        a1_output = self.a1.run_with_image(
            "Identify the salient visual content in this image using the required output format.",
            image,
        )

        a2_output = self.a2.run_with_image(
            f"Generate an initial image description using these A1 notes:\n\n{a1_output}",
            image,
        )

        a3_output = self.a3.run_with_image(
            "Critique the description in reference-free mode.\n\n"
            f"A1 identification notes:\n{a1_output}\n\n"
            f"A2 initial description:\n{a2_output}",
            image,
        )

        a4_output = self.a4.run_with_image(
            "Refine the description in reference-free mode.\n\n"
            f"A1 identification notes:\n{a1_output}\n\n"
            f"A2 initial description:\n{a2_output}\n\n"
            f"A3 critique:\n{a3_output}",
            image,
        )

        return {
            "A1": a1_output,
            "A2": a2_output,
            "A3": a3_output,
            "A4": a4_output,
        }
