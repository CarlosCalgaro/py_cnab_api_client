from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field, field_validator
from typing import Optional


class Boleto(BaseModel):
  """Modelo Pydantic para boletos.
  Campos marcados como obrigatórios seguem as regras de validação
  traduzidas do código original (mensagens em português).
  """
  valor: Decimal = Field(..., description="Valor do boleto (obrigatório)")
  cedente: str = Field(..., min_length=1, description="Nome do cedente (obrigatório)")
  documento_cedente: str = Field(..., min_length=1, description="Documento do cedente (obrigatório)")
  sacado: str = Field(..., min_length=1, description="Nome do sacado (obrigatório)")
  sacado_documento: str = Field(..., min_length=1, description="Documento do sacado (obrigatório)")
  agencia: str = Field(..., min_length=1, description="Agência bancária (obrigatório)")
  carteira: str = Field(default='2', min_length=1, description="Carteira do cedente (obrigatório)")
  conta_corrente: str = Field(..., min_length=1, description="Número da conta corrente (obrigatório)")
  convenio: str = Field(..., min_length=1, description="Convênio do cedente (obrigatório)")
  data_vencimento: date = Field(..., description="Data de vencimento do boleto (obrigatório)")
  nosso_numero: str = Field(..., min_length=1, description="Nosso número (obrigatório)")
  posto: str = Field(..., min_length=1, description="Posto de atendimento (obrigatório)")
  byte_idt: str = Field(default='1', min_length=1, description="Byte identificador (obrigatório)")
