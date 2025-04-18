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

Social Media Sentiments Analysis Dataset
https://www.kaggle.com/datasets/kashishparmar02/social-media-sentiments-analysis-dataset

Clone this repository to your local machine:

git clone https://github.com/your_username/social_media_sentiment_analysis.git
git clone https://github.com/Ravina510/Sentiment-Analysis.git
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

Modify the Script:
Make sure your sentiment_analysis.py file includes the necessary modules and data processing as outlined before.

Testing Execution:

After setting up, simply run:
python sentiment_analysis.py
Copy code 
Expected Output:

When the script runs successfully, it should output:
A printed accuracy score.
A classification report with precision, recall, and F1-scores for each sentiment class.
A confusion matrix chart depicting the model’s classification performance.

Evaluation Metrics
Depending on the output of the sentiment analysis, the following metrics will be available:

Precision: The proportion of positive identifications that were actually correct.
Recall: The proportion of actual positives that were identified correctly by the model.
F1-Score: The harmonic mean of precision and recall, providing a balance between them.
Support: The number of actual occurrences of each class in the specified dataset.
License
This project is licensed under the MIT License - see the LICENSE file for details.

------------------------------------------------------------

output from terminal
C:\Users\ravina\Desktop\Python\ClimateRiskNewsSummarizer>python sentiment_analysis.py
[nltk_data] Downloading package stopwords to
[nltk_data]     C:\Users\H555606\AppData\Roaming\nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
   Unnamed: 0.1  Unnamed: 0                                               Text    Sentiment            Timestamp            User     Platform  ... Retweets  Likes       Country  Year  Month  Day  Hour 
0             0           0   Enjoying a beautiful day at the park!        ...   Positive    2023-01-15 12:30:00   User123          Twitter    ...     15.0   30.0     USA        2023      1   15    12 
1             1           1   Traffic was terrible this morning.           ...   Negative    2023-01-15 08:45:00   CommuterX        Twitter    ...      5.0   10.0     Canada     2023      1   15     8 
2             2           2   Just finished an amazing workout! 💪          ...   Positive    2023-01-15 15:45:00   FitnessFan      Instagram   ...     20.0   40.0   USA          2023      1   15    15
3             3           3   Excited about the upcoming weekend getaway!  ...   Positive    2023-01-15 18:20:00   AdventureX       Facebook   ...      8.0   15.0     UK         2023      1   15    18 
4             4           4   Trying out a new recipe for dinner tonight.  ...   Neutral     2023-01-15 19:55:00   ChefCook        Instagram   ...     12.0   25.0    Australia   2023      1   15    19 

[5 rows x 15 columns]
Accuracy: 0.24
                        precision    recall  f1-score   support

         Acceptance          0.00      0.00      0.00         2
      Acceptance             0.00      0.00      0.00         0
           Admiration        0.00      0.00      0.00         1
        Admiration           0.00      0.00      0.00         1
         Affection           0.00      0.00      0.00         1
      Ambivalence            1.00      1.00      1.00         1
         Anger               0.00      0.00      0.00         1
        Anticipation         0.00      0.00      0.00         1
        Arousal              0.00      0.00      0.00         3
                  Awe        0.00      0.00      0.00         1
         Awe                 0.00      0.00      0.00         1
                  Bad        0.00      0.00      0.00         1
             Betrayal        0.00      0.00      0.00         2
        Betrayal             0.00      0.00      0.00         1
         Bitter              0.00      0.00      0.00         1
           Bitterness        1.00      1.00      1.00         1
          Bittersweet        0.00      0.00      0.00         1
              Boredom        0.00      0.00      0.00         1
         Calmness            0.00      0.00      0.00         1
          Captivation        0.00      0.00      0.00         1
     Celestial Wonder        0.00      0.00      0.00         1
             Colorful        0.00      0.00      0.00         1
      Confusion              1.00      0.33      0.50         3
           Connection        0.00      0.00      0.00         1
        Contemplation        0.00      0.00      0.00         1
          Contentment        0.50      0.33      0.40         3
        Contentment          0.00      0.00      0.00         1
         Coziness            0.00      0.00      0.00         1
         Creativity          0.00      0.00      0.00         1
            Curiosity        0.00      0.00      0.00         2
           Curiosity         0.00      0.00      0.00         0
          Curiosity          0.00      0.00      0.00         1
      Curiosity              1.00      1.00      1.00         2
           Desolation        0.33      1.00      0.50         1
              Despair        0.00      0.00      0.00         0
           Devastated        0.00      0.00      0.00         2
              Disgust        0.00      0.00      0.00         1
         Disgust             0.00      0.00      0.00         2
        Elation              0.00      0.00      0.00         3
             Elegance        0.00      0.00      0.00         1
          Embarrassed        0.00      0.00      0.00         1
       EmotionalStorm        0.00      0.00      0.00         1
        Empowerment          0.00      0.00      0.00         1
         Enjoyment           0.00      0.00      0.00         2
           Enthusiasm        0.00      0.00      0.00         1
              Envious        0.00      0.00      0.00         2
  Envisioning History        0.00      0.00      0.00         1
           Euphoria          0.00      0.00      0.00         0
         Euphoria            0.00      0.00      0.00         1
           Excitement        0.13      1.00      0.23         3
         Excitement          0.00      0.00      0.00         3
        Excitement           0.00      0.00      0.00         1
         Fear                0.00      0.00      0.00         1
              Fearful        1.00      1.00      1.00         1
           Frustrated        0.33      1.00      0.50         1
          Frustration        0.00      0.00      0.00         3
         Fulfillment         0.00      0.00      0.00         2
             Grateful        1.00      1.00      1.00         1
      Grief                  0.00      0.00      0.00         1
                Happy        0.00      0.00      0.00         6
                 Hate        1.00      0.50      0.67         2
           Heartbreak        0.00      0.00      0.00         2
              Hopeful        0.25      1.00      0.40         1
        InnerJourney         0.00      0.00      0.00         1
        Inspiration          0.00      0.00      0.00         1
             Inspired        1.00      1.00      1.00         1
            Isolation        0.00      0.00      0.00         1
          Jealousy           0.00      0.00      0.00         1
                  Joy        0.22      1.00      0.36         8
         Joy                 0.00      0.00      0.00         1
        JoyfulReunion        0.00      0.00      0.00         1
         Kind                0.00      0.00      0.00         1
           Loneliness        0.25      1.00      0.40         1
      Loneliness             0.00      0.00      0.00         1
             LostLove        0.00      0.00      0.00         1
      Melancholy             0.00      0.00      0.00         2
       Miscalculation        0.00      0.00      0.00         1
              Neutral        0.00      0.00      0.00         1
        Nostalgia            0.00      0.00      0.00         1
      Nostalgia              1.00      1.00      1.00         1
      Numbness               1.00      1.00      1.00         1
          Overwhelmed        0.00      0.00      0.00         1
              Playful        1.00      0.50      0.67         2
            Positive         0.13      0.67      0.22         9
                Proud        1.00      1.00      1.00         1
        Reflection           0.00      0.00      0.00         1
       Regret                0.00      0.00      0.00         1
           Resilience        0.00      0.00      0.00         1
            Reverence        0.00      0.00      0.00         1
                  Sad        0.00      0.00      0.00         0
         Sadness             0.00      0.00      0.00         2
        Satisfaction         0.00      0.00      0.00         1
             Serenity        0.00      0.00      0.00         2
        Serenity             0.00      0.00      0.00         0
      Serenity               1.00      0.50      0.67         2
             Solitude        0.00      0.00      0.00         1
          Sorrow             0.00      0.00      0.00         1
         Spark               0.00      0.00      0.00         1
         Surprise            0.00      0.00      0.00         1
        Thrill               0.00      0.00      0.00         1
             Vibrancy        0.00      0.00      0.00         1
 Whispers of the Past        0.00      0.00      0.00         1
                 Zest        0.00      0.00      0.00         1

              accuracy                           0.24       147
             macro avg       0.15      0.17      0.14       147
          weighted avg       0.17      0.24      0.16       147

Confusion Matrix:\n [[0 2 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 ...
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]]

