# Twitter Sentiment Analysis

Analisi testuale di tweet simulati su argomenti di attualità. Il progetto esegue classificazione del sentiment (positivo, neutro, negativo) su contenuti generati artificialmente e aggrega i risultati per categoria tematica.

## Obiettivi

- Simulare un flusso NLP completo, dall'elaborazione dei testi alla classificazione del sentiment.
- Dimostrare l'uso di strumenti leggeri per l'analisi linguistica e la visualizzazione.
- Produrre output coerenti e replicabili, senza dipendenze da API esterne.

## Tecnologie utilizzate

- Python 3
- TextBlob
- Pandas
- Matplotlib

## Struttura del progetto

📦 twitter-sentiment-analysis
├── twitter_sentiment_analysis.py
├── twitter_sentiment_mock.csv
├── twitter_sentiment_mock.png
└── README.md

markdown
Copia
Modifica

## Istruzioni per l'esecuzione

1. Installare le dipendenze:

```bash
pip install pandas textblob matplotlib
Eseguire lo script:

bash
Copia
Modifica
python twitter_sentiment_analysis.py
Verranno generati i file:

twitter_sentiment_mock.csv: dataset dei tweet con sentiment

twitter_sentiment_mock.png: visualizzazione a barre aggregate per topic

Output attesi
Grafico aggregato per categoria (Bitcoin, AI, Climate Change) e sentiment associato, utile per una rapida analisi d'impatto tematico.
