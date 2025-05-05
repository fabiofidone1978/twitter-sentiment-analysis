# twitter_sentiment_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob
import random

# -----------------------------
# Progetto: Twitter Sentiment Analysis (Mocked - No API)
# -----------------------------

# Step 1: Generazione tweet simulati
np.random.seed(42)
topics = ["Bitcoin", "AI", "Climate Change"]
tweets = []

for _ in range(300):
    topic = random.choice(topics)
    polarity = np.random.uniform(-1, 1)
    if polarity > 0.3:
        text = f"I love {topic}! It's amazing and full of potential."
    elif polarity < -0.3:
        text = f"I hate {topic}. It's a terrible idea."
    else:
        text = f"{topic} is okay, I guess."
    tweets.append({"topic": topic, "text": text,
                  "sentiment": TextBlob(text).sentiment.polarity})

# Step 2: Creazione DataFrame
df = pd.DataFrame(tweets)
df['sentiment_label'] = df['sentiment'].apply(
    lambda x: 'positive' if x > 0.1 else ('negative' if x < -0.1 else 'neutral'))

# Step 3: Conteggio per grafico
sentiment_counts = df.groupby(
    ['topic', 'sentiment_label']).size().unstack().fillna(0)

# Step 4: Visualizzazione
sentiment_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title("🧠 Twitter Sentiment by Topic (Mock)")
plt.ylabel("N. Tweet")
plt.xlabel("Argomento")
plt.tight_layout()
plt.savefig("twitter_sentiment_mock.png")

# Salva CSV
df.to_csv("twitter_sentiment_mock.csv", index=False)
