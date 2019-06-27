import polarity_analyser
from textblob import TextBlob
import tweepy
from flask import Flask, render_template, request
app = Flask(__name__)


consumerkey = "#"
consumersecret = "#"
accesstoken = "#"
accesstokensecret = "#"

auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesstokensecret)
api = tweepy.API(auth)


@app.route("/")
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    # explicit 404
    return render_template('404.html'), 404


@app.route("/read", methods=['GET', 'POST'])
def index4():
    if(request.method == "POST"):

        global positive, negative, neut, pname
        pname = request.form["product"]
        #print(type(pname)
        fetchtweets = api.search(pname)

        x = 0
        positive= 0
        negative= 0
        neut = 0

        tweets = list()
        for i in fetchtweets:
            x = x + 1

            analysis = polarity_analyser.polarity_finder(
                polarity_analyser.replacement_patterns(polarity_analyser.tokenize_words(i.text)))
            print(analysis)
            #print(i.text)
            tweets.append(i.text)
            #print(analysis)
            if(analysis > 0):
                #print("positive")
                positive= positive+ 1
            elif(analysis == 0):
                #print("neutral")
                neut = neut + 1
            else:
                #print("negative")
                negative= negative+ 1

        #print("total tweets")
        #print(x)
        #print("positive tweets")
        #print(count)
        #print("negative tweets")
        #print(count1)
        #print("percentage of positives")
        a = round((positive/ x) * 100, 2)
        #print(a)
        #print("percentage of negatives")
        b = round((negative/ x) * 100, 2)
        #print(b)
        #print("percentage of neutral")
        c = round((neut / x) * 100, 2)
        #print(c)
        #print(pname)
        if a >= 80:
            recom = "Very Good"
        elif 50 < a < 80:
            recom = "Good"
        elif 30 < a < 51:
            recom = "Not comparable"
        elif 10 < a < 31:
            recom = "Bad"
        else:
            recom = "Awful"

        return render_template('test.html', totaltweets=x, positivetweets=positive, negativetweets=negative, neutraltweets=neut, percentageofpositives=a, percentageofnegatives=b, percentageofneutral=c, len=len(tweets), tweets=tweets, Grade=recom,
                               prod=pname)


@app.route('/pie_charts', methods=['GET', 'POST'])
def pie_charts():
    global positive, negative, neut, pname
    if request.method == 'POST':

        return redirect(url_for('index'))

    return render_template('pie_charts.html', positives=positive, negatives=negative, neutrals=neut, pname=pname)


@app.route('/aboutus', methods=['GET', 'POST'])
def index1():
    return render_template('aboutus.html')


if(__name__ == "__main__"):
    app.run(debug=True)
