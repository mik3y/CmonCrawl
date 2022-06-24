import aioredis
import time
from index_query import DomainRecord


async def process_and_forward(
    redis_conn: aioredis.Redis, record: DomainRecord
) -> int | None:
    # Already set
    if redis_conn.get(record.url) is not None:
        return None

    # Try set if not already set
    cur_time = int(time.time())
    if redis_conn.setnx(record.url, cur_time) is None:
        return None

    return cur_time


def create_connection(url: str):
    return aioredis.from_url(url)