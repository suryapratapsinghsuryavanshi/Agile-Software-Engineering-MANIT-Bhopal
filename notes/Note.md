## Agile Methodology
It is used to overcome the drawbacks of the treiditional waterfall model. In waterfall model, once a phase has been compleate we can not go back to made changes in that phase.

The stages of the agile methodology compraises of the following stages:
| Phase | Software's |
| -- | -- |
| Requirement Gathering | Rally, Jira, HPLM, TFS, MS-Exel |
| Software Design | |
| Code Development | VsCode, Android Studio |
| Testing | JUnit, QUnit, AnyUnit, Selenium |
| Maintaince | Git, GitHub, BitBucket |

## Testing
Testing is nothing is about to check the code develop by the developer are run properly or not, in other word we can say the testing is a phase where we can check the developed product are fullfil the specified need or not. In testing we can parform multiple type of testing to minimize the veriation from the requirement and minimize the mistackes happen during the development cycle.

Testing are devided into below part:
- <b>White Box Testing(Programmer):</b> Test as part requirement
- <b>Black Box Testing(Non-Programmer):</b> Functional Testing

### Black Box Vs White Box

| Black Box Testing | White Box Testing |
| -- | -- |
| Functional Testing | Structured Testing |
| Tester are non-programmer in nature | Tester are to be a programmer |
| Software Requirement Specification are required | No SRS required, Detaild Technical Solution Design are required |
| Trail & Error | Finding Bugs |
| Intarnal Structure are hidden | Internal Structure are open |
| No Knowladge of programming are required | Knowladge of programming are required |
| It is Exostive or required more time | It is not Exostive no more time required |

### $ \alpha $ Testing Vs $ \beta $ Testing
| $ \alpha $ Testing | $ \beta $ Testing |
| -- | -- |
| Write testcase by organization | Write testcase by oter source(user) |
| White + Black box testing | Black box testing |
| High voleume of test cases are there | One or more test cases are there |
| No such test | Relibility & Scalability is testable |
| No such cases exists | Scope of feuture is testable in here |

### Waterfall Vs Agile Props(P) and Cons(C)
| Waterfall model | Agile |
| -- | -- |
| Clear goal and direction(P) | High costumre interventio(P) |
| Time Consuming(C) | Dedicated Teams(C) |
| Process can be easly measure(P) | Lessor Risk(P) |
| Costly distification(C) | Hard to execurte(C) |
| Save time and mony(P) | Imporove Quality(P) |
| Risk fector(C) | Documentation can be ignored(C) |

```bash
Agile
  |
  |--- Scrum
  |
  |--- Kenban
  |
  |--- Lean
  |
  |--- Extream Programming
  |
  |--- Crystel
```

#### Kenban
```bash
Input | Analyes | Code | Develop | Test | Plane |
------|---------|------|---------|------|-------|
  []  |   []    |  []  |   []    |  []  |  []   |
  []  |         |  []  |         |      |       |
  []  |   []    |      |   []    |  []  |  []   |
  []  |         |      |   []    |  []  |       |
  []  |         |  []  |         |  []  |       |
  []  |   []    |  []  |   []    |      |  []   |
```

## Agile Testing Strategis
i. Iteration 0 - It envoles standard the env. and testing requirements and uses cases and sumarize project first cost evaluation is done.

ii. Constructive Itration:
- Conformation Testing - 
    - Acceptance Testing(Evaluate parformance and acceptance of user)
    - Developer Testing(Unit interegration of the code.)

iii. Investigative - Probably data are ignored in conformation testing are cover under the investigative testing scheme.
- Tester are detarmaine potential problems in the form of defects storyes.
- It focuses issues like interegation testing and safer tasking.
- And increment the quality of the solution.

iv. Realeases and Endgame - This phase is also known as transfar phase it include following steps:
- Train user for testing like beta/early testing.
- Supporting pepals & operational team.
- Marketing of product realeas
- Backup and restoration.
- Formation of system and user documentation.

## Setp of Product flow
```bash
[ Introduction ] -> [ Constriction itration ] -> [ Realease Endgame ] -> [ Production ]

Step - 1: Initialize the project.
Step - 2: Delivar a working system that meet the requirements of the stack holders.
Step - 3: Deploy realeas
Step - 4: Operations & Support realeas
```

## Agile Test Quadrent
```bash
               |
               |
    Q-1        |     Q-2
               |
               |
               |
---------------|----------------
               |
               |
               |
    Q-3        |     Q-4
               |
               |

    Fig. Agile Test Quadrent
```
- <b>Quadrent-1</b>:
    - It focuses on testing the intarnal quality of code
    - It is technology drivin & It used for automation testing.
    - It comprisis of: a) Unit Testing, b) Component Testing
- <b>Quadrent-2</b>:
    - It focuses on costomar requirement that are provided to testing team before and throughout the testing process.
    - Test cases are business drivan & used for manual and automated functional testing.
    - It involvs: 
        - a) Pair Testing
        - b) Testing senerio & workflows
        - c) Testing user storys and experiences
- <b>Quadrent-3</b>:
    - It involves testing feedback recive from 1 & 2 quadrent feed heare and testing the review and responses get from 1 & 2 quadrent are used to stranthing the code.
    - It involvs:
        - Pair Testing
        - User Acceptance Testing
        - Collebrative Testing
- <b>Quadrent-4</b>:
    - It focuses on non-functional requirement like parformance, security, stabality.
    - It involvs:
        - Stress Testing
        - Load Testing
        - Security Testing
        - Stability Testing
        - Infrastructure Testing
        - Data migratation Testing
        - Performance Testing

Testing is the process of evaluating a system or application to identify any errors, defects, or bugs. The primary purpose of testing is to ensure that the software meets the specified requirements and functions correctly. It is a crucial phase in the software development life cycle (SDLC) to deliver high-quality software products.

There are several types of testing, broadly categorized into two main groups: manual testing and automated testing. Each type of testing serves a specific purpose in the software development process. Here are some common types of testing:

## Type of Testing

### Manual Testing:

1. **Unit Testing:**
   - Focuses on individual units or components of a system.
   - Ensures that each unit functions as intended.

2. **Integration Testing:**
   - Verifies that different units or modules work together as expected when integrated.
   - Detects interface defects between components.

3. **System Testing:**
   - Evaluates the complete and integrated software system.
   - Ensures that the system meets specified requirements.

4. **Acceptance Testing:**
   - Validates if the software meets the user's acceptance criteria.
   - Includes alpha and beta testing.

5. **Regression Testing:**
   - Ensures that new changes do not adversely affect the existing functionalities of the system.
   - Performed after code modifications or updates.

6. **Smoke Testing:**
   - Conducted to verify whether the critical functionalities of the system work correctly.
   - Ensures that a build is stable enough for further testing.

### Automated Testing:

1. **Functional Testing:**
   - Validates that the software functions according to specified requirements.
   - Includes testing of user interfaces, APIs, databases, security, etc.

2. **Performance Testing:**
   - Assesses the system's responsiveness, speed, and scalability under various conditions.
   - Types include load testing, stress testing, and scalability testing.

3. **Security Testing:**
   - Identifies vulnerabilities and weaknesses in the software's security.
   - Includes penetration testing, vulnerability scanning, and security audits.

4. **Usability Testing:**
   - Evaluates the user-friendliness of the software.
   - Focuses on user interface, navigation, and overall user experience.

5. **Compatibility Testing:**
   - Ensures that the software works correctly across different environments, devices, and browsers.
   - Verifies compatibility with various operating systems and hardware configurations.

6. **Automation Testing:**
   - Involves using automated tools to execute test scripts and validate the software.
   - Speeds up the testing process and improves repeatability.

7. **Non-functional Testing:**
   - Addresses aspects such as performance, reliability, and usability.
   - Includes reliability testing, recovery testing, and maintainability testing.

The selection of testing types depends on the project requirements, development methodology, and the specific goals of the testing process. A combination of manual and automated testing is often employed to achieve comprehensive test coverage.

## What are the iterations in agile testing?

In Agile testing, the development and testing activities are carried out in small, iterative cycles known as iterations or sprints. The Agile methodology emphasizes collaboration, adaptability, and delivering incremental value to the customer. The most commonly used framework for Agile development is Scrum, which divides the development process into fixed-length iterations called sprints. Here are the key aspects of iterations in Agile testing:

1. **Sprint Planning:**
   - At the beginning of each sprint, there is a sprint planning meeting where the development and testing teams, along with the product owner, discuss and plan the work for the upcoming iteration.
   - User stories or features are selected from the product backlog for implementation during the sprint.

2. **Development and Testing:**
   - During the sprint, development and testing activities occur concurrently.
   - Developers implement features, and testers verify them against acceptance criteria and conduct various types of testing.

3. **Daily Stand-ups:**
   - Daily stand-up meetings are held to facilitate communication and collaboration among team members.
   - Team members share updates on their progress, discuss any challenges, and plan their tasks for the day.

4. **Continuous Integration:**
   - Agile teams often practice continuous integration, where code changes are frequently integrated into a shared repository.
   - Automated build and test processes help ensure that the code remains functional throughout the development process.

5. **Incremental Delivery:**
   - At the end of each iteration, a potentially shippable product increment is delivered to the stakeholders.
   - This allows for regular feedback and ensures that the product is continuously evolving based on user input.

6. **Review and Retrospective:**
   - At the end of each sprint, there is a sprint review meeting where the team demonstrates the completed work to stakeholders.
   - A retrospective meeting is held to reflect on the sprint, discuss what went well, identify areas for improvement, and make adjustments for the next iteration.

7. **Adaptability:**
   - Agile methodologies embrace change, and the feedback received from stakeholders during reviews and retrospectives can lead to adjustments in priorities or features for the next sprint.

8. **Backlog Refinement:**
   - Throughout the iteration, the product backlog is continuously refined and reprioritized based on changing requirements, feedback, and emerging insights.

By working in short iterations, Agile testing allows for flexibility, early delivery of valuable features, and rapid adaptation to changing requirements. This iterative and collaborative approach helps teams respond quickly to customer needs and market dynamics.

## Scrum
Scrum is an agile framework for managing and organizing the development of complex software and product development projects. It provides a flexible and iterative approach to software development that emphasizes collaboration, adaptability, and customer satisfaction. Scrum is widely used for managing and delivering products with a focus on delivering value to the customer in a timely manner.

Here are some key concepts and roles in the Scrum framework:

### Roles in Scrum:

1. **Scrum Team:**
   - Typically consists of 5-9 individuals who collectively have the skills to deliver a potentially shippable product.
   - Cross-functional team including developers, testers, designers, etc.

2. **Product Owner:**
   - Represents the stakeholders and is responsible for defining and prioritizing the product backlog.
   - Makes decisions on what features to include in the product.

3. **Scrum Master:**
   - Facilitates the Scrum process and ensures that the team is following the Scrum framework.
   - Helps the team overcome obstacles and continuously improves the development process.

### Scrum Artifacts:

1. **Product Backlog:**
   - A prioritized list of all desired features and enhancements for a product.
   - Managed by the Product Owner and continually refined and reprioritized.

2. **Sprint Backlog:**
   - A subset of the product backlog selected for a specific sprint.
   - Contains the tasks the team commits to completing during the sprint.

3. **Increment:**
   - The sum of all the product backlog items completed during a sprint.
   - Should be a potentially shippable product increment.

### Scrum Events:

1. **Sprint:**
   - A time-boxed period (usually 2-4 weeks) during which a potentially shippable product increment is created.
   - The basic unit of development in Scrum.

2. **Sprint Planning:**
   - A meeting at the beginning of each sprint where the team and Product Owner collaborate to define the sprint goal and select backlog items for the sprint.

3. **Daily Scrum (Stand-up):**
   - A daily 15-minute meeting for the team to synchronize activities and create a plan for the next 24 hours.

4. **Sprint Review:**
   - A meeting at the end of the sprint where the team demonstrates the completed work to stakeholders and receives feedback.

5. **Sprint Retrospective:**
   - A meeting at the end of the sprint where the team reflects on the sprint, discusses what went well and what could be improved, and creates a plan for implementing improvements in the next sprint.

Scrum is lightweight, easy to understand, and promotes a collaborative and iterative approach to software development. It is widely used in various industries beyond software development, including product development and project management. The framework provides a set of guidelines and practices that enable teams to deliver high-quality products with increased adaptability to changing requirements.

## Kanban
Kanban is a popular agile methodology that originated in Japan and was initially applied in manufacturing. Over time, it has been adapted for various knowledge work domains, including software development and project management. Kanban is based on visualizing work, limiting work in progress, and maximizing flow, with an emphasis on continuous delivery and improvement.

Here are key principles and concepts of Kanban:

### Core Principles:

1. **Visualizing Work:**
   - Work items are visualized on a Kanban board, which typically consists of columns representing different stages of the workflow.
   - Each work item is represented by a card that moves through the columns as it progresses.

2. **Work in Progress (WIP) Limits:**
   - WIP limits are applied to each column on the Kanban board to control the amount of work in progress at any given time.
   - Helps in preventing overloading the team and promotes a smooth flow of work.

3. **Flow:**
   - Focuses on the smooth and continuous flow of work through the entire process.
   - Minimizing bottlenecks and optimizing the flow of work items is a key objective.

4. **Feedback Loops:**
   - Encourages quick feedback loops to identify and address issues promptly.
   - Teams can continuously improve based on feedback from the process and stakeholders.

5. **Continuous Improvement (Kaizen):**
   - Teams are encouraged to reflect on their processes regularly and make incremental improvements.
   - The emphasis is on evolving and optimizing the workflow over time.

### Kanban Board Columns:

1. **To Do:**
   - Represents the backlog or the pool of work that needs to be done.

2. **In Progress:**
   - Work items that are actively being worked on.

3. **Review/QA:**
   - Work items that are under review or quality assurance.

4. **Done:**
   - Completed work items that are ready for delivery.

### Practices:

1. **Pull System:**
   - Work is pulled into the system based on capacity rather than being pushed onto team members.
   - New work is initiated only when there is available capacity.

2. **Classes of Service:**
   - Work items can be categorized into different classes based on priority, size, or other criteria.
   - Helps in managing different types of work with different policies.

3. **Explicit Policies:**
   - Clearly defined policies for each stage of the workflow.
   - Teams follow explicit rules and guidelines for moving work items from one stage to another.

4. **Meetings:**
   - Regular meetings focus on reviewing the Kanban board, discussing blockers, and planning for improvement.
   - Unlike Scrum, Kanban does not prescribe specific ceremonies like sprint planning or retrospectives.

Kanban provides flexibility and adaptability, making it suitable for teams with fluctuating workloads or those seeking to introduce agile practices incrementally. It is often used in conjunction with Lean principles to create a more efficient and responsive workflow. Kanban is particularly beneficial in environments where continuous delivery and quick response to changing priorities are crucial.

## Extreme Programming (XP)
Extreme Programming (XP) is an agile software development methodology that aims to improve software quality and responsiveness to changing customer requirements. XP emphasizes customer satisfaction, teamwork, and continuous feedback. It was introduced by Kent Beck in the late 1990s and has since gained popularity for its focus on delivering high-quality software through a set of specific practices and values.

### Key Principles and Practices of Extreme Programming (XP):

1. **User Stories:**
   - Requirements are captured as user stories, short descriptions of functionality from an end user's perspective.

2. **Small Releases:**
   - Frequent, small releases of the software allow for rapid feedback and continuous improvement.

3. **Pair Programming:**
   - Two programmers work together at one computer. One writes the code (the "driver"), and the other reviews each line of code as it is written (the "observer").
   - Facilitates knowledge sharing, code review, and collective code ownership.

4. **Test-Driven Development (TDD):**
   - Developers write automated tests before writing the corresponding code.
   - Ensures that the code meets the requirements and allows for easier maintenance.

5. **Continuous Integration:**
   - Developers integrate their code frequently, typically multiple times a day.
   - Automated builds and tests are executed to identify integration issues early.

6. **Refactoring:**
   - Code is continuously improved and simplified without changing its external behavior.
   - Enhances maintainability and code quality.

7. **Simple Design:**
   - Emphasizes the importance of keeping the design of the system as simple as possible while still meeting the requirements.
   - Aims to avoid unnecessary complexity.

8. **Collective Code Ownership:**
   - Team members are collectively responsible for the codebase, and anyone can make changes to any part of the code.
   - Encourages collaboration and shared responsibility.

9. **Continuous Feedback:**
   - Frequent communication with customers and stakeholders ensures that the development team is building the right features.
   - Emphasis on quick adaptation to changing requirements.

10. **On-Site Customer:**
    - A representative of the customer is present and available to the development team to provide instant feedback and answer questions.

11. **Coding Standards:**
    - A set of coding standards is established and followed by the entire team to maintain consistency and readability.

12. **Planning Game:**
    - A collaborative planning process where the customer and the development team negotiate and prioritize features for upcoming releases.

XP is designed to be flexible and responsive to changing requirements. It is particularly well-suited for projects where requirements are expected to evolve and where quick response to customer feedback is essential. While some XP practices may be more challenging to adopt in certain organizational cultures, many teams find value in the discipline, collaboration, and quality focus that XP promotes.
