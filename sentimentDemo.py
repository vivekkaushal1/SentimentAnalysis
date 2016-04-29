from flask import Flask, request, render_template
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from twilio.rest import TwilioRestClient

#app = Flask(__name__)
#Twilio API Credentials
account_sid = ""
auth_token = ""
client = TwilioRestClient(account_sid, auth_token)

##@app.route('/')
##def my_form():
##    return render_template("index.html")

#@app.route('/', methods=['GET', 'POST'])
#def index():
    #toCall = request.form['senty']
call = client.calls.create(url="Twiml file URL.",
                           to ="NUmber to call.",
                           from_="Twilio API registered number.", method="GET",record="true")
#trans_sid = call.sid
    #sentence = request.form['senty']
notifications = client.calls.get(call.sid).recordings.list()
for n in notifications:
    print (n.sid)
    
trans = client.recordings.get(record_sid).transcriptions.list()
for t in trans:
    trans_sid = t.sid

transcription = client.transcriptions.get(trans_sid)
sentence = transcription.transcription_text
print(sentence)
sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(sentence)
for k in sorted(ss):
    print('{0}: {1}, '.format(k, ss[k]))
    #return render_template('index.html')
#print(ss)

##if __name__ == '__main__':
##    app.run(host='127.0.0.1', port=int('8080'), debug=True)
