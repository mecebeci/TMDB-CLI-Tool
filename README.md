# TMDB CLI Tool

A simple command-line interface (CLI) to fetch and display movie data from [The Movie Database (TMDB)](https://www.themoviedb.org/). This tool allows you to search for movies, view now playing, popular, top-rated, and upcoming movies directly in your terminal.

---

## Features

* Search for a movie by name.
* List **now playing** movies.
* List **popular** movies.
* List **top-rated** movies.
* List **upcoming** movies.

---

## Requirements

* Python 3.8 or higher
* [TMDB API key](https://www.themoviedb.org/documentation/api)
* Packages:

  * `requests`
  * `python-dotenv`

You can install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Installation (Editable / Local)

1. Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
# or
.\venv\Scripts\Activate.ps1  # Windows PowerShell
```

2. Install the project in editable mode:

```bash
pip install --upgrade pip
pip install -e .
```

---

## Usage

The CLI command is `tmdb-app`. Use the `--type` argument to choose a command.

### Commands

#### Search for a movie

```bash
tmdb-app --type search --name "Inception"
```

* `--type search` tells the CLI you want to search.
* `--name` is the movie name you want to search for.

#### List now playing movies

```bash
tmdb-app --type playing
```

#### List popular movies

```bash
tmdb-app --type popular
```

#### List top-rated movies

```bash
tmdb-app --type top
```

#### List upcoming movies

```bash
tmdb-app --type upcoming
```

---

## Project Structure

```
tmdb-cli-tool/
│── tmdb_app/
│   ├── __init__.py
│   └── main.py         # CLI entry point and command parsing
│
├── README.md
├── pyproject.toml       # build configuration
├── requirements.txt
└── venv/                # optional virtual environment
```

---

## Environment Variables

Create a `.env` file in the project root and add your TMDB API key:

```
TMDB_API_KEY=your_api_key_here
```

The CLI will read the API key automatically.

---
