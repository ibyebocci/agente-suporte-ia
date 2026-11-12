MAX_PASSOS = 5

def consultar_pedido(pedido_id):
    return f"Pedido {pedido_id}: atraso de 45 min"

def escalar_humano(mensagens):
    return "Encaminhado para um atendente humano."

ferramentas = {"consultar_pedido": consultar_pedido}

def llm(mensagens, ferramentas):
    # modelo FALSO só para testar a estrutura
    if not any(m["papel"] == "ferramenta" for m in mensagens):
        return {"ferramenta": "consultar_pedido", "args": ["123"], "texto": None}
    return {"ferramenta": None, "args": None,
            "texto": "Sentimos muito pelo atraso! Aplicamos um cupom de R$ 10."}

def executar(nome, args):
    if nome not in ferramentas:          # validação de permissão
        return "Ferramenta não permitida."
    return ferramentas[nome](*args)

def rodar_agente(mensagem_cliente):
    mensagens = [{"papel": "sistema", "texto": "Seja educado."},
                 {"papel": "cliente", "texto": mensagem_cliente}]
    for passo in range(MAX_PASSOS):
        resposta = llm(mensagens, ferramentas)
        if resposta["ferramenta"]:
            resultado = executar(resposta["ferramenta"], resposta["args"])
            mensagens += [{"papel": "modelo", "texto": f"chamou {resposta['ferramenta']}"},
                          {"papel": "ferramenta", "texto": resultado}]
        else:
            return resposta["texto"]
    return escalar_humano(mensagens)

print(rodar_agente("Meu pedido 123 está atrasado"))