"""
Shared Agent Memory Example

Objective:
- Central Knowledge Store
- Multiple Agents Access Same Memory
- Update Shared State
- Read Previous Outputs
"""

import json


# ==================================
# Central Shared Memory
# ==================================

class SharedMemory:

    def __init__(self):
        self.memory = {}

    def store(self, key, value):
        self.memory[key] = value

    def read(self, key):
        return self.memory.get(key)

    def get_all(self):
        return self.memory

    def update(self, key, value):
        self.memory[key] = value


# ==================================
# Initialize Shared Memory
# ==================================

shared_memory = SharedMemory()

shared_memory.store("project", "Ride Booking App")
shared_memory.store("technology", "Python Django")
shared_memory.store("database", "PostgreSQL")


# ==================================
# Business Analyst Agent
# ==================================

class BusinessAnalystAgent:

    def run(self):

        print("\n[Business Analyst] Reading Shared Memory")

        project = shared_memory.read("project")

        user_story = f"""
        As a customer,
        I want to book rides using {project}
        so that I can travel easily.
        """

        shared_memory.store("user_story", user_story)

        print("[Business Analyst] Stored User Story")


# ==================================
# Architect Agent
# ==================================

class ArchitectAgent:

    def run(self):

        print("\n[Architect] Reading Shared Memory")

        project = shared_memory.read("project")
        database = shared_memory.read("database")
        user_story = shared_memory.read("user_story")

        architecture = {
            "project": project,
            "database": database,
            "architecture": "3-Tier Architecture",
            "user_story_used": True
        }

        shared_memory.store("architecture", architecture)

        print("[Architect] Stored Architecture")


# ==================================
# Developer Agent
# ==================================

class DeveloperAgent:

    def run(self):

        print("\n[Developer] Reading Shared Memory")

        tech = shared_memory.read("technology")
        architecture = shared_memory.read("architecture")

        code_structure = {
            "backend": tech,
            "modules": [
                "Authentication",
                "Booking",
                "Payments",
                "Tracking"
            ]
        }

        shared_memory.store(
            "code_structure",
            code_structure
        )

        print("[Developer] Stored Code Structure")


# ==================================
# QA Agent
# ==================================

class QAAgent:

    def run(self):

        print("\n[QA] Reading Shared Memory")

        code_structure = shared_memory.read(
            "code_structure"
        )

        test_plan = {
            "modules_tested":
                code_structure["modules"],
            "test_types": [
                "Functional",
                "Integration",
                "Regression"
            ]
        }

        shared_memory.store(
            "test_plan",
            test_plan
        )

        print("[QA] Stored Test Plan")


# ==================================
# Run Workflow
# ==================================

ba = BusinessAnalystAgent()
architect = ArchitectAgent()
developer = DeveloperAgent()
qa = QAAgent()

ba.run()
architect.run()
developer.run()
qa.run()


# ==================================
# Final Shared Memory
# ==================================

print("\n" + "=" * 60)
print("FINAL SHARED MEMORY")
print("=" * 60)

print(
    json.dumps(
        shared_memory.get_all(),
        indent=4
    )
)