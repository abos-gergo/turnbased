from typing import List, Type
from ctypes import _SimpleCData

__all__: List[str]

# TODO: Update the `npt.mypy_plugin` such that it substitutes `c_intp` for
# a specific `_SimpleCData[int]` subclass (e.g. `ctypes.c_long`)
c_intp: Type[_SimpleCData[int]]

def load_library(libname, loader_path): ...
def ndpointer(dtype=..., ndim=..., shape=..., flags=...): ...
def as_ctypes(obj): ...
def as_array(obj, shape=...): ...
def as_ctypes_type(dtype): ...