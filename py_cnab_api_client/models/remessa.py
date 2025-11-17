from pydantic import Field, BaseModel
from .pagamento import Pagamento


class Remessa(BaseModel):
  
  pagamentos: list[Pagamento] = Field(..., description="Lista de pagamentos na remessa (obrigatório)")
  empresa_mae: str = Field(..., min_length=1, description="Nome da empresa mãe (obrigatório)")
  agencia: str = Field(..., min_length=1, description="Agência bancária (obrigatório)")
  conta_corrente: str = Field(..., min_length=1, description="Número da conta corrente (obrigatório)")
  digito_conta: str = Field(..., min_length=1, description="Dígito da conta corrente (obrigatório)")
  aceite: str = Field(default= 'A', min_length=1, description="Aceite do título (obrigatório)")
  byte_idt: str = Field(default='2', min_length=1, description="Byte identificador (obrigatório)")
  posto: str = Field(..., min_length=1, description="Posto de atendimento (obrigatório)")
  sequencial_remessa: int = Field(..., description="Número sequencial da remessa (obrigatório)")
  documento_cedente: str = Field(..., min_length=1, description="Documento do cedente (obrigatório)")
  parcela: str = Field(default= '1', min_length=1, description="Parcela (obrigatório)")
