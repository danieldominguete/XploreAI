# %%
from dotenv import load_dotenv
from langchain_openai.llms import OpenAI
from langchain_core.prompts import PromptTemplate

# %%
# Carregando variaveis de ambiente
load_dotenv()

# %%
llm = OpenAI()
prompt_template = PromptTemplate.from_template("O que é {assunto}?")
print(prompt_template.format(assunto="a inteligência artificial"))

# %%
