from enum import Enum, auto


# ─────────────────────────────────────────────
# EVENTS
# ─────────────────────────────────────────────
class EventType(Enum):
    MARKET_OPEN = auto()
    SQUARE_OFF  = auto()

    LTP_UPDATE    = auto()
    MINUTE_UPDATE = auto()
    CANDLE_UPDATE = auto()

    ENTRY_SIGNAL = auto()
    NO_SIGNAL    = auto()

    TRADE_OPENED = auto()
    SL_HIT       = auto()
    TRADE_EXITED = auto()

    DAY_SUMMARY = auto()
