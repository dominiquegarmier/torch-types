from __future__ import annotations

from typing import Annotated
from typing import Any

import torch


__all__ = [
    'Tensor',
]


class Tensor:
    def __class_getitem__(self, annotations: tuple[Any, ...]):
        if not isinstance(annotations[0], torch.dtype):
            annotations = (torch.float, *annotations)
        for dim in annotations[1:]:
            if not (isinstance(dim, str | int) or dim is Ellipsis):
                raise TypeError(
                    f'expected dimension size or name (int or str), got {dim} of type {type(dim)}'
                )
        if not isinstance(annotations, tuple):
            annotations = (annotations,)
        return Annotated[(torch.Tensor, *annotations)]
