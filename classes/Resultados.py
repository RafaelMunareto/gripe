import os
import pandas as pd
import numpy as np
import pickle
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

class Resultados:
    def __init__(self, dados):
        self.dados = dados

    def interface_interativa(self):
        estado_widget = widgets.Dropdown(options=sorted(self.dados['Nome_UF'].unique()), description='Estado:')
        regiao_widget = widgets.Dropdown(description='Região:')
        municipio_widget = widgets.Dropdown(description='Município:')
        modelo_widget = widgets.Dropdown(options=os.listdir('./modelos'), description='Modelo:')

        def atualizar_regioes_municipios(*args):
            regioes = sorted(self.dados[self.dados['Nome_UF'] == estado_widget.value]['Nome_Mesorregião'].unique())
            regiao_widget.options = regioes
            municipios = sorted(self.dados[(self.dados['Nome_UF'] == estado_widget.value) & (self.dados['Nome_Mesorregião'] == regiao_widget.value)]['Nome_Município'].unique())
            municipio_widget.options = municipios

        estado_widget.observe(atualizar_regioes_municipios, 'value')
        regiao_widget.observe(atualizar_regioes_municipios, 'value')

        display(estado_widget, regiao_widget, municipio_widget, modelo_widget)

        predicao_botao = widgets.Button(description="Realizar Predição")
        output_area = widgets.Output()

        def realizar_predicoes(b):
            with output_area:
                output_area.clear_output()
                self.exibir_resultados(estado_widget.value, regiao_widget.value, municipio_widget.value, modelo_widget.value)

        predicao_botao.on_click(realizar_predicoes)

        display(predicao_botao, output_area)

    def exibir_resultados(self, estado, regiao, municipio, modelo_selecionado):
        print(f"Resultados para {estado}, {regiao}, {municipio} usando o modelo {modelo_selecionado}.")
        # Aqui você pode adicionar o código para realizar e exibir a predição, e o gráfico.
        
        # Placeholder para um gráfico de comparação (a implementação real dependerá de seus dados e predições)
        plt.figure(figsize=(10, 6))
        plt.title(f'Comparação de casos para {estado}, {regiao}, {municipio}')
        plt.xlabel('Ano')
        plt.ylabel('Número de Casos')
        plt.grid(True)
        plt.show()
