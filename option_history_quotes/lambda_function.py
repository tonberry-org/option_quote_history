from typing import Any, Mapping
from option_history_quotes.option_quote_ingestor import OptionQuoteIngestor
import option_history_quotes.config as config
from tda_tonberry_trader.tdsession import TDSession
from datetime import date, timedelta

import logging

logging.basicConfig(
    level=config.get_logging_level(), format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)


def lambda_handler(event: Mapping[str, Any], context: Mapping[str, Any]) -> str:
    symbol = event.get("symbol")
    logger.info(f"processing {symbol}")

    tdsession = TDSession(
        "option_history_quotes",
        code=config.get_code(),
        client_id=config.get_client_id(),
    )

    option_quote = tdsession.get_option_chain_by_date(
        symbol=symbol,
        fromDate=date.today(),
        toDate=date.today() + timedelta(days=config.get_expiration_range()),
        strikeCount=config.get_strike_count(),
    ).output
    option_quote_ingestor = OptionQuoteIngestor()
    option_quote_ingestor.ingest_options_quote(option_quote)
    return "OK"
