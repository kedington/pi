import requests

chunk_len = 1000
domain = "https://api.pi.delivery"
endpoint = "/v1/pi"

with open("pi.txt", 'w') as outfile:
    for i in range(1000):
        resp = requests.get('{0}{1}?start={2}&numberOfDigits={3}'.format(domain, endpoint, chunk_len*i, chunk_len))
        if resp.status_code == 200:
            outfile.write(resp.json()["content"])
        else:
            print("cry ;(")

