import requests
import csv

class ArxivAPIInterface:
    def __init__(self):
        self.base_url = "http://export.arxiv.org/api/query?"

    def get_articles(self, query, top_k):
        response = requests.get(f"{self.base_url}search_query={query}&start=0&max_results={top_k}")
        articles = response.json()['entries']
        return articles

    def download_article(self, article_id):
        response = requests.get(f"{self.base_url}id_list={article_id}")
        article = response.json()['entries'][0]
        with open('arxiv_library.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([article['id'], article['title'], article['summary']])
