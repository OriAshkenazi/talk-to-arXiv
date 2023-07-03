class Conversation:
    def __init__(self, arxiv_api, summarizer):
        self.arxiv_api = arxiv_api
        self.summarizer = summarizer
        self.messages = []

    def get_messages(self):
        return self.messages

    def get_full_message(self):
        return ' '.join(self.messages)

    def call_arxiv_function(self, messages, full_message):
        if 'get_articles' in full_message:
            query = messages[-1]
            articles = self.arxiv_api.get_articles(query, 5)
            self.messages.append(articles)
            return True
        elif 'read_article_and_summarize' in full_message:
            article_id = messages[-1]
            summary = self.summarizer.read_article_and_summarize(article_id)
            self.messages.append(summary)
            return True
        return False
