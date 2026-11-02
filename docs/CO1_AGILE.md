# CO1 – Software Engineering and Agile Development

This document explains the software engineering principles applied in the GradeMind project.

## Software Engineering Basics
Software Engineering is the systematic application of engineering approaches to the development of software. 
The **Software Development Lifecycle (SDLC)** is a framework defining tasks performed at each step in the software development process.

The phases are:
1. **Requirements**: Understanding what the system must do (e.g., predicting student performance based on metrics).
2. **Design**: Planning the architecture, UI/UX, and data structures (e.g., Flask web app interacting with a Scikit-Learn model).
3. **Implementation**: Writing the code (Python, Flask, HTML, CSS).
4. **Testing**: Verifying the software works as intended (using Pytest).
5. **Deployment**: Releasing the software (using Docker, Kubernetes).
6. **Maintenance**: Updating and improving the software over time.

## SDLC Models
- **Waterfall**: Sequential, rigid, each phase must complete before the next begins.
- **Iterative**: Develop the system in repeated cycles (iterations).
- **Spiral**: Combines iterative development with risk analysis.
- **Agile**: Iterative and incremental approach focusing on flexibility and customer collaboration.

**GradeMind follows an Agile development approach** because it allows for continuous improvement, adaptability to changing requirements, and early delivery of working software.

## Agile Manifesto
The four Agile values are:
1. **Individuals and interactions** over processes and tools
2. **Working software** over comprehensive documentation
3. **Customer collaboration** over contract negotiation
4. **Responding to change** over following a plan

## Scrum
Scrum is an Agile framework used to manage work.

### Roles
- **Product Owner**: Defines the vision and manages the product backlog (prioritizing features).
- **Scrum Master**: Ensures Scrum practices are followed and removes impediments for the team.
- **Development Team**: Professionals who do the work of delivering a potentially releasable increment of product.

### Events
- **Sprint**: A time-boxed period (e.g., 2 weeks) during which a usable, and potentially releasable product increment is created.
- **Sprint Planning**: Planning the work to be performed in the Sprint.
- **Daily Scrum**: A short, daily event for the Development Team to synchronize activities.
- **Sprint Review**: Inspecting the increment and adapting the Product Backlog if needed.
- **Sprint Retrospective**: Inspecting how the last Sprint went with regards to people, relationships, process, and tools.

### Artifacts
- **Product Backlog**: An ordered list of everything that is known to be needed in the product.
- **Sprint Backlog**: The set of Product Backlog items selected for the Sprint.
- **Increment**: The sum of all the Product Backlog items completed during a Sprint.

## User Stories
Example GradeMind user stories:
1. As a faculty member, I want to enter student academic information, so that I can predict the student's performance category.
2. As a faculty member, I want to view a dashboard of overall student performance, so that I can identify trends.
3. As a developer, I want to containerize the application, so that it can be easily deployed across different environments.
4. As a system admin, I want to monitor application performance, so that I can ensure high availability.
5. As a data scientist, I want to version my dataset, so that I can track changes and reproduce experiments.
6. As a data scientist, I want to track my model training experiments, so that I can compare different runs.
7. As a user, I want the system to validate my inputs, so that I don't get errors from incorrect data.
8. As a security engineer, I want the code to be scanned for vulnerabilities, so that the application is secure.

## Estimation and Velocity
**Estimation**: We use story points (e.g., Fibonacci sequence: 1, 2, 3, 5, 8) to estimate the relative effort required for a user story.
- *Example*: Creating the simple 'About' page might be a 1, while implementing the entire ML prediction pipeline might be an 8.

**Velocity**: The amount of work (story points) a team can complete in a single Sprint.
- *Example Calculation*: In Sprint 1, the team completed stories worth 5, 3, and 2 points. Velocity = 10 points.

## Agile Tools
The project can be managed using tools like:
- **Jira**: Useful for complex projects, tracking issues, sprints, and detailed workflows.
- **Trello**: A simpler, visual board based on Kanban (To Do, In Progress, Done) for tracking tasks.
