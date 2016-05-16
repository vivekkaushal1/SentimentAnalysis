from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
import twilio.twiml
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import time

account_sid = "ACd4d2ed67e95352bec6e67d7575853ed5"
auth_token = "34939163211d4a7e8ec1a6789de9aa67"

app = Flask(__name__)

client = TwilioRestClient(account_sid, auth_token)

@app.route('/', methods=['GET', 'POST'])
def welcome():
	resp = twilio.twiml.Response()
	resp.say("Thank you for calling.")
	with resp.gather(numDigits=1, action="/analyze", method="POST") as g:
		g.say("""Press 1 to record your voice.""")
	return str(resp)

@app.route("/analyze", methods=['GET', 'POST'])
def sentiment():
	key_pressed = request.values.get('Digits', None)
	if key_pressed == "1":
		resp = twilio.twiml.Response()
		resp.say("Please record your message.")
		resp.record(maxLength="60", action="/handleRecord", transcribe='true')
		return str(resp)
	else:
		return redirect("/")

@app.route("/handleRecord", methods=['GET', 'POST'])
def sentimentAnalysis():
	resp = twilio.twiml.Response()
	#recording_url = request.values.get("RecordingUrl", None)
	#resp.play(recording_url)
	#transcription = client.transcriptions.get('TR1d6dcd65b92da276c4be2b40701a99f4')
	#sentence = transcription.transcription_text
	
#	v = someFunction(sentence)
#	resp.say("Please check your messages.")
	with resp.gather(numDigits=1, action="/please", method="POST") as g:
		g.say("Press 2 to generate report.")

	return str(resp)

@app.route("/please", methods=['GET', 'POST'])
def someFunction():
	key_pressed = request.values.get("Digits", None)
	if key_pressed =="2":
                time.sleep(15)
		resp = twilio.twiml.Response()
		trans = []
		for t in client.transcriptions.list():
                        trans.append(str(t.sid))
                print "0"
                #print (trans)
                #work = trans[0]
                #print work
                tran = client.transcriptions.get('TRc24e962c979c03d1309cb92b6480ea25')
##                if client.status.get(trans[0])=='completed':
##                        tran = client.transcriptions.get(trans[0])
##                        print (tran)
##                else:
##                        print(client.status.get(trans[0]))
		text = str(tran.transcription_text)
		#print (text)
		#resp.say(text)
		#client.messages.create(to="+16825646201", from_="+16822324171", body=text)
		sid = SentimentIntensityAnalyzer()
		print "1"
		ss = sid.polarity_scores(text)
		print "2"
		result=[]
		#resp.say("Pass.")
		for k in sorted(ss):
			result.append('{0}, {1}'.format(k, ss[k]))
		#print (result)
		neg,valNeg = result[1].split(" ")
		pos,valPos = result[3].split(" ")
		if valNeg < valPos:
			client.messages.create(to="+16825646201", from_="+16822324171", body="The statement is Positive.")
		else:
			client.messages.create(to="+16825646201", from_="+16822324171", body="The statement is Negative.")
		resp.say("Bye. Have a great day.")
		return str(resp)

	else:
		return redirect("/")

if __name__ == '__main__':
	app.run()
