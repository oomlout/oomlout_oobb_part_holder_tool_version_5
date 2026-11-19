"""Shared paths and I/O for the three catalogue stages."""
from pathlib import Path
import os
import re
import tempfile

import yaml

ROOT = Path(__file__).resolve().parent


def write_file(path, content):
    """Replace a generated file only after all bytes have been written."""
    data = content.encode("utf-8") if isinstance(content, str) else content
    if path.is_file() and path.read_bytes() == data:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as output:
        output.write(data)
    try:
        os.replace(output.name, path)
    finally:
        Path(output.name).unlink(missing_ok=True)


def records(**kwargs):
    stage = kwargs.get("stage", "parts")
    selected = kwargs.get("filter", "")
    root = kwargs.get("root", ROOT)
    manifest = root / "parts_source" / "catalogue.txt"
    if not manifest.is_file():
        raise FileNotFoundError("Run working_oomp_populate.py first")
    identifiers = [name for name in manifest.read_text().splitlines() if selected in name]
    if not identifiers:
        raise ValueError(f"No holder matches {selected!r}")
    for part_id in identifiers:
        directory = root / stage / part_id
        metadata = yaml.safe_load((directory / "working.yaml").read_text(encoding="utf-8"))
        yield part_id, directory, metadata


def natural_key(value):
    return [int(piece) if piece.isdigit() else piece for piece in re.split(r"(\d+)", value)]


def cli_options(**kwargs):
    import argparse
    parser = argparse.ArgumentParser(description=kwargs.get("description", "Build OOBB tool holders"))
    parser.add_argument("--filter", default="", help="Build matching OOMP IDs")
    return vars(parser.parse_args())

