import pandas as pd

TRAIT_KEYWORDS = {
    "resilience": ["adapt", "overcome", "persist", "withstand"],
    "curiosity": ["explore", "question", "why", "discover"],
    "creativity": ["innovate", "original", "novel", "imagine"],
    "analytical": ["calculate", "measure", "compare", "analyze"],
    "compassion": ["empathy", "support", "care", "understand"],
}

def keyword_score(text: str) -> dict:
    scores = {trait: 0 for trait in TRAIT_KEYWORDS}
    lower_text = text.lower()
    for trait, keywords in TRAIT_KEYWORDS.items():
        for word in keywords:
            if word in lower_text:
                scores[trait] += 1
    return scores

def process_traits(csv_path: str) -> list[dict]:
    df = pd.read_csv(csv_path)
    trait_map = []
    for _, row in df.iterrows():
        segment_id = row.get("Segment #", "Unknown")
        text = row.get("Conceptual Extraction", "") + " " + row.get("Practical Application", "")
        scores = keyword_score(text)
        trait_map.append({
            "segment": segment_id,
            "dominant_trait": max(scores, key=scores.get),
            "trait_scores": scores
        })
    return trait_map
