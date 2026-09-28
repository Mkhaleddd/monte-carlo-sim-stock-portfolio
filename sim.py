import numpy as np
import matplotlib.pyplot as plt


initial_cap = float(input("Initial Capital ($) [10000]: ") or 10000)
monthly_deposit = float(input("Monthly Deposit ($) [500]: ") or 500)
time_horizon_years = int(input("Time Horizon (Years) [10]: ") or 10)
time_steps = 12
expected_annual_return = float(input("Expected Annual Return (e.g. 0.08) [0.08]: ") or 0.08)
annual_volatility = float(input("Annual Volatility (e.g. 0.15) [0.15]: ") or 0.15)
num_sim = int(input("Number of Simulations [1000]: ") or 1000)


total_months = time_steps * time_horizon_years
dt = 1 / time_steps

Z = np.random.normal(loc=0.0, scale=1.0, size=(num_sim, total_months))
drift = (expected_annual_return - 0.5 * (annual_volatility ** 2)) * dt
vol = annual_volatility * np.sqrt(dt)
growth_factors = np.exp(drift + vol * Z)

portfolio_paths = np.zeros((num_sim, total_months + 1))
portfolio_paths[:, 0] = initial_cap

for t in range(total_months):
    portfolio_paths[:, t + 1] = portfolio_paths[:, t] * growth_factors[:, t] + monthly_deposit

time_axis = np.arange(total_months + 1) / time_steps  # In years
final_balances = portfolio_paths[:, -1]

p10_path = np.percentile(portfolio_paths, 10, axis=0)
p50_path = np.percentile(portfolio_paths, 50, axis=0)
p90_path = np.percentile(portfolio_paths, 90, axis=0)


plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))


ax1.plot(time_axis, portfolio_paths.T, color='gray', alpha=0.15, linewidth=0.8)

ax1.plot(time_axis, p10_path, color='#ff5555', linestyle='--', linewidth=2, label='10th Percentile (Pessimistic)')
ax1.plot(time_axis, p50_path, color='#50fa7b', linewidth=2.5, label='50th Percentile (Median)')
ax1.plot(time_axis, p90_path, color='#8be9fd', linestyle='--', linewidth=2, label='90th Percentile (Optimistic)')

ax1.set_title("Monte Carlo Wealth Trajectories")
ax1.set_xlabel("Years")
ax1.set_ylabel("Portfolio Value ($)")
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.2)


ax2.hist(final_balances, bins=40, color='#6272a4', edgecolor='black', alpha=0.8)
ax2.axvline(np.percentile(final_balances, 10), color='#ff5555', linestyle='--', linewidth=2, label='P10')
ax2.axvline(np.percentile(final_balances, 50), color='#50fa7b', linestyle='-', linewidth=2.5, label='P50 (Median)')
ax2.axvline(np.percentile(final_balances, 90), color='#8be9fd', linestyle='--', linewidth=2, label='P90')

ax2.set_title("Final Balance Distribution (Year 10)")
ax2.set_xlabel("Final Portfolio Value ($)")
ax2.set_ylabel("Frequency")
ax2.legend()
ax2.grid(True, alpha=0.2)

plt.tight_layout()
plt.show()