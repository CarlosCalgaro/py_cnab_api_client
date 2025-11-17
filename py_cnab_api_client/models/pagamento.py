from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field, field_validator
from typing import Optional


class Pagamento(BaseModel):
  """Modelo Pydantic para Pagamentos.
  Campos marcados como obrigatórios seguem as regras de validação
  traduzidas do código original (mensagens em português).
  """
  valor: Decimal = Field(..., description="Valor do boleto (obrigatório)")
  nosso_numero: str = Field(..., min_length=1, description="Nosso número (obrigatório)")
  data_vencimento: date = Field(..., description="Data de vencimento do boleto (obrigatório)")
  data_emissao: date = Field(..., description="Data de emissão do boleto (obrigatório)")
  valor: Decimal = Field(..., description="Valor do boleto (obrigatório)")
  documento_sacado: str = Field(..., min_length=1, description="Documento do sacado (obrigatório)")
  nome_sacado: str = Field(..., min_length=1, description="Nome do sacado (obrigatório)")
  endereco_sacado: str = Field(..., min_length=1, description="Endereço do sacado (obrigatório)")
  bairro_sacado: str = Field(..., min_length=1, description="Bairro do sacado (obrigatório)")
  cep_sacado: str = Field(..., min_length=8, max_length=8, description="CEP do sacado, 8 dígitos (obrigatório)")
  cidade_sacado: str = Field(..., min_length=1, description="Cidade do sacado (obrigatório)")
  uf_sacado: str = Field(..., min_length=2, max_length=2, description="UF do sacado, 2 dígitos (obrigatório)")
  identificacao_ocorrencia: str = Field(..., min_length=2, max_length=2, description="Código da ocorrência (obrigatório)")

  @field_validator('uf_sacado')
  @classmethod
  def uf_must_have_two_chars(cls, v):
    if v is None or len(v) != 2:
      raise ValueError('UF do sacado deve ter 2 dígitos.')
    return v


  @field_validator('cep_sacado')
  @classmethod
  def cep_must_have_eight_digits(cls, v):
    if v is None or len(v) != 8:
      raise ValueError('CEP do sacado deve ter 8 dígitos.')
    return v

  @field_validator('identificacao_ocorrencia')
  @classmethod
  def identificacao_ocorrencia_length(cls, v):
    if v is None or len(v) != 2:
      raise ValueError('identificacao_ocorrencia deve ter 2 dígitos.')
    return v
