# social_media_sentiment_analysis
Data scraping from social media platforms can provide insights into public sentiment regarding climate change and insurance industry responses.

This project aims to analyze social media sentiment data and classify sentiments into positive, negative, and neutral categories. 
It leverages Natural Language Processing (NLP) techniques and machine learning algorithms to extract valuable insights from textual data.

Prerequisites
Ensure you have the following installed:

Python 3.6 or higher
pip (Python package installer)

Setup Instructions
Clone the Repository

Clone this repository to your local machine:

git clone https://github.com/your_username/social_media_sentiment_analysis.git
cd social_media_sentiment_analysis

Dataset
The project uses a dataset containing social media posts and their corresponding sentiment labels. Ensure the dataset is in CSV format and structured as follows:

Columns:
Unnamed: 0: Index (not used in analysis)
Text: The actual text of the social media post
Sentiment: The sentiment label (Positive, Negative, Neutral)
Other columns (optional): Timestamp, User, Platform, Hashtags, Retweets, Likes, Country, Year, Month, Day, Hour.
Please store your dataset in a folder named data and name the CSV file as sentimentdataset.csv.

Installation
Run the following commands to install the required packages:
pip install pandas scikit-learn nltk matplotlib seaborn

Running the Analysis
To execute the sentiment analysis, run the following command in your terminal:

python sentiment_analysis.py
