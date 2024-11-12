# `pyright --verifytypes` bug with `TypeAliasType`

## System requirements

- [`uv`](https://docs.astral.sh/uv/getting-started/installation/)
- `python >= 3.10`

## Installation

```shell
$ uv sync
Using CPython 3.12.7
Creating virtual environment at: .venv
Resolved 4 packages in 0.68ms
Installed 4 packages in 2ms
 + demo==0.1.0 (from file://~/Workspace/pyright-verifytypes-typealiastype)
 + nodeenv==1.9.1
 + pyright==1.1.388
 + typing-extensions==4.12.2
```

</details>

## The `demo` project

The `demo` project exports one single type alias, `Real`, which is the backported variant of

```py
type Real = float | decimal.Decimal | fractions.Fraction
```

i.e.

```py
Real = typing_extensions.TypeAliasType("Real", float | decimal.Decimal | fractions.Fraction)
```

## Type-checking

It's valid according to pyright in strict mode:

```shell
$ uv run pyright demo
0 errors, 0 warnings, 0 informations
```

## `--verifytypes`

Because of typeshed issues, `pyright --verifytypes` will report many problems:

```shell
$ uv run pyright --verifytypes demo
added 1 package, and audited 2 packages in 1s

found 0 vulnerabilities
Module name: "demo"
Package directory: "~/Workspace/pyright-verifytypes-typealiastype/demo"
Module directory: "~/Workspace/pyright-verifytypes-typealiastype/demo"
Path of py.typed file: "~/Workspace/pyright-verifytypes-typealiastype/demo/py.typed"

Public modules: 1
   demo

Symbols used in public interface:
demo.Real
  ~/Workspace/pyright-verifytypes-typealiastype/demo/__init__.py:20:1 - error: Type is missing type annotation and could be inferred differently by type checkers
    Inferred type is "Real"
decimal.Decimal.__ge__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/decimal.pyi:73:9 - error: Type of parameter "value" is partially unknown
    Parameter type is "_ComparableNum"
numbers.Rational
   error: Type of base class "numbers.Real" is partially unknown
numbers.Real
   error: Type of base class "numbers.Complex" is partially unknown
numbers.Real.__divmod__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:123:9 - error: Type annotation for parameter "other" is missing
numbers.Real.__rdivmod__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:124:9 - error: Type annotation for parameter "other" is missing
numbers.Real.__floordiv__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:126:9 - error: Type annotation for parameter "other" is missing
numbers.Real.__rfloordiv__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:128:9 - error: Type annotation for parameter "other" is missing
numbers.Real.__mod__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:130:9 - error: Type annotation for parameter "other" is missing
numbers.Real.__rmod__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:132:9 - error: Type annotation for parameter "other" is missing
numbers.Real.__lt__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:134:9 - error: Type annotation for parameter "other" is missing
numbers.Real.__le__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:136:9 - error: Type annotation for parameter "other" is missing
numbers.Complex.__add__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:78:9 - error: Type annotation for parameter "other" is missing
numbers.Complex.__radd__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:80:9 - error: Type annotation for parameter "other" is missing
numbers.Complex.__sub__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:85:9 - error: Type annotation for parameter "other" is missing
numbers.Complex.__rsub__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:86:9 - error: Type annotation for parameter "other" is missing
numbers.Complex.__mul__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:88:9 - error: Type annotation for parameter "other" is missing
numbers.Complex.__rmul__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:90:9 - error: Type annotation for parameter "other" is missing
numbers.Complex.__truediv__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:92:9 - error: Type annotation for parameter "other" is missing
numbers.Complex.__rtruediv__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:94:9 - error: Type annotation for parameter "other" is missing
numbers.Complex.__pow__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:96:9 - error: Type annotation for parameter "exponent" is missing
numbers.Complex.__rpow__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/numbers.pyi:98:9 - error: Type annotation for parameter "base" is missing
decimal.Decimal.__gt__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/decimal.pyi:74:9 - error: Type of parameter "value" is partially unknown
    Parameter type is "_ComparableNum"
decimal.Decimal.__le__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/decimal.pyi:75:9 - error: Type of parameter "value" is partially unknown
    Parameter type is "_ComparableNum"
decimal.Decimal.__lt__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/decimal.pyi:76:9 - error: Type of parameter "value" is partially unknown
    Parameter type is "_ComparableNum"
fractions.Fraction
   error: Type of base class "numbers.Rational" is partially unknown
fractions.Fraction.__new__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/fractions.pyi:27:9 - error: Type of parameter "numerator" is partially unknown
    Parameter type is "int | Rational"
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/fractions.pyi:27:9 - error: Type of parameter "denominator" is partially unknown
    Parameter type is "int | Rational | None"
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/fractions.pyi:27:9 - error: Type of parameter "value" is partially unknown
    Parameter type is "float | Decimal | str"
fractions.Fraction.from_decimal
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/fractions.pyi:31:9 - error: Type of parameter "dec" is partially unknown
    Parameter type is "Decimal"
fractions.Fraction.__lt__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/fractions.pyi:135:9 - error: Type of parameter "b" is partially unknown
    Parameter type is "_ComparableNum"
fractions.Fraction.__gt__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/fractions.pyi:136:9 - error: Type of parameter "b" is partially unknown
    Parameter type is "_ComparableNum"
fractions.Fraction.__le__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/fractions.pyi:137:9 - error: Type of parameter "b" is partially unknown
    Parameter type is "_ComparableNum"
fractions.Fraction.__ge__
  ~/.cache/pyright-python/1.1.388/node_modules/pyright/dist/typeshed-fallback/stdlib/fractions.pyi:138:9 - error: Type of parameter "b" is partially unknown
    Parameter type is "_ComparableNum"

Symbols exported by "demo": 2
  With known type: 1
  With ambiguous type: 0
  With unknown type: 1

Other symbols referenced but not exported by "demo": 292
  With known type: 259
  With ambiguous type: 0
  With unknown type: 33

Symbols without documentation:
  Functions without docstring: 129
  Functions without default param: 4
  Classes without docstring: 11

Type completeness score: 50%
```

</summary>

None of these errors are our responsibility, so we decide to silence them with `--ignoreexternal`:

```shell
$ uv run pyright --ignoreexternal --verifytypes demo
Module name: "demo"
Package directory: "~/Workspace/pyright-verifytypes-typealiastype/demo"
Module directory: "~/Workspace/pyright-verifytypes-typealiastype/demo"
Path of py.typed file: "~/Workspace/pyright-verifytypes-typealiastype/demo/py.typed"

Public modules: 1
   demo

Symbols used in public interface:
demo.Real
  ~/Workspace/pyright-verifytypes-typealiastype/demo/__init__.py:20:1 - error: Type is missing type annotation and could be inferred differently by type checkers
    Inferred type is "Real"

Symbols exported by "demo": 2
  With known type: 1
  With ambiguous type: 1
  With unknown type: 0
    (Ignoring unknown types imported from other packages)

Other symbols referenced but not exported by "demo": 0
  With known type: 0
  With ambiguous type: 0
  With unknown type: 0

Symbols without documentation:
  Functions without docstring: 0
  Functions without default param: 0
  Classes without docstring: 0

Type completeness score: 50%
```

It still reports an error about a missing type annotation, then proceeds to correctly infer it as `Real`...?

## This doesn't with `TypeAlias` and `type _`

If we instead replace the `Real` type alias type with a `Real: TypeAlias = ...`, then the error
disappears:


```shell
$ uv run pyright --ignoreexternal --verifytypes demo
Module name: "demo"
Package directory: "~/Workspace/pyright-verifytypes-typealiastype/demo"
Module directory: "~/Workspace/pyright-verifytypes-typealiastype/demo"
Path of py.typed file: "~/Workspace/pyright-verifytypes-typealiastype/demo/py.typed"

Public modules: 1
   demo

Symbols used in public interface:

Symbols exported by "demo": 2
  With known type: 2
  With ambiguous type: 0
  With unknown type: 0
    (Ignoring unknown types imported from other packages)

Other symbols referenced but not exported by "demo": 0
  With known type: 0
  With ambiguous type: 0
  With unknown type: 0

Symbols without documentation:
  Functions without docstring: 0
  Functions without default param: 0
  Classes without docstring: 0

Type completeness score: 100%
```

And if we use `type Real = ...` instead, then there also is error.

So this issue is specific to the manual use of `TypeAliasType`.
