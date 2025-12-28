"""Tests for Banner and BannerConfig classes."""

import pytest

from classbanners.banner import Banner, BannerConfig


class TestBannerConfig:
    """Tests for BannerConfig dataclass."""

    def test_default_values(self) -> None:
        """Test that default values are set correctly."""
        config = BannerConfig()
        assert config.width == 800
        assert config.height == 200
        assert config.background_color == "#4A90D9"
        assert config.text_color == "#FFFFFF"
        assert config.font_size == 48
        assert config.padding == 20
        assert config.text_align == "center"

    def test_custom_values(self) -> None:
        """Test that custom values can be set."""
        config = BannerConfig(
            width=1200,
            height=400,
            background_color="#FF0000",
            font_size=72,
        )
        assert config.width == 1200
        assert config.height == 400
        assert config.background_color == "#FF0000"
        assert config.font_size == 72

    def test_invalid_width_raises_error(self) -> None:
        """Test that invalid width raises ValueError."""
        with pytest.raises(ValueError, match="Width must be positive"):
            BannerConfig(width=0)

        with pytest.raises(ValueError, match="Width must be positive"):
            BannerConfig(width=-100)

    def test_invalid_height_raises_error(self) -> None:
        """Test that invalid height raises ValueError."""
        with pytest.raises(ValueError, match="Height must be positive"):
            BannerConfig(height=0)

    def test_invalid_font_size_raises_error(self) -> None:
        """Test that invalid font size raises ValueError."""
        with pytest.raises(ValueError, match="Font size must be positive"):
            BannerConfig(font_size=0)

    def test_negative_padding_raises_error(self) -> None:
        """Test that negative padding raises ValueError."""
        with pytest.raises(ValueError, match="Padding cannot be negative"):
            BannerConfig(padding=-5)

    def test_negative_border_width_raises_error(self) -> None:
        """Test that negative border width raises ValueError."""
        with pytest.raises(ValueError, match="Border width cannot be negative"):
            BannerConfig(border_width=-1)

    def test_invalid_background_color_raises_error(self) -> None:
        """Test that invalid background color raises ValueError."""
        with pytest.raises(ValueError, match="background_color must be a valid hex color"):
            BannerConfig(background_color="invalid")

    def test_invalid_text_color_raises_error(self) -> None:
        """Test that invalid text color raises ValueError."""
        with pytest.raises(ValueError, match="text_color must be a valid hex color"):
            BannerConfig(text_color="red")

    def test_invalid_border_color_raises_error(self) -> None:
        """Test that invalid border color raises ValueError."""
        with pytest.raises(ValueError, match="border_color must be a valid hex color"):
            BannerConfig(border_color="#GGG")

    def test_valid_short_hex_colors(self) -> None:
        """Test that short hex colors are accepted."""
        config = BannerConfig(background_color="#ABC", text_color="#FFF")
        assert config.background_color == "#ABC"
        assert config.text_color == "#FFF"

    def test_valid_hex_colors_with_alpha(self) -> None:
        """Test that hex colors with alpha channel are accepted."""
        config = BannerConfig(background_color="#FF0000FF", text_color="#00FF00AA")
        assert config.background_color == "#FF0000FF"
        assert config.text_color == "#00FF00AA"


class TestBanner:
    """Tests for Banner dataclass."""

    def test_create_banner(self) -> None:
        """Test creating a banner with title."""
        banner = Banner(title="Test Banner")
        assert banner.title == "Test Banner"
        assert banner.subtitle == ""
        assert banner.image is None

    def test_create_banner_with_subtitle(self) -> None:
        """Test creating a banner with subtitle."""
        banner = Banner(title="Main Title", subtitle="Subtitle")
        assert banner.title == "Main Title"
        assert banner.subtitle == "Subtitle"

    def test_banner_with_custom_config(self) -> None:
        """Test creating a banner with custom config."""
        config = BannerConfig(width=1000, height=300)
        banner = Banner(title="Test", config=config)
        assert banner.config.width == 1000
        assert banner.config.height == 300

    def test_save_without_image_raises_error(self) -> None:
        """Test that saving without generating raises ValueError."""
        banner = Banner(title="Test")
        with pytest.raises(ValueError, match="No image to save"):
            banner.save("test.png")

    def test_show_without_image_raises_error(self) -> None:
        """Test that showing without generating raises ValueError."""
        banner = Banner(title="Test")
        with pytest.raises(ValueError, match="No image to show"):
            banner.show()
