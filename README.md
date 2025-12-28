# ClassBanners

Generate customizable class banners with Python.

## Requirements

- Python 3.9 or higher

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/ShaunCahill/ClassBanners.git
cd ClassBanners
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

### Step 3: Activate the virtual environment

**Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### Step 4: Install the package

```bash
pip install -e .
```

## Usage

### Command Line

Generate a banner with a title:

```bash
classbanners "Welcome to Class"
```

Add a subtitle and custom output file:

```bash
classbanners "Math 101" -s "Room 204" -o math.png
```

Customize colors and font size:

```bash
classbanners "Science Lab" -b "#2E7D32" -c "#FFFFFF" -f 64
```

Display the banner after generation:

```bash
classbanners "Physics" --show
```

### CLI Options

| Option | Description |
|--------|-------------|
| `title` | Banner title text (required) |
| `-s, --subtitle` | Subtitle text |
| `-o, --output` | Output file path (default: banner.png) |
| `-W, --width` | Banner width in pixels (default: 800) |
| `-H, --height` | Banner height in pixels (default: 200) |
| `-b, --background` | Background color as hex (default: #4A90D9) |
| `-c, --color` | Text color as hex (default: #FFFFFF) |
| `-f, --font-size` | Font size in points (default: 48) |
| `--font` | Path to custom TTF font file |
| `--show` | Display banner after generation |

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

### Configuration Options

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

### Setup

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install with dev dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Linting and Type Checking

```bash
ruff check .
mypy src/
```

## License

MIT License
