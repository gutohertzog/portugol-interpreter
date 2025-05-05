# Changelog

Todas as alterações relevantes do projeto serão documentadas nesse arquivo.

O formato é baseado no [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e este projeto adota o [Versionamento Semântico (inglês)](https://semver.org/spec/v2.0.0.html).

## [Não Lançado]

## [v0.0.1] - 2025-04-29

### Adicionado

- Arquivo `CHANGELOG.md`.
- Arquivo Portugol.g4, com apenas as operações básicas de `+`, `-`, `*`, `/` e `- unário`.
- Arquivos PortugolLexico.g4 e PortugolSintatico.g4 (extraídos de [Portugol Studio](https://github.com/UNIVALI-LITE/Portugol-Studio/tree/master/core/src/main/antlr) e adaptados para o Python).
- Adicionado o script para gerar a gramática automaticamente, `generate_grammar.sh`.
- Arquivo .gitignore.
- Arquivo main.py.
- Arquivo de requisitos.
- Pasta grammar, com os códigos gerados para testes preliminares.

### Modificado

- Primeira versão do `README.md`.

[Não Lançado]: https://github.com/gutohertzog/portugol-interpreter/compare/v0.0.1...HEAD
[v0.0.1]: https://github.com/gutohertzog/portugol-interpreter/releases/tag/v0.0.1
