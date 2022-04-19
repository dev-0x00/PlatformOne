import requests
import time

from  tweeterbot import Twitter

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=["POST"])
def SendToBot():
    #fetch user message from whatsapp
    message = request.values.get("Body",  "").lower()
    greetings = ["hello", "hi"]

    if "hello" in message:
        """this  is the greeting part incase its the first theing the user sends"""
        #sending message back to the bot
        response = MessagingResponse()
        message = response.message()
        message.body("Hello, how may i help you?")

    elif "feeds" and "twitter" in message:

        #sending tweets from my timeline, 10 tweet each time this endpoint is hit.
        response = MessagingResponse()
        message = response.message()
        twitter = Twitter()
        api = twitter.Authentication()
        tweets = twitter.Tweets(api)
        for tweet in tweets:   
            message.body(f"{tweet}")        
    elif "trending" and "twitter" in message:
        #sending message back to the bot
        response = MessagingResponse()
        message = response.message()
        twitter = Twitter()
        api = twitter.Authentication()
        trending = twitter.Trending(api)
        message.body("{}".format(trending))

    elif "search" in message:
        keyword = message.split(" ")[1]
        #sending message back to the bot
        response = MessagingResponse()
        message = response.message()
        message.body("returning search results for {}".format(keyword))
    
    else:
        #sending message back to the bot
        response = MessagingResponse()
        message = response.message()
        message.body("Nothing fetched from any media")
        
    return str(response)


if __name__ == "__main__":
    app.run()

