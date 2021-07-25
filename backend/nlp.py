
import os
from dotenv import load_dotenv
from google.cloud import language_v1
from pprint import pprint


# Instantiates a client
load_dotenv()
credentials = os.getenv(key='credentials')
client = language_v1.LanguageServiceClient(credentials=credentials)

text = u"Hello, world!"
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

pprint('-' * 100)
pprint('Text:')
pprint('-' * 100)
pprint(f'{text}')
pprint('-' * 100)
pprint('Sentiment:')
pprint('-' * 100)
pprint(f'Score: {sentiment.score}')
pprint(f'Magnitude: {sentiment.magnitude}')
