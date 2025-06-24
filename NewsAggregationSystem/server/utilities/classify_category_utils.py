class ClassifyCategory:

    @staticmethod
    def classify_category(text: str):
        if any(keyword in text for keyword in ["stock", "market", "business", "invest"]):
            return "Business"
        elif any(keyword in text for keyword in ["movie", "music", "celebrity", "entertainment"]):
            return "Entertainment"
        elif any(keyword in text for keyword in ["game", "match", "score", "tournament", "team"]):
            return "Sports"
        elif any(keyword in text for keyword in ["tech", "ai", "gadget", "software", "hardware"]):
            return "Technology"
        else:
            return "General"