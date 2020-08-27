# A Happy Meal: Predicting McDonald's User Ratings on Yelp Utilizing NLP and Machine Learning

![yelp_title](img/yelp-logo.png)

## Overview

McDonald's Corporation is an American fast food company, founded in 1940 as a restaurant operated by Richard and Maurice McDonald, in San Bernardino, California, United States. They rechristened their business as a hamburger stand, and later turned the company into a franchise, with the Golden Arches logo being introduced in 1953 at a location in Phoenix, Arizona. In 1955, Ray Kroc, a businessman, joined the company as a franchise agent and proceeded to purchase the chain from the McDonald brothers. McDonald's had its original headquarters in Oak Brook, Illinois, but moved its global headquarters to Chicago in June 2018. [(source: Wikipedia)](https://en.wikipedia.org/wiki/McDonald%27s)

Yelp is an American public company headquartered in San Francisco, California. The company develops, hosts, and markets the Yelp.com website and the Yelp mobile app, which publish crowd-sourced reviews about businesses. It also operates an online reservation service called Yelp Reservations. [(source: Wikipedia)](https://en.wikipedia.org/wiki/Yelp)]

A critical

## Contents

- [Dataset](#Dataset)
- [Questions](#Questions)
- [Exploration](#Exploration)
- [Analysis](#Analysis)
- [Geography](#Geography)
- [Summary](#Summary)
- [Discussion](#Discussion)

# Dataset

The original [Yelp dataset](https://www.yelp.com/dataset/) contains:

- 8,021,122 reviews
- 209,393 businesses
- 200,000 pictures
- 10 metropolitan areas
- 1,320,761 tips
- 1,968,703 users
- Over 1.4 million business attributes like hours, parking, availability, and ambience
- Aggregated check-ins over time for each of the 209,393 businesses

![million](img/million_rows.gif)

See [Dataset Documentation.](https://www.yelp.com/dataset/documentation/main)

## Filtering for "McDonald's" restaurants

First, we search for businesses in the "business "dataset" that have the string "McDonald's" in the "name" column.

The "reviews" dataset with the "McDonald's" dataset are merged on the "business_id" column.

A final dataframe is created for McDonald's businesses with Yelp reviews: **20414 rows by 18 columns.**

The dataset encompasses a total of **12 states/provinces and a 216 cities.**

---

```
Number of Stores Currently Open:  799
Number of Stores Currently Closed:  56
Total Number of Unique Stores:  855
Number of Total Reviews:  20414
```

# Questions

- What food words or menu items are most likely discussed in reviews?
- Which states/provinces or cities have the highest number of reviews?
- What meal time (e.g, breakfast, lunch, dinner, brunch) is mentioned the most in reviews?
- What menu items (e.g., French fries, McNuggets, Big Mac, Coke, Quarterpounder) are mentioned the most in reviews?

# Objective

- number of topics
- key words
- dominant topic of each review
- topic modeling
- sentiment analysis
- correlation positiv eand negative
- recommendations
- geography patterns (by state/province and city)

# Exploration

# NLP

## Text Preprocessing

### Raw Text

```
"I think most of us have certain expectations of any restaurant. My experience with this location has poisoned me against all McDonald's. It started when my wife said she wanted a fruit smoothy. We ordered our smoothies which came to $8 for 2 larges. Cool fun thing to do right...\n\nThe next day I saw my card had been double charged. So I went back and asked the manager if she could make it right. I said I didn't even need a cash refund it would have been fine to just take it off the order I was about to make. She said she could not do that and that she had no way to look it up. She gave me a phone number to their office in Mentor. I called the person in Mentor who looked up my order she said I needed to wait 10 days or so because the card had been authorized but not charged twice. \n\n10 days later the charge came off but I expect when I go out for food my card will not be double authorized. Be that as it may $8 worth of food would have fixed this. I will NEVER go back to McDonald's because of how this was handled."
```

### Round 1

```
'i think most of us have certain expectations of any restaurant my experience with this location has poisoned me against all mcdonalds it started when my wife said she wanted a fruit smoothy we ordered our smoothies which came to  for  larges cool fun thing to do right\n\nthe next day i saw my card had been double charged so i went back and asked the manager if she could make it right i said i didnt even need a cash refund it would have been fine to just take it off the order i was about to make she said she could not do that and that she had no way to look it up she gave me a phone number to their office in mentor i called the person in mentor who looked up my order she said i needed to wait  days or so because the card had been authorized but not charged twice <mark>\n\n<mark> days later the charge came off but i expect when i go out for food my card will not be double authorized be that as it may  worth of food would have fixed this i will never go back to mcdonalds because of how this was handled'
```

### Round 2

```
'i think most of us have certain expectations of any restaurant my experience with this location has poisoned me against all mcdonalds it started when my wife said she wanted a fruit smoothy we ordered our smoothies which came to  for  larges cool fun thing to do rightthe next day i saw my card had been double charged so i went back and asked the manager if she could make it right i said i didnt even need a cash refund it would have been fine to just take it off the order i was about to make she said she could not do that and that she had no way to look it up she gave me a phone number to their office in mentor i called the person in mentor who looked up my order she said i needed to wait  days or so because the card had been authorized but not charged twice  days later the charge came off but i expect when i go out for food my card will not be double authorized be that as it may  worth of food would have fixed this i will never go back to mcdonalds because of how this was handled'
```

## Insights

### By Food

### By Time

### By Emotion

### By People

# Analysis

## "A picture is worth a thousand words."

### Text Length of Review By Rating (1-5 Stars)

![text_length](img/text_length_by_stars.png)

## "The customer is always right."

# Geography

## Arizona

- 8 out of the top 15 cities with the highest number of reviews are in Arizona.

![by_city](img/by_city.png)

## Nevada

- The state/prvoince with the highest number of reviews is Nevada.
- The city with the highest number of reviews is Las Vegas.

# Machine Learning Models

## Classification

### Random Forest

```
[[2529    0    5    1   14]
 [ 435    2    8    2   10]
 [ 270    1   29   23   58]
 [ 162    1   21   34  102]
 [ 161    0    7   21  187]]
              precision    recall  f1-score   support

         1.0       0.71      0.99      0.83      2549
         2.0       0.50      0.00      0.01       457
         3.0       0.41      0.08      0.13       381
         4.0       0.42      0.11      0.17       320
         5.0       0.50      0.50      0.50       376

    accuracy                           0.68      4083
   macro avg       0.51      0.34      0.33      4083
weighted avg       0.62      0.68      0.59      4083

0.6811168258633358
```

In predicting ratings using NLP from text data of reviews, the Random Forest algorithm achieved an accuracy of **68.11%**.

### Multinomial Naive Bayes

```
Confusion Matrix for Multinomial Naive Bayes:
[[2542    1    5    0    1]
 [ 433    5   15    1    3]
 [ 250    7   68   32   24]
 [ 164    3   50   48   55]
 [ 187    0   11   22  156]]
Score: 69.04
Classification Report:               precision    recall  f1-score   support

         1.0       0.71      1.00      0.83      2549
         2.0       0.31      0.01      0.02       457
         3.0       0.46      0.18      0.26       381
         4.0       0.47      0.15      0.23       320
         5.0       0.65      0.41      0.51       376

    accuracy                           0.69      4083
   macro avg       0.52      0.35      0.37      4083
weighted avg       0.62      0.69      0.61      4083
```

In predicting ratings using NLP from text data of reviews, the Multinomial Naive Bayes algorithm achieved an accuracy of **69.04%**

### Decision Tree

```
Confusion Matrix for Decision Tree:
[[2019  223  145   72   90]
 [ 269   75   60   25   28]
 [ 137   54   76   58   56]
 [  65   32   51   62  110]
 [  85   22   50   69  150]]
Score: 58.34
Classification Report:               precision    recall  f1-score   support

         1.0       0.78      0.79      0.79      2549
         2.0       0.18      0.16      0.17       457
         3.0       0.20      0.20      0.20       381
         4.0       0.22      0.19      0.20       320
         5.0       0.35      0.40      0.37       376

    accuracy                           0.58      4083
   macro avg       0.35      0.35      0.35      4083
weighted avg       0.58      0.58      0.58      4083
```

In predicting ratings using NLP from text data of reviews, the Multinomial Naive Bayes algorithm achieved an accuracy of **58.34%**.

### Support Vector Machines (SVM)

# Summary

- Arizona and Nevada have a high number of reviews for McDonald's in their state.
- Burgers and fries are commonly talked about in reviews.
- Breakfast is the most commonly talked about meal of the day in reviews.
- Although the official menu item is called chicken "McNuggets", the majority of users refer to the menu item as just simply "nuggets".
- In addition, customers prefer to use "fries" instead of "French fries" much more often in the written reviews.

![nuggets](img/nuggets.gif)

# Discussion

- How can company stakeholders make strategic decisions in product development given these insights from data?
- What metrics can be analyzed to indicate performance through the next quarter or fiscal year?
- How can data scientists utilize machine learning to detect fake reviews that artificially affect the ratings of businsesses?

![ronald](img/ronald_dance.gif)
