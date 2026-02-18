import os
import argparse
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
        model='gemini-2.5-flash', contents=messages
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
    print(response.text)


if __name__ == "__main__":
    main()
