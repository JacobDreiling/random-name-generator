import requests

topic= requests.get('https://en.wikipedia.org/wiki/Special:Random').text

print(topic[topic.find('<title>')+7:topic.find('Wikipedia')-3])
