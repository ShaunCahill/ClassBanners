"""Command-line interface for ClassBanners."""

import argparse
import sys
from pathlib import Path

from classbanners.banner import BannerConfig
from classbanners.generator import BannerGenerator


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        prog="classbanners",
        description="Generate customizable class banners",
    )
    parser.add_argument("title", help="Banner title text")
    parser.add_argument("-s", "--subtitle", default="", help="Subtitle text")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("banner.png"),
        help="Output file path (default: banner.png)",
    )
    parser.add_argument(
        "-W", "--width", type=int, default=800, help="Banner width (default: 800)"
    )
    parser.add_argument(
        "-H", "--height", type=int, default=200, help="Banner height (default: 200)"
    )
    parser.add_argument(
        "-b",
        "--background",
        default="#4A90D9",
        help="Background color (default: #4A90D9)",
    )
    parser.add_argument(
        "-c", "--color", default="#FFFFFF", help="Text color (default: #FFFFFF)"
    )
    parser.add_argument(
        "-f", "--font-size", type=int, default=48, help="Font size (default: 48)"
    )
    parser.add_argument("--font", type=Path, help="Path to custom font file")
    parser.add_argument(
        "--show", action="store_true", help="Display the banner after generation"
    )

    return parser.parse_args(args)


def main(args: list[str] | None = None) -> int:
    """Main entry point for the CLI."""
    parsed = parse_args(args)

    config = BannerConfig(
        width=parsed.width,
        height=parsed.height,
        background_color=parsed.background,
        text_color=parsed.color,
        font_size=parsed.font_size,
        font_path=parsed.font,
    )

    generator = BannerGenerator(config)
    banner = generator.create_banner(parsed.title, parsed.subtitle)

    banner.save(parsed.output)
    print(f"Banner saved to: {parsed.output}")

    if parsed.show:
        banner.show()

    return 0


if __name__ == "__main__":
    sys.exit(main())
