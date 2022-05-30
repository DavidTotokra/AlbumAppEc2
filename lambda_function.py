import requests
import json
import os

TOKEN = os.getenv('5344265965:AAFGMlhtoi5NFuSWcORrSnxkobX0niS-Gn8')
BASE_URL = f"https://api.telegram.org/bot5344265965:AAFGMlhtoi5NFuSWcORrSnxkobX0niS-Gn8"


def lambda_handler(event, context):
    try:
        data = json.loads(event["body"])
        message = str(data["message"]["text"])
        first_name = data["message"]["chat"]["first_name"]
        chat_id = data["message"]["chat"]["id"]

        response = {"chat_id": chat_id, }

        # Reagiere auf die Eingabe
        # Fallunterscheidung
        if message.startswith('/start'):
            response[
                'text'] = f"Hello {first_name} \nwrite or click: \n /dog to get random dog photo \n /cat to get a cat " \
                          f"photo" \
                          f" \n /python to learn python \n /name your first name name ".encode(
                " utf8 ")
            requests.post(f"{BASE_URL}/sendMessage", response)

        elif message.startswith('/dog'):
            contents = requests.get('https://random.dog/woof.json').json()
            response['photo'] = contents['url']
            requests.post(f"{BASE_URL}/sendPhoto", response)

        elif message.startswith('/cat'):
            response['photo'] = f'https://cataas.com/cat/says/Hello%20{first_name}'
            requests.post(f"{BASE_URL}/sendPhoto", response)

        # weitere Kommandos


        elif message.startswith('/hid'):
            hid = "http://ec2-52-201-77-6.compute-1.amazonaws.com/"
            response["text"] = f"Album Foto {hid}".encode("utf-8")
            requests.post(f"{BASE_URL}/sendMessage", response)

        elif message.startswith('/python'):
            hid = "https://https://youtu.be/V_JM8CnMlBw"
            response["text"] = f"Python {hid}".encode("utf-8")
            requests.post(f"{BASE_URL}/sendMessage", response)

        elif message.startswith('/name'):
            response['text'] = f"{first_name}".encode("utf8")
            requests.post(f"{BASE_URL}/sendMessage", response)

        else:
            response['text'] = f"Please /start, {first_name}".encode("utf8")
            requests.post(f"{BASE_URL}/sendMessage", response)

    except Exception as e:
        print(e)

    return {"statusCode": 200}