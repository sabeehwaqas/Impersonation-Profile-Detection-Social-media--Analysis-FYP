from transformers import BertTokenizer, BertModel
import torch
from torch.nn import CosineSimilarity


# Load the BERT model and tokenizer
model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Define the two sentences
sentence1 = "This is a sample sentence"
sentence2 = "This is an example sentence"

# Encode the sentences into BERT's format
encoded_sentence1 = tokenizer.encode(sentence1, return_tensors='pt')
encoded_sentence2 = tokenizer.encode(sentence2, return_tensors='pt')

# Use BERT to generate embeddings for the sentences
embeddings1 = model(encoded_sentence1)[0][:, 0, :]
embeddings2 = model(encoded_sentence2)[0][:, 0, :]

# Calculate cosine similarity between the embeddings
cosine_similarity = CosineSimilarity(dim=1, eps=1e-6)
similarity = cosine_similarity(embeddings1, embeddings2).item()

print("Similarity: ", similarity)
