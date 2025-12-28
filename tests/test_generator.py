"""Tests for BannerGenerator class."""

from pathlib import Path
from tempfile import TemporaryDirectory

from PIL import Image

from classbanners.banner import Banner, BannerConfig
from classbanners.generator import BannerGenerator


class TestBannerGenerator:
    """Tests for BannerGenerator class."""

    def test_generate_basic_banner(self) -> None:
        """Test generating a basic banner."""
        generator = BannerGenerator()
        banner = Banner(title="Test Banner")
        result = generator.generate(banner)

        assert result is banner
        assert banner.image is not None
        assert isinstance(banner.image, Image.Image)

    def test_banner_dimensions(self) -> None:
        """Test that generated banner has correct dimensions."""
        config = BannerConfig(width=1000, height=250)
        generator = BannerGenerator(config)
        banner = generator.create_banner("Test")

        assert banner.image is not None
        assert banner.image.size == (1000, 250)

    def test_create_banner_convenience_method(self) -> None:
        """Test the create_banner convenience method."""
        generator = BannerGenerator()
        banner = generator.create_banner("Title", "Subtitle")

        assert banner.title == "Title"
        assert banner.subtitle == "Subtitle"
        assert banner.image is not None

    def test_banner_with_subtitle(self) -> None:
        """Test generating a banner with subtitle."""
        generator = BannerGenerator()
        banner = generator.create_banner("Main Title", "Subtitle Text")

        assert banner.image is not None
        # Just verify it generates without error

    def test_save_banner(self) -> None:
        """Test saving a generated banner."""
        generator = BannerGenerator()
        banner = generator.create_banner("Test")

        with TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "test_banner.png"
            banner.save(output_path)

            assert output_path.exists()
            # Verify it's a valid image
            saved_image = Image.open(output_path)
            assert saved_image.size == (800, 200)

    def test_save_creates_parent_directories(self) -> None:
        """Test that save creates parent directories if needed."""
        generator = BannerGenerator()
        banner = generator.create_banner("Test")

        with TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "nested" / "dir" / "banner.png"
            banner.save(output_path)

            assert output_path.exists()

    def test_custom_config_per_banner(self) -> None:
        """Test using different configs for different banners."""
        generator = BannerGenerator()

        config1 = BannerConfig(width=500, height=100)
        config2 = BannerConfig(width=1000, height=300)

        banner1 = generator.create_banner("Banner 1", config=config1)
        banner2 = generator.create_banner("Banner 2", config=config2)

        assert banner1.image is not None
        assert banner2.image is not None
        assert banner1.image.size == (500, 100)
        assert banner2.image.size == (1000, 300)

    def test_banner_with_border(self) -> None:
        """Test generating a banner with border."""
        config = BannerConfig(border_width=5, border_color="#FF0000")
        generator = BannerGenerator(config)
        banner = generator.create_banner("Bordered Banner")

        assert banner.image is not None
        # Verify generation completes without error

    def test_different_text_alignments(self) -> None:
        """Test different text alignment options."""
        generator = BannerGenerator()

        for align in ["left", "center", "right"]:
            config = BannerConfig(text_align=align)  # type: ignore[arg-type]
            banner = generator.create_banner("Aligned Text", config=config)
            assert banner.image is not None
