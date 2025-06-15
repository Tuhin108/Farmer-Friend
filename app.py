import os
from flask import Flask, render_template, request
from mistralai import Mistral

app = Flask(__name__)

# Load the API key from the environment
api_key = os.environ.get("MISTRAL_API_KEY", "your_api_key_here")
model = "mistral-large-latest"

# Initialize the Mistral client
client = Mistral(api_key=api_key)

def get_mistral_response(prompt):
    """
    Uses the Mistral API to get a chatbot response based on the provided prompt.
    """
    try:
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {"role": "user", "content": prompt},
            ]
        )
        # Adjust this parsing if the response structure changes
        return chat_response.choices[0].message.content
    except Exception as e:
        return f"Error retrieving recommendation: {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crop', methods=['GET', 'POST'])
def crop():
    if request.method == 'POST':
        # Collect inputs from the crop recommendation form
        location    = request.form.get('location')
        nitrogen    = request.form.get('nitrogen')
        potassium   = request.form.get('potassium')
        phosphorus  = request.form.get('phosphorus')
        temperature = request.form.get('temperature')
        humidity    = request.form.get('humidity')
        ph_value    = request.form.get('ph_value')
        rainfall    = request.form.get('rainfall')

        # Build a prompt using the provided inputs
        prompt = (
            f"Based on the following conditions for crop recommendation:\n"
            f"Location: {location}\n"
            f"Nitrogen: {nitrogen}\n"
            f"Potassium: {potassium}\n"
            f"Phosphorus: {phosphorus}\n"
            f"Temperature: {temperature}\n"
            f"Humidity: {humidity}\n"
            f"pH: {ph_value}\n"
            f"Rainfall: {rainfall}\n"
            "Please recommend the best crop to grow for maximizing profits."
        )

        recommendation = get_mistral_response(prompt)
        return render_template('result.html', recommendation=recommendation)
    return render_template('crop.html')

@app.route('/fertilizer', methods=['GET', 'POST'])
def fertilizer():
    if request.method == 'POST':
        # Collect inputs from the fertilizer recommendation form
        temperature = request.form.get('temperature')
        humidity    = request.form.get('humidity')
        moisture    = request.form.get('moisture')
        soil_type   = request.form.get('soil_type')
        crop_type   = request.form.get('crop_type')
        nitrogen    = request.form.get('nitrogen')
        potassium   = request.form.get('potassium')
        phosphorus  = request.form.get('phosphorus')

        # Build a prompt using the provided inputs
        prompt = (
            f"Based on the following conditions for fertilizer recommendation:\n"
            f"Temperature: {temperature}\n"
            f"Humidity: {humidity}\n"
            f"Moisture: {moisture}\n"
            f"Soil Type: {soil_type}\n"
            f"Crop Type: {crop_type}\n"
            f"Nitrogen: {nitrogen}\n"
            f"Potassium: {potassium}\n"
            f"Phosphorus: {phosphorus}\n"
            "Please recommend the best fertilizer to use for optimal crop health."
        )

        recommendation = get_mistral_response(prompt)
        return render_template('result.html', recommendation=recommendation)
    return render_template('fertilizer.html')

if __name__ == '__main__':
    app.run(debug=True)
