from .base import BankAdapter
from ..models.boleto import Boleto
from ..models.remessa import Remessa

class SicrediAdapter(BankAdapter):
    bank_code = '748'
    bank_name = "sicredi"
    
    def __init__(self):
      pass
    
    
    def format_boleto(self, boleto: Boleto) -> dict:
        return boleto.model_dump_json()

    def format_remessa(self, remessa: Remessa) -> dict:
        return remessa.model_dump_json()