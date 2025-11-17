from py_cnab_api_client.models.boleto import Boleto
from py_cnab_api_client.models.remessa import Remessa
from py_cnab_api_client.errors import ClientError
from py_cnab_api_client.banks.registry import get_bank_adapter_by_code
from urllib.parse import urljoin

import requests
import json

class Client:
  def __init__(self, config):
    self._config = config

  def boleto(self, boleto: Boleto, bank_code: str, type: str = 'pdf') -> bytes:
    url = urljoin(self._config.base_url, "boleto/")
    adapter = get_bank_adapter_by_code(bank_code)
    request_data = {
        "data": adapter.format_boleto(boleto),
        "type": type,
        "bank": adapter.bank_name
    }

    response = requests.get(url, params=request_data)
    try:
        response.raise_for_status()
        return response.content
    except requests.exceptions.HTTPError as e:
        self._raise_response_error(e)
  
  def nosso_numero(self, boleto: Boleto, bank_code: str) -> dict:
    url = urljoin(self._config.base_url, "boleto/nosso_numero")
    adapter = get_bank_adapter_by_code(bank_code)
    request_data = {
        "bank": adapter.bank_name,
        "data": adapter.format_boleto(boleto)
    }
    response = requests.get(url, params=request_data)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        self._raise_response_error(e)
  
  def remessa(self, remessa: Remessa, bank_code: str, type: str = 'cnab240') -> bytes:
    url = urljoin(self._config.base_url, "remessa")
    adapter = get_bank_adapter_by_code(bank_code)
    request_data = {
        "type": type,
        "bank": adapter.bank_name
    }

    files = {
        "data": adapter.format_remessa(remessa)
    }

    response = requests.post(url, data=request_data, files=files)
    try:
      response.raise_for_status()
      return response.content
    except requests.exceptions.HTTPError as e:
      self._raise_response_error(e)

  def _raise_response_error(self, e: Exception) -> None:
    try:
      if e.response.text:
        raise ClientError(json.loads(e.response.text))
      else:
        raise ClientError(e.response.text)
    except json.JSONDecodeError:
      raise ClientError(e)