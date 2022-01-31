from _typeshed import (
    OpenBinaryMode,
    OpenBinaryModeReading,
    OpenBinaryModeUpdating,
    OpenBinaryModeWriting,
    OpenTextMode,
    StrOrBytesPath,
)
from asyncio import AbstractEventLoop
from typing import Any, AnyStr, Literal, overload

from ..base import AiofilesContextManager
from ..threadpool.binary import AsyncBufferedIOBase, AsyncBufferedReader, AsyncFileIO, _UnknownAsyncBinaryIO
from ..threadpool.text import AsyncTextIOWrapper
from .temptypes import AsyncSpooledTemporaryFile, AsyncTemporaryDirectory

# Text mode: always returns AsyncTextIOWrapper
@overload
def NamedTemporaryFile(
    mode: OpenTextMode,
    buffering: int,
    encoding: str | None = ...,
    newline: str | None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    delete: bool = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncTextIOWrapper]: ...

# Unbuffered binary: AsyncFileIO
@overload
def NamedTemporaryFile(
    mode: OpenBinaryMode,
    buffering: Literal[0],
    encoding: str | None = ...,
    newline: str | None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    delete: bool = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncFileIO]: ...

# Buffered binary reading/updating: AsyncBufferedReader
@overload
def NamedTemporaryFile(
    mode: OpenBinaryModeUpdating | OpenBinaryModeReading = ...,
    buffering: Literal[-1, 1] = ...,
    encoding: str | None = ...,
    newline: str | None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    delete: bool = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncBufferedReader]: ...

# Buffered binary writing: AsyncBufferedIOBase
@overload
def NamedTemporaryFile(
    mode: OpenBinaryModeWriting = ...,
    buffering: Literal[-1, 1] = ...,
    encoding: str | None = ...,
    newline: str | None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    delete: bool = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncBufferedIOBase]: ...

# Buffering cannot be determined: fall back to _UnknownAsyncBinaryIO
@overload
def NamedTemporaryFile(
    mode: OpenBinaryMode = ...,
    buffering: int = ...,
    encoding: str | None = ...,
    newline: str | None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    delete: bool = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, _UnknownAsyncBinaryIO]: ...

# Text mode: always returns AsyncTextIOWrapper
@overload
def TemporaryFile(
    mode: OpenTextMode,
    buffering: int,
    encoding: str | None = ...,
    newline: str | None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncTextIOWrapper]: ...

# Unbuffered binary: AsyncFileIO
@overload
def TemporaryFile(
    mode: OpenBinaryMode,
    buffering: Literal[0],
    encoding: str | None = ...,
    newline: str | None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncFileIO]: ...

# Buffered binary reading/updating: AsyncBufferedReader
@overload
def TemporaryFile(
    mode: OpenBinaryModeUpdating | OpenBinaryModeReading = ...,
    buffering: Literal[-1, 1] = ...,
    encoding: str | None = ...,
    newline: str | None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncBufferedReader]: ...

# Buffered binary writing: AsyncBufferedIOBase
@overload
def TemporaryFile(
    mode: OpenBinaryModeWriting = ...,
    buffering: Literal[-1, 1] = ...,
    encoding: str | None = ...,
    newline: str | None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, AsyncBufferedIOBase]: ...

# Buffering cannot be determined: fall back to _UnknownAsyncBinaryIO
@overload
def TemporaryFile(
    mode: OpenBinaryMode = ...,
    buffering: int = ...,
    encoding: str | None = ...,
    newline: str | None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AiofilesContextManager[None, None, _UnknownAsyncBinaryIO]: ...
@overload
def SpooledTemporaryFile(
    max_size: int,
    mode: OpenTextMode,
    buffering: int = ...,
    encoding: str | None = ...,
    newline: str | None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AsyncSpooledTemporaryFile[str]: ...
@overload
def SpooledTemporaryFile(
    max_size: int = ...,
    mode: OpenBinaryMode = ...,
    buffering: int = ...,
    encoding: str | None = ...,
    newline: str | None = ...,
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AsyncSpooledTemporaryFile[bytes]: ...
def TemporaryDirectory(
    suffix: AnyStr | None = ...,
    prefix: AnyStr | None = ...,
    dir: StrOrBytesPath | None = ...,
    loop: AbstractEventLoop | None = ...,
    executor: Any | None = ...,
) -> AsyncTemporaryDirectory[AnyStr]: ...
