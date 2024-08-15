## Description:
# This script reads a PDF file containing a table
# and converts it to a markdown table using the PyMuPDF package.

## Dependencies:
# pip install pymupdf
# pip install pandas
# pip install tabulate

## Python version
# $ python --version
# Python 3.12.4

## Installed packages
# $ pip list
# Package         Version
# --------------- -----------
# numpy           2.0.1
# pandas          2.2.2
# pip             24.2
# PyMuPDF         1.24.9
# PyMuPDFb        1.24.9
# python-dateutil 2.9.0.post0
# pytz            2024.1
# six             1.16.0
# tabulate        0.9.0
# tzdata          2024.1

"""Module providing functions to identify and extract tables from PDF files."""

import pymupdf  # import package PyMuPDF

# open the pdf file
pdf = pymupdf.open("Sales_Report.pdf")

# get the first page
page = pdf[0]

# get the tables in the page
tables = page.find_tables()

# get the first table
table = tables[0]

# convert the table to pandas dataframe
df = table.to_pandas()

# format the dataframe to markdown
markdown_table = df.to_markdown()

# print the markdown table
print(markdown_table)

# run the code
# python identification_and_formatting.py
# |    | Product   | Region   | Sales (Q1)   | Sales (Q2)   | Sales (Q3)   | Sales (Q4)   |
# |---:|:----------|:---------|:-------------|:-------------|:-------------|:-------------|
# |  0 | Product A | North    | 12,000       | 15,000       | 13,500       | 14,000       |
# |  1 | Product B | South    | 10,500       | 11,000       | 12,500       | 13,000       |
# |  2 | Product C | East     | 8,000        | 9,500        | 10,000       | 11,500       |
# |  3 | Product D | West     | 9,000        | 8,500        | 9,200        | 9,800        |
# |  4 | Product E | Central  | 7,000        | 7,500        | 8,000        | 8,200        |
