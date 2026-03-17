# Extract Title and Introduction from Google Scholar

This project provides a Python script to extract titles and introductions (abstracts) of academic articles from Google Scholar based on a predefined search query. The script retrieves the first 100 matching articles and saves the results to a CSV file named `articles.csv`.

## Prerequisites

- Python 3.6 or higher
- The `scholarly` library (install via pip)

## Installation

1. Clone or download this repository.
2. Install the required Python package:

   ```
   pip install scholarly
   ```

## How to Use

1. Ensure you have Python and the `scholarly` library installed.
2. Run the script:

   ```
   python extract.py
   ```

3. The script will perform a search on Google Scholar using a predefined query related to domain identification, source code, and large language models.
4. Upon completion, it will print the number of articles retrieved and save the data to `articles.csv` in the same directory.
5. Open `articles.csv` to view the extracted titles and introductions.

Note: The search query is hardcoded in the script. If you need to modify the query, edit the `query` variable in `extract.py`.

## Output

The output CSV file (`articles.csv`) contains two columns:
- `title`: The title of the article
- `introduction`: The abstract/introduction of the article

If no articles are found, no CSV file will be created, and a message will be printed.
