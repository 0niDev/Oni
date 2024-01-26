import requests
import json

api = "YOU_API"

def getRequest(api):
    return json.decoder.JSONDecoder().decode(requests.get(api).text)['cnt']

def getAPI():
    pass

def main():
    while True:
        msg = input(">")
        print(getRequest(api.replace("[msg]", msg)))



if __name__ == "__main__":
    main()