import os
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

llm = ChatOllama(
    model="gemma2:2b",
    temperature=0.7,
    num_predict=256
)

def get_name_menu(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="""
        I want to open a restaurant for {cuisine} food. 
        Suggest 5 fancy names for this.
        
        IMPORTANT: 
        1. Return the names as a comma-separated list.
        2. Do not number them.
        3. Output ONLY the names.
        
        Example: Name A, Name B, Name C, Name D, Name E
        """
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_names")

    prompt_template_menu = PromptTemplate(
        input_variables=['restaurant_names'],
        template="""
        I am opening a restaurant that might be named one of the following: {restaurant_names}.
        
        Suggest 5 specific menu items that would fit this theme.
        Return them as a comma-separated list. output ONLY the items.
        """
    )
    menu_chain = LLMChain(llm=llm, prompt=prompt_template_menu, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, menu_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_names', 'menu_items'],
        verbose=True
    )
    
    response = chain.invoke({'cuisine': cuisine})
    
    return response