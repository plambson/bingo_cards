# Bingo Card Generator

Generates a printable HTML file of randomized bingo cards from a plain text word list.

## Usage

Call `generate_bingo_cards()` at the bottom of the script with your desired parameters:

```python
generate_bingo_cards('mylist.txt', 'output.html', cards=50)
```

### Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `infile` | required | Path to a `.txt` file with one term per line |
| `outfile` | `'out.html'` | Name of the HTML file to generate |
| `cards` | `100` | Number of bingo cards to generate |

## Input File Format

A plain `.txt` file with one bingo term per line. At least 24 terms are required to fill a card (the center square is a free space).

```
Term One
Term Two
Term Three
...
```

## Output

An HTML file with one bingo card per page, ready to print. Each card is randomly shuffled. The input filename (without extension) is printed at the bottom of each page.

## Requirements

- Python 3
