# Revisão do projeto

## Pontos de atenção

- Entradas que não sejam números causam erro (`ValueError`) porque são convertidas diretamente com `int()` e `float()`.
- O saldo é mantido apenas em memória e volta a `1000.0` ao reiniciar o programa.
- Não há persistência de dados, cadastro de contas ou autenticação.
- O uso de `float` é suficiente para um exercício inicial, mas valores monetários reais normalmente exigem uma estratégia de precisão específica.
- O código não utiliza funções, o que dificulta a reutilização e a manutenção.

## Decisão

Nenhuma alteração foi feita no código porque a solicitação foi preservar a lógica original sem autorização.

