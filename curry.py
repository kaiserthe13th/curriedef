from __future__ import annotations
from typing import Any


class curried:
    def __init__(self, f: function) -> None:
        self.f: function = f
        if f.__code__.co_kwonlyargcount > 0:
            raise ValueError("only functions without keyword arguments can be curried")
        self.given_args = []

    def __call__(self, *args: Any) -> Any:
        ga = [*self.given_args, *args]
        if len(ga) == self.f.__code__.co_argcount:
            return self.f(*ga)
        elif len(ga) > self.f.__code__.co_argcount:
            raise TypeError(f"{self.f.__code__.co_name}() takes {self.f.__code__.co_argcount} positional arguments but {len(ga)} were given")
        ret = self
        ret.given_args = ga
        return ret

    def reset(self):
        self.given_args = []

