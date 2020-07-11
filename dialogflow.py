import json
import requests

def reply_with_ai(myamsg):
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ya29.c.Ko8B0gcDGbu0xIGkQ_4U5uUnpX7p4DrxXZ_sXAzIO4-JPb2zty5Pfhwd34Dfb1RcM9BxdogJeUzv61lbuc39zxEtgAJOslqUJJN5qEjuIHqera0PL6cAMH6J-YFemz1pOmZUJq4Ix23DShlVzIbHlrbdC6YNBJb33hspWtwh_4D-hat_-fwMwYjXTfMglDUT8Dg',
    }

    data = '{"queryInput":{"text":{"text":'+myamsg+'"languageCode":"en"}},"queryParams":{"timeZone":"Asia/Calcutta"}}'

    response = requests.post(
        'https://dialogflow.clients6.google.com/v2/projects/indy-regrkc/agent/sessions/ba1a3ae9-8d0f-7b7b-d112-e5f17ba38a1a:detectIntent',
        headers=headers, data=data)
    data = json.loads(response.text)
    return data['queryResult']['fulfillmentMessages'][0]['text']['text'][0]
