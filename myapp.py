from flask import Flask, request, render_template
from aiGPT import aiGPT

app = Flask(__name__)
model = aiGPT()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    prediction = model.predict(text)
    return render_template('results.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
