import polars as pl

df = pl.read_csv("data/*", infer_schema_length=0)

print(df)