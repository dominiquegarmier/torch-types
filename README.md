# torch-types

mypy compliant type annotations for dtype and shapes of tensors.

## Installation

```
pip install git+https://github.com/dominiquegarmier/torch-types
```

```python
# setup.cfg
plugins = torch_types.mypy
```

## Usage

```python
from __future__ import annotations

import torch
from torch_types import Tensor

N: int
y: Tensor[1, 2, N] = ...
x: Tensor[torch.float32, 1, 2, N] = ...
z: Tensor[1, 2, ...] = ...
```

internally mypy will treat these types as `torch.Tensor`. `Tensor` gets represented as a `typing.Annotated` type. Which is not currently fully sported by `mypy`. The mypy-plugin will replace the `Tensor` type with `torch.Tensor` and remove the annotations.

## Note

These types are purely for documentation purposes. They are not checked by mypy or at runtime. The mypy-plugin is required to not get type erros, due to incomplete support of `typing.Literal` and `typing.Annotated` in mypy.

## License

[MIT](LICENSE)
