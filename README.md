# ideology
Ideological analysis of politicians and voters, hopefully along the same axes

Current data is from the Pew Research center (this is on voters). We also hope to scrape govtrack.us data.

Workflow so far:

"R CMD BATCH scripts/csv.R" -- converts SPSS data to CSV

"python summary.py data/rawdata.csv" -- produces a simple summary.
