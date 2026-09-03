import sys
from typing import Optional

from networksec.logging import logger


class NetworkSecurityException(Exception):
    """Base exception for all network security-related errors."""

    def __init__(
        self,
        message: str,
        error_code: str = "NETWORKSEC_ERROR",
        details: Optional[str] = None,
    ) -> None:
        self.message = message
        self.error_code = error_code
        self.details = details
        super().__init__(message)

    def __str__(self) -> str:
        if self.details:
            return f"[{self.error_code}] {self.message}: {self.details}"
        return f"[{self.error_code}] {self.message}"


def handle_exception(exc: Exception, message: str = "An error occurred") -> str:
    """Log an exception and return a readable error message."""
    error_message = f"{message}: {exc}"
    logger.exception(error_message)
    print(error_message, file=sys.stderr)
    return error_message


def raise_networksec_exception(
    message: str,
    error_code: str = "NETWORKSEC_ERROR",
    details: Optional[str] = None,
) -> None:
    """Raise a custom NetworkSecurityException with structured metadata."""
    raise NetworkSecurityException(message, error_code, details)
