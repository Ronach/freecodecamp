import urllib
# https://pypi.org/project/oauth/ import oauth = vieux paquet pour OAuth 1.0a
# Pour OAuth 2.0
# import authlib : pip install Authlib -> bangerg
# import requests : pip install requests
# import requests-oauthlib : pip install requests-oauthlib
import hidden


def augment(url, parameters):
    # On donne à secrets les valeurs écrites dans hidden.py pour s'authentifier
    secrets = hidden.oauth()
    consumer = oauth.OAuthCOnsumer(secrets['consumer_key'], secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])
    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                                                               token=token, http_method='GET', http_url=url,
                                                               parameters=parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
    return oauth_request.to_url()
