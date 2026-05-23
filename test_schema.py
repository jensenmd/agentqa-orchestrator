import os
from google import genai
from pydantic import BaseModel, Field

# 1. Define the rigid structure using Pydantic. 
# This is the "cage" the AI is forced to fill out.
class QABugReport(BaseModel):
    bug_id: str = Field(description="A unique identifier like BUG-101")
    component: str = Field(description="The area affected, e.g., Auth, Database, UI")
    severity: str = Field(description="High, Medium, or Low")
    summary: str = Field(description="A one-sentence plain English summary of the issue")
    suggested_fix: str = Field(description="A concise technical recommendation for the developer")

# 2. Initialize our client
client = genai.Client()

# 3. Simulate a messy, conversational email a human tester might write
unstructured_input = """
Hey team, while I was testing the user dashboard on the staging branch this morning, 
the login page completely crashed with a 500 error when I tried entering a password 
with a special character like an exclamation mark. It looks like the SQL query string parser 
is breaking because it isn't escaping inputs properly in the backend authentication module. 
We need to handle special characters correctly. Let's call this ticket BUG-742. 
It's super critical because nobody can log in if they have a secure password!
"""

print("Sending messy text to Gemini...")

# 4. Execute the call, passing our schema directly into the configuration
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=unstructured_input,
    config={
        'response_mime_type': 'application/json',
        'response_schema': QABugReport, # Enforces our exact Pydantic model structure
    },
)

print("\n--- Processed Structured Output ---")
print(response.text)
print("-----------------------------------\n")