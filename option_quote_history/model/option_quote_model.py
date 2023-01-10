from decimal import Decimal
from enum import Enum
from pydantic import BaseModel


class OptionType(str, Enum):
    PUT = "PUT"
    CALL = "CALL"


class OptionQuoteModel(BaseModel):
    optionType: OptionType
    symbol: str
    strikePrice: Decimal
    expirationDate: int
    daysToExpiration: int
    expirationType: str
    multiplier: int
    intrinsicValue: Decimal
    exchangeName: str
    bid: Decimal
    bid_size: int
    ask: Decimal
    ask_size: int
    last: Decimal
    last_size: int
    highPrice: Decimal
    lowPrice: Decimal
    openPrice: Decimal
    closePrice: Decimal
    totalVolume: int
    tradeDate: str
    tradeTimeInLong: int
    quoteTimeInLong: int
    netChange: Decimal
    volatility: Decimal
    delta: Decimal
    gamma: Decimal
    theta: Decimal
    vega: Decimal
    rho: Decimal
    openInterest: Decimal
    mark: Decimal
    inTheMoney: bool
