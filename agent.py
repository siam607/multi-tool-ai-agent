import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.agents import AgentExecutor, ZeroShotAgent
from langchain.chains import LLMChain
from tools.db_tools import InstitutionsDBTool, HospitalsDBTool, RestaurantsDBTool
from tools.web_search_tool import get_web_search_tool

load_dotenv()

def main():
    # 1. Initialize LLM (Google Gemini)
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    
    # 2. Initialize Custom Tools
    tools = [
        InstitutionsDBTool(),
        HospitalsDBTool(),
        RestaurantsDBTool(),
        get_web_search_tool()
    ]
    
    # 3. Create the Prompt for Zero-Shot Agent
    prefix = """Answer the following questions as best you can. You have access to the following tools:"""
    suffix = """Begin!

Question: {input}
Thought:{agent_scratchpad}"""
    
    prompt = ZeroShotAgent.create_prompt(
        tools, 
        prefix=prefix, 
        suffix=suffix, 
        input_variables=["input", "agent_scratchpad"]
    )
    
    # 4. Create the LLM Chain
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    
    # 5. Create the Agent
    agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools)
    
    # 6. Create the Executor
    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=agent, 
        tools=tools, 
        verbose=True, 
        handle_parsing_errors=True
    )
    
    print("🤖 Multi-Tool AI Agent (Gemini) is ready! Type 'exit' to quit.")
    
    while True:
        question = input("\n❓ Ask a question: ")
        if question.lower() == 'exit':
            break
        
        try:
            response = agent_executor.invoke({"input": question})
            print(f"\n💡 Answer: {response['output']}")
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()