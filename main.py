from textblob import TextBlob
from newspaper import Article
import matplotlib.pyplot as plt

def live_sniper():
    print("--- 🎯 LIVE NEWS SENTIMENT SNIPER ---")
    url = input("Paste a News Article URL: ")

    try:
        # 1. Download and Parse the Article
        print("🔍 Scanning article content...")
        article = Article(url)
        article.download()
        article.parse()

        # 2. Analyze the 'Vibe' of the text
        blob = TextBlob(article.text)
        overall_sentiment = blob.sentiment.polarity
        
        # 3. Break it down by sentences to see the "Emotional Flow"
        sentence_scores = [s.sentiment.polarity for s in blob.sentences]

        print(f"\nHeadline: {article.title}")
        print(f"Overall Vibe Score: {overall_sentiment:.2f}")

        # 4. Visualizing the "Emotional Rollercoaster" of the article
        plt.figure(figsize=(10, 4))
        plt.plot(sentence_scores, marker='o', linestyle='-', color='#bc13fe')
        plt.axhline(0, color='black', lw=1, ls='--')
        plt.title(f"Sentiment Flow: {article.title[:50]}...", fontsize=12)
        plt.xlabel("Sentence Number")
        plt.ylabel("Sentiment (-1 to 1)")
        plt.grid(alpha=0.3)
        
        print("\n📈 Graphing the emotional flow... Close the graph to exit.")
        plt.show()

    except Exception as e:
        print(f"❌ Error: Could not scan that site. Try a different link! ({e})")

live_sniper()