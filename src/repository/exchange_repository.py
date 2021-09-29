from src.blockchain_utils.credentials import get_indexer
import time


class ExchangeRepository:
    def __init__(self):
        self.indexer = get_indexer()

    def exchange_image(self, exchange_id: int):
        time.sleep(5)
        response = self.indexer.search_assets(asset_id=exchange_id)
        return response["assets"][0]["params"]["url"]

    def exchange_owner(self, exchange_id: int):
        time.sleep(5)
        response = self.indexer.asset_balances(asset_id=exchange_id)
        return response["balances"][0]["address"]
