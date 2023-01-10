from option_quote_history.option_quote_ingestor import OptionQuoteIngestor
import option_quote_history.config as config
from tda_tonberry_trader.tdsession import TDSession
from datetime import date, timedelta, datetime


def main(argv: list[str]) -> None:
    tdsession = TDSession(
        "option_history_quotes",
        code=config.get_code(),
        client_id=config.get_client_id(),
    )

    option_quote = tdsession.get_option_chain_by_date(
        "SPY",
        fromDate=date.today(),
        toDate=date.today() + timedelta(days=90),
        strikeCount=75,
    ).output
    option_quote_ingestor = OptionQuoteIngestor()
    option_quote_ingestor.ingest_options_quote(option_quote)


if __name__ == "__main__":
    main(["hellow"])
