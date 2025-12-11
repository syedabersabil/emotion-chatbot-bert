# 🧠 Emotion-Based Chatbot (BERT + NLP)

An intelligent chatbot that detects emotions from user messages and responds accordingly using **BERT** (Bidirectional Encoder Representations from Transformers) for emotion classification.

## 🎯 Features

- **Emotion Detection**: Classifies text into 4 emotions:
  - 😊 Happy
  - 😔 Sad  
  - 😤 Angry
  - 😟 Anxious

- **Context-Aware Responses**: Bot generates empathetic responses based on detected emotion
- **Real-time Classification**: Uses pretrained DistilBERT model for fast inference
- **Interactive Web UI**: Built with Streamlit for easy interaction
- **Confidence Scores**: Shows emotion detection confidence and all emotion probabilities

## 📦 Tech Stack

- **NLP Model**: DistilBERT (`bhadresh-savani/distilbert-base-uncased-emotion`)
- **Framework**: PyTorch + Transformers (Hugging Face)
- **Web Interface**: Streamlit
- **Language**: Python 3.8+

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/syedabersabil/emotion-chatbot-bert.git
cd emotion-chatbot-bert
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Open in browser**
- The app will automatically open at `http://localhost:8501`
- If not, manually navigate to the URL shown in terminal

## 💻 Usage

### Web Interface
1. Type your message in the chat input
2. Bot will detect your emotion and respond accordingly
3. Click on "View Detection Details" to see confidence scores
4. Use "Clear Chat" button to start fresh

### Example Interactions

**Input:** "I'm so excited about my new project!"
**Detected Emotion:** Happy 😊
**Response:** Positive and encouraging reply

**Input:** "I'm worried about my upcoming exams"
**Detected Emotion:** Anxious 😟  
**Response:** Calming and supportive reply

## 📁 Project Structure

```
emotion-chatbot-bert/
├── src/
│   ├── __init__.py
│   ├── infer.py              # Emotion detection logic
│   └── chatbot_logic.py      # Response generation
├── app.py                    # Streamlit web app
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 🧠 How It Works

1. **Input Processing**: User message is tokenized using BERT tokenizer
2. **Emotion Classification**: DistilBERT model predicts emotion probabilities
3. **Label Mapping**: Model outputs (joy, sadness, anger, fear, etc.) are mapped to 4 core emotions
4. **Response Generation**: Emotion-specific response templates are used
5. **Output**: Bot replies with contextually appropriate message

### Model Details

- **Base Model**: DistilBERT (distilled version of BERT)
- **Training Data**: Emotion dataset with 6 classes (joy, sadness, anger, fear, love, surprise)
- **Our Mapping**:
  - `joy, love, surprise` → **happy**
  - `sadness` → **sad**
  - `anger` → **angry**
  - `fear` → **anxious**

## 🚀 Deployment

### Streamlit Cloud (Free)
1. Push code to GitHub (already done!)
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo
4. Deploy `app.py`

### Hugging Face Spaces
1. Create account on [huggingface.co](https://huggingface.co)
2. Create new Space (Streamlit)
3. Connect this repo or upload files

### Local Development
```bash
streamlit run app.py --server.port 8501
```

## 📊 Future Enhancements

- [ ] Add LSTM layer for sequential emotion tracking
- [ ] Support for Hindi/Hinglish text
- [ ] Conversation history analysis
- [ ] Export chat logs
- [ ] Voice input support
- [ ] More emotion categories (confused, excited, etc.)
- [ ] Custom model training notebook

## 📝 License

MIT License - Feel free to use for learning and projects!

## 👨‍💻 Author

**Syed Aber Sabil**
- GitHub: [@syedabersabil](https://github.com/syedabersabil)

## 🚀 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features  
- Submit pull requests

---

**Built with ❤️ for NLP learning | Powered by BERT & Transformers**
