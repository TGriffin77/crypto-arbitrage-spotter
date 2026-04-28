import asyncio

import src.fetch_exchanges as fe

async def main(exchange_names: list[str]):
    # Initialize the exchanges
    
    exchanges = await fe.fetch_exchanges(exchange_names)

    # Fetch the order book for BTC/USDT on each exchange
    try:
        order_book_task = [ex.fetch_order_book('BTC/USDT', limit=10) for ex in exchanges.values()]
        results = await asyncio.gather(*order_book_task, return_exceptions=True)
        
        for eid, ticker in zip(exchanges.keys(), results):
            if isinstance(ticker, Exception):
                print(f"Error fetching order book for {eid}: {ticker}")
            else:
                print(f"{eid} - Best Bid: {ticker['bids'][0][0]} / Best Ask: {ticker['asks'][0][0]}")
    
    finally:
        close_task = [ex.close() for ex in exchanges.values()]
        close = await asyncio.gather(*close_task)

if __name__ == "__main__":
    exchange_names = ['binanceus', 'coinbase', 'kraken', 'okx', 'gemini', 'bitstamp','cryptocom','bullish']
    asyncio.run(main(exchange_names=exchange_names))
