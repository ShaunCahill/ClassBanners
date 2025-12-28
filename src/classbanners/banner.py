"""Banner data models and configuration."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

from PIL import Image


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

    def save(self, path: Path | str, format: str | None = None) -> None:
        """Save the banner to a file.

        Args:
            path: Output file path.
            format: Image format (e.g., 'PNG', 'JPEG'). Auto-detected if None.

        Raises:
            ValueError: If no image has been generated.
        """
        if self._image is None:
            raise ValueError("No image to save. Generate the banner first.")

        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        self._image.save(path, format=format)

    def show(self) -> None:
        """Display the banner image.

        Raises:
            ValueError: If no image has been generated.
        """
        if self._image is None:
            raise ValueError("No image to show. Generate the banner first.")
        self._image.show()
