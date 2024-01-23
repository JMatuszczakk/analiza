#DpF3sM4OKCg_CrYbr5vTbTdimzmatVhB
from polygon import RESTClient
client = RESTClient(api_key="DpF3sM4OKCg_CrYbr5vTbTdimzmatVhB")

ticker = "SPL"

# List Aggregates (Bars)
aggs = []
for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2023-01-01", to="2023-06-13", limit=50000):
    aggs.append(a)
print(aggs)