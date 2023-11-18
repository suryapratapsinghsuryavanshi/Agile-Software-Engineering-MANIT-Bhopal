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
