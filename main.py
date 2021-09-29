from src.blockchain_utils.credentials import get_client, get_account_credentials
from src.services.exchange_service import ExchangeService
from src.services.exchange_platform import ExchangePlatform

client = get_client()
admin_pk, admin_addr, _ = get_account_credentials(1)
buyer_pk, buyer_addr, _ = get_account_credentials(2)

exchange_service = ExchangeService(exchange_creator_address=admin_addr,
                         exchange_creator_pk=admin_pk,
                         client=client,
                         asset_name="Algobot",
                         unit_name="Algobot")

exchange_service.create_nft()

exchange_platform_service = ExchangePlatform(admin_pk=admin_pk,
                                         admin_address=admin_addr,
                                         client=client,
                                         exchange_id=exchange_service.exchange_id)

exchange_platform_service.app_initialization(exchange_owner_address=admin_addr)

exchange_service.change_exchange_credentials_txn(escrow_address=exchange_platform_service.escrow_address)

exchange_platform_service.initialize_escrow()
exchange_platform_service.fund_escrow()
exchange_platform_service.make_sell_offer(sell_price=100000, exchange_owner_pk=admin_pk)

exchange_service.opt_in(buyer_pk)

exchange_platform_service.buy_nft(exchange_owner_address=admin_addr,
                                buyer_address=buyer_addr,
                                buyer_pk=buyer_pk,
                                buy_price=100000)
