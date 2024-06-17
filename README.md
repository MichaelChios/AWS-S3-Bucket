# Basic Cloud Computing Project

## Fetch data from a REST API
I used https://rapidapi.com/hub to choose a free API that I liked and then I extracted the data and saved it in a JSON file.

## Clean the raw data
I parsed through the raw data and selected only what I needed and stored it in a different JSON file.

## Create an SQL Database and store the filtered data
Using SQLite, I created a database with only one table and some columns, based on the filtered data. The data I used required multiple tables, as the best practice,
but I used only one, as it wasn't the main point of the project.

## Extract the data from the database and convert it to a csv file.
With a basic "SELECT" query, I extracted the data from the database and converted it into a csv file.

## Store the csv file in an AWS S3 Bucket
First, I created a free account in https://aws.amazon.com/s3/ and then I created an S3 Bucket and stored the csv file.\
You can find easy guides on how to create an account and an AWS Bucket on YouTube.
