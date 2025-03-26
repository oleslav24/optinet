# optinet
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

Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.8+
- Required libraries:
  - `numpy` (for matrix operations)
  - `torch` (for LNN implementation with PyTorch)
  - `matplotlib` (for visualization)
  - `pandas` (for data handling)

You can install them via pip:
```bash
pip install numpy torch matplotlib pandas
```
Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/oleslav24/optinet.git
   cd optinet
   ```
2. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

Usage
The project includes scripts to simulate ZNN and LNN algorithms, generate synthetic data, and visualize results.

Running the ZNN Simulation
Simulate resource control with ZNN:
```bash
python scripts/run_znn.py --dataset synthetic --steps 1000 --tau 0.0001 --eta 100
```
- `--dataset`: Choose `nordugrid` or `synthetic`.
- `--steps`: Number of simulation steps.
- `--tau`, `--eta`: ZNN parameters (default values from the paper).

Running the Hybrid ZNN-LNN Simulation
Run the hybrid model:
```bash
python scripts/run_hybrid.py --dataset nordugrid --steps 1000
```

Visualizing Results
Generate plots similar to Fig. 1-3 from the paper:
```bash
python scripts/plot_results.py --results results/znn_output.csv
```

---

## Project Structure
```
optinet/
├── data/                # Sample datasets (NorduGrid-inspired and synthetic)
├── scripts/             # Main simulation and visualization scripts
│   ├── run_znn.py       # ZNN simulation
│   ├── run_hybrid.py    # Hybrid ZNN-LNN simulation
│   └── plot_results.py  # Plotting results
├── results/             # Output files (CSV, plots)
├── requirements.txt     # List of dependencies
└── README.md            # This file
```

---

Examples
ZNN Performance
Run the ZNN simulation and visualize CO2 emissions vs. task solving time:
```bash
python scripts/run_znn.py --dataset synthetic --steps 500
python scripts/plot_results.py --results results/znn_output.csv
```
Output: A plot similar to Fig. 1 from the paper.

Hybrid ZNN-LNN
Test the hybrid model on NorduGrid data:
```bash
python scripts/run_hybrid.py --dataset nordugrid --steps 500
```
Output: Reduced task latency and emissions, showcasing LNN's adaptability.


Scientific Basis
This project is based on the paper:
- Antamoshkin, O., Masich, I., Bryukhanova, E., & Kraeva, E. "Carbon Footprint Minimization on the Basis of Time-Varying Matrix Problems." (In preparation, 2025).
 

Funding: Supported by the Ministry of Science and Higher Education of the Russian Federation (Grant No. 075-15-2022-1121).


Contributing
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request. For major changes, open an issue first to discuss.


License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


Contact
For questions, contact Igor Masich at [oleslav24@gmail.com](mailto:oleslav24@gmail.com).
