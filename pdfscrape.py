import tabula
import pandas as pd

scraped_data = tabula.read_pdf('./tables.pdf', multiple_tables = True, pages = 41)
sliced_data = scraped_data[0][["Spearman’s Coefficient"]]

sliced_data.to_csv('./scraped_data.csv')
