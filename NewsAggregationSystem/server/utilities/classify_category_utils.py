from NewsAggregationSystem.server.utilities.logger import logger

class ClassifyCategory:

    @staticmethod
    def classify_category(text: str):
        if any(keyword in text for keyword in ["stock", "market", "business", "invest"]):
            logger.info(f"Keyword match found in text for category: Business")
            return "Business"
        elif any(keyword in text for keyword in ["movie", "music", "celebrity", "entertainment"]):
            logger.info(f"Keyword match found in text for category: Entertainment")
            return "Entertainment"
        elif any(keyword in text for keyword in ["game", "match", "score", "tournament", "team"]):
            logger.info(f"Keyword match found in text for category: Sports")
            return "Sports"
        elif any(keyword in text for keyword in ["tech", "ai", "gadget", "software", "hardware"]):
            logger.info(f"Keyword match found in text for category: Technology")
            return "Technology"
        else:
            logger.info(f"No specific keyword match found. Assigned category: General")
            return "General"