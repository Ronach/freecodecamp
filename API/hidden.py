# A completer à partir des options "developer" de mon compte Twitter --> on ne m'a pas accordé l'accès à l'API
# It is very insecure to have them hardcoded here
def oauth():
    return {"consumer_key": "",
            "consumer_secret": "",
            "token_key": "",
            "token_secret": ""}
