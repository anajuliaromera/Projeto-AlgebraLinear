# Vetores - R² e R³ com Visualização e Exportação

Este projeto é uma aplicação gráfica feita em Python que permite o usuário inserir vetores nos espaços vetoriais R² ou R³, verificar sua dependência linear, calcular combinações lineares e visualizar os vetores e combinações em um gráfico interativo. Além disso, o resultado pode ser exportado em vários formatos ou copiado para a área de transferência.

---

## Funcionalidades

- Escolha entre espaço vetorial R² (2 dimensões) ou R³ (3 dimensões).
- Entrada de até 3 vetores, cada um com componentes no formato `x,y` (R²) ou `x,y,z` (R³).
- Verificação automática de dependência linear dos vetores inseridos.
- Entrada opcional de coeficientes para testar se a combinação linear dos vetores resulta no vetor nulo.
- Visualização gráfica dos vetores e da combinação linear (quando aplicada).
- Exportação dos resultados para arquivos `.txt`, `.csv` e `.json`.
- Cópia do resultado formatado para a área de transferência.
- Salvamento do gráfico gerado em arquivo `.png`.

---

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `numpy`
  - `tkinter` (normalmente já incluída no Python)
  - `matplotlib`
  - `pyperclip`

### Instalação das dependências (via pip)

```bash
pip install numpy matplotlib pyperclip
```

---

## Como usar

1. Execute o script Python:

    ```bash
    python seu_script.py
    ```

2. Selecione o espaço vetorial (R² ou R³).
3. Digite até três vetores, separados por vírgulas:
   - Para R²: exemplo `1,2`
   - Para R³: exemplo `1,2,3`
4. Opcionalmente, digite coeficientes para testar combinação linear (ex: `2,-1,3`).
5. Clique em **Calcular**.
6. Veja o resultado da dependência linear e se a combinação linear forma o vetor nulo.
7. Visualize os vetores e combinação no gráfico.
8. Utilize os botões para exportar resultados, copiar para área de transferência ou salvar o gráfico.

---

## Estrutura do código

- `verificar_dependencia_linear(vetores)`: Verifica se os vetores são linearmente dependentes ou independentes.
- `combinacao_linear(vetores, coeficientes)`: Calcula a combinação linear dos vetores com os coeficientes dados.
- Funções auxiliares para limpar e atualizar os campos da interface e para desenhar os gráficos.
- Funções de exportação para TXT, CSV, JSON e cópia para área de transferência.
- Interface gráfica feita com Tkinter e visualização dos vetores com Matplotlib (2D ou 3D).

---

## Exemplos

- Entrando os vetores para R²:  
  ```
  1,0
  0,1
  1,1
  ```

- Coeficientes para testar combinação linear:  
  ```
  1,-1,0
  ```

---

## Observações

- Todos os vetores devem ter a mesma dimensão selecionada.
- Para testar combinação linear, o número de coeficientes deve ser igual ao número de vetores inseridos.
- Os gráficos têm limite fixo de -10 a 10 em cada eixo para facilitar a visualização.

---

## Licença

Este projeto é livre para uso e modificação.

---

