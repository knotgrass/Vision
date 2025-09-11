import os, sys
from pathlib import Path
from loguru import logger


def setup_logging():
    """
    Configure Loguru logger with custom settings for the eKYC application.
    """
    # Remove default logger
    logger.remove()

    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Console logging with colors
    logger.add(
        sys.stdout,
        colorize=True,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <yellow>{thread.id}</yellow> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level=os.getenv("LOG_LEVEL", "INFO"),
    )

    # File logging - General application logs
    logger.add(
        log_dir / "app.log",
        rotation="10 MB",
        retention="30 days",
        compression="zip",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {thread.id} | {name}:{function}:{line} - {message}",
        level="DEBUG",
    )


def get_logger(name: str = None):
    """
    Get a logger instance with optional name.

    Args:
        name (str, optional): Logger name. Defaults to None.

    Returns:
        Logger: Configured logger instance
    """
    if name:
        return logger.bind(name=name)
    return logger


# Initialize logging when module is imported
setup_logging()

# Export the logger for easy access
__all__ = ["logger", "get_logger", "setup_logging"]
