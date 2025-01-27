import requests

def fetchAndSaveToFile(url, path):
  r = requests.get(url)
  with open(path, 'w') as f:
    f.write(r.text)
    print("Saved")
  

url = "https://timesofindia.indiatimes.com/india"

fetchAndSaveToFile(url, "data/times.html")