
from datetime import datetime
from event_type_module import EventType
from logger_module import AppLogger
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from datetime import timezone, timedelta
import pytz


# ─────────────────────────────────────────────
# TIMEZONE
# ─────────────────────────────────────────────
IST = pytz.timezone("Asia/Kolkata")


def now_ist():
    return datetime.now(IST)


def now_ist_naive():
    return datetime.now(IST).replace(tzinfo=None)




@dataclass
class Event:
    type: EventType
    payload: Any = None
    timestamp: datetime = field(default_factory=now_ist_naive)