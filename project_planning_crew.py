"""
project_planning_crew.py

Enterprise Project Planning Crew

Input:
HRMS Platform

Agents:
1. Product Owner Agent
2. Business Analyst Agent
3. Architect Agent
4. Project Manager Agent

Output:
- Requirements
- User Stories
- Architecture
- Roadmap
- Sprint Plan
"""

import json


# ==========================================
# Base Agent
# ==========================================

class Agent:

    def __init__(self, name):
        self.name = name

    def execute(self, data):
        pass


# ==========================================
# Product Owner Agent
# ==========================================

class ProductOwnerAgent(Agent):

    def execute(self, product_name):

        requirements = {
            "project": product_name,
            "vision":
                "Centralized HRMS platform for employee lifecycle management",

            "modules": [
                "Employee Management",
                "Attendance Management",
                "Leave Management",
                "Payroll",
                "Performance Management",
                "Recruitment",
                "Reports & Analytics"
            ]
        }

        return requirements


# ==========================================
# Business Analyst Agent
# ==========================================

class BusinessAnalystAgent(Agent):

    def execute(self, requirements):

        user_stories = [

            {
                "id": "US001",
                "story":
                    "As an employee, I want to apply for leave online."
            },

            {
                "id": "US002",
                "story":
                    "As HR, I want to manage employee records."
            },

            {
                "id": "US003",
                "story":
                    "As a manager, I want to approve leave requests."
            },

            {
                "id": "US004",
                "story":
                    "As payroll admin, I want salary processing."
            }
        ]

        return user_stories


# ==========================================
# Architect Agent
# ==========================================

class ArchitectAgent(Agent):

    def execute(self, data):

        architecture = {

            "architecture_style":
                "Microservices Architecture",

            "frontend":
                "React",

            "backend":
                "Python Django REST Framework",

            "database":
                "PostgreSQL",

            "authentication":
                "JWT Authentication",

            "deployment":
                "Docker + Kubernetes",

            "services": [
                "Employee Service",
                "Leave Service",
                "Payroll Service",
                "Recruitment Service",
                "Reporting Service"
            ]
        }

        return architecture


# ==========================================
# Project Manager Agent
# ==========================================

class ProjectManagerAgent(Agent):

    def execute(self, data):

        roadmap = {

            "Phase 1":
                "Requirements Gathering",

            "Phase 2":
                "Architecture Design",

            "Phase 3":
                "Development",

            "Phase 4":
                "Testing",

            "Phase 5":
                "Deployment"
        }

        sprint_plan = {

            "Sprint 1": [
                "Project Setup",
                "Authentication",
                "Employee Module"
            ],

            "Sprint 2": [
                "Leave Management",
                "Attendance Module"
            ],

            "Sprint 3": [
                "Payroll Module",
                "Recruitment Module"
            ],

            "Sprint 4": [
                "Reports",
                "Dashboard",
                "Analytics"
            ],

            "Sprint 5": [
                "Testing",
                "Bug Fixes",
                "Deployment"
            ]
        }

        return roadmap, sprint_plan


# ==========================================
# Crew Execution
# ==========================================

PROJECT = "HRMS Platform"

print("\n" + "=" * 80)
print("ENTERPRISE PROJECT PLANNING CREW")
print("=" * 80)

product_owner = ProductOwnerAgent("ProductOwner")
business_analyst = BusinessAnalystAgent("BusinessAnalyst")
architect = ArchitectAgent("Architect")
project_manager = ProjectManagerAgent("ProjectManager")


# Step 1
requirements = product_owner.execute(PROJECT)

# Step 2
user_stories = business_analyst.execute(requirements)

# Step 3
architecture = architect.execute({
    "requirements": requirements,
    "user_stories": user_stories
})

# Step 4
roadmap, sprint_plan = project_manager.execute({
    "requirements": requirements,
    "architecture": architecture
})


# ==========================================
# Final Output
# ==========================================

sdlc_package = {

    "Requirements": requirements,

    "User Stories": user_stories,

    "Architecture": architecture,

    "Roadmap": roadmap,

    "Sprint Plan": sprint_plan
}

print(
    json.dumps(
        sdlc_package,
        indent=4
    )
)