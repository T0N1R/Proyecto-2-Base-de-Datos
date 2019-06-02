import twitter

consumer_key = ' '
consumer_secret = ' '
access_token = ' '
access_token_secret = ' '


api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

#print(api.VerifyCredentials())   

post_update = api.PostUpdates(status = 'Prueba con python-twitter: {}, {}, {}'.format("usuario1", "usuario2", "usuario3"))

print(post_update)