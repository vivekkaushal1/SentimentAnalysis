Sentiment Analysis on Recorded Voice using Twilio API

Description:
The attached python code is a flask app to perform sentiment analysis on the user recorded voice by converting it to text using the Twilio Transcription API.
I have used Python NLTK Sentiment Analysis library to perform sentiment analysis of the generated text.
The flaskapp is deployed on Ubuntu virtual machine on AWS on an EC2 instance.
The Public DNS link of the EC2 instance serves as the server to the Twilio API to route different functions.
Pre-requisites to run the app:
> Python 2.7.11
> Twilio Client
> Flask Framework
> Python NLTK
> Vader Data from NLTK library
I installed these on the Ubuntu VM on AWS and deployed the flaskapp on it.
To run the file a user just needs to run the flaskapp.py file included in the report.
As the restrictions of Free Account on Twilio only 1 registered number can make and receive calls and messages from the Twilio client.



