import os
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
class TratamentoDados:
    def __init__(self):
        self.dados = None
        self.previsores = None
        self.alvo = None
        self.dados_municipios = None

    def carregar_dados(self, caminhos):
        print('Carregando dados...')
        dados_anuais = [pd.read_csv(caminho, sep=';', encoding='utf-8') for caminho in caminhos]
        self.dados = pd.concat(dados_anuais)

    def carregar_dados_municipios(self, caminho):
        print('Carregando dados municipios...')
        self.dados_municipios = pd.read_csv(caminho, sep=';', encoding='utf-8')     
        self.dados_municipios = self.dados_municipios[['UF', 'Nome_UF', 'Nome_Mesorregião', 'Nome_Microrregião', 'Código Município Completo', 'Nome_Município']]
    
    def tratar_dados(self):
        print('Fazendo tratamento dos dados...')
        self.dados['DT_NOTIFIC'] = pd.to_datetime(self.dados['DT_NOTIFIC'], format='%d/%m/%Y')
        self.dados['DT_NASC'] = pd.to_datetime(self.dados['DT_NASC'], format='%d/%m/%Y', errors='coerce')
        self.dados['ANO'] = self.dados['DT_NOTIFIC'].dt.year
        self.dados['MES'] = self.dados['DT_NOTIFIC'].dt.month
        self.dados = pd.get_dummies(self.dados, columns=['SG_UF_NOT', 'CS_SEXO', 'CS_GESTANT', 'CS_RACA'])
        self.dados = self.dados.dropna(subset=['CO_REGIONA', 'DT_NASC'])

    def mesclar_dados_municipios(self):
        print('Mesclando dados de municipio com os dados gerais...')
        # Assegurar que os códigos de municípios estejam no formato correto
        self.dados['CO_MUN_NOT'] = self.dados['CO_MUN_NOT'].astype(str)
        self.dados_municipios['Código Município Completo'] = self.dados_municipios['Código Município Completo'].astype(str)

        # Mesclar com base nos códigos dos municípios
        self.dados = pd.merge(self.dados, self.dados_municipios, how='left', left_on='CO_MUN_NOT', right_on='Código Município Completo')

    def preparar_previsores_alvo(self):
        print('Criando previsores e alvo...')
        dados_agregados = self.dados.groupby(['ANO', 'MES', 'Nome_UF', 'Nome_Mesorregião', 'Nome_Microrregião', 'Nome_Município']).size().reset_index(name='CASOS')
        self.previsores = dados_agregados.drop('CASOS', axis=1)
        self.alvo = dados_agregados['CASOS']

    def escalonar_salvar_previsores_alvo(self):
        print('Escalonando...')
        scaler = StandardScaler()
        previsores_escalados = scaler.fit_transform(self.previsores)
        with open('./variaveis/previsores.pickle', 'wb') as f:
            pickle.dump(previsores_escalados, f)
        with open('./variaveis/alvo.pickle', 'wb') as f:
            pickle.dump(self.alvo, f)
