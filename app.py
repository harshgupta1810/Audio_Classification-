from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import librosa

app = Flask(__name__)
model = tf.keras.models.load_model('./final_model1.h5')
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    audio, sample_rate = librosa.load(file)
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_scaled_features = np.mean(mfccs_features.T, axis=0)
    mfccs_scaled_features = mfccs_scaled_features.reshape(1, -1)

    # Make predictions using the loaded model
    predictions = model.predict(mfccs_scaled_features)
    predicted_label = np.argmax(predictions)

    # Map the predicted label index to the actual class label
    class_names = ['Air Conditioner', 'Car Horn', 'Children Playing', 'Dog Bark',
                   'Drilling', 'Engine Idling', 'Gun Shot', 'Jackhammer', 'Siren',
                   'Street Music']
    prediction_class = class_names[predicted_label]

    return prediction_class
if __name__ == '__main__':
    app.run(debug=True)