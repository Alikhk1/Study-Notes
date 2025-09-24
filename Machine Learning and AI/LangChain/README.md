# LangChain Notes

## LangChain
Open-source framework designed to simplify the development of applications powered by large language models (LLMs).

- **LangSmith**: Deploying Apps
- **LangGraph**: Deploying AI Agents

## Prompt Templates
Fundamental LangChain components that act as reusable recipes for defining prompts for LLMs.

- Include instructions, examples, and additional context
- Import: `from langchain_core.prompts import PromptTemplate`
- **Chat roles**: system, human, AI - define responses
  - Import: `from langchain_core.prompts import ChatPromptTemplate`
- **Few-shot prompting**
  - Import: `from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate`

## LangChain Expression Language (LCEL)
- `|` : Chain operator

## Chains
Connect calls to different components.

### Types of Chains:
1. **Sequential Chains**: Problems that can be solved sequentially (more than 1 user input)

## LangChain Agents
- Use LLMs to determine actions
- Use **Tools** which are functions called by the agent
  - Math, Wikipedia tools
- **ReAct agents**: Reasoning and Acting
  - Thought → Act → Observe
- **LangGraph**: Branch of LangChain ecosystem specifically for designing agent systems
  - Install: `pip install langgraph==0.2.74`

## Custom Tools
Tools must be formatted in a specific way to be compatible with agents:

- `name`
- `description`: Used by LLM as context to determine when to use it
- `return_direct`: Tells whether the agent should stop after invoking this tool ('False' = don't stop)

Import: `from langchain_core.tools import tool`
- Imports `@tool` decorator to decorate custom functions
- Modifies functions to correct format

## Retrieval Augmented Generation (RAG)
User query is embedded to retrieve the most relevant information from database, these documents are added to the prompt.

### RAG Steps:
1. **Document Loading**
   - LangChain document loaders are classes designed to load & configure documents for systems integration

2. **Splitting into chunks**
   - So documents fit the LLM's context window
   - **Chunk Overlap**: Counteracts lost information during chunk splitting
   
   **Types:**
   1. **CharacterTextSplitter**: Splits based on separator first, then evaluates chunk size & overlap. Splits may be longer than chunk size
   2. **RecursiveCharacterTextSplitter**

3. **Storage + Retrieval**
   - Uses Vector DB

## LangChain Ecosystem
- **LangChain Hub**: Contains catalog of prompts for range of tasks
- **LangChain Templates**: Ready to use code blocks
- **LangSmith**: Troubleshooting & evaluating applications
- **LangServe**: Deploying applications
