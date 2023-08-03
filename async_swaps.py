from subgrounds import AsyncSubgrounds
from datetime import datetime, timedelta
import asyncio
import time
import os

date_ranges = [
    (start_date, start_date + timedelta(days=1))
    for start_date in [datetime(2023, 7, 1) + timedelta(days=i) for i in range(0, 30, 1)]       # partition query by day
]

# Create a data folder if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")


async def run_query(date_range):
    async with AsyncSubgrounds() as sg:
        univ3 = await sg.load_subgraph(
            "https://api.thegraph.com/subgraphs/name/messari/uniswap-v3-ethereum"
        )

        t0 = time.perf_counter()
        start_date, end_date = date_range
        swaps_qp = univ3.Query.swaps(
    first=1000,                                                                                 # limit the number of results. Univ3 daily swap count can exceed 100k.
            where=[
                univ3.Swap.timestamp > int(start_date.timestamp()),
                univ3.Swap.timestamp < int(end_date.timestamp()),
            ]
        )

        print(f"Query for {start_date.date()} started")

        # Convert the result to a DataFrame
        df = await sg.query_df(swaps_qp)

        # Save the DataFrame to a CSV file
        filename = f"data/swaps_{start_date.date()}.csv"
        df.to_csv(filename, index=False)

        t1 = time.perf_counter()
        print(f"Query for {start_date.date()} completed in {t1-t0:0.2f}s and saved to {filename}")


async def main():
    t0 = time.perf_counter()

    tasks = [run_query(date_range) for date_range in date_ranges]
    await asyncio.gather(*tasks)

    t1 = time.perf_counter()
    print(f"Async Queries completed in {t1-t0:0.2f}s ")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
