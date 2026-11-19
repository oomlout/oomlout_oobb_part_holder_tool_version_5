"""Materialize the source records as canonical OOMP parts, synchronously."""
from copy import deepcopy

import oomp
import yaml

from holder_catalogue import cli_options, records, write_file


def main(**kwargs):
    selected = kwargs.get("filter", "")
    for part_id, source, part in records(stage="parts_source", filter=selected):
        destination = source.parents[1] / "parts" / part_id
        manual = destination / "working_manual.yaml"
        if manual.is_file():
            part.update(yaml.safe_load(manual.read_text(encoding="utf-8")) or {})
        options = {
            **deepcopy(part),
            "make_files": False,
        }
        result = oomp.add_part(**options)
        if result["id"] != part_id:
            raise ValueError(f"OOMP ID disagrees with source directory {part_id}")
        for field in ("id", "directory", "md5", "md5_6", "md5_6_alpha"):
            part[field] = result[field]
        write_file(destination / "working.yaml", yaml.safe_dump(part, sort_keys=False, allow_unicode=True))


load_parts = main


if __name__ == "__main__":
    main(**cli_options())

