from pathlib import Path

APOLOGY_LINE = "Sorry I jammed. You fed me a receipt, a napkin, and hope. I am a printer, not a shredder."
TARGET_PATH = Path("/output/entry.txt")


def ensure_payload_ready(text: str) -> None:
    if not isinstance(text, str):
        raise TypeError("payload must be text")
    if len(text) < 1 or len(text) > 120:
        raise ValueError("payload length out of gate range")
    if not text.strip():
        raise ValueError("payload must not be whitespace only")
    text.encode("utf-8")


def verify_roundtrip(path: Path, expected: str) -> None:
    actual = path.read_text(encoding="utf-8")
    if actual != expected:
        raise RuntimeError("roundtrip mismatch after write")
    ensure_payload_ready(actual)


def emit_apology_note() -> None:
    ensure_payload_ready(APOLOGY_LINE)
    TARGET_PATH.parent.mkdir(parents=True, exist_ok=True)
    TARGET_PATH.write_text(APOLOGY_LINE, encoding="utf-8")
    verify_roundtrip(TARGET_PATH, APOLOGY_LINE)


if __name__ == "__main__":
    emit_apology_note()
