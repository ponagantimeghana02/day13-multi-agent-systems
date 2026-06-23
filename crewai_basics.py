import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Research Agent
def research_agent(topic):
    print("\n🔍 Research Agent Working...\n")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
                You are a Research Agent.
                Responsibilities:
                - Collect information
                - Validate facts
                - Organize findings
                """
            },
            {
                "role": "user",
                "content": f"Research and provide detailed findings on {topic}"
            }
        ]
    )

    return response.choices[0].message.content


# Writer Agent
def writer_agent(research_data):
    print("\n✍️ Writer Agent Working...\n")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
                You are a Technical Writer.

                Responsibilities:
                - Generate reports
                - Summarize findings
                - Create professional documentation
                """
            },
            {
                "role": "user",
                "content": f"""
                Create a professional AI Industry Report using:

                {research_data}

                Include:
                1. Executive Summary
                2. Industry Overview
                3. Current Trends
                4. Opportunities
                5. Challenges
                6. Future Outlook
                7. Conclusion
                """
            }
        ]
    )

    return response.choices[0].message.content


# Orchestrator
def main():
    topic = "AI Industry"

    print("=" * 60)
    print("MULTI-AGENT AI REPORT GENERATION")
    print("=" * 60)

    research_output = research_agent(topic)

    print("\n✅ Research Completed")

    final_report = writer_agent(research_output)

    print("\n✅ Report Generated")
    print("\n" + "=" * 60)
    print("FINAL REPORT")
    print("=" * 60)
    print(final_report)


if __name__ == "__main__":
    main()