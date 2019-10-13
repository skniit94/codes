import requests

request_session = requests.Session()


try:

    resp = request_session.post("http://commonlambdapp.goibibo.dev/api/action_handler/",
                                json={
                                    'intent':"greetings",
                                    'subIntent':"default",
                                    'context': {
                                        'first_name': 'Saurabh'
                                    }
                                },
                                headers={'Connection': 'close'},
                                )
    print (resp)

except requests.Timeout:
    print ("request timed out")
