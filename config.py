
from datetime import datetime, time as dtime, timedelta
# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
class Config:
    API_KEY       = "U3%3#D1t20A50h8451M11761U757+J7v"
    API_SECRET    = "r3563u194~291q60v11615L8H_r731z5"
    SESSION_TOKEN = "55686654"

    MANUAL_EXPIRY = "2026-05-26T06:00:00.000Z"   # set "" to auto-detect

    # ── Instrument / Exchange ──────────────────────────────────────────────────
    # Change INSTRUMENT to trade a different index or stock:

    INSTRUMENT      = "NIFTY"   # stock_code used for all API calls
    SPOT_EXCHANGE   = "NSE"     # exchange for cash/spot quote
    DERIV_EXCHANGE  = "NFO"     # exchange for options (derivatives segment)
    ATM_STRIKE_STEP = 50       # rounding step for ATM calculation
    # ──────────────────────────────────────────────────────────────────────────

    LOT_SIZE = 20
    QUANTITY = LOT_SIZE

    SL_PCT = 0.25

    EMA_PERIOD   = 5
    SLOPE_THRESH = 0

    MAX_REENTRY  = 10
    REENTRY_WAIT = 5 * 60   # seconds

    ENTRY_TIME      = dtime(9, 20)
    SQUARE_OFF_TIME = dtime(15, 15)

    CANDLE_INTERVAL  = "1minute"
    CANDLE_FROM_TIME = dtime(9, 15)

    TICK_INTERVAL_SEC   = 15
    SIGNAL_INTERVAL_SEC = 60

    # Retry / rate-limit config
    LTP_MAX_RETRIES  = 3
    LTP_RETRY_DELAY  = 1.5    # base back-off seconds (multiplied by attempt number)
    LTP_CALL_STAGGER = 0.35   # seconds between consecutive CE/PE calls
    MIN_VALID_PREMIUM = 1.0   # reject LTP below this before opening a trade
