
from py_cnab_api_client.models.pagamento import Pagamento
from py_cnab_api_client.models.boleto import Boleto


def pagamento_to_boleto(
  pagamento: 'Pagamento',
  cedente: str,
  documento_cedente: str,
  agencia: str,
  conta_corrente: str,
  convenio: str,
  posto: str,
  ) -> 'Boleto':
    boleto = Boleto(
      valor=pagamento.valor,
      sacado=pagamento.nome_sacado,
      sacado_documento=pagamento.documento_sacado,
      data_vencimento=pagamento.data_vencimento,
      nosso_numero=pagamento.nosso_numero,
      cedente=cedente,
      documento_cedente=documento_cedente,
      agencia=agencia,
      conta_corrente=conta_corrente,
      convenio=convenio,
      posto=posto,
    )
    return boleto