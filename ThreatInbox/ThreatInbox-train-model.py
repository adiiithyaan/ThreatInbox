import pandas as pd
import re
import joblib

from feature_engineering import URLFeatures
from datasets import load_dataset
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression



print("Loading dataset in streaming mode...")

dataset = load_dataset(
     "SetFit/enron_spam",
    split="train",
    streaming=True
)

texts = []
labels = []


MAX_SAMPLES = 50000

for i, sample in enumerate(dataset):

    text = sample.get("text") or sample.get("email") or ""

    label = sample.get("label")

    if text and label is not None:

        if isinstance(label, str):
            label = label.lower()

        texts.append(text)
        labels.append(label)

    if i >= MAX_SAMPLES:
        break

print(f"Loaded {len(texts)} samples")


df = pd.DataFrame({
    "text": texts,
    "label": labels
})

class URLFeatures(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        features = []

        for text in X:

            urls = re.findall(r'https?://\S+|www\.\S+', str(text))

            num_urls = len(urls)

            suspicious_words = len(re.findall(
                r'urgent|verify|password|bank|login|click|account|suspended|update',
                str(text).lower()
            ))

            long_urls = sum(len(url) > 30 for url in urls)

            features.append([
                num_urls,
                suspicious_words,
                long_urls
            ])

        return pd.DataFrame(features)


features = FeatureUnion([

    ("tfidf", TfidfVectorizer(
        stop_words="english",
        max_features=5000
    )),

    ("url_features", URLFeatures())

])


pipeline = Pipeline([

    ("features", features),

    ("classifier", LogisticRegression(
        max_iter=1000
    ))

])


print("Training model...")

X = df["text"]
y = df["label"]

pipeline.fit(X, y)


joblib.dump(pipeline, "pipeline.pkl")

print("✅ ThreatInbox model trained and saved successfully!")