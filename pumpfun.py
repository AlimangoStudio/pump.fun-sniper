import requests
from dataclasses import dataclass
from typing import Optional

@dataclass
class CoinData:
    signature: Optional[str] = None
    sol_amount: Optional[int] = None
    token_amount: Optional[int] = None
    is_buy: Optional[bool] = None
    user: Optional[str] = None
    timestamp: Optional[int] = None
    mint: Optional[str] = None
    virtual_sol_reserves: Optional[int] = None
    virtual_token_reserves: Optional[int] = None
    name: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    image_uri: Optional[str] = None
    metadata_uri: Optional[str] = None
    twitter: Optional[str] = None
    telegram: Optional[str] = None
    bonding_curve: Optional[str] = None
    associated_bonding_curve: Optional[str] = None
    creator: Optional[str] = None
    created_timestamp: Optional[int] = None
    raydium_pool: Optional[str] = None
    complete: Optional[bool] = None
    total_supply: Optional[int] = None
    website: Optional[str] = None
    show_name: Optional[bool] = None
    king_of_the_hill_timestamp: Optional[int] = None
    market_cap: Optional[float] = None
    reply_count: Optional[int] = None
    last_reply: Optional[str] = None
    nsfw: Optional[bool] = None
    market_id: Optional[str] = None
    inverted: Optional[str] = None
    username: Optional[str] = None
    profile_image: Optional[str] = None
    creator_username: Optional[str] = None
    creator_profile_image: Optional[str] = None
    usd_market_cap: Optional[float] = None

def get_coins_data():
    url = "https://client-api-2-74b1891ee9f9.herokuapp.com/coins"
    params = {
        "offset": 0,
        "limit": 50,
        "sort": "last_trade_timestamp",
        "order": "DESC",
        "includeNsfw": "true"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.pump.fun/",
        "Origin": "https://www.pump.fun",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "If-None-Match": 'W/"1204f-o3jvHbXrN4D/lV6/d4pGlZjSVMQ"'
    }

    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        coins_data = response.json()
        coin_objects = []
        for data in coins_data:
            coin = CoinData(**data)
            coin_objects.append(coin)
        return coin_objects
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Example usage:
coins = get_coins_data()
if coins:
    for coin in coins:
        print(coin.name)