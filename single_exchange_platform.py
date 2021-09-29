from src.blockchain_utils.credentials import get_client, get_account_credentials
from src.services.exchange_service import ExchangeService
from src.services.exchange_platform import ExchangePlatform

client = get_client()
acc_pk, acc_address, _ = get_account_credentials(account_id=2)
exchange_buyer_pk, exchange_buyer_address, _ = get_account_credentials(account_id=3)

exchange_service = ExchangeService(exchange_creator_pk=acc_pk,
                         exchange_creator_address=acc_address,
                         client=client,
                         unit_name="TOK",
                         asset_name="Tokility",
                         exchange_url="https://ipfs.io/ipfs/QmSg13NNtvpL6ebgeGKxZUHTCxcg4ut6k4dcMrUu5sG664?filename=6.png")

exchange_service.create_nft()

exchange_platform = ExchangePlatform(admin_pk=acc_pk,
                                 admin_address=acc_address,
                                 exchange_id=exchange_service.exchange_id,
                                 client=client)

exchange_platform.app_initialization(exchange_owner_address=acc_address)

exchange_service.change_exchange_credentials_txn(escrow_address=exchange_platform.escrow_address)

exchange_platform.initialize_escrow()

exchange_platform.fund_escrow()

exchange_platform.make_sell_offer(sell_price=10000, exchange_owner_pk=acc_pk)

exchange_service.opt_in(exchange_buyer_pk)

exchange_platform.buy_nft(exchange_owner_address=acc_address, buyer_address=exchange_buyer_address,
                        buyer_pk=exchange_buyer_pk, buy_price=10000)
