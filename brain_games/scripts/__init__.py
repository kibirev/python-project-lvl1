from .cli import welcome_user
from .brain_even import parity_check

parity_check()
welcome_user()


__all__ = ["welcome_user", "parity_check"]