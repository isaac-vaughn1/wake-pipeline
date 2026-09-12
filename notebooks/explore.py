import duckdb
from wake.config import LANDING_DIR

f = str(LANDING_DIR / "ais-2024-01-15.parquet")
conn = duckdb.connect()
conn.execute("install spatial; load spatial;")

# get an idea of the data's structure
print(conn.sql(f"describe select * from '{f}'"))
print(conn.sql(f"select * from '{f}' limit 10"))
print(conn.sql(f"select count(*) from '{f}'"))
