# 🎯 SENTIMENT SNIPER | Live News NLP Engine

A Python-based Intelligence tool that scrapes live news articles and performs **Natural Language Processing (NLP)** to map the emotional "flow" of a story. 

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![NLP](https://img.shields.io/badge/NLP-TextBlob-green)
![Data](https://img.shields.io/badge/Data-Matplotlib-orange)

## 🚀 How it Works
1. **Targeting:** Provide any news URL (CNN, BBC, IGN, etc.).
2. **Extraction:** The engine bypasses bot-detection using custom User-Agents and scrapes the full article text.
3. **Analysis:** The script breaks the article into sentences and calculates a **Polarity Score** ($[-1.0, 1.0]$) for each.
4. **Visualization:** Generates a "Sentiment Flow" graph showing the emotional rollercoaster of the journalism.

## 🛠️ Tech Stack
- **TextBlob:** For Lexicon-based sentiment analysis.
- **Newspaper3k:** For advanced web scraping and article parsing.
- **Matplotlib:** For rendering the Cyberpunk-themed data dashboard.
- **LXML_HTML_Clean:** For sanitizing raw HTML into readable data.

## 📥 Installation
1. Clone the repo:
   ```bash

   git clone [https://github.com/SamsaDon07/sentiment-sniper.git](https://github.com/SamsaDon07/sentiment-sniper.git)
