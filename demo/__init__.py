from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
from typing import TypeAlias

from typing_extensions import TypeAliasType

# Real: TypeAlias = float | Decimal | Fraction
# type Real = float | Decimal | Fraction
Real = TypeAliasType("Real", float | Decimal | Fraction)

__all__ = ("Real",)


def __dir__() -> tuple[str]:
    return __all__
