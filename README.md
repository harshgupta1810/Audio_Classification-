# Audio Classification using MFCC and Neural Networks

This project is an implementation of audio classification using Mel-Frequency Cepstral Coefficients (MFCC) and Neural Networks. The code provided here is the first part of the project, which includes data preprocessing, feature extraction, model creation, and training.

## Dataset Description

The dataset used for this project is the UrbanSound8K dataset, which contains 8732 labeled sound excerpts (<=4s) of urban sounds from 10 classes: air_conditioner, car_horn, children_playing, dog_bark, drilling, engine_idling, gun_shot, jackhammer, siren, and street_music. The classes are drawn from the urban sound taxonomy. The audio files are pre-sorted into ten folds (folders named fold1-fold10) to help in the reproduction of and comparison with the automatic classification results.

### Dataset Source
The dataset can be downloaded from Kaggle using the following command:
```bash
kaggle datasets download -d chrisfilo/urbansound8k
```

## Table of Contents

1. [Project Name](#project-name)
2. [Dataset Description](#dataset-description)
3. [Table of Contents](#table-of-contents)
4. [frontend](#frontend)
5. [Project Demo](#project-demo)
6. [Installation](#installation)
7. [Usage](#usage)
8. [Configuration](#configuration)
9. [Contributing](#contributing)
10. [License](#license)
11. [Acknowledgments](#acknowledgments)
12. [Documentation](#documentation)

# Frontend for Audio Classification

This is the frontend part of the Audio Classification project. It consists of a Flask web application (`app.py`) and an HTML template (`index.html`) for audio classification.

### `app.py`

This Flask web application serves as the backend for the audio classification. It loads the trained model and provides an endpoint for audio prediction.

### Project Setup

1. Install the required libraries using `pip`.
```bash
pip install flask tensorflow numpy librosa
```

2. Save the trained model as `final_model1.h5` in the same directory as `app.py`.

### Code Explanation

- The Flask application loads the trained model using `tf.keras.models.load_model`.
- It defines two routes - `/` for rendering the main page and `/predict` for handling audio classification.
- When a POST request is made to `/predict`, it reads the audio file from the request, extracts MFCC features, and performs audio classification using the loaded model.
- The predicted class label is returned as the response.

### `index.html`

This HTML template creates a simple web page for audio classification. Users can either drag and drop an audio file or select it using the file input. The predicted class label will be displayed, and the audio will be played on the page.

### Code Explanation

- The template uses CSS styles for styling and responsiveness.
- It contains a drop area where users can drag and drop the audio file or use the file input to upload.
- The JavaScript code handles the file upload, sends it to the backend for classification, and displays the predicted class label on the page.
- The predicted class label is shown in a result div, and the audio is played using the audio element.

Note: This frontend is designed to work with the backend code provided earlier. Make sure to run the Flask web application (`app.py`) to use this frontend for audio classification.

---

_Frontend code designed and developed by Harsh Gupta (Desperate Enuf)._

## Project Name

Audio Classification using MFCC and Neural Networks

## Project Demo

_Replace this section with a link or instructions on how to access the live demo of your project._


## Installation

1. Clone the repository to your local machine.
```bash
git clone <repository_url>
```

2. Install the required Python packages.
```bash
pip install -r requirements.txt
```

## Usage

1. Download the UrbanSound8K dataset from Kaggle using the provided command.

2. Run the Jupyter notebook `audio_classification.ipynb` to preprocess the audio data, extract MFCC features, create and train the neural network model.

3. To use the trained model for prediction, load the saved model and pass an audio file through it. An example for doing this is given in the last section of the Jupyter notebook.

## Configuration

_No specific configuration is required for this project._

## Contributing

_If you wish to contribute to this project, please follow the guidelines below:_
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with descriptive commit messages.
4. Push your changes to your forked repository.
5. Create a pull request to the original repository.

## License

_This project is licensed under the [MIT License](LICENSE)._

## Acknowledgments

_Include any credits or acknowledgments you want to give to others or resources you have used._

## Documentation

_Replace this section with detailed documentation for the project. You can include information on how to use the code, the meaning of different functions, explanations of the concepts used (such as MFCC), and any other relevant information to help beginners understand the code._

---

_Designed and developed by Harsh Gupta (Desperate Enuf)._
