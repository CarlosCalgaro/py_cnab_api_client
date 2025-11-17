from typing import Dict, Type
from .sicredi import SicrediAdapter
from .base import BankAdapter

_ADAPTERS : Dict[str, Type[BankAdapter]] = {
  SicrediAdapter.bank_code: SicrediAdapter,
}

def get_bank_adapter_by_code(bank_code: int) -> Type[BankAdapter]:
  try:
    return _ADAPTERS[bank_code]()
  except KeyError:
    raise ValueError(f"Bank adapter not found for bank code: {bank_code}")