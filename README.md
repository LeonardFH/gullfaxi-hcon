>>> %Run -c $EDITOR_CONTENT
<p align="center">
  <img src="images/gullfaxi_logo.png" alt="GullfaxiHCON Logo" width="300">
</p>

# GullfaxiHCON

GitHub: [github.com/LeonardFH/gullfaxi-hcon](https://github.com/LeonardFH/gullfaxi-hcon)  
PyPI: [pypi.org/project/gullfaxi-hcon](https://pypi.org/project/gullfaxi-hcon)

A fast, interpretable, dictionary-based framework for BAM impact sensitivity (H50) prediction from SMILES strings.

**GullfaxiHCON** (pronounced "GOOL-fax-ee-HCON") predicts the 50% initiation height (H50) using [PLACEHOLDER: method summary - composition-derived baseline with bond-specific correction terms / group-additivity scheme / etc.]. It requires no 3D conformers, no DFT calculations, and no GPU acceleration.

Named after the gold-maned horse of the giant Hrungnir, later given to Magni, son of Thor, reflecting the software's connection to impact, force, and initiation.

---

## Current Status

The package implements **BAM impact sensitivity (H50) prediction for organic molecules** containing C, H, O, N, and common heteroatoms (S, F, Cl, Br, P, I).

The framework is designed with extensibility in mind, allowing additional sensitivity endpoints (friction, electrostatic discharge, thermal) to be added in future versions.

---

## Key Performance

| Metric | Value |
|--------|-------|
| **Mean Absolute Error** | **[PLACEHOLDER] cm** (pooled, across [PLACEHOLDER] molecules, [PLACEHOLDER] independent datasets) |
| **Inference Speed** | **[PLACEHOLDER] molecules/second** (single core) / **[PLACEHOLDER] molecules/second** ([PLACEHOLDER] cores) |
| **Parameters** | **[PLACEHOLDER]** (fully interpretable [PLACEHOLDER] coefficients) |
| **Hardware** | Standard laptop CPU (no GPU required) |

---

## Published Research

A full account of the method, validation, and benchmark results is available as a preprint:

> Haasbroek, L. F. (2026). *GullfaxiHCON: [PLACEHOLDER: full paper title].* ChemRxiv. DOI: [10.XXXX/chemrxiv-2026-XXXXX](https://doi.org/10.XXXX/chemrxiv-2026-XXXXX)

For detailed performance across specific datasets, convergence behaviour, stability analyses, and [PLACEHOLDER], please refer to the paper.

---

## Quick Start

### Installation

```bash
pip install gullfaxi-hcon
```

### Train and Predict

```python
from gullfaxi import train_h50, predict_h50, predict_h50_batch
import pandas as pd
from sklearn.metrics import mean_absolute_error

# Train a dictionary on your own dataset
weights = train_h50(
    data_path="trainingdata.csv",  # columns: SMILES, H50
    output_path="my_weights.pkl",
    filter_formulations=True,      # Recommended for pure compounds
    filter_hcon=True,              # Recommended for H,C,O,N only
    verbose=True
)

# Predict a single molecule
h50 = predict_h50("CCO", weights_path="my_weights.pkl")

# Predict a batch of molecules
smiles_list = ["CCO", "CC", "c1ccccc1", "O"]
results = predict_h50_batch(smiles_list, weights_path="my_weights.pkl")
```

---

## Philosophy

GullfaxiHCON explicitly challenges the assumption that high-accuracy impact sensitivity prediction requires deep learning, 3D conformers, or expensive quantum calculations.

**The paper demonstrates** that a physically motivated linear model with fewer than [PLACEHOLDER] parameters can achieve competitive accuracy while being:
- **Transparent** - the [PLACEHOLDER: coefficients] represent [PLACEHOLDER: physical interpretation - e.g. bond-specific contributions to impact sensitivity]. Their relative magnitudes provide chemical insight into which [PLACEHOLDER] contribute most to [PLACEHOLDER: initiation behaviour].
- **Fast** - microsecond-scale inference on commodity hardware.
- **Stable** - dictionaries transfer across independent datasets and converge rapidly.
- **Diagnostic** - the model can identify systematic biases in [PLACEHOLDER: drop-weight test] datasets.

**Important note:** [PLACEHOLDER: any caveats about the interpretation of the fitted coefficients, analogous to the Hofvarpnir note about the reference volume + corrections being a paired system.]

---

## Data Sources

The training and evaluation data used in the paper may be obtained from the following publicly available sources:

- **[PLACEHOLDER Author (Year)]**: [PLACEHOLDER full citation]. DOI: [10.XXXX/XXXXX](https://doi.org/10.XXXX/XXXXX)
  - **Dataset:** [PLACEHOLDER repository link]

- **[PLACEHOLDER Author (Year)]**: [PLACEHOLDER full citation]. DOI: [10.XXXX/XXXXX](https://doi.org/10.XXXX/XXXXX)
  - **Dataset:** [PLACEHOLDER repository link]

- **[PLACEHOLDER Author (Year)]**: [PLACEHOLDER full citation]. DOI: [10.XXXX/XXXXX](https://doi.org/10.XXXX/XXXXX)

These datasets are available as Supporting Information with their respective papers or via the linked public repositories.

---

## Tips for Best Performance

For optimal accuracy, we recommend training separate dictionaries for each chemical family:

- **HCON only** (C, H, N, O) - best overall performance
- **HCON + F** - fluorine-containing molecules
- **HCON + Cl** - chlorine-containing molecules
- **HCON + S** - sulfur-containing molecules
- **HCON + P** - phosphorus-containing molecules

Avoid mixing different heteroatom types (e.g., S and Cl together) in a single training run, as this can degrade prediction accuracy.

For molecules containing rare halogens (Br, I), the HCON-only dictionaries are recommended, as there is insufficient data to train reliable halogen-specific [PLACEHOLDER].

---

## Formulations and Mixtures

GullfaxiHCON handles multi-component systems (SMILES strings containing a dot, e.g., `"CCO.O=C(O)C"`) using [PLACEHOLDER: mass-weighted averaging / stoichiometric mixing / etc.] of the predicted H50 of each component.

For datasets containing a **large number of formulations**, improved accuracy can be achieved by training separate dictionaries on formulation data only. For datasets with **only a few formulations**, the pure-trained dictionaries provide reliable estimates.

For detailed formulation performance, see the paper.

---

## [PLACEHOLDER: Additional Section - e.g. Crystal Habit, Particle Size, Polymorph Effects]

[PLACEHOLDER: one or two paragraphs analogous to the Polymorphs section in the Hofvarpnir README, covering any structural or morphological factors specific to impact sensitivity prediction - e.g. crystal habit, particle size distribution, polymorphic form.]

---

## Community Benchmarks

If you use GullfaxiHCON on your own dataset, I invite you to share your results.

Email: **leonardfhaasbroek@gmail.com**

Please include:
- MAE, RMSE, R2
- Number of molecules
- Dataset description and source (if public)

Results will be posted here (with your permission).

---

## A Friendly Note

Hi there,

I built GullfaxiHCON because impact sensitivity prediction should be fast, transparent, and accessible. I'm glad you found it.

If you need to get in touch: leonardfhaasbroek@gmail.com

## License

This project is distributed under the BSD 3-Clause License.

---

## Citation

If you use this software or method in your research, please use the following citation format:

```text
Haasbroek, L. F. (2026). GullfaxiHCON: Fast dictionary-based BAM impact sensitivity (H50) prediction (Version 0.1.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX
```

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

---

## Contact

Leonard F. Haasbroek  
leonardfhaasbroek@gmail.com
>>> 
