import os
import argparse
from prompts import *
from call_function import *
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

#Takes the user arguments
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

#Types list for the AI
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

def main():
    #Generates the response
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt),
    )
    #Checks token usage
    token_count = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.prompt_token_count

    #Checks that the metadata is not none
    if not response.usage_metadata:
        raise RuntimeError("Metadata None")

    #Prints the results and checks if --verbose flag is True
    if args.verbose == True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {token_count}")
        print(f"Response tokens: {response_tokens}")
    
    if response.function_calls is not None:
        for i in response.function_calls:
            #print(f"Calling function: {i.name}({i.args})")
            function_call_result = call_function(i, verbose=args.verbose)

            if len(function_call_result.parts) == 0:
                raise Exception("Parts list is empty")

            if function_call_result.parts[0].function_response == None:
                raise Exception("Function Response is None")
    
            if function_call_result.parts[0].function_response.response == None:
                raise Exception("Function Response is None")

            if args.verbose == True:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            else:
                print(f"Calling function: {i.name}({i.args})")


    else:
        print(response.text)

    

if __name__ == "__main__":
    main()
