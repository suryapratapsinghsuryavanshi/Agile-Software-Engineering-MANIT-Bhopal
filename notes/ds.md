# Data Science
> AWS Learning Resource: [LINK](https://aws.amazon.com/what-is/data-science/)

## Hypothesis
A hypothesis is a prediction or assumption that is made before an experiment is conducted. It is a possible answer to a question and is based on observations, theories, and other sources. It is a statement that can be tested and can be proven true or false. Or it is a hypothesis of an statement to be tested about the true value of a population perameter using sample statistics.
- A sample is drawn from the population and analysed.
- The result of the analysis are used to decide whether the claim is ture or not.

#### Example:
A judge assumes that a person charged with a crime is innocent and subject this assumption(hypothesis) to a verification by reviewing the evidence and hearing testimony before reaching to a verdict.

### Types of Hypothesis
![Types of Hypothesis](https://cdn.educba.com/academy/wp-content/uploads/2023/12/Type-of-Hypothesis-1.jpg)

1. **Null Hypothesis ($H_0$)**: 
- The hypothesis which is initilly assumed to be true, although it may in fact be either true or false based on the sample data.
- $_0$ implies 'no difference' between sample statistic and the parameter value.
- Hypothesis testing requires that the null hypothesis be considered true, until it is proved false on the basis of result observed from the sample data.
- $H_0$ : $\mu (\leq, =, \geq) \mu_0$
- Where $\mu$ is the population mean and $\mu_0$ is the hypothesized value of the population mean.

2. **Alternative Hypothesis ($H_1$)**:It is the opposite of the null hypothesis. The hypothesis concluded to be true if the null hypothesis is rejected.
- In other words, the alternative hypothesis states that specific population parameter value is not equal to the value stated in the null hypothesis.
- Written as $H_1$ : $\mu (\lt, \neq, \gt) \mu_0$

**Directional Hypothesis**: 
- $H_0$ : There is no diffrence between the average pulse rate of men and women.
- $H_1$ : Men have lower average pulse rate than women.

**Non-Directional Hypothesis**:
- $H_0$ : Men and women have same verbal ability.
- $H_1$ : Men and women have different verbal ability.

### Level of Significance
- It is the probability of rejecting the null hypothesis when it is true. It is denoted by $\alpha$(alpha).
- It is the risk a decision-maker takes of rejecting the null hypothesis when it is really true.
- The guid provided by the statistical theory is that this porbability must be 'small'.
- Traditionally:
    - $\alpha = 0.05$ is selected for consumer research projects.
    - $\alpha = 0.01$ for quality assurance
    - $\alpha = 0.10$ for political polling.

### Errors in Hypothesis
**When $H_0$ is True**
- Accept $H_0$ : Correct Decision (1 - $\alpha$)
- Reject $H_0$ : Type I Error ($\alpha$)

**When $H_0$ is False**
- Accept $H_0$ : Type II Error ($\beta$)
- Reject $H_0$ : Correct Decision (1 - $\beta$)

### Steps of Hypothesis
1. **State the Hypothesis**: 
    - $H_0$ : $\mu = \mu_0$
    - $H_1$ : $\mu \neq \mu_0$
2. **State the Level of Significance**
3. **Establish critical or rejection region**
4. **Select the suitable Test of Significance or Test Statistic**
    - Z-Test
    - T-Test
    - F-Test
    - Chi-Square Test

### Hypothesis Testing
It is a way to test the hypothesis are true of false.
![Hypothesis Testing](https://leanmanufacturing.online/wp-content/uploads/2020/10/Hypothesis-test-decision-tree-1024x612.png)
