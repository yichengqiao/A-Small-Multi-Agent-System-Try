
import spacy

class QuestionUnderstandingAgent:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def analyze_query(self, query):
        doc = self.nlp(query)
        keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
        intent = self.determine_intent(doc)
        return {"query": query, "intent": intent, "keywords": keywords}

    def determine_intent(self, doc):
        question_words = {"what": "informational", "how": "procedural", "why": "explanatory", "who": "person", "when": "temporal", "where": "locational"}
        for token in doc:
            if token.lower_ in question_words:
                return question_words[token.lower_]
        return "general"
