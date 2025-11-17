from __future__ import annotations
from pydantic import BaseModel

class CnabApiConfig(BaseModel):
  base_url: str
  timeout_seconds: int = 30