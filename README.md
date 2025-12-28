# ClassBanners

Generate customizable class banners with Python.

## Requirements

- Python 3.9+
- Pillow (installed automatically)

## Installation

```bash
# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install from source
pip install -e .

# Or install dependencies only
pip install -r requirements.txt
```

## Quick Start

### Python API

```python
from classbanners import BannerGenerator, BannerConfig

# Create a generator with default settings
generator = BannerGenerator()

# Generate a simple banner
banner = generator.create_banner("Math 101", "Fall 2024")
banner.save("math_banner.png")

# Custom configuration
config = BannerConfig(
    width=1200,
    height=300,
    background_color="#2E7D32",
    text_color="#FFFFFF",
    font_size=72,
)

generator = BannerGenerator(config)
banner = generator.create_banner("Science Lab")
banner.save("science_banner.png")
```

### Command Line

```bash
# Basic usage
classbanners "Welcome to Class"

# With options
classbanners "Math 101" -s "Room 204" -o math.png -b "#2E7D32" -f 64

# Show the banner after generation
classbanners "Physics" --show
```

## Configuration Options

| Option | Default | Description |
|--------|---------|-------------|
| `width` | 800 | Banner width in pixels |
| `height` | 200 | Banner height in pixels |
| `background_color` | #4A90D9 | Background color (hex) |
| `text_color` | #FFFFFF | Text color (hex) |
| `font_size` | 48 | Font size in points |
| `font_path` | None | Path to custom TTF font |
| `padding` | 20 | Padding from edges |
| `border_width` | 0 | Border width (0 = no border) |
| `border_color` | #000000 | Border color (hex) |
| `text_align` | center | Text alignment (left/center/right) |

## Development

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linter
ruff check .

# Run type checker
mypy src/
```

## License

MIT License
