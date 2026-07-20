# Central Limit Theorem Simulation

This notebook serves for me to feel by my hands how the Central Limit Theorem (CLT) works using simulated dice rolls.

The distribution of individual dice rolls is uniform rather than normal. Anyways, when many random samples are generated and the mean of each sample is calculated, the sampling distribution of the mean becomes increasingly more normal as the sample size grows.

The notebook compares sizes of 2, 10, 20, 50, 100, 200, 500, 1000.

## Tools:

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

## Results:

The mean of the sampling distribution remains close to the population mean:

$$
E[\bar{X}] = \mu
$$

Also, the standard error decreases according to the formula:

$$
SE(\bar{X}) = \frac{\sigma}{\sqrt{n}}
$$