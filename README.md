# Monte Carlo Stock Portfolio Simulator

A Python-based financial quantitative tool that simulates future stock portfolio wealth paths using **Geometric Brownian Motion (GBM)**. It models dollar-cost averaging through recurring monthly deposits and generates statistical distributions (percentiles and trajectories) to analyze portfolio outcomes over time.

---

## Key Features

- **Geometric Brownian Motion (GBM):** Models asset price dynamics considering both deterministic drift ($\mu$) and stochastic volatility ($\sigma$).
- **Vectorized Monte Carlo Engine:** Built using `numpy` array operations to simulate thousands of parallel market trajectories simultaneously.
- **Dollar-Cost Averaging:** Supports dynamic recurring monthly deposits on top of initial capital investment.
- **Dynamic User Inputs:** Prompts for custom simulation parameters with sensible defaults.
- **Data Visualization:** Plots sample portfolio trajectories alongside key percentile bounds (10th, 50th, 90th) and terminal wealth histograms using `matplotlib`.

---

## Theoretical Background

The asset price paths follow the discretized Geometric Brownian Motion equation:

$$S_{t + \Delta t} = S_t \cdot \exp\left( \left(\mu - \frac{1}{2}\sigma^2\right)\Delta t + \sigma \sqrt{\Delta t} \, Z \right)$$

Where:
- $S_t$: Portfolio value at time $t$
- $\mu$: Expected annual return (drift)
- $\sigma$: Annual volatility
- $\Delta t$: Time step size ($\frac{1}{12}$ for monthly steps)
- $Z \sim \mathcal{N}(0, 1)$: Standard normal random shock

With recurring monthly deposits $D$, the iteration step is updated as:

$$S_{t + 1} = (S_t \cdot g_t) + D$$


```bash
pip install numpy matplotlib
