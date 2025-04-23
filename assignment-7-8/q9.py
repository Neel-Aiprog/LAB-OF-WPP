
import regex as re

class CustomTokenizer:
    def __init__(self):
        self.patterns = {
            "date": r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b",
            "url": r"https?://[^\s]+",  
            "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",  # Match emails
            "number": r"\b\d{1,3}(?:,\d{3})*\b|\b\d+\.\d+\b|\b\d+/\d+\b",
            "punctuation": r"[.,!?;:\"'(){}[\]<>]",  # Punctuation marks
            "social_handle": r"@\w+",  # Matches @username
            "words": r"[\p{L}\p{M}]+",  # Matches words in Unicode (modify for specific language)
        }
    
    def tokenize(self, text):
        tokens = []
        
        for category, pattern in self.patterns.items():
            matches = re.findall(pattern, text, re.UNICODE)
            for match in matches:
                tokens.append((category, match))
        
        return tokens

tokenizer = CustomTokenizer()
text = "Contact me at user@example.com or visit https://example.com. My handle is @user123. Today's date is 12/03/2024 and I owe you 3,22,243.50."

tokens = tokenizer.tokenize(text)
for token in tokens:
    print(token)
