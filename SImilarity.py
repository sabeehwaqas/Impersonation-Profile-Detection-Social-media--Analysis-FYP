import difflib

def similarity_score(str1, str2):
    """Returns a similarity score between two strings"""
    seq_matcher = difflib.SequenceMatcher(None, str1, str2)
    return seq_matcher.ratio()

# Example usage:
#str1 = "Hello, world!"
#str2 = "Hello, world!"
#score = similarity_score(str1, str2)
#print(f"The similarity score between '{str1}' and '{str2}' is: {score}")
