"""Banner data models and configuration."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from PIL import Image


# Regex pattern for hex color validation (3, 4, 6, or 8 hex digits)
_HEX_COLOR_PATTERN = re.compile(r"^#(?:[0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")


def _validate_hex_color(color: str, field_name: str) -> None:
    """Validate that a string is a valid hex color."""
    if not _HEX_COLOR_PATTERN.match(color):
        raise ValueError(
            f"{field_name} must be a valid hex color (e.g., '#FF0000'), got '{color}'"
        )


@dataclass
class BannerConfig:
    """Configuration for banner generation."""

    width: int = 800
    height: int = 200
    background_color: str = "#4A90D9"
    text_color: str = "#FFFFFF"
    font_size: int = 48
    font_path: Path | None = None
    padding: int = 20
    border_width: int = 0
    border_color: str = "#000000"
    text_align: Literal["left", "center", "right"] = "center"

    def __post_init__(self) -> None:
        """Validate configuration values."""
        if self.width <= 0:
            raise ValueError("Width must be positive")
        if self.height <= 0:
            raise ValueError("Height must be positive")
        if self.font_size <= 0:
            raise ValueError("Font size must be positive")
        if self.padding < 0:
            raise ValueError("Padding cannot be negative")
        if self.border_width < 0:
            raise ValueError("Border width cannot be negative")
        _validate_hex_color(self.background_color, "background_color")
        _validate_hex_color(self.text_color, "text_color")
        _validate_hex_color(self.border_color, "border_color")


@dataclass
class Banner:
    """Represents a generated banner."""

    title: str
    subtitle: str = ""
    config: BannerConfig = field(default_factory=BannerConfig)
    _image: Image.Image | None = field(default=None, repr=False)

    @property
    def image(self) -> Image.Image | None:
        """Get the generated banner image."""
        return self._image

    @image.setter
    def image(self, value: Image.Image) -> None:
        """Set the banner image."""
        self._image = value

    def save(self, path: Path | str, image_format: str | None = None) -> None:
        """Save the banner to a file.

        Args:
            path: Output file path.
            image_format: Image format (e.g., 'PNG', 'JPEG'). Auto-detected if None.

        Raises:
            ValueError: If no image has been generated.
        """
        if self._image is None:
            raise ValueError("No image to save. Generate the banner first.")

        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        self._image.save(path, format=image_format)

    def show(self) -> None:
        """Display the banner image.

        Raises:
            ValueError: If no image has been generated.
        """
        if self._image is None:
            raise ValueError("No image to show. Generate the banner first.")
        self._image.show()
