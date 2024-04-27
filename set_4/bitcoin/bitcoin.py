import sys
import requests
import json


def main():
    if len(sys.argv) != 2:
        exit("Command line argument not added")

    try:
        n = float(sys.argv[1])
    except:
        exit("not a float")

    try:
        data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data.raise_for_status()  # Raise an exception if the request was not successful
        # print(json.dumps(data.json(), indent=4))
        bitcoin_data = data.json()
        bitcoin_value = float(bitcoin_data['bpi']['USD']['rate_float'])
        return_val= n*bitcoin_value
        print(f"${return_val:,.4f}", end="")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    main()
