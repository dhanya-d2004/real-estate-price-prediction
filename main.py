from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load cleaned data and model
data = pd.read_csv('cleaned_data.csv')
pipe = pickle.load(open("RidgeModel.pkl", 'rb'))

@app.route('/')
def index():
    # Get sorted unique locations for the dropdown
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    # Collect form inputs
    location = request.form.get('location')
    bhk = int(request.form.get('bhk'))
    bath = int(request.form.get('bath'))
    sqft = float(request.form.get('total_sqft'))

    # Create input DataFrame for prediction
    input_df = pd.DataFrame([[location, sqft, bath, bhk]],
                            columns=['location', 'total_sqft', 'bath', 'bhk'])

    # Predict and return the price
    prediction = pipe.predict(input_df)[0]
    return f"Predicted Price: ₹{round(prediction, 2)} lakhs"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
