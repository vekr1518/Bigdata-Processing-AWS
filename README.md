# Bigdata-Processing-AWS

## Introduction
In this project, we are going to process a dataset from kaggle (Amazon Book Ratings.csv). The dataset is huge (3 GB) and has 1 million records.
We are going to process this 3 GB data in AWS EMR Framework.

## Architecture

## Implementation Steps
* Load the source data from [Kaggle](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews) to S3 bucket
* Create an EMR cluster with EC2 instance 
* Create a key value pair and connect to the cluster using SSH in your terminal
* Create a script [Amazon_Book_Review.py](https://github.com/vekr1518/Bigdata-Processing-AWS/blob/main/Amazon_Book_Review.py)
* Execute the script using spark-submit

