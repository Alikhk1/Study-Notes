from langchain_openai import ChatOpenAI #Class used to define model used in langchain apps

#-----------------------Defining model to be used, makes request to OpenAI API-----------------------------------------------------
llm = ChatOpenAI(
    model='gpt-4o-mini',
    api_key=' ',
    # Extra parameters
    max_completion_tokens = 50, 
    temperature = 1
)
# Prompting the Model
llm.invoke('What is Langchain')

#------------------Working with open source models, downloaded in local directory, use HUGGINGFACE------------------------------------------------------
from langchain_huggingface import HuggingFacePipeline

# Defining Model
llm = HuggingFacePipeline.from_model_id(
    model_id = 'meta-llama/Llama-3.2-3B-Instruct',
    task='text-generation',
    pipeline_kwargs={'max_new_tokens': 100}
)
# Prompting the model
llm.invoke("What is Hugging Face")


"""******************************************************************"""
#--------------------------------------------------------PROMPT TEMPLATES-------------------------------------------------------------------------------
from langchain_core.prompts import PromptTemplate

template = "Explain this concept simply and precisely: {concept}"

# Convet the template string into a Prompt Template
prompt_template = PromptTemplate.from_template(
    template = template
)

# Variable Insertion
prompt = prompt_template.invoke({"concept": "Prompting LLMs"})
print(prompt) # OUTPUT: "Explain this concept simply and precisely: Prompingting LLMs"

# Using Template for prompts using chain | . User input will be transfered to template and then to LLM 
llm_chain = prompt_template | llm # Already definied LLM
print(llm_chain.invoke({'concept':'Promping LLMS'}))

#=====>> CHAT ROLES PROMPT TEMPLATE <<======
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages(
    [
        ("system","You're a calculator"),
        ("human", "Answer 2+2"),
        ("ai", "2+2=4"),
        ("human", "Answer this math question: {math}")
    ]
)

#====>> FEW SHOT PROMPT TEMPLATE <<=====
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

example_prompt = PromptTemplate.from_template(
    "Question: {question} \n {answer}"
)

prompt_template = FewShotPromptTemplate(
    example= examples, # list of dicts,
    example_prompt= example_prompt # Format template,
    suffix="Question = {input}", # Format User Input,
    input_variables=["input"] # What input variable will the user input be assigned to
)

llm_chain = prompt_template | llm
response = llm_chain.invoke({"input":"What is Pakistan?"})
print(response.content)


"""******************************************************************"""
#--------------------------------------------------------SEQUENTIAL CHAINS-------------------------------------------------------------------------------

destination_prompt = PromptTemplate(
    input_variables= ['destination'],
    template= 'I am planning a trip to {destination}. Can you suggest some activites to do there?.'
)

activities_prompt = PromptTemplate(
    input_variables= ['activities'],
    template = 'Create itinerary from your top 3 activites for this place: {activities}'
)

Sequential_chain = ({'activities': destination_prompt | llm | StrOutputParser()}
                    | activities_prompt
                    | llms
                    | StrOutputParser()
                  )

print(Sequential_chain.invoke({'destination': 'Rome'}))

"""******************************************************************"""
#--------------------------------------------------------LANGCHAIN AGENTS-------------------------------------------------------------------------------

from langgraph.prebuilt import create_react_agent
from langchain_community.agent_toolkits.load_tools import load_tools

# Initialize Model
llm = ChatOpenAI(model='gpt-4o-mini', api_key='')
# Load Math Tool
tools = load_tools(['llm-math'], llm=llm)
# Create Agent
agent = create_react_agent(llm, tools)
# Invoke agent
messages = agent.invoke({'messages': [("human", "What is the square root of 101?")]})
print(messages['messages'][-1].content) # Square root is aprox 10.

#====>> CUSTOM TOOLS <<=====
from langchain_core.tools import tool
# use @tool decorator over customer functions
@tool
def financial_report(company_name,finances) -> str:
    """Generates a Financial Report"""
    report = f"Company name: {company_name}\n"
    report += f"Revenue: {finances}"
    return report

# By using @tool, its formated 
print(financial_report.name)
print(financial_report.description) # the doc string
print(financial_report.return_direct) # False by default; so agent shouldn't stop 
print(financial_report.args) # layout the argument names and types

agent = create_react_agent(llm, [financial_report]) # use the custom tool

messages = agent.invoke({'messages':[('human','techstack made $10 million in sales. Generate Financial report')]})

print(messages['messages'][-1].content)

"""******************************************************************"""
#------------------------------------------- Retrieval Augmented Generation (RAG)--------------------------------------------------------------------

#                                                        ====>> DOCUMENT LOADERS <<=====

#====>> PDF Loader <<=====
from Langchain_community.document_loaders import PyPDFLoader
# Instantiate 
loader = PyPDFLoader('path/to/file/attention_is_all_you_need.pdf')
# Load document into memory, assigns object to data varaible
data = loader.load()
print(data[0])

#====>> CSV Loader <<=====
from Langchain_community.document_loaders.csv_loader import CSVLoader   
loader = CSVLoader('fifa_countries_audience.csv')
data = loader.load()
print(data[0])

#====>> HTML FILE Loader <<=====
from Langchain_community.document_loaders import UnstructuredHTMLLoader
loader = UnstructuredHTMLLoader('White_house_executive_order.html')
data = loader.load()
print(data[0])
print(data[0].metadata) # Extract Documents Metadata

#                                                        ====>> TEXT SPLITTERS <<=====

#====>> CharacterTextSplitter <<=====
from langchain_text_splitters import CharacterTextSplitter

ct_splitter = CharacterTextSplitter(
    separator= '.',
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)

docs = ct_splitter.split_text(quote) # split_text method
print(docs) # List of Strings

#====>> RecursiveCharacterTextSplitter <<=====
from langchain_text_splitters import RecursiveCharacterTextSplitter

rc_splitter = RecursiveCharacterTextSplitter(
    separators= ["\n\n", "\n", " ", ""], # Takes a List of separators, left to right to see if chunks can be combined.
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)

docs = rc_splitter.split_text(quote) 
print(docs) 
docs = rc_splitter.split_documents(data) # For Documents use the split_documents method.
print(docs[0]) 

#                                                        ====>> STORAGE AND RETRIEVAL <<=====
from langchain import OpenAIEmbeddings
from langchain import Chroma

embedding_function = OpenAIEmbeddings(api_key='', model='text-embedding-3-small')

# Create Chroma DB from set of Documents:
vectorstore = Chroma.from_documents(
    docs,
    embedding=embedding_function,
    persist_directory='path/to/directory'
)

# Convert DB into retriever to integrate it with other LangChain components:
retriever = vectorstore.as_retriever(
    search_type='similarity',
    search_kwargs={'k':2} # Return top 2 most similar documents 
)

# So now the model knows what to do, we design the prompt:

from langchain_core.prompts import ChatPromptTemplate
message="""Review and fix following marketting copy with guidlines in consideration:
Guidelines: {guidelines}
Copy: {copy}
Fixed Copy:
"""
prompt_template = ChatPromptTemplate.from_messages([('human',message)])

# Now Chain it all togather
from langchain_core.runnables import RunnablePassthrough

rag_chain = ({'guidelines': retriever, "copy": RunnablePassthrough()} # Runnable is a placeholder for when we hook the chain
             | prompt_template
             | llm)

respone = rag_chain.invoke("Here at techstack our users are best in the world")
print(respone.content)





