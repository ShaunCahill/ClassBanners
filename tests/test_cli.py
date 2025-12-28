"""Tests for CLI module."""

from pathlib import Path
from tempfile import TemporaryDirectory

from classbanners.cli import main, parse_args


class TestParseArgs:
    """Tests for argument parsing."""

    def test_required_title(self) -> None:
        """Test that title is parsed correctly."""
        args = parse_args(["My Banner"])
        assert args.title == "My Banner"

    def test_default_values(self) -> None:
        """Test default argument values."""
        args = parse_args(["Title"])
        assert args.subtitle == ""
        assert args.output == Path("banner.png")
        assert args.width == 800
        assert args.height == 200
        assert args.background == "#4A90D9"
        assert args.color == "#FFFFFF"
        assert args.font_size == 48
        assert args.font is None
        assert args.show is False

    def test_custom_output(self) -> None:
        """Test custom output path."""
        args = parse_args(["Title", "-o", "custom.png"])
        assert args.output == Path("custom.png")

    def test_subtitle(self) -> None:
        """Test subtitle argument."""
        args = parse_args(["Title", "-s", "Subtitle"])
        assert args.subtitle == "Subtitle"

    def test_dimensions(self) -> None:
        """Test width and height arguments."""
        args = parse_args(["Title", "-W", "1200", "-H", "300"])
        assert args.width == 1200
        assert args.height == 300

    def test_colors(self) -> None:
        """Test color arguments."""
        args = parse_args(["Title", "-b", "#FF0000", "-c", "#00FF00"])
        assert args.background == "#FF0000"
        assert args.color == "#00FF00"

    def test_font_options(self) -> None:
        """Test font-related arguments."""
        args = parse_args(["Title", "-f", "72", "--font", "/path/to/font.ttf"])
        assert args.font_size == 72
        assert args.font == Path("/path/to/font.ttf")


class TestMain:
    """Tests for main CLI function."""

    def test_main_creates_banner(self) -> None:
        """Test that main creates a banner file."""
        with TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "test.png"
            result = main(["Test Banner", "-o", str(output)])

            assert result == 0
            assert output.exists()

    def test_main_with_subtitle(self) -> None:
        """Test main with subtitle argument."""
        with TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "test.png"
            result = main(["Title", "-s", "Subtitle", "-o", str(output)])

            assert result == 0
            assert output.exists()

    def test_main_with_custom_config(self) -> None:
        """Test main with custom configuration."""
        with TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "custom.png"
            result = main([
                "Custom Banner",
                "-o", str(output),
                "-W", "1000",
                "-H", "250",
                "-b", "#00FF00",
                "-f", "64",
            ])

            assert result == 0
            assert output.exists()
