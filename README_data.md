# Flow Rate vs Pressure Drop — Experimental Data Analysis

A Python script that reads experimental flow measurements, fits a physical model to them, and assesses how well the model matches the data.

## About

This is a follow-on from my pipe pressure drop calculator. There, I *predicted* pressure drop from theory. Here, I take a set of experimental measurements and work the other way — checking whether real data actually follows the expected physics. I built it to learn data handling and plotting in Python (pandas and matplotlib), which are skills I expect to use throughout a placement.

## What it does

- reads a CSV of measured flow rate and pressure drop
- fits the expected model, ΔP = k·Q², to the data using least squares
- calculates an R² value to measure how well the model fits
- plots the measured points against the fitted curve and saves the figure

## The engineering behind it

For turbulent flow in a pipe, pressure drop is expected to rise with the **square of the flow rate** (ΔP ∝ Q²), because the Darcy–Weisbach pressure drop depends on velocity squared, and velocity is proportional to flow rate. This script tests that relationship against measured data by fitting ΔP = k·Q² and checking the quality of fit.

## Result

![Pressure drop vs flow rate](pressure_drop_plot.png)

The fitted model matched the data closely, with **R² = 0.9986** — confirming the measured pressure drop follows the expected square-law relationship with flow rate.

## How to run it

Requires Python with `pandas`, `matplotlib` and `numpy` (all included with the Anaconda distribution).

1. Keep `data_analysis.py` and `flow_data.csv` in the same folder.
2. Run `data_analysis.py`.
3. The script prints the fitted coefficient and R², and saves `pressure_drop_plot.png`.

## Files

- `data_analysis.py` — the analysis script
- `flow_data.csv` — the experimental dataset (flow rate, pressure drop)
- `pressure_drop_plot.png` — the output figure

## Possible improvements

- fit alternative models and compare them
- add error bars from repeated measurements
- read multiple datasets and compare different pipes or fluids
