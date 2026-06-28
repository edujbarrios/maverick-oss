# maverick-oss

**Multi-Agent Validation for Explainable Visual Reasoning and Image Consistency Knowledge**

## Overview

**maverick-oss** is the open-source, reference-free release of the broader **MAVERICK** research framework, developed as part of a Master's Thesis in Artificial Intelligence by **Eduardo J. Barrios**.

The repository provides a modular pipeline for image description with vision-language models (VLMs). It is designed for research contexts that require interpretable visual reasoning, explicit uncertainty handling, and configurable prompt-based experimentation.

## Cognitive Inspiration

MAVERICK is motivated by evidence that visual understanding is not a single-pass process. Human observers identify objects and regions, organize spatial and semantic relations, integrate prior knowledge, and revise interpretations when ambiguity or inconsistency is detected. This view is consistent with research on scene perception and visual cognition, where object recognition, eye movements, scene interpretation, and cognitive processing interact dynamically ([Henderson & Hollingworth, 1999](https://doi.org/10.1146/annurev.psych.50.1.243)). It also follows the broader account of vision as an interaction between low-level visual input, spatial organization, object structure, and higher-level interpretation ([Palmer, 1999](https://mitpress.mit.edu/9780262161831/vision-science/)).

maverick-oss operationalizes this process as four stages:

1. **Identification**: detect salient visual elements, attributes, regions, and uncertainties.
2. **Description**: generate an initial image description from the identified elements.
3. **Critique**: evaluate the description for completeness, clarity, uncertainty, and unsupported claims.
4. **Refinement**: produce a revised final description using the observations and critique.

## Architecture

The system contains exactly four configurable agents:

| Agent | Name | Role |
| --- | --- | --- |
| A1 | Identifier | Extracts salient objects, entities, regions, attributes, and uncertainties from the image. |
| A2 | Descriptor | Generates an initial description from A1 observations. |
| A3 | Critic | Reviews the description without using an external reference description. |
| A4 | Refiner | Produces the final description by integrating A1, A2, and A3 outputs. |

Each agent can be assigned its own model, API key, base URL, temperature, and prompt. The implementation uses an OpenAI-compatible chat-completion interface, allowing different hosted or local providers to be tested through the same abstraction.

## Prompts

Prompts are stored in `src/maverick_oss/prompts.py`:

- `A1_IDENTIFIER_PROMPT`
- `A2_DESCRIPTOR_PROMPT`
- `A3_CRITIC_PROMPT`
- `A4_REFINER_PROMPT`

The default prompts follow **structured prompting** principles: each prompt defines the agent role, task objective, input contract, reasoning procedure, constraints, and expected output format. They are intentionally domain-general and should be adapted for specific experimental settings.

Prompt behavior should be treated as experimentally sensitive. VLM outputs can vary with prompt wording, decoding parameters, model family, and visual encoder design. In transformer-based vision systems, image evidence is often represented through patch-level tokens; therefore, patch resolution, visual tokenization, and cross-modal alignment may influence which objects, attributes, colors, and spatial relations are emphasized. maverick-oss keeps agents, prompts, and models configurable because different LLM/VLM backends may show different concept associations, spatial-reasoning limitations, and grounding behavior, as reported in work on concept association bias ([Yamada et al., 2024](https://doi.org/10.48550/arXiv.2212.12043)) and spatial reasoning in vision-language models ([Kamath et al., 2023](https://doi.org/10.18653/v1/2023.emnlp-main.568)).

## Execution Mode

This repository supports **reference-free execution only**.

The full MAVERICK research framework includes additional reference-based validation components. Those components, including external text-to-text validation modules and unpublished evaluation metrics, are not included in this public release.

maverick-oss therefore does not compare generated descriptions against reference descriptions. The public release is limited to the four-agent reference-free pipeline described above.

## API Requirements

maverick-oss uses an **OpenAI-compatible API** for VLM and language-model calls. Compatible providers include OpenAI, llm7.io, local OpenAI-compatible endpoints, and other services exposing `/chat/completions` APIs.

Hosted providers require API keys. Credentials and provider endpoints must be configured locally and should not be committed to version control.

## Configuration

A minimal configuration assigns credentials per agent:

```python
AGENT_CONFIG = {
    "A1": {"api_key": "..."},
    "A2": {"api_key": "..."},
    "A3": {"api_key": "..."},
    "A4": {"api_key": "..."},
}
```

A complete configuration may specify provider, model, and decoding parameters:

```python
AGENT_CONFIG = {
    "A1": {
        "api_key": "YOUR_API_KEY",
        "base_url": "https://api.openai.com/v1",
        "model": "gpt-4o-mini",
        "temperature": 0.2,
    },
    "A2": {
        "api_key": "YOUR_API_KEY",
        "base_url": "https://api.openai.com/v1",
        "model": "gpt-4o-mini",
        "temperature": 0.3,
    },
    "A3": {
        "api_key": "YOUR_API_KEY",
        "base_url": "https://api.openai.com/v1",
        "model": "gpt-4o-mini",
        "temperature": 0.2,
    },
    "A4": {
        "api_key": "YOUR_API_KEY",
        "base_url": "https://api.openai.com/v1",
        "model": "gpt-4o-mini",
        "temperature": 0.2,
    },
}
```

Environment variables are also supported:

```bash
OPENAI_API_KEY=your_api_key
OPENAI_BASE_URL=https://api.openai.com/v1
MAVERICK_MODEL=gpt-4o-mini
```

For local inference servers, set `OPENAI_BASE_URL` to the local OpenAI-compatible endpoint.

## Streamlit UI

maverick-oss includes a minimal Streamlit interface for image upload, pipeline execution, and inspection of A1-A4 outputs.

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the interface:

```bash
streamlit run maverick-oss.py
```

## Open Source Scope

maverick-oss is a simplified public release intended to support transparent, reproducible research on multi-agent VLM workflows. It excludes unpublished components from the full MAVERICK framework while preserving a usable foundation for reference-free visual reasoning experiments.

## License

This project is licensed under the **Mozilla Public License 2.0 (MPL-2.0)**.

Attribution to **Eduardo J. Barrios** is required in derivative works, publications, and redistributed versions of this project. See `LICENSE` for the license notice and terms.

## Citation

If you use maverick-oss in academic or applied work, please cite the repository using the metadata in `CITATION.cff`.

```bibtex
@software{barrios_maverick_oss_2026,
  author = {Barrios, Eduardo J.},
  title = {maverick-oss: A Reference-Free Multi-Agent Pipeline for Image Description with Vision-Language Models},
  year = {2026},
  license = {MPL-2.0}
}
```

## Disclaimer

maverick-oss is provided for research and educational purposes. Users are responsible for validating outputs before applying the system in high-stakes or domain-specific settings.
