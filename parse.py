#Gonna use Ollama to execute the LLM as it allows us to run opensource LLMs locally on our computer
#Could use OpenAI, Gemini etc 
#Langchain allows us to connect LLMs to our python code

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

#prompt we give the LLM. can be adjusted to be more specific and accurate if needed
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model = "llama3.1")

#we need to give it some more details so that it knows what to do with that as well as the com content that we're about to pass to it
def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt| model #first go to prompt then the model

    parsed_results = []

    #pass the chunks to our LLM and grab the results then store in here
    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description}) #call LLM. When you do you have to pass 2 variables and they need to match the variables specified above
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results) #the faster your computer is the faster it will run. Could add asynchronous code to speed this up
