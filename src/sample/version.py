"""Version information for the sample package."""

from __future__ import annotations

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Tuple
    from typing import Union

    VERSION_TUPLE = Tuple[Union[int, str], ...]
else:
    VERSION_TUPLE = object

version: str
__version__: str
__version_tuple__: VERSION_TUPLE
version_tuple: VERSION_TUPLE

__version__ = version = "0.1.dev3+g8acb144.d20241001"
__version_tuple__ = version_tuple = (0, 1, "dev3", "g8acb144.d20241001")
