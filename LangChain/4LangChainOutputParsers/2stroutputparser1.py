from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

temp1=PromptTemplate(
    template='write a detail report on {topic}',
    input_variables=['topic']
)

temp2=PromptTemplate(
    template='write a 5 line summary on {text}',
    input_variables=['text']
)

parser= StrOutputParser()
chain= temp1 | model | parser | temp2 | model |parser

result = chain.invoke({'topic':'black hole'})

print(result)