"""
API wrapper for CCTX exchanges
Binance, Coinbase, Kraken, OKX, Bybit, etc.

"""
import asyncio
import ccxt.async_support as ccxt

async def fetch_exchanges(exs: list[str]) -> dict[str, ccxt.Exchange]:
    """
    Fetch the list of exchanges on CCTX for this project.
    """
    res = {}

    for eid in exs:
        exchange_class = getattr(ccxt, eid)
        res[eid] = exchange_class({'enableRateLimit': True})

    return res

