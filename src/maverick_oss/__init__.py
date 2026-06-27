"""MAVERICK-OSS reference-free multi-agent image description pipeline."""

__all__ = ["MaverickPipeline"]


def __getattr__(name: str):
    if name == "MaverickPipeline":
        from maverick_oss.pipeline import MaverickPipeline

        return MaverickPipeline
    raise AttributeError(name)
