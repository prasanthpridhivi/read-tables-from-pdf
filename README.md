Goal:
Given a pdf file, read tables in the pdf and generate a csv file

Requirements:
1. A pdf file with around 800 pages as input
2. Each page in the pdf file has a table
3. The goal was to have an excel file with all the table information so that we can sort by columns

Implementation:
1. We use python library 'tabula' (pip install tabula-py); it has very good apis to read pdf tables
2. 'tabula' lets you specify which page/pages in the pdf you want to read the tables
3. 'tabula' reads the tables and stores it as a list
4. Once we get the list, we store the list into 'pandas' dataframe
5. Then we write the dataframe to a csv file

Duratation:
1. Took around 3 hrs to identify the best libraries to read pdf, write the code
2. The runtime to generate the csv file for a pdf of around 800 pages is about 40 seconds