MAX_PASSOS = 5 #Limite máximo de loops

def consultar_pedido(pedido_id): #Função que recebe o ID do pedido
    return f"Pedido {pedido_id}: atraso de 45 min" #Retorna um aviso pré definido de atraso com o ID do pedido

def escalar_humano(mensagens): #Função que recebe o histórico de mansagens, mneste caso, essa função servirá como fallback caso, em 5 loops, o modelo não resolva 
    return "Encaminhado para um atendente humano." #Aviso de encaminhamento para o atendente 

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
