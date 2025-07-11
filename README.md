# 🍉 Fruitpedia CLI

A beautifully crafted command-line tool to explore the world of fruits — with features like fruit info lookup, color-based search, fuzzy matching, data export (JSON/CSV), and color listings.

> ⚡ Built with Python, `Click`, `Pandas`, `RapidFuzz`, and `Rich`  
> ✅ UTF-8 compatible and beginner-friendly  
> 📦 Ready for PyPI and GitHub Actions

---

## 🚀 Features

- 🔍 **Get fruit info** — Get nutrients, color, and taste of any fruit by name.
- 🎨 **Search by color** — List fruits matching a given color.
- 📋 **List all colors** — View all supported fruit colors in the dataset.
- 🧠 **Fuzzy search** — Suggest closest fruit names if input is misspelled.
- 💾 **Export support** — Export query results as JSON or CSV files.
- ✅ **UTF-8 compatible** — Ensures smooth console output on Windows and Linux.

---

## 🛠️ Installation

### Prerequisites

- Python 3.8 or later
- `pip` package manager

### Steps

1. Clone the repository:

```bash
git clone https://github.com/ningappa89/fruitpedia.git
cd fruitpedia

2. Install the package in editable mode (recommended for development):
pip install -e .

3. (Optional) Install extra dependencies if exporting or advanced features are used:
pip install pandas rapidfuzz rich

📦 Usage Guide
The CLI is accessible via the module:
python -m fruitpedia.cli [OPTIONS]


Basic Commands
1. Get detailed info about a fruit
python -m fruitpedia.cli --info apple


output:
🍎 Fruit Information:
  Color: Red
  Taste: Sweet
  Nutrients: fiber, vitamin C

If the fruit is misspelled:
python -m fruitpedia.cli --info aplpe

Output:
❌ Fruit 'aplpe' not found.
🔎 Did you mean: apple?

2. List fruits by color
python -m fruitpedia.cli --search-color yellow

Output:
🎨 Fruits with color 'Yellow':
  - banana
  - pineapple
  - lemon

3. List all available fruit colors
python -m fruitpedia.cli --list-colors

Output:
🎨 Available Fruit Colors:
  - black
  - blue
  - brown
  - green
  - orange
  - pink
  - purple
  - red
  - white
  - yellow
  # ...and more

💾 Export Results
Export command output to a file in either JSON or CSV format:
python -m fruitpedia.cli --search-color red --export json

This generates a file named red_output.json with all matching fruits and their details.

Supported export formats:
json
csv
⚠️ Important: Export format values are strictly json or csv. Using filenames or other extensions will cause errors.


## 🧪 Manual Testing Scenarios
You can manually test each feature using VS Code Terminal or any shell:

| Scenario                         | Command                                         | Expected Behavior                                         |
|----------------------------------|--------------------------------------------------|-----------------------------------------------------------|
| Get info on a known fruit        | `--info apple`                                   | Shows detailed info on apple                             |
| Get info on an unknown fruit     | `--info unknownfruit`                            | Shows "Fruit not found" and suggests closest name         |
| Search fruits by a color         | `--search-color red`                             | Lists all fruits with red color                           |
| List all supported colors        | `--list-colors`                                  | Lists all available fruit colors                          |
| Export search results to JSON    | `--search-color yellow --export json`            | Creates `yellow_output.json` with fruits data             |
| Export search results to CSV     | `--search-color yellow --export csv`             | Creates `yellow_output.csv` with fruits data              |
| Invalid export format            | `--search-color yellow --export results.csv`     | Error about invalid export option                         |
| No options passed                | *(Run without arguments)*                        | Shows help or message prompting usage                     |



🧱 Project Structure
fruitpedia/
│
├── fruitpedia/
│   ├── __init__.py
│   ├── cli.py           # CLI interface using Click
│   ├── data.py          # Fruit data + info lookup
│   └── search.py        # Search & filter logic by color
│
├── tests/
│   ├── test_cli.py      # CLI command tests
│   ├── test_data.py     # Data retrieval tests
│   └── test_search.py   # Search/filter tests
│
├── README.md
├── LICENSE
└── pyproject.toml


🙋 Contributing
Contributions are welcome! Please follow these guidelines:

Fork the repository and create your feature branch.

Write clear, well-documented code.

Add tests for new features.

Run all tests before submitting a pull request:

pytest tests/

Format your code with black:
black fruitpedia tests

📄 License
This project is licensed under the MIT License. See LICENSE for details.

⭐ Support & Star
If you find this project helpful, please give it a ⭐ on GitHub!


Contact
For questions or feedback, please open an issue or contact me at [ningskanav89@gmail.com].