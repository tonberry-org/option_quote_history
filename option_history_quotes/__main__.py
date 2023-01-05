from option_history_quotes.option_quote_ingestor import OptionQuoteIngestor
import option_history_quotes.config as config
from tda_tonberry_trader.tdsession import TDSession


def main(argv: list[str]) -> None:
    tdsession = TDSession(
        "option_history_quotes",
        code=config.get_code(),
        client_id=config.get_client_id(),
    )

    option_quote = tdsession.get_option_chains("SPY").output
    option_quote_ingestor = OptionQuoteIngestor()
    option_quote_ingestor.ingest_options_quote(option_quote)


if __name__ == "__main__":
    main(["hellow"])