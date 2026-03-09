import os
from dotenv import load_dotenv
import anthropic
from session_logger import log_exchange

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

user_message = "Explique en une phrase ce qu'est une context window."

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=256,
    messages=[{"role": "user", "content": user_message}]
)

output_text = response.content[0].text
tokens_used = response.usage.input_tokens + response.usage.output_tokens

log_exchange(
    prompt=user_message,
    response=output_text,
    model=response.model,
    metadata={"tokens": tokens_used}
)

print(f"Réponse : {output_text}")
print(f"Tokens consommés : {tokens_used}")