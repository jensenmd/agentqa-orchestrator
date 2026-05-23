import os
from google import genai

# The SDK automatically looks for the GEMINI_API_KEY environment variable
client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Respond with exactly three words: System online, Sergeant.',
)

print("\n--- Response From Gemini ---")
print(response.text)
print("----------------------------\n")