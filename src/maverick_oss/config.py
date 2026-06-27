from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AgentConfig:
    api_key: str
    base_url: str = "https://api.openai.com/v1"
    model: str = "gpt-4o-mini"
    temperature: float = 0.2


def build_agent_config(
    api_key: str,
    base_url: str = "https://api.openai.com/v1",
    model: str = "gpt-4o-mini",
) -> dict[str, AgentConfig]:
    """Build a shared demo configuration for all four agents."""
    return {
        "A1": AgentConfig(api_key=api_key, base_url=base_url, model=model, temperature=0.2),
        "A2": AgentConfig(api_key=api_key, base_url=base_url, model=model, temperature=0.3),
        "A3": AgentConfig(api_key=api_key, base_url=base_url, model=model, temperature=0.2),
        "A4": AgentConfig(api_key=api_key, base_url=base_url, model=model, temperature=0.2),
    }
