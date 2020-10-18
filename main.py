import config
import tweepy
from monkeylearn import MonkeyLearn

#setup aunthentication
auth=tweepy.OAuthHandler(config.consumer_key,config.consumer_secret)
auth.set_access_token(config.access_token,config.access_token_secret)
api=tweepy.API(auth)
ml = MonkeyLearn('c9fd6cb46ad6fdd3ce1f3ebfd2dd709988b2269f')

'''
public_tweets = api.home_timeline(count=1)
for tweet in public_tweets:
    print(tweet)

users=api.get_user()
for user in users:
    print(user.text)
'''
def search(word):
    tweets=api.search(word,count=1)
    for tweet in tweets:
        s = tweet.entities
        print(tweet.id)
        for key, val in s.items():
            if (key == 'user_mentions'):
                if (len(val) > 0):
                    dic = val[0]
                    for k, v in dic.items():
                        if (k == 'screen_name'):
                            print(v)
                print(val)

def update_status_twitter(s):
    api.update_status(s)

tags = api.trends_place(23424977)
def get_trends(tags):
    tag = tags[0]
    trend_names = []
    for k, v in tag.items():
        print(k, " val-> ", v)
        if (k == 'trends'):
            trend_names.append(v)

            print(trend_names)
    tn = []
    trend_names = trend_names[0]
    for i in trend_names:
        for k, v in i.items():
            if (k == 'name'):
                tn.append(v)

    print(tn)


def sentiment_analyzer(tn):
    res = {}
    for n in tn:
        print("\n")
        print("these are the tweets from the popular trend->", n)
        tweets = api.search(n, count=50)
        for tweet in tweets:
            data = [tweet.text]
            model_id = 'cl_pi3C7JiL'
            result = ml.classifiers.classify(model_id, data)
            # print(tweet.text)
            b = result.body[0]
            print(b)
            for k, v in b.items():
                if (k == 'classifications'):
                    # print(v[0])
                    for k, v in v[0].items():
                        if (k == 'tag_name'):
                            print(k, v)

                            if (v == 'Positive'):
                                url = f"https://twitter.com/user/status/{tweet.id}"
                                res['tweet'] = [{'topic': n},
                                                {'url': url},
                                                {'user_tweet': tweet.text}
                                                ]
                                print(res)


def get_trends(tag):
    trend_names = []
    for k, v in tag.items():
        print(k, " val-> ", v)
        if (k == 'trends'):
            trend_names.append(v)
            print(trend_names)
    tn = []
    trend_names = trend_names[0]
    for i in trend_names:
        for k, v in i.items():
            if (k == 'name'):
                tn.append(v)










'''def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s='Jiibo_jqqqqqqqqqqqq'
    if(len(s)<=10):
        print_hi(s)
    else:
        print("Too long  hoe")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''

# tag=api.trends_available()
# print(tag)
