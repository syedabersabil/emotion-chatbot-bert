"""Chatbot response logic based on detected emotion"""
import random
from .infer import predict_emotion

# Emotion-specific responses (Hindi + English mix)
RESPONSES = {
    "happy": [
        "Wow, tum kaafi positive aur happy lag rahe ho! 😊 Keep spreading this energy!",
        "Yeh sunke accha laga! Khush rehna zaroori hai. Kya baat hai aaj ki? 🎉",
        "Amazing vibes! Tum jo bhi kar rahe ho, keep doing it! 🌟",
        "I can feel your happiness! Aise hi excited rehna. Share karo kya special hai? 💫"
    ],
    "sad": [
        "Lagta hai tum thoda low feel kar rahe ho. 😔 Agar baat karni hai, I'm here to listen.",
        "It's okay to feel sad sometimes. Apne feelings express karo, help karta hai. Main sun raha hoon. 💙",
        "Tum akele nahi ho. Kabhi kabhi difficult feel hota hai, but things get better. Kya hua? 🤗",
        "I understand you're going through something. Take your time, and share jab mann ho. 🌧️"
    ],
    "angry": [
        "Tum kaafi frustrated ya angry lag rahe ho. 😤 Deep breath lo, phir bolo kya problem hai?",
        "Gussa aana natural hai. But let's try to work through this calmly. Kya irritate kar raha hai? 🔥",
        "I can sense your anger. Express karo freely, sometimes speaking helps release tension. 💢",
        "Seems like something really bothered you. Want to talk about it? I'm here. 😠"
    ],
    "anxious": [
        "Tum thoda tense aur anxious feel kar rahe ho. 😟 Koi specific worry hai? Let's break it down.",
        "Anxiety mushkil hoti hai. Take a moment, breathe. Phir batao kya tension de raha hai? 🌀",
        "I can feel you're worried about something. Step by step handle karte hain. What's on your mind? 😰",
        "Anxious hona normal hai. Share karo specifically kya concern hai, we'll figure it out together. 💭"
    ]
}

# Follow-up prompts to encourage conversation
FOLLOW_UPS = {
    "happy": [
        "Aur batao, kya plans hain?",
        "Kya aaj kuch special kiya?",
        "Share your story!"
    ],
    "sad": [
        "Want to talk more about it?",
        "Kya hua exactly?",
        "I'm listening..."
    ],
    "angry": [
        "Tell me more about what happened.",
        "Kya specifically frustrate kar raha hai?",
        "Let it out, it helps."
    ],
    "anxious": [
        "Kya specific worry hai?",
        "Let's tackle this together.",
        "Break it down for me."
    ]
}

def get_bot_reply(text: str):
    """
    Generate bot reply based on emotion detection
    
    Args:
        text: User's message
        
    Returns:
        tuple: (emotion, reply, metadata)
    """
    # Detect emotion
    emotion, confidence, all_scores = predict_emotion(text)
    
    # Select response
    main_reply = random.choice(RESPONSES[emotion])
    follow_up = random.choice(FOLLOW_UPS[emotion])
    
    full_reply = f"{main_reply}\n\n{follow_up}"
    
    # Metadata for debugging/display
    metadata = {
        "emotion": emotion,
        "confidence": round(confidence, 2),
        "all_scores": {k: round(v, 2) for k, v in all_scores.items()}
    }
    
    return emotion, full_reply, metadata
