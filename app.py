import ipywidgets as widgets
from IPython.display import display
from classes.TratamentoDados import TratamentoDados
from classes.MachineLearning import MachineLearning
from classes.Resultados import Resultados

# Defina os caminhos para seus dados aqui
caminhos_dados = ['./dados/gripe_2021.csv', './dados/gripe_2022.csv', './dados/gripe_2023.csv']
caminho_dados_municipios = './dados/cod_municipios.csv'

# Criação dos objetos das classes
tratamento = TratamentoDados()
ml = MachineLearning()

# Carregar os dados
tratamento.carregar_dados(caminhos_dados)
tratamento.carregar_dados_municipios(caminho_dados_municipios)

# Dropdown ou radio buttons para escolher a operação
operacao_widget = widgets.Dropdown(
    options=['Tratamento de Dados', 'Machine Learning', 'Resultados'],
    description='Operação:',
)

def on_executar_clicked(b):
    operacao = operacao_widget.value

    if operacao == 'Tratamento de Dados':
        tratamento.tratar_dados()
        tratamento.mesclar_dados_municipios()
        tratamento.preparar_previsores_alvo()
        tratamento.escalonar_salvar_previsores_alvo()
        print('Tratamento de dados concluído.')

    elif operacao == 'Machine Learning':
        ml.carregar_previsores_alvo()
        ml.treinar_modelos()
        ml.criar_modelo_hibrido()
        print('Modelos de Machine Learning treinados e salvos.')

    elif operacao == 'Resultados':
        # Carregar os dados mesclados e tratados para visualização
        dados_resultados = tratamento.dados
        resultados = Resultados(dados_resultados)
        resultados.interface_interativa()
        print('Interface de resultados exibida.')

executar_botao = widgets.Button(description='Executar')
executar_botao.on_click(on_executar_clicked)

display(operacao_widget, executar_botao)
