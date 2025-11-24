from enum import Enum


class ModelType(str, Enum):
    """
    High-level classification of model implementation types supported by
    the system.

    **Values**

    - **Api** — External API-based model accessible via HTTP.
    - **Pytorch_jit** — Model packaged as a PyTorch JIT artifact.
    - **Transformer_hf** — HuggingFace transformer model.
    """
    Api = "Api"
    Pytorch_jit = "Pytorch_jit"
    Transformer_hf = "Transformer_hf"
