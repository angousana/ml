import requests as req, json, re

def h2(api, headers, data, host=0):
    if host==0:
        host="https://xxx.angou.repl.co/h2.php"
    else:
        host="https://xxx-"+str(host)+".angousana.repl.co/h2.php"
    try:
        return json.loads(req.post(host, data={'url': api, 'header': str(headers), 'data': str(data)}).text)
    except:
        return [None, None]

# h2dat=h2("http://ifconfig.me", "", "")
# print(h2dat[0])
# print(h2dat[1])
