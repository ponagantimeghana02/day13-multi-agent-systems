import os
import autogen

from dotenv import load_dotenv
import os

load_dotenv()
# Groq Configuration
llm_config = {
    "config_list": [
        {
            "model": "llama-3.3-70b-versatile",
            "api_key": os.getenv("GROQ_API_KEY"),
            "base_url": "https://api.groq.com/openai/v1"
        }
    ],
    "temperature": 0.3
}

# User Proxy Agent
user_proxy = autogen.UserProxyAgent(
    name="UserProxy",
    human_input_mode="NEVER",
    code_execution_config=False
)

# Assistant Agent
assistant = autogen.AssistantAgent(
    name="Assistant",
    llm_config=llm_config,
    system_message="""
    You are a Senior Business Analyst.

    Generate a detailed Software Requirement
    Specification (SRS) document.
    """
)

# Reviewer Agent
reviewer = autogen.AssistantAgent(
    name="Reviewer",
    llm_config=llm_config,
    system_message="""
    Review the SRS document and improve:
    - Functional Requirements
    - Non-Functional Requirements
    - Security
    - Scalability
    - Architecture
    """
)

requirement = """
Generate a Software Requirement Specification
for a Ride Booking Application.
"""

# Assistant Generates SRS
assistant_response = assistant.generate_reply(
    messages=[
        {
            "role": "user",
            "content": requirement
        }
    ]
)

print("\n=== GENERATED SRS ===\n")
print(assistant_response)

# Reviewer Improves SRS
review_response = reviewer.generate_reply(
    messages=[
        {
            "role": "user",
            "content": str(assistant_response)
        }
    ]
)

print("\n=== IMPROVED SRS ===\n")
print(review_response)