## Associative Memory Network
Associative memory networks, particularly Hopfield networks, are a type of recurrent neural network often used for content-addressable memory recall.

#### Auto Associative Memory Network Vs Hetro Associative Memory Network:

| Aspect                            | Auto-Associative Memory (AAM) Network                                                                                     | Hetero-Associative Memory (HAM) Network                                                                                    |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **Function**                     | Associates input patterns with similar patterns from the same set                                                         | Associates input patterns with different output patterns                                                                   |
| **Usage**                        | Pattern completion, noise reduction, pattern recognition tasks within the same set                                       | Tasks where input and output patterns may not be similar but have associative relationships                               |
| **Network Architecture**         | Input and output layers typically have the same number of neurons                                                         | Input and output layers typically have different numbers of neurons                                                        |
| **Training**                     | Trained with similar patterns from the same set, aiming to minimize difference between input and output patterns          | Trained with pairs of patterns from different sets to establish associations between them                                   |
| **Reconstruction**               | Aims to reconstruct or retrieve input pattern from partial or noisy inputs                                               | Recognizes and recalls patterns across different sets based on learned associations                                       |


#### Memory Capacity Calculation:
Hopfield network with N neurons, calculates the maximum number of memories that can be stored without significant loss or corruption. Use the formula:  <em>Maximum Memories = 0.15 x N</em>

#### Weight Calculation(Hebb Rule):
$w_{ij}(old) = w_{ij}(new)+x_iy_j$

Where:
- $w_{ij}(old)$ is the old weight
- $w_{ij}(new)$ is the new weight
- $x_i$ is the i-th input
- $y_j$ is the j-th output

#### Example(Hebb Rule):
Train a Hetro Associative Memory Network with Hebb Rule to store input to output.

| Input | Output |
|-------|--------|
| 1 0 1 0 | 1 0 |
| 1 0 0 1 | 1 0 |
| 1 1 0 0 | 0 1 |
| 0 0 1 1 | 0 1 |

Input Vector
$x_1 = [1, 0 ,1, 0]$

Output Vector
$y_1 = [1, 0]$

Weight Calculation

$w_{ij}(old) = w_{ij}(new)+x_iy_j$

For 1st input:

$w_{11}(old) = w_{11}(new)+1*1 = 0+1 = 1$

$w_{12}(old) = w_{12}(new)+0*1 = 0+0 = 0$

$w_{21}(old) = w_{21}(new)+1*0 = 0+0 = 0$

$w_{22}(old) = w_{22}(new)+0*0 = 0+0 = 0$

$w_{31}(old) = w_{31}(new)+1*1 = 0+1 = 1$

$w_{32}(old) = w_{32}(new)+0*1 = 0+0 = 0$

$w_{41}(old) = w_{41}(new)+1*0 = 0+0 = 0$

$w_{42}(old) = w_{42}(new)+0*0 = 0+0 = 0$

Same way calculate for 2nd, 3rd and 4th input.

$w = \begin{bmatrix} 2 & 1 \\ 0 & 1 \\ 1 & 1 \\ 1 & 1 \end{bmatrix}$

#### Weight Calculation(Outer Product Rule):
$w = \sum_{i=0}^{n}{S^T_i(p).t_i(p)}$

Where:
- $S^T_i(p)$ is the transpose of the i-th memory
- $t_i(p)$ is the i-th test memory

#### Example(Outer Product Rule):
Train a Hetro Associative Memory Network with Outer Product Rule to store input to output.

| Input | Output |
|-------|--------|
| 1 0 1 0 | 1 0 |
| 1 0 0 1 | 1 0 |
| 1 1 0 0 | 0 1 |
| 0 0 1 1 | 0 1 |

Input Vector
$S_1 = [1, 0 ,1, 0]$

Test Vector
$t_1 = [1, 0]$

Weight Calculation
$w_1 = [1, 0, 1, 0]^T . [1, 0]$

Weight matrix
$w_1 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \\ 1 & 0 \\ 0 & 0 \end{bmatrix}$

Same way calculate $w_2$, $w_3$ and $w_4$.

$w = \begin{bmatrix} 1 & 0 \\ 0 & 0 \\ 1 & 0 \\ 0 & 0 \end{bmatrix} + \begin{bmatrix} 1 & 0 \\ 0 & 0 \\ 0 & 0 \\ 1 & 0 \end{bmatrix} + \begin{bmatrix} 0 & 1 \\ 0 & 1 \\ 0 & 0 \\ 0 & 0 \end{bmatrix} + \begin{bmatrix} 0 & 0 \\ 0 & 0 \\ 0 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 0 & 1 \\ 1 & 1 \\ 1 & 1 \end{bmatrix}$

