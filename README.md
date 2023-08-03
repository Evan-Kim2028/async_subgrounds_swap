# Async Subgrounds Query Example
This notebook demonstrates how to use [`Subgrounds`](https://github.com/0xPlaygrounds/subgrounds) asynchronous queries to speed up your subgraph queries. 
[Uniswapv3](https://thegraph.com/hosted-service/subgraph/messari/uniswap-v3-ethereum) subgraph is used in this example to asynchronously query the `swaps` entity, which is notoriously one of the
largest subgraph entities. 


### Installation

First setup a virtual environment:

```python3 -m venv .venv
source .venv/bin/activate```

After the virutal environment is active, install the following repositories:

```pip install git+https://github.com/0xPlaygrounds/subgrounds.git@feat/async
   pip install polars
   pip install asyncio
```

Run the query with `python async_swaps.py`. Load the query results in a polars dataframe with `python read_files.py`