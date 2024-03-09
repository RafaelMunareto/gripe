#!/bin/bash

# Criando o ambiente virtual
echo "Criando ambiente virtual..."
python3 -m venv myenv

# Ativando o ambiente virtual
echo "Ativando o ambiente virtual..."
source myenv/bin/activate

# Instalando dependências
echo "Instalando dependências do arquivo requirements.txt..."
pip install -r requirements.txt

echo "Ambiente configurado e dependências instaladas."
