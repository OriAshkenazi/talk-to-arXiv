from ArxivAPIInterface import ArxivAPIInterface
from Summarizer import Summarizer
from Conversation import Conversation
from PresentationInterface import PresentationInterface

def main():
    arxiv_api = ArxivAPIInterface()
    summarizer = Summarizer()
    conversation = Conversation(arxiv_api, summarizer)
    presentation_interface = PresentationInterface()

    while True:
        messages = conversation.get_messages()
        full_message = conversation.get_full_message()
        if conversation.call_arxiv_function(messages, full_message):
            continue
        presentation_interface.display_messages(messages)

if __name__ == "__main__":
    main()
