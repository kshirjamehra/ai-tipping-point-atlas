# The AI Tipping Point Atlas

![Status](https://img.shields.io/badge/Status-Research_Prototype-blueviolet?style=for-the-badge)
![Field](https://img.shields.io/badge/Field-Complexity_Science-FF4B4B?style=for-the-badge)
![Tech](https://img.shields.io/badge/Stack-Streamlit_%7C_SciPy-00CC96?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-gray?style=for-the-badge)
## 📑 Abstract

**Predicting the "Edge of Chaos" in Recursive Systems.**

As AI models become increasingly recursive (training on their own outputs), they behave like nonlinear dynamic systems. This project maps the mathematical thresholds where such systems transition from stability to irreversible chaotic behavior.

Using the **Logistic Map** ($x_{n+1} = rx_n(1-x_n)$) as a proxy for recursive self-improvement, this tool visualizes **Bifurcation Diagrams** and detects **Critical Slowing Down**—a statistical precursor to systemic collapse.

---

## 📸 Visualization Suite

### 1. Global Stability Map (Bifurcation Diagram)
> *Visualizing the period-doubling route to chaos. As the recursive rate ($r$) increases, the system's equilibrium splits, eventually descending into deterministic chaos.*

![Bifurcation Map](bifurcation_map.png)

### 2. Early Warning Signal (EWS) Detection
> *Real-time monitoring of Lag-1 Autocorrelation. A spike in autocorrelation (Critical Slowing Down) signals that the system is losing resilience and approaching a tipping point.*

![EWS Analysis](ews_analysis.png)

*(Ensure you have images named `bifurcation_map.png` and `ews_analysis.png` in your repository)*

---

## 🧠 Key Concepts Implemented

* **Deterministic Chaos:** The system is governed by simple rules, yet produces behavior that appears random and is impossible to predict long-term.
* **Period-Doubling Bifurcation:** The specific pathway by which a stable system fragments into oscillating states before turning chaotic.
* **Critical Slowing Down:** A phenomenon where a system takes longer to recover from small perturbations as it nears a tipping point. We measure this via **Lag-1 Autocorrelation**.

---

## 🛠️ Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/ai_tipping_point_atlas.git](https://github.com/yourusername/ai_tipping_point_atlas.git)
cd ai_tipping_point_atlas
2. Install Scientific Dependencies
Bash

pip install -r requirements.txt
3. Launch the Atlas
Bash

python -m streamlit run app.py
📂 Repository Structure
Plaintext

📁 ai_tipping_point_atlas
│
├── 📄 app.py              # The Chaos Engine & Dashboard
├── 📄 requirements.txt    # Dependencies (NumPy, Plotly, SciPy)
├── 📄 README.md           # Research Documentation
├── 🖼️ bifurcation_map.png # Screenshot 1
└── 🖼️ ews_analysis.png    # Screenshot 2

Built for the study of Nonlinear Dynamics & AI Safety Kshirja Mehra | 2026
