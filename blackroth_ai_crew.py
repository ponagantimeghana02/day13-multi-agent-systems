"""
blackroth_ai_crew.py

BlackRoth AI Operations Crew

Workflow:
User Request
     ↓
Agent Selection
     ↓
Specialized Agent
     ↓
Validation Agent
     ↓
Final Response

Capabilities:
- Document Search
- HR Queries
- Payroll Assistance
- Client Support
- Project Status
- Report Generation
"""

from datetime import datetime


# ==========================================
# Base Agent
# ==========================================

class Agent:

    def __init__(self, name):
        self.name = name

    def execute(self, request):
        raise NotImplementedError


# ==========================================
# HR Agent
# ==========================================

class HRAgent(Agent):

    def execute(self, request):

        return {
            "agent": self.name,
            "response":
                "HR Policy: Employees are eligible for annual leave after probation completion."
        }


# ==========================================
# Payroll Agent
# ==========================================

class PayrollAgent(Agent):

    def execute(self, request):

        return {
            "agent": self.name,
            "response":
                "Payroll processed monthly. Payslips are available through the employee portal."
        }


# ==========================================
# Customer Support Agent
# ==========================================

class CustomerSupportAgent(Agent):

    def execute(self, request):

        return {
            "agent": self.name,
            "response":
                "Support ticket created successfully. Expected resolution within 24 hours."
        }


# ==========================================
# Project Management Agent
# ==========================================

class ProjectManagementAgent(Agent):

    def execute(self, request):

        return {
            "agent": self.name,
            "response":
                "Project Status: Sprint 4 completed. Sprint 5 currently in progress."
        }


# ==========================================
# Technical Documentation Agent
# ==========================================

class TechnicalDocumentationAgent(Agent):

    DOCUMENTS = {
        "django":
            "Django is a high-level Python web framework.",
        "api":
            "REST APIs use HTTP methods such as GET, POST, PUT and DELETE.",
        "postgresql":
            "PostgreSQL is an open-source relational database."
    }

    def execute(self, request):

        request = request.lower()

        for keyword, content in self.DOCUMENTS.items():

            if keyword in request:
                return {
                    "agent": self.name,
                    "response": content
                }

        return {
            "agent": self.name,
            "response":
                "No matching document found."
        }


# ==========================================
# Analytics Agent
# ==========================================

class AnalyticsAgent(Agent):

    def execute(self, request):

        return {
            "agent": self.name,
            "response":
                """
                Analytics Report

                Active Projects : 12
                Open Tickets    : 35
                Team Utilization: 82%
                Sprint Velocity : 91%
                """
        }


# ==========================================
# Validation Agent
# ==========================================

class ValidationAgent(Agent):

    def execute(self, response):

        validation = {
            "validated": True,
            "reviewed_at": str(datetime.now()),
            "final_response": response
        }

        return validation


# ==========================================
# Agent Router
# ==========================================

class AgentRouter:

    def __init__(self):

        self.hr = HRAgent("HR Agent")

        self.payroll = PayrollAgent(
            "Payroll Agent"
        )

        self.support = CustomerSupportAgent(
            "Customer Support Agent"
        )

        self.pm = ProjectManagementAgent(
            "Project Management Agent"
        )

        self.docs = TechnicalDocumentationAgent(
            "Technical Documentation Agent"
        )

        self.analytics = AnalyticsAgent(
            "Analytics Agent"
        )

    def select_agent(self, request):

        request = request.lower()

        if "leave" in request \
                or "employee" in request \
                or "hr" in request:

            return self.hr

        elif "salary" in request \
                or "payroll" in request \
                or "payslip" in request:

            return self.payroll

        elif "ticket" in request \
                or "support" in request \
                or "client" in request:

            return self.support

        elif "project" in request \
                or "sprint" in request \
                or "status" in request:

            return self.pm

        elif "report" in request \
                or "analytics" in request \
                or "dashboard" in request:

            return self.analytics

        else:
            return self.docs


# ==========================================
# BlackRoth AI Crew
# ==========================================

class BlackRothAICrew:

    def __init__(self):

        self.router = AgentRouter()

        self.validator = ValidationAgent(
            "Validation Agent"
        )

    def process_request(self, user_request):

        print("\n" + "=" * 70)
        print("USER REQUEST")
        print("=" * 70)

        print(user_request)

        selected_agent = self.router.select_agent(
            user_request
        )

        print(
            f"\nSelected Agent: {selected_agent.name}"
        )

        agent_response = selected_agent.execute(
            user_request
        )

        print(
            "\nSpecialized Agent Response:"
        )

        print(agent_response)

        validated_response = \
            self.validator.execute(
                agent_response
            )

        print(
            "\nValidation Agent Review:"
        )

        print(validated_response)

        return validated_response


# ==========================================
# Demo
# ==========================================

if __name__ == "__main__":

    crew = BlackRothAICrew()

    requests = [

        "Show HR leave policy",

        "Generate analytics report",

        "What is Django?",

        "Show payroll information",

        "Current project sprint status"
    ]

    for req in requests:

        result = crew.process_request(req)

        print("\nFINAL RESPONSE")
        print(result)

        print("\n" + "-" * 70)