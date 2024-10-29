""" TODO """


import openai, os
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

class HumanAgent:
    def __init__(self, model_name: str):
        self.agent_identifier = model_name 

    def __call__(self, observation: str) -> str:
        print(observation)
        return input("Please enter the action: ")

class GPTAgent:
    def __init__(self, model_name: str):
        """
        Initialize the GPTAgent with the specified OpenAI model.
        
        Args:
            model_name (str): The name of the OpenAI model to use (e.g., "gpt-4").
        """
        self.model_name = model_name
        self.agent_identifier = model_name
        # Load the OpenAI API key from environment variable
        openai.api_key = os.getenv("OPENAI_API_KEY")
        if not openai.api_key:
            raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        self.client = openai.OpenAI(base_url="https://openrouter.ai/api/v1")
    
    def __call__(self, observation: str) -> str:
        """
        Process the observation using the OpenAI model and return the action.
        
        Args:
            observation (str): The input string to process.
        
        Returns:
            str: The response generated by the model.
        """
        # try:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": observation}
            ],
            # max_tokens=150, ## 
            n=1,
            stop=None,
            temperature=0.7,
        )
        # Extract the assistant's reply
        action = response.choices[0].message.content.strip()
        return action
        # except Exception as e:
        #     return f"An error occurred: {e}"


class HFLocalAgent:
    def __init__(self, model_name: str, quantize: bool = False):
        """
        Initialize the HFTransformerAgent with the specified Hugging Face model, optionally using quantization.
        
        Args:
            model_name (str): The name of the Hugging Face model to use (e.g., "gpt2", "facebook/blenderbot-400M-distill").
            quantize (bool): Whether to quantize the model to 8-bit for lower memory usage (default: False).
        """
        self.model_name = model_name
        self.agent_identifier = model_name
        self.quantize = quantize
        
        # Load the tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Load the model with or without quantization
        if quantize:
            self.model = AutoModelForCausalLM.from_pretrained(model_name, load_in_8bit=True)
        else:
            self.model = AutoModelForCausalLM.from_pretrained(model_name)
        
        # Initialize the text generation pipeline
        self.pipeline = pipeline('text-generation', model=self.model, tokenizer=self.tokenizer)
    
    def __call__(self, observation: str) -> str:
        """
        Process the observation using the Hugging Face model and return the action.
        
        Args:
            observation (str): The input string to process.
        
        Returns:
            str: The response generated by the model.
        """
        # Generate a response
        try:
            response = self.pipeline(observation, max_new_tokens=300, num_return_sequences=1, temperature=0.7, return_full_text=False)
            # Extract and return the text output
            action = response[0]['generated_text'].strip()
            return action
        except Exception as e:
            return f"An error occurred: {e}"