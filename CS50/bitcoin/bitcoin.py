import requests
import sys

if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

try:
    amount = float(sys.argv[1])
except:
    print("Command-line argument is not a number")
    sys.exit(1)

# API endpoint
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
try:
    # Fetching data from the API
    response = requests.get(url)
except requests.RequestException:
     print("RequestException")
     sys.exit(1)

# Parsing JSON response
data = response.json()

# Extracting USD rate
usd_rate = data['bpi']['USD']['rate_float']

# Calculating amount in USD
amount_in_usd = amount * usd_rate

# Displaying USD rate
print(f"${amount_in_usd:,.4f}")
