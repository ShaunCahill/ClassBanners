"""Banner generation logic."""

from __future__ import annotations

import logging
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from classbanners.banner import Banner, BannerConfig

logger = logging.getLogger(__name__)


class BannerGenerator:
    """Generates banner images from Banner objects."""

    def __init__(self, config: BannerConfig | None = None) -> None:
        """Initialize the generator with optional default configuration.

        Args:
            config: Default configuration for generated banners.
        """
        self.default_config = config or BannerConfig()

    def generate(self, banner: Banner) -> Banner:
        """Generate the banner image.

        Args:
            banner: The Banner object to generate.

        Returns:
            The same Banner object with the image property set.
        """
        config = banner.config

        # Create the base image
        image = Image.new("RGB", (config.width, config.height), config.background_color)
        draw = ImageDraw.Draw(image)

        # Add border if specified
        if config.border_width > 0:
            self._draw_border(draw, config)

        # Load font
        font = self._get_font(config.font_size, config.font_path)
        subtitle_font = self._get_font(config.font_size // 2, config.font_path)

        # Calculate text positions
        title_y = self._calculate_text_y(config, bool(banner.subtitle))
        self._draw_text(
            draw,
            banner.title,
            font,
            config.text_color,
            config.width,
            title_y,
            config.text_align,
            config.padding,
        )

        # Draw subtitle if present
        if banner.subtitle:
            subtitle_y = title_y + config.font_size + 10
            self._draw_text(
                draw,
                banner.subtitle,
                subtitle_font,
                config.text_color,
                config.width,
                subtitle_y,
                config.text_align,
                config.padding,
            )

        banner.image = image
        return banner

    def create_banner(
        self,
        title: str,
        subtitle: str = "",
        config: BannerConfig | None = None,
    ) -> Banner:
        """Create and generate a banner in one step.

        Args:
            title: The main banner title.
            subtitle: Optional subtitle text.
            config: Optional configuration (uses default if None).

        Returns:
            A fully generated Banner object.
        """
        banner = Banner(
            title=title,
            subtitle=subtitle,
            config=config or self.default_config,
        )
        return self.generate(banner)

    def _get_font(
        self, size: int, font_path: Path | None = None
    ) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
        """Load a font at the specified size."""
        if font_path:
            try:
                return ImageFont.truetype(str(font_path), size)
            except OSError:
                logger.warning(
                    "Failed to load font '%s', falling back to default", font_path
                )
        # Fall back to default font
        try:
            return ImageFont.truetype("DejaVuSans.ttf", size)
        except OSError:
            logger.debug("DejaVuSans.ttf not found, using PIL default font")
            return ImageFont.load_default()

    def _draw_border(self, draw: ImageDraw.ImageDraw, config: BannerConfig) -> None:
        """Draw a border around the banner."""
        bw = config.border_width
        draw.rectangle(
            [bw // 2, bw // 2, config.width - bw // 2, config.height - bw // 2],
            outline=config.border_color,
            width=bw,
        )

    def _calculate_text_y(self, config: BannerConfig, has_subtitle: bool) -> int:
        """Calculate the Y position for the title text."""
        if has_subtitle:
            # Account for subtitle when centering
            total_text_height = config.font_size + (config.font_size // 2) + 10
            return (config.height - total_text_height) // 2
        return (config.height - config.font_size) // 2

    def _draw_text(
        self,
        draw: ImageDraw.ImageDraw,
        text: str,
        font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
        color: str,
        width: int,
        y: int,
        align: str,
        padding: int,
    ) -> None:
        """Draw text on the banner."""
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]

        if align == "left":
            x = padding
        elif align == "right":
            x = width - text_width - padding
        else:  # center
            x = (width - text_width) // 2

        draw.text((x, y), text, font=font, fill=color)
