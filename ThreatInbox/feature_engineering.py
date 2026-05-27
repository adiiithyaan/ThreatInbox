import re
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class URLFeatures(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        features = []

        for text in X:

            text = str(text)

            urls = re.findall(r'https?://\S+|www\.\S+', text)

            num_urls = len(urls)

            suspicious_words = len(re.findall(
                r'urgent|verify|password|bank|login|click|account|suspended|update',
                text.lower()
            ))

            long_urls = sum(len(url) > 30 for url in urls)

            features.append([
                num_urls,
                suspicious_words,
                long_urls
            ])

        return pd.DataFrame(features)