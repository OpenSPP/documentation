"""
CEL (Common Expression Language) Pygments Lexer for OpenSPP

This lexer provides syntax highlighting for CEL expressions used in OpenSPP
eligibility rules, entitlement formulas, and other configuration expressions.

Based on the CodeMirror implementation in spp_cel_widget.
"""

from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import (
    Comment,
    Keyword,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
    Text,
    Whitespace,
)

__all__ = ["CelLexer"]


class CelLexer(RegexLexer):
    """
    Lexer for CEL (Common Expression Language) expressions.

    CEL is used in OpenSPP for eligibility rules and entitlement formulas.
    """

    name = "CEL"
    aliases = ["cel"]
    filenames = ["*.cel"]
    mimetypes = ["text/x-cel"]

    # CEL keywords
    keywords = (
        "and",
        "or",
        "not",
        "in",
    )

    # Boolean and null literals
    constants = (
        "true",
        "false",
        "null",
    )

    # CEL built-in functions from OpenSPP
    builtins = (
        "age_years",
        "today",
        "now",
        "days_ago",
        "months_ago",
        "years_ago",
        "between",
        "exists",
        "count",
        "head",
        "has_role",
        "contains",
        "startswith",
        "endswith",
        "metric",
        "program",
        "has_tag",
        "date",
        "days_since",
        "hours_since",
        "is_business_day",
        "min",
        "max",
        "sum",
        "avg",
        "abs",
        "size",
        "matches",
        "filter",
        "map",
        "all",
        "exists_one",
        "type",
        "string",
        "int",
        "uint",
        "double",
        "bool",
        "duration",
        "timestamp",
    )

    tokens = {
        "root": [
            # Whitespace
            (r"\s+", Whitespace),
            # Comments (// style)
            (r"//.*$", Comment.Single),
            # Strings (double-quoted)
            (r'"', String.Double, "string-double"),
            # Strings (single-quoted)
            (r"'", String.Single, "string-single"),
            # Numbers (integers and floats)
            (r"-?\d+\.\d+", Number.Float),
            (r"-?\d+", Number.Integer),
            # Boolean and null constants
            (words(constants, suffix=r"\b"), Keyword.Constant),
            # Keywords
            (words(keywords, suffix=r"\b"), Keyword),
            # Built-in functions (followed by parenthesis)
            (
                r"(" + "|".join(builtins) + r")(\s*)(\()",
                bygroups(Name.Builtin, Whitespace, Punctuation),
            ),
            # Function calls (identifier followed by parenthesis)
            (r"([a-zA-Z_][a-zA-Z0-9_]*)(\s*)(\()", bygroups(Name.Function, Whitespace, Punctuation)),
            # Property access (after dot)
            (r"(\.)([a-zA-Z_][a-zA-Z0-9_]*)", bygroups(Punctuation, Name.Attribute)),
            # Comparison operators (must be before single char operators)
            (r"==|!=|>=|<=|&&|\|\|", Operator),
            # Single char operators
            (r"[<>=!+\-*/%]", Operator),
            # Punctuation
            (r"[.,\(\)\[\]\{\}:]", Punctuation),
            # Identifiers (variables)
            (r"[a-zA-Z_][a-zA-Z0-9_]*", Name.Variable),
            # Catch-all for other characters
            (r".", Text),
        ],
        "string-double": [
            (r'\\[\\"]', String.Escape),
            (r'[^"\\]+', String.Double),
            (r'"', String.Double, "#pop"),
        ],
        "string-single": [
            (r"\\[\\']", String.Escape),
            (r"[^'\\]+", String.Single),
            (r"'", String.Single, "#pop"),
        ],
    }


def setup(app):
    """
    Sphinx extension setup function.

    Registers the CEL lexer with Pygments so it can be used in code blocks.
    """
    from sphinx.highlighting import lexers

    lexers["cel"] = CelLexer(startinline=True)

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
