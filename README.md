# XploreAI

Biblioteca Python e cookbook para experimentos em engenharia de AI

## Estrutura do repositório

```
src/xploreai/   → biblioteca (publicável no PyPI)
cookbook/       → scripts e notebooks de receitas locais (ex.: langchain/)
references/     → material de estudo externo (somente leitura)
```

## Módulos da biblioteca (`src/xploreai/`)

Pacotes por domínio; cada módulo segue o prefixo **`xai_`** (Xplore AI).

| Pacote | Arquivo | Responsabilidade |
|--------|---------|------------------|
| `environment` | `xai_localhost.py` | Estrutura de pastas para runs locais |
| `log` | `xai_log.py` | Logging estruturado e perfil de ambiente em execuções |
| `utils` | `xai_environment.py` | Localizar a raiz do projeto (`pyproject.toml`) |
| `utils` | `xai_memory.py` | Conversão e utilitários de memória (unidades binárias) |

## Configuração do ambiente

Este projeto usa **[uv](https://docs.astral.sh/uv/)** para ambientes e dependências.
Não use `requirements.txt` na raiz nem `pip install` — tudo fica em **`pyproject.toml`** + **`uv.lock`**.

### 1. Instalar uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Inicializar ambiente do projeto

Na raiz do repositório (onde está o `pyproject.toml`):

```bash
uv sync --all-groups
```

O `uv sync` cria `.venv/`, instala dependências fixadas em `uv.lock` e registra **`xploreai`** em modo editável a partir de `src/xploreai/`.

Para **criar um projeto Python novo** com uv (fora deste repo):

```bash
uv init --python 3.12
uv add pandas          # exemplo: adiciona dependencia e atualiza pyproject.toml + uv.lock
uv sync
```

### 3. Notebooks sem output no Git (nbstripout)

Este repo **nao usa** o pacote [`pre-commit`](https://pre-commit.com/) para notebooks. A limpeza e feita pelo **filtro Git** do [`nbstripout`](https://github.com/kynan/nbstripout) (ja dependencia em `pyproject.toml`).

**Uma vez por clone** (depois de `uv sync`), na raiz do repo:

```bash
uv run nbstripout --install --attributes .gitattributes
```

Isso registra o filtro em `.git/config` e versiona regras em `.gitattributes` (`*.ipynb filter=nbstripout`). No `git add`, outputs sao removidos do que entra no indice; no working tree voce pode continuar executando o notebook normalmente.

Conferir se esta ativo:

```bash
uv run nbstripout --is-installed
uv run nbstripout --status
```

Se recriar o `.venv` ou mudar o caminho do Python, reinstale o filtro:

```bash
uv run nbstripout --install --attributes .gitattributes --force
```

Limpar notebooks ja versionados (one-shot), se necessario:

```bash
uv run nbstripout $(git ls-files '*.ipynb')
```

Validar CI/local sem alterar arquivos:

```bash
uv run nbstripout --verify $(git ls-files '*.ipynb')
```

### 4. Execução

Validação do setup:

```bash
uv run xploreai
```

Testes:

```bash
uv run pytest
```

Exemplo de cookbook:

```bash
uv run python cookbook/01_langchain/prompt_template.py
```

## Versionamento semântico (Commitizen)

Commits seguem **[Conventional Commits](https://www.conventionalcommits.org/)** via [Commitizen](https://commitizen-tools.github.io/commitizen/). A versão do pacote vive em `pyproject.toml` (`[project].version`); o `cz bump` atualiza essa versão, o `CHANGELOG.md` e cria a tag Git `vX.Y.Z`.

### Commits e push

```bash
git add .
uv run cz commit
git push   # sem publicação de nova versão
```

| Tipo | Quando usar | Bump |
|------|-------------|------|
| `feat` | Nova funcionalidade | minor |
| `fix` | Correção de bug | patch |
| `docs` | Documentação | — |
| `refactor` | Refatoração | patch |
| `test` | Testes | — |
| `chore` | Manutenção | — |

### Release e publicação

```bash
uv run cz bump          # bump de versão + CHANGELOG + tag
uv build                # gera dist/*.whl
uv run --with xploreai --no-project -- python -c "import xploreai"  # testar artefato
uv run --env-file .env --no-project -- uv publish   # PyPI (token em UV_PUBLISH_TOKEN)
git push && git push --tags
```
