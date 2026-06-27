from maverick_oss.config import build_agent_config


def test_build_agent_config_contains_exactly_four_agents():
    config = build_agent_config(api_key="test-key")

    assert set(config) == {"A1", "A2", "A3", "A4"}
    assert all(agent_config.api_key == "test-key" for agent_config in config.values())
