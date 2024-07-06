import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required nltk resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')  # Add this line to download the resource

# Define a function to extract nouns and important keywords from a string
def extract_nouns_keywords(text):
    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Remove stop words from the words list
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]

    # Lemmatize the words to reduce them to their base form
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(w) for w in words]

    # Use part-of-speech tagging to identify nouns and important keywords
    tagged_words = nltk.pos_tag(words)
    nouns_keywords = [word for word, tag in tagged_words if tag.startswith('N') or tag.startswith('J')]

    return nouns_keywords

# Example usage
text = "Former Governor of Punjab,Former Advisor to Chief Minister Punjab,Member PTI since April 1996,held different organizational offices from Tehsil to Central Team."
nouns_keywords = extract_nouns_keywords(text)
#print(nouns_keywords)
