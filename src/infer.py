"""Emotion inference using pretrained BERT model"""
from transformers import pipeline

# Load emotion classification model
classifier = pipeline(
    "text-classification",
    model="bhadresh-savani/distilbert-base-uncased-emotion",
    top_k=None
)

# Map model labels to our 4 emotions
LABEL_MAP = {
    "joy": "happy",
    "sadness": "sad",
    "anger": "angry",
    "fear": "anxious",
    "love": "happy",
    "surprise": "happy"
}

def predict_emotion(text: str):
    """
    Predict emotion from text
    
    Args:
        text: Input text from user
        
    Returns:
        tuple: (emotion, confidence, all_scores)
    """
    if not text.strip():
        return "anxious", 0.0, {}

    # Get predictions
    preds = classifier(text)[0]
    
    # Aggregate scores for our 4 emotions
    scores = {"happy": 0.0, "sad": 0.0, "angry": 0.0, "anxious": 0.0}
    
    for pred in preds:
        label = pred["label"]
        score = float(pred["score"])
        
        if label in LABEL_MAP:
            mapped_emotion = LABEL_MAP[label]
            scores[mapped_emotion] += score
    
    # Get dominant emotion
    emotion = max(scores, key=scores.get)
    confidence = scores[emotion]
    
    return emotion, confidence, scores


if __name__ == "__main__":
    # Test
    test_texts = [
        "I'm so happy today!",
        "I feel really sad and alone",
        "This makes me so angry!",
        "I'm worried about my exams"
    ]
    
    for text in test_texts:
        emotion, conf, _ = predict_emotion(text)
        print(f"Text: {text}")
        print(f"Emotion: {emotion} (confidence: {conf:.2f})\n")
