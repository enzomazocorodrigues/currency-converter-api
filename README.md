# API de Conversão de Moedas

Este repositório contém uma API baseada em Flask para conversão de moedas. Permite aos usuários converter uma quantia especificada de dinheiro de Real Brasileiro (BRL) para Dólar Americano (USD) e Euro (EUR).

## Executando o Projeto

Para executar o projeto, siga estes passos:

1. Clone o repositório para a sua máquina local:

    ```bash
    git clone https://github.com/enzomazocorodrigues/currency-converter-api.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd currency-converter-api
    ```

3. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

4. Execute a aplicação Flask:

    ```bash
    python main.py
    ```

5. O servidor será iniciado e você poderá acessar os endpoints da API.

## Acessando a Rota `/convertemoeda`

Após o servidor ser iniciado, você poderá acessar a rota `/convertemoeda` para converter moeda. Veja como fazer:

- **Endpoint:** `/convertemoeda`
- **Método:** GET
- **Parâmetros:**
  - `valor` (Obrigatório): A quantia de dinheiro para converter de Real Brasileiro (BRL) para Dólar Americano (USD) e Euro (EUR).

Exemplo de requisição:

```bash
curl -G "http://localhost:5000/convertemoeda" \
-d "valor=100"
```

Exemplo de resposta:

```json
{
    "conversao": {
        "real": 100.0,
        "dolar": 19.93898670069587,
        "euro": 18.657412590022016,
        "maquina": "<hostname_da_maquina>"
    }
}
```

## Notas
- A API obtém taxas de câmbio em tempo real da [Awesome API](https://economia.awesomeapi.com.br).
- Certifique-se de ter uma conexão com a internet ativa para buscar as taxas de câmbio mais recentes.
- A API retorna as quantias convertidas em USD e EUR, juntamente com a quantia original em BRL e o nome da máquina onde a conversão foi realizada.


## Contribuidores
<!-- - [![Enzo Rodrigues](https://github.com/enzomazocorodrigues.png)](https://github.com/enzomazocorodrigues) -->
<!-- - [![Contributor 2](https://github.com/contributor2.png)](https://github.com/contributor2)
- [![Contributor 3](https://github.com/contributor3.png)](https://github.com/contributor3) -->

<div>
    <a href="https://github.com/enzomazocorodrigues" style="display: flex; align-items: center; gap: 8px;">
        <img src="https://github.com/enzomazocorodrigues.png" alt="Enzo Rodrigues" style="border-radius: 50%; width: 32px; height: 32px;">
        Enzo Rodrigues
    </a>
</div>
