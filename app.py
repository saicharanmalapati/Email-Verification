import requests
import webbrowser

code = " "

while code:
    code = str(input())
    print(code)
    url = 'https://stnzgjanig.execute-api.us-east-1.amazonaws.com/dev/country/{0}'.format(
        code)
    r = requests.get(url)
    r1 = r.json()

    if "score" in r1:
        data = r1["score"]
        print(data)
    else:
        print("NONE")
# print(data)
