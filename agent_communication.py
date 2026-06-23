"""
Agent Communication Framework

Features:
1. Agent-to-Agent Communication
2. Task Assignment
3. Response Routing
4. Event Publishing
5. Communication Logging

Workflow:

Manager Agent
      ↓
Research Agent
      ↓
Architect Agent
      ↓
Developer Agent
"""

from datetime import datetime
import json


# ==========================================
# Communication Bus
# ==========================================

class CommunicationBus:

    def __init__(self):
        self.logs = []
        self.events = []

    def send_message(
            self,
            sender,
            receiver,
            message
    ):

        log = {
            "timestamp": str(datetime.now()),
            "type": "MESSAGE",
            "from": sender,
            "to": receiver,
            "message": message
        }

        self.logs.append(log)

        print(
            f"\n[{sender}] --> [{receiver}]"
        )
        print("MESSAGE:", message)

    def publish_event(
            self,
            publisher,
            event_name,
            payload
    ):

        event = {
            "timestamp": str(datetime.now()),
            "type": "EVENT",
            "publisher": publisher,
            "event": event_name,
            "payload": payload
        }

        self.events.append(event)
        self.logs.append(event)

        print(
            f"\nEVENT PUBLISHED: {event_name}"
        )

    def route_response(
            self,
            sender,
            receiver,
            response
    ):

        log = {
            "timestamp": str(datetime.now()),
            "type": "RESPONSE",
            "from": sender,
            "to": receiver,
            "response": response
        }

        self.logs.append(log)

        print(
            f"\n[{sender}] --> [{receiver}]"
        )
        print("RESPONSE:", response)

    def show_logs(self):

        print("\n" + "=" * 80)
        print("COMMUNICATION LOGS")
        print("=" * 80)

        print(
            json.dumps(
                self.logs,
                indent=4
            )
        )


# ==========================================
# Base Agent
# ==========================================

class Agent:

    def __init__(self, name, bus):
        self.name = name
        self.bus = bus


# ==========================================
# Research Agent
# ==========================================

class ResearchAgent(Agent):

    def execute(self, task):

        result = {
            "requirements": [
                "User Registration",
                "Driver Registration",
                "Ride Booking",
                "Live Tracking",
                "Payments"
            ]
        }

        self.bus.publish_event(
            self.name,
            "RESEARCH_COMPLETED",
            result
        )

        return result


# ==========================================
# Architect Agent
# ==========================================

class ArchitectAgent(Agent):

    def execute(self, research_output):

        result = {
            "architecture":
                "Microservices Architecture",

            "database":
                "PostgreSQL",

            "apis": [
                "/login",
                "/book-ride",
                "/payment"
            ]
        }

        self.bus.publish_event(
            self.name,
            "ARCHITECTURE_COMPLETED",
            result
        )

        return result


# ==========================================
# Developer Agent
# ==========================================

class DeveloperAgent(Agent):

    def execute(self, architecture):

        result = {
            "backend":
                "Python Django",

            "frontend":
                "React",

            "modules": [
                "Auth",
                "Booking",
                "Tracking",
                "Payment"
            ]
        }

        self.bus.publish_event(
            self.name,
            "DEVELOPMENT_COMPLETED",
            result
        )

        return result


# ==========================================
# Manager Agent
# ==========================================

class ManagerAgent(Agent):

    def assign_task(
            self,
            agent,
            task
    ):

        self.bus.send_message(
            self.name,
            agent.name,
            task
        )

    def receive_response(
            self,
            sender,
            response
    ):

        self.bus.route_response(
            sender,
            self.name,
            response
        )


# ==========================================
# Initialize Framework
# ==========================================

bus = CommunicationBus()

manager = ManagerAgent(
    "ManagerAgent",
    bus
)

research = ResearchAgent(
    "ResearchAgent",
    bus
)

architect = ArchitectAgent(
    "ArchitectAgent",
    bus
)

developer = DeveloperAgent(
    "DeveloperAgent",
    bus
)


# ==========================================
# Workflow Execution
# ==========================================

PROJECT = "Ride Booking Application"


# Step 1
manager.assign_task(
    research,
    f"Research requirements for {PROJECT}"
)

research_output = research.execute(PROJECT)

manager.receive_response(
    research.name,
    research_output
)


# Step 2
manager.assign_task(
    architect,
    "Design architecture"
)

architecture_output = architect.execute(
    research_output
)

manager.receive_response(
    architect.name,
    architecture_output
)


# Step 3
manager.assign_task(
    developer,
    "Generate development plan"
)

developer_output = developer.execute(
    architecture_output
)

manager.receive_response(
    developer.name,
    developer_output
)


# ==========================================
# Final SDLC Package
# ==========================================

print("\n" + "=" * 80)
print("FINAL OUTPUT")
print("=" * 80)

final_package = {
    "research": research_output,
    "architecture": architecture_output,
    "development": developer_output
}

print(
    json.dumps(
        final_package,
        indent=4
    )
)


# ==========================================
# Communication Logs
# ==========================================

bus.show_logs()