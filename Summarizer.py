import csv
from gensim.summarization import summarize

class Summarizer:
    def read_article_and_summarize(self, article_id):
        with open('arxiv_library.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == article_id:
                    return summarize(row[2])
