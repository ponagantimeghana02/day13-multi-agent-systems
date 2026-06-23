from dotenv import load_dotenv
import os

from autogen import AssistantAgent

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm_config = {
    "config_list": [
        {
            "model": "llama-3.3-70b-versatile",
            "api_key": GROQ_API_KEY,
            "base_url": "https://api.groq.com/openai/v1"
        }
    ],
    "temperature": 0.3
}


# ==========================
# Business Analyst Agent
# ==========================

business_analyst = AssistantAgent(
    name="BusinessAnalyst",
    llm_config=llm_config,
    system_message="""
    You are a Senior Business Analyst.

    Generate:
    1. User Stories
    2. Acceptance Criteria

    Output should be detailed and professional.
    """
)


# ==========================
# Architect Agent
# ==========================

architect = AssistantAgent(
    name="Architect",
    llm_config=llm_config,
    system_message="""
    You are a Senior Software Architect.

    Generate:

    1. System Architecture
    2. Database Design
    3. API Design

    Include:
    - ER Diagram Description
    - Tables
    - REST APIs
    """
)


# ==========================
# Developer Agent
# ==========================

developer = AssistantAgent(
    name="Developer",
    llm_config=llm_config,
    system_message="""
    You are a Senior Full Stack Developer.

    Generate:

    1. Project Structure
    2. Module Design
    3. Backend Components
    4. Frontend Components

    Use MERN Stack.
    """
)


# ==========================
# QA Agent
# ==========================

qa = AssistantAgent(
    name="QA",
    llm_config=llm_config,
    system_message="""
    You are a Senior QA Engineer.

    Generate:

    1. Test Plan
    2. Test Cases
    3. Functional Testing
    4. Integration Testing
    5. Regression Testing

    Provide detailed QA artifacts.
    """
)


PROJECT = """
Ride Booking Application

Features:
- User Registration
- Login
- Driver Registration
- Book Ride
- Live Tracking
- Fare Calculation
- Payments
- Ride History
- Ratings & Reviews
- Admin Dashboard
"""


print("\n" + "=" * 80)
print("BUSINESS ANALYST OUTPUT")
print("=" * 80)

ba_output = business_analyst.generate_reply(
    messages=[
        {"role": "user", "content": PROJECT}
    ]
)

print(ba_output)


print("\n" + "=" * 80)
print("ARCHITECT OUTPUT")
print("=" * 80)

architect_output = architect.generate_reply(
    messages=[
        {
            "role": "user",
            "content": f"""
            Project Details:

            {PROJECT}

            Business Analysis Output:

            {ba_output}
            """
        }
    ]
)

print(architect_output)


print("\n" + "=" * 80)
print("DEVELOPER OUTPUT")
print("=" * 80)

developer_output = developer.generate_reply(
    messages=[
        {
            "role": "user",
            "content": f"""
            Project:

            {PROJECT}

            Business Analysis:

            {ba_output}

            Architecture:

            {architect_output}
            """
        }
    ]
)

print(developer_output)


print("\n" + "=" * 80)
print("QA OUTPUT")
print("=" * 80)

qa_output = qa.generate_reply(
    messages=[
        {
            "role": "user",
            "content": f"""
            Project:

            {PROJECT}

            Business Analysis:

            {ba_output}

            Architecture:

            {architect_output}

            Development Design:

            {developer_output}
            """
        }
    ]
)

print(qa_output)


print("\n" + "=" * 80)
print("COMPLETE SDLC PACKAGE GENERATED")
print("=" * 80)