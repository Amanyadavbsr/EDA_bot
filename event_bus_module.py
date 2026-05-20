import threading
from typing import Callable
from dataclasses import dataclass
from typing import Any
from event_type_module import EventType
from event_module import Event
from logger_module import AppLogger


# ─────────────────────────────────────────────
# EVENT BUS
# ─────────────────────────────────────────────
class EventBus:
    def __init__(self):
        self._handlers: dict = {}
        self._lock = threading.Lock()

    def subscribe(self, event_type: EventType, handler: Callable):
        with self._lock:
            self._handlers.setdefault(event_type, []).append(handler)

    def publish(self, event: Event):
        with self._lock:
            handlers = list(self._handlers.get(event.type, []))

        logger.debug(f"[Bus] ▶ {event.type.name}")

        for h in handlers:
            try:
                h(event)
            except Exception as e:
                logger.exception(f"[Bus] Handler {h.__qualname__} raised: {e}")
