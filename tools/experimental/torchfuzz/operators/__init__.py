"""Torchfuzz operators module."""

# pyrefly: ignore  # import-error
from torchfuzz.operators.arg import ArgOperator

# pyrefly: ignore  # import-error
from torchfuzz.operators.base import Operator

# pyrefly: ignore  # import-error
from torchfuzz.operators.constant import ConstantOperator

# pyrefly: ignore  # import-error
from torchfuzz.operators.item import ItemOperator

# pyrefly: ignore  # import-error
from torchfuzz.operators.layout import (
    FlattenOperator,
    ReshapeOperator,
    SqueezeOperator,
    UnsqueezeOperator,
    ViewOperator,
)

# pyrefly: ignore  # import-error
from torchfuzz.operators.matrix_multiply import (
    AddmmOperator,
    BmmOperator,
    MatmulOperator,
    MMOperator,
)

# pyrefly: ignore  # import-error
from torchfuzz.operators.nn_functional import (
    DropoutOperator,
    EmbeddingOperator,
    LayerNormOperator,
    LinearOperator,
    ReLUOperator,
    SoftmaxOperator,
)

# pyrefly: ignore  # import-error
from torchfuzz.operators.registry import (
    get_operator,
    list_operators,
    register_operator,
    set_operator_weight,
    set_operator_weight_by_torch_op,
    set_operator_weights,
    set_operator_weights_by_torch_op,
)

# pyrefly: ignore  # import-error
from torchfuzz.operators.scalar_pointwise import (
    ScalarAddOperator,
    ScalarDivOperator,
    ScalarMulOperator,
    ScalarPointwiseOperator,
    ScalarSubOperator,
)

# pyrefly: ignore  # import-error
from torchfuzz.operators.tensor_pointwise import (
    AddOperator,
    DivOperator,
    MulOperator,
    PointwiseOperator,
    SubOperator,
)


__all__ = [
    "Operator",
    "PointwiseOperator",
    "AddOperator",
    "MulOperator",
    "SubOperator",
    "DivOperator",
    "ScalarPointwiseOperator",
    "ScalarAddOperator",
    "ScalarMulOperator",
    "ScalarSubOperator",
    "ScalarDivOperator",
    "ItemOperator",
    "ConstantOperator",
    "ArgOperator",
    "ViewOperator",
    "ReshapeOperator",
    "FlattenOperator",
    "SqueezeOperator",
    "UnsqueezeOperator",
    "MMOperator",
    "AddmmOperator",
    "BmmOperator",
    "MatmulOperator",
    "EmbeddingOperator",
    "LinearOperator",
    "ReLUOperator",
    "SoftmaxOperator",
    "DropoutOperator",
    "LayerNormOperator",
    "get_operator",
    "register_operator",
    "list_operators",
    "set_operator_weight",
    "set_operator_weights",
    "set_operator_weight_by_torch_op",
    "set_operator_weights_by_torch_op",
]
