import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?\
    access_key=b453f57ac04288eb1762e23b57d5aa1e")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()
