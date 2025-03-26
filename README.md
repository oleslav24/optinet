# OptiNet Simulation: Distributed System Control Models

This repository contains a synthetic dataset and simulation code to evaluate task scheduling algorithms in a distributed computing network of 100,000 nodes over one month.
Simulation and analysis of ZNN, LNN and hubrid algorithms for optimizing distributed computing systems, targeting carbon footprint reduction. Integrates real-time predictive modeling with sustainability goals, validated on NorduGrid and synthetic datasets.

Carbon Footprint Minimization Simulation

Simulation and analysis of Zeroing Neural Networks (ZNN) and Liquid Neural Networks (LNN) algorithms for optimizing distributed computing systems, targeting carbon footprint reduction. Integrates real-time predictive modeling with sustainability goals, validated on NorduGrid and synthetic datasets.

This project implements the methods described in the paper *"Carbon Footprint Minimization on the Basis of Time-Varying Matrix Problems"* by Oleslav Antamoshkin et al., focusing on resource control in distributed dynamic computing systems (DDCS) to reduce CO2 emissions by up to 7%.

Features
- **ZNN Implementation**: Real-time optimization of time-varying matrix problems using exponential error decay.
- **LNN Integration**: Adaptive time constants for enhanced responsiveness to noisy and dynamic inputs.
- **Hybrid ZNN-LNN Workflow**: Combines ZNN's precision with LNN's flexibility for robust resource allocation.
- **Datasets**: Simulated on NorduGrid-inspired (2.7M nodes) and synthetic (3M nodes) data.
- **Visualization**: Reproduces key results (e.g., Fig. 1-3 from the paper) for carbon emissions and task latency.


## Structure

- `data/synthetic_distributed_tasks.csv`: Generated dataset of 1M tasks across 100k nodes.
- `code/simulation_core.py`: Python script to compute energy use and carbon emissions.
- `results/`: Place for saving model outputs and analysis.

## How to Use

1. Clone the repository:
```bash
git clone https://github.com/oleslav24/optinet.git
cd optinet
```

2. Add the files from this archive into the cloned directory.

3. Run simulation code:
```python
from code.simulation_core import calculate_energy_and_emissions
import pandas as pd

df = pd.read_csv("data/synthetic_distributed_tasks.csv")
df = calculate_energy_and_emissions(df)
print(df.head())
```

Scientific Basis
This project is based on the paper:
- Antamoshkin, O., Masich, I., Bryukhanova, E., & Kraeva, E. "Carbon Footprint Minimization on the Basis of Time-Varying Matrix Problems." (In preparation, 2025).

Contributing
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request. For major changes, open an issue first to discuss.




## License

MIT License.

## Contact

For questions, contact Igor Masich at [oleslav24@gmail.com](mailto:oleslav24@gmail.com).
