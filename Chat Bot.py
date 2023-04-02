import openai
import os

# Set up the OpenAI API client
openai.api_key = os.environ["OPENAI_API_KEY"]


def get_response(prompt):
    # Make an API call to OpenAI GPT
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.8,
    )

    # Extract the generated text from the API response
    generated_text = response.choices[0].text.strip()
    return generated_text


# Main loop for user interaction
print("Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Format the user input as a chat prompt
    prompt = f"User: {user_input}\nAssistant:"

    # Get the chatbot's response
    response = get_response(prompt)
    print("ChatBot: {}".format(response))