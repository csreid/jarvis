import requests
import xml.etree.ElementTree as ET
import sys

while True:
    sys.stdout.write("Jarvis > ")
    query = raw_input()
    if query.strip().lower() != "goodbye" and query.lower() != "exit":
        payload = {'input': query, 'appid': 'H36EWR-XPLKG5G6V5', 'format': 'plaintext'}
        r = requests.get("http://api.wolframalpha.com/v2/query", params = payload)
        decoded = r.text.encode('ascii', 'ignore')
        root = ET.fromstring(decoded)
        result = root.find("./pod/[@title='Result']/subpod/plaintext")
        if result is not None:
            print result.text
        else:
            print "I'm sorry. My responses are limited... you must ask the right questions."
    else:
        break
