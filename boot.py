import tkinter as tk
from tkinter import scrolledtext
import yfinance as yf


def obter_cotacoes(tickers):
    resultado_text.delete(1.0, tk.END)  # Limpar o resultado anterior

    for ticker in tickers:
        try:
            # Adicionar ".SA" ao ticker
            ticker_completo = f"{ticker}.SA"

            # Obter dados da ação
            acao = yf.Ticker(ticker_completo)

            # Obter informações sobre a ação
            info_acao = acao.info

            # Verificar se 'ask' está presente nas informações
            if 'ask' in info_acao and info_acao['ask'] is not None:
                # Obter a cotação atual
                cotacao_atual = info_acao['ask']
                resultado_text.insert(
                    tk.END, f"Cotação atual de {ticker_completo}: {cotacao_atual}\n")
            else:
                resultado_text.insert(
                    tk.END, f"Erro: Não foi possível obter a cotação de {ticker_completo}\n")

        except Exception as e:
            resultado_text.insert(
                tk.END, f"Erro ao obter cotação de {ticker_completo}: {e}\n")

# Função chamada ao pressionar o botão


def buscar_cotacoes():
    tickers = entrada_tickers.get().split(',')
    obter_cotacoes(tickers)


# Configuração da interface gráfica
root = tk.Tk()
root.title("Consulta de Cotações")

# Entrada para inserir tickers
tk.Label(root, text="Digite os tickers separados por vírgula:").pack(pady=10)
entrada_tickers = tk.Entry(root)
entrada_tickers.pack(pady=10)

# Botão para buscar cotações
botao_buscar = tk.Button(root, text="Buscar Cotações", command=buscar_cotacoes)
botao_buscar.pack(pady=10)

# Área de resultado
resultado_text = scrolledtext.ScrolledText(root, width=40, height=10)
resultado_text.pack(pady=10)

# Iniciar loop da interface gráfica
root.mainloop()
