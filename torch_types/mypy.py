from __future__ import annotations

from collections.abc import Callable

from mypy.plugin import AnalyzeTypeContext
from mypy.plugin import Plugin
from mypy.types import Type


def plugin(version: str) -> type[Plugin]:
    return TorchTypesPlugin


class TorchTypesPlugin(Plugin):
    def get_type_analyze_hook(
        self, fullname: str
    ) -> Callable[[AnalyzeTypeContext], Type] | None:
        if fullname in ('torch_types.Tensor', 'torch_types.tensor.Tensor'):
            return analyze_tensor
        return None


def analyze_tensor(ctx: AnalyzeTypeContext) -> Type:
    # TODO: once we get better support for variadic types...
    tp = ctx.api.named_type('torch.Tensor', [])
    return ctx.api.analyze_type(tp)
