def detect_shell(pid: int | None = None, max_depth: int = 10) -> tuple[str, str]: ...

class ShellDetectionFailure(OSError): ...
