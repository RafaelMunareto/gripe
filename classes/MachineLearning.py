import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

class MachineLearning:
    def __init__(self):
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def carregar_previsores_alvo(self):
        with open('./variaveis/previsores.pickle', 'rb') as f:
            previsores = pickle.load(f)
        with open('./variaveis/alvo.pickle', 'rb') as f:
            alvo = pickle.load(f)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(previsores, alvo, test_size=0.3, random_state=42)

    def treinar_modelos(self):
        modelos = {
            'KNN': KNeighborsClassifier(),
            'MLP': MLPClassifier(max_iter=50) 
        }

        for nome, modelo in modelos.items():
            modelo.fit(self.X_train, self.y_train)
            modelo_arquivo = f'./modelos/{nome}.pickle'
            with open(modelo_arquivo, 'wb') as f:
                pickle.dump(modelo, f)

    def criar_modelo_hibrido(self):
        modelos = ['KNN', 'MLP']
        modelos_carregados = {nome: pickle.load(open(f'./modelos/{nome}.pickle', 'rb')) for nome in modelos}
        voting_clf = VotingClassifier(estimators=[(nome, modelo) for nome, modelo in modelos_carregados.items()], voting='soft')
        voting_clf.fit(self.X_train, self.y_train)
        with open('./modelos/ModeloHibrido.pickle', 'wb') as f:
            pickle.dump(voting_clf, f)
