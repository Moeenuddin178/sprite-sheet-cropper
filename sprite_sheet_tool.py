#!/usr/bin/env python3
"""
Sprite sheet slicer and reassembler.

Given a sprite sheet image, slices it into equal-sized frames, crops each frame by
user-provided margins, and rebuilds a new sprite sheet from the cropped frames.
"""

from __future__ import annotations

import math
import os
import sys
from pathlib import Path
from typing import Tuple

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "This script depends on Pillow. Install it with `pip install Pillow`."
    ) from exc


def prompt_for_int(message: str, minimum: int | None = None) -> int:
    """Prompt the user for an integer, optionally enforcing a minimum."""
    while True:
        raw = input(message).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if minimum is not None and value < minimum:
            print(f"Value must be at least {minimum}.")
            continue

        return value


def prompt_for_crop() -> Tuple[int, int, int, int]:
    """Ask the user how many pixels to crop from each edge."""
    print("Enter crop margins (in pixels). Use 0 to skip cropping on an edge.")
    top = prompt_for_int("Top crop: ", minimum=0)
    right = prompt_for_int("Right crop: ", minimum=0)
    bottom = prompt_for_int("Bottom crop: ", minimum=0)
    left = prompt_for_int("Left crop: ", minimum=0)
    return top, right, bottom, left


def slice_frames(
    image: Image.Image, columns: int, rows: int, crop_margins: Tuple[int, int, int, int]
) -> list[Image.Image]:
    """Split the image into equal frames, apply per-frame cropping, and return the list."""
    width, height = image.size
    frame_width = width / columns
    frame_height = height / rows

    if not math.isclose(frame_width, int(frame_width)) or not math.isclose(
        frame_height, int(frame_height)
    ):
        raise ValueError(
            "Image dimensions are not evenly divisible by the provided rows/columns."
        )

    frame_width = int(frame_width)
    frame_height = int(frame_height)

    top_crop, right_crop, bottom_crop, left_crop = crop_margins
    max_crop_x = left_crop + right_crop
    max_crop_y = top_crop + bottom_crop

    if max_crop_x >= frame_width or max_crop_y >= frame_height:
        raise ValueError(
            "Cropping values remove the entire frame. Adjust crop margins and try again."
        )

    frames: list[Image.Image] = []

    for row in range(rows):
        for col in range(columns):
            left = col * frame_width
            upper = row * frame_height
            right = left + frame_width
            lower = upper + frame_height
            frame = image.crop((left, upper, right, lower))

            cropped = frame.crop(
                (
                    left_crop,
                    top_crop,
                    frame_width - right_crop,
                    frame_height - bottom_crop,
                )
            )
            frames.append(cropped)

    return frames


def rebuild_sprite_sheet(
    frames: list[Image.Image], columns: int, rows: int
) -> Image.Image:
    """Rebuild a sprite sheet from the processed frames."""
    if not frames:
        raise ValueError("No frames were generated; cannot rebuild sprite sheet.")

    frame_width, frame_height = frames[0].size

    for frame in frames:
        if frame.size != (frame_width, frame_height):
            raise ValueError("All frames must share the same size after cropping.")

    sheet_width = frame_width * columns
    sheet_height = frame_height * rows

    sprite_sheet = Image.new("RGBA", (sheet_width, sheet_height), (0, 0, 0, 0))

    index = 0
    for row in range(rows):
        for col in range(columns):
            sprite_sheet.paste(
                frames[index], (col * frame_width, row * frame_height)
            )
            index += 1

    return sprite_sheet


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python sprite_sheet_tool.py <input_sprite_sheet.png> [output.png]")
        raise SystemExit(1)

    input_path = Path(sys.argv[1]).expanduser().resolve()
    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")

    output_path = (
        Path(sys.argv[2]).expanduser().resolve()
        if len(sys.argv) > 2
        else input_path.with_stem(f"{input_path.stem}_cropped").with_suffix(".png")
    )

    with Image.open(input_path) as sprite_sheet:
        sprite_sheet = sprite_sheet.convert("RGBA")
        print(f"Loaded sprite sheet: {input_path}")
        print(f"Image size: {sprite_sheet.width}x{sprite_sheet.height}px")

        columns = prompt_for_int("How many columns (frames per row)? ", minimum=1)
        rows = prompt_for_int("How many rows? ", minimum=1)

        if columns * rows == 0:
            raise SystemExit("Columns and rows must both be positive integers.")

        crop_margins = prompt_for_crop()

        frames = slice_frames(sprite_sheet, columns, rows, crop_margins)
        print(f"Sliced and cropped {len(frames)} frames.")

        result_sheet = rebuild_sprite_sheet(frames, columns, rows)
        result_sheet.save(output_path)
        print(f"Saved rebuilt sprite sheet to: {output_path}")


if __name__ == "__main__":
    main()


