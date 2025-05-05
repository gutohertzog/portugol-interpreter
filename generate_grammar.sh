#!/bin/bash

# Novo caminho considerando a estrutura atual
GRAMMAR_DIR="antlr"
OUTPUT_DIR="${GRAMMAR_DIR}/grammar"

# Verifica ANTLR
if ! command -v antlr4 &> /dev/null; then
    echo "ANTLR4 não está instalado. Instale primeiro:"
    echo "https://www.antlr.org/"
    exit 1
fi

echo "Gerando arquivos na nova estrutura..."
echo "Diretório de saída: ${OUTPUT_DIR}"

# Limpeza segura
if [ -d "${OUTPUT_DIR}" ]; then
    echo "Removendo arquivos antigos..."
    rm -f "${OUTPUT_DIR}/"*.py "${OUTPUT_DIR}/"*.interp "${OUTPUT_DIR}/"*.tokens
fi

# Geração dos arquivos
cd "${GRAMMAR_DIR}" && \
antlr4 -Dlanguage=Python3 -visitor -no-listener -o "grammar" Portugol.g4

echo "Concluído! Verifique os arquivos em:"
ls -l "${OUTPUT_DIR}"
