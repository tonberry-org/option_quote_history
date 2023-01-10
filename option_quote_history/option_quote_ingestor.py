from typing import Any
from tdaclient.schema.option_chain_response import OptionChainOutput
import boto3
from datetime import datetime
import option_quote_history.config as config


class OptionQuoteIngestor:
    def __init__(self) -> None:
        self._ddb_option_history_quotes = boto3.resource("dynamodb").Table(
            config.get_ddb_option_table()
        )
        self._ddb_option_history_underlying_quotes = boto3.resource("dynamodb").Table(
            config.get_ddb_underlying_table()
        )

    def ingest_option_underlying(self, options: OptionChainOutput) -> str:
        underlying = options.underlying
        id = f"{underlying.symbol}:{underlying.quoteTime}"
        item = underlying.dict()
        item["id"] = id
        timestamp = datetime.fromtimestamp(underlying.quoteTime / 1000.0)
        item["timestamp"] = timestamp.isoformat()
        item["date"] = timestamp.date().isoformat()
        self._ddb_option_history_underlying_quotes.put_item(Item=item)
        return id

    def __remove_none(self, item: dict[str, Any]) -> dict[str, Any]:
        return {k: v for k, v in item.items() if v is not None}

    def ingest_options_quote(self, options: OptionChainOutput) -> None:
        underling_id = self.ingest_option_underlying(options)
        with self._ddb_option_history_quotes.batch_writer() as batch:
            for exp_dat in options.callExpDateMap:
                for strike in options.callExpDateMap[exp_dat]:
                    item = options.callExpDateMap[exp_dat][strike][0]
                    item_dict = item.dict()
                    item_dict["timestamp"] = datetime.fromtimestamp(
                        item.quoteTimeInLong / 1000.0
                    ).isoformat()
                    item_dict["strike"] = strike
                    item_dict["expiration"] = exp_dat
                    item_dict["underlying_id"] = underling_id
                    batch.put_item(Item=item_dict)
