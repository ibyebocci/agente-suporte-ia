# Agente de suporte (exemplo didático)

Esqueleto de um agente de IA em Python: o modelo **pede** ferramentas, o código **executa e valida**, e há limites para evitar loops e custos.

## Conceitos demonstrados

- **Loop de agente** com `MAX_PASSOS` (evita loop infinito e gasto descontrolado)
- **Tool use**: o modelo propõe a chamada, o código decide se executa
- **Permissões mínimas**: só ferramentas da lista `FERRAMENTAS` são executadas
- **Fallback seguro**: se acabarem os passos, o caso vai para um humano
- **Memória de curto prazo**: histórico em `mensagens`

## Como rodar

Requer Python 3.

```bash
python agente.py
```

Saída esperada:

```
Sentimos muito pelo atraso! Aplicamos um cupom de R$ 10.
```

Para ver o fallback, mude `MAX_PASSOS = 1` em `agente.py`.

## Observações

- O `llm` é **simulado**, para testar a estrutura sem API. Em um agente real, substitua por uma chamada a um modelo (Claude, GPT, Gemini).
- Esqueleto didático: falta tratamento de exceções, timeout, limite de tokens, logs e testes automatizados.

## Próximos passos

- [ ] Integrar um modelo real via API
- [ ] Adicionar a ferramenta `abrir_reembolso` com teto de valor
- [ ] Criar um conjunto de testes com cenários (incluindo falha de ferramenta)
- [ ] Registrar passos, tokens e custo por conversa
