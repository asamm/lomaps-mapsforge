"""
Minimal compatibility shim for the removed stdlib `cgi` module (Python 3.13+).
This file is intentionally small: it provides the subset of the original `cgi` API
that older third-party libraries commonly use (e.g. Cheetah.Template).

Drop this file at the project root so an `import cgi` performed while running
from the project will pick up this shim before the stdlib module.

Provided:
- escape(s, quote=True) -> delegates to html.escape
- FieldStorage: very small parser for QUERY_STRING-based inputs and getvalue()
- parse_qs alias to urllib.parse.parse_qs

This is not a full replacement for the stdlib `cgi` package. If you depend on
more features, prefer running under Python 3.11/3.12 or upgrading the
third-party package to a Python-3.13-compatible release.
"""

from __future__ import annotations

import os
import io
import html
import urllib.parse
from typing import Any, Dict, List, Optional

# Re-export parse_qs in case callers import it from cgi
parse_qs = urllib.parse.parse_qs


def escape(s: Any, quote: bool = True) -> str:
    """Compatibility for old cgi.escape -> html.escape.

    Accepts bytes/None and returns a string.
    """
    if s is None:
        return ""
    if isinstance(s, bytes):
        s = s.decode("utf-8", errors="replace")
    return html.escape(str(s), quote=quote)


class FieldStorage:
    """Tiny FieldStorage replacement.

    Notes:
    - Only parses QUERY_STRING from environ (GET parameters).
    - Implements getvalue(name, default=None) returning first value or list.
    - Accepts the common constructor parameters but ignores file uploads and
      multipart parsing.
    """

    def __init__(
        self,
        fp: Optional[io.IOBase] = None,
        headers: Any = None,
        outerboundary: Any = None,
        environ: Optional[Dict[str, str]] = None,
        keep_blank_values: bool = False,
        strict_parsing: bool = False,
        **_kwargs,
    ) -> None:
        environ = environ or os.environ
        qs = environ.get("QUERY_STRING", "")
        # parse_qs returns values as lists
        self._data: Dict[str, List[str]] = urllib.parse.parse_qs(
            qs, keep_blank_values=keep_blank_values, strict_parsing=strict_parsing
        )

    def getvalue(self, name: str, default: Optional[Any] = None) -> Any:
        v = self._data.get(name)
        if v is None:
            return default
        # Return first value (common cgi.getvalue behavior)
        return v[0] if v else default

    # Mapping-like convenience
    def __getitem__(self, name: str) -> List[str]:
        return self._data[name]

    def keys(self):
        return self._data.keys()

    def items(self):
        return self._data.items()


# Provide a minimal FieldStorage 'MiniFieldStorage' alias used by some libraries
MiniFieldStorage = FieldStorage

