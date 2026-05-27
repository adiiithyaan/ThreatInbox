from flask import Flask, render_template, request
import joblib
from feature_engineering import URLFeatures

app = Flask(__name__)

pipeline = joblib.load("pipeline.pkl")

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        email = request.form.get("email")

        file = request.files.get("file")

        if file and file.filename != "":
            email = file.read().decode("utf-8")

        prediction = pipeline.predict([email])[0]

        confidence = max(pipeline.predict_proba([email])[0]) * 100

        result = "Phishing" if prediction == 1 else "Safe"

        return render_template("result.html",
                               prediction=result,
                               confidence=round(confidence, 2))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)