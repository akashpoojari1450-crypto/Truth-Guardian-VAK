---
title: Truth Guardian (VAK-∞)
emoji: 🛡️
colorFrom: blue
colorTo: gold
sdk: docker
pinned: false
app_port: 8000
base_path: /web
tags:
  - openenv
  - pytorch
  - meta-hackathon
---

# 🔱 Truth Guardian (VAK-∞)
### Team Vakratunda | SIT Valachil Node

> [!IMPORTANT]
> 🎥 **[CLICK HERE TO WATCH THE PROJECT DEMO VIDEO](https://youtu.be/eyrkVPflfLI)**
> 🚀 **Live App:** [Hugging Face Space](https://huggingface.co/spaces/Akash154/Truth-Guardian-VAK)

## Project Overview
**Truth Guardian (VAK-∞)** is an active-defense environment built for the **Meta PyTorch OpenEnv Hackathon**. Instead of just blocking spam, this system uses **Behavioral DNA Scanning** and a **Hunter-Protocol** to trace scammer sources and neutralize threats.

### Key Features
* **Behavioral DNA Scan:** Analyzes intent to flag markers for Urgency, Financial fraud, and Social Engineering.
* **Trident-Intercept:** Specialized trap for sensitive OTPs that traces the scammer's IP and proxy node (e.g., Sringeri Node).
* **Active-Defense Rewards:** Agents in this environment earn rewards for successfully neutralizing deceptive interactions.

---

## Quick Start (OpenEnv Integration)

Interact with the security shield using the `TruthGuardianEnv` class:

```python
from truth_guardian import TruthGuardianAction, TruthGuardianEnv

try:
    # Initialize the Truth Guardian Environment
    env = TruthGuardianEnv.from_docker_image("truth_guardian-env:latest")

    # Reset the security session
    result = env.reset()
    
    # Test a suspicious message
    test_msg = "URGENT: Your account is locked. Verify here: [http://bit.ly/scam](http://bit.ly/scam)"
    result = env.step(TruthGuardianAction(message=test_msg))
    
    print(f"Status: {result.observation.status}")
    print(f"DNA Flags: {result.observation.dna_markers}")
finally:
    env.close()
