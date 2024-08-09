# Movie Recommendation System with Sentiment Analysis

## Screenshot
![WhatsApp Image 2024-08-07 at 10 39 51 PM](https://github.com/user-attachments/assets/1a8ad923-c9fc-42f5-93c1-c2ea0c806d53)

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model](#model)
- [Sentiment Analysis](#sentiment-analysis)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Overview
This project aims to create a movie recommendation system that incorporates sentiment analysis to improve the accuracy of recommendations. The system uses user reviews and ratings to recommend movies that the user is likely to enjoy. The sentiment analysis component helps in understanding the emotions conveyed in the reviews to further refine the recommendations.

## Features
- Personalized movie recommendations based on user ratings and reviews.
- Sentiment analysis on user reviews to enhance recommendation accuracy.
- Interactive user interface to input ratings and reviews.
- Visualization of recommendation results.

## Installation
To set up this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AmulyaShetty11/Movie-Recommendation-System-with-Sentiment-Analysis.git
   cd Movie-Recommendation-System-with-Sentiment-Analysis
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the project, follow these steps:

1. **Start the application:**
   ```bash
   python app.py
   ```

2. **Open your web browser and navigate to:**
   ```
   http://localhost:5000
   ```

3. **Interact with the application:**
   - Input your movie ratings and reviews.
   - Get personalized movie recommendations.

## Dataset
The dataset used in this project includes user ratings and reviews of movies. You can download the dataset from [MovieLens](https://grouplens.org/datasets/movielens/) or any other similar source.

## Model
The recommendation system utilizes collaborative filtering and content-based filtering techniques to provide movie recommendations. The sentiment analysis model is built using natural language processing (NLP) techniques to analyze the sentiment of user reviews.

## Sentiment Analysis
The sentiment analysis component uses pre-trained NLP models to determine the sentiment of user reviews. This analysis helps in understanding the user's emotional response to movies, which in turn improves the accuracy of recommendations.

## Technologies Used
- **Programming Language:** Python
- **Web Framework:** Flask
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn, TensorFlow/Keras
- **Natural Language Processing:** NLTK, TextBlob, or similar libraries
- **Visualization:** Matplotlib, Seaborn
- **Database:** SQLite or any other suitable database

## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. **Fork the repository**
2. **Create a new branch:**
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Commit your changes:**
   ```bash
   git commit -m 'Add some feature'
   ```
4. **Push to the branch:**
   ```bash
   git push origin feature/YourFeature
   ```
5. **Open a pull request**

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements
- Thanks to the [MovieLens](https://grouplens.org/datasets/movielens/) for providing the movie rating dataset.
- Special thanks to the developers of the libraries and tools used in this project.
