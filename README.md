# chess_age
Exploring peak relative strength by age for top 100 chess players

You can simply run the Jupyter notebook if you want to use the included data to explore for yourself.

If you want to include the latest rating lists, study women's ratings or focus on juniors, chess.py
is a script that lets you download the data from the fide ratings site. Make sure to modify start, stop
and step values for the range function as indicated in the file as needed, otherwise you will simply download
the same data as is already provided. You'll also need to modify the pages kwarg in chess_soup.py to correspond
to the number of pages you've downloaded.

Otherwise, the Jupyter notebook should be sufficient for you to explore the Pandas dataframe as much as you want.
Feel free to create a new version and make a pull request if you'd like to improve the existing work or explore
new ideas.
