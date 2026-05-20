import logging
import sys
from datetime import datetime
from logging.handlers import RotatingFileHandler
from threading import Lock
import zoneinfo  # Built-in since Python 3.9


class AppLogger:
    """A thread-safe Singleton class managing app logging with IST timestamps."""

    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(
        self, log_file: str = "app.log", log_level: int = logging.DEBUG
    ):
        if self._initialized:
            return

        self.log_file = log_file
        self.log_level = log_level
        self._configure_root_logger()
        self._initialized = True

    @staticmethod
    def _ist_converter(*args):
        """Converts log timestamps to Indian Standard Time (IST)."""
        # Fetches current UTC time and shifts it to Asia/Kolkata timezone
        utc_dt = datetime.now(zoneinfo.ZoneInfo("UTC"))
        ist_dt = utc_dt.astimezone(zoneinfo.ZoneInfo("Asia/Kolkata"))
        return ist_dt.timetuple()

    def _configure_root_logger(self):
        """Sets up formats with IST conversion and hooks handlers."""
        # Formats
        console_fmt = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s", "%H:%M:%S"
        )
        file_fmt = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )

        # Inject the IST timezone converter into formatters
        console_fmt.converter = self._ist_converter
        file_fmt.converter = self._ist_converter

        # Handlers
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(console_fmt)

        file_handler = RotatingFileHandler(
            self.log_file, maxBytes=5_242_880, backupCount=3, encoding="utf-8"
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(file_fmt)

        # Root Logger config
        root = logging.getLogger()
        root.setLevel(self.log_level)
        root.handlers.clear()
        root.addHandler(console_handler)
        root.addHandler(file_handler)

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        """Returns a named logger instance for tracking specific modules."""
        return logging.getLogger(name)