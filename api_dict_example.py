# Example dictionary for reading data into

market_data = {
    'bid': 0,
    'ask': 0,
    'last': 0,
    'daily_high': 0,
    'daily_low': 0
}

# Next, perform API magic to get the values and fill in your dictionary

# Finally, you can use pprint instead of print to make output look more
# readable on the command line

from pprint import pprint

pprint(market_data)
