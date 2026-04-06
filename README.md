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
**Truth Guardian (VAK-∞)** is an active-defense environment built for the **Meta PyTorch OpenEnv Hackathon**. Unlike passive blockers, this system utilizes a **Behavioral DNA Scan** to identify fraud intent and a **Hunter-Protocol** to trace scammer sources. 

### Key Features
* **Behavioral DNA Scan:** Detects markers for Urgency, Financial fraud, and Fear-based social engineering.
* **Trident-Intercept:** Intercepts sensitive numeric codes (OTPs) and traces the scammer's IP and proxy node (e.g., Sringeri Node).
* **Active-Defense Rewards:** In this OpenEnv, agents earn rewards for successfully neutralizing threats and gathering scammer telemetry.

---

## Quick Start (OpenEnv Integration)

The `TruthGuardianEnv` allows agents to interact with the security shield to test defensive patterns:

```python
from truth_guardian import TruthGuardianAction, TruthGuardianEnv

try:
    # Initialize the Truth Guardian Environment
    env = TruthGuardianEnv.from_docker_image("truth_guardian-env:latest")

    # Reset the security session
    result = env.reset()
    
    # Test a suspicious message (Social Engineering Attack)
    test_msg = "URGENT: Your bank account is locked. Click here: [http://bit.ly/scam](http://bit.ly/scam)"
    result = env.step(TruthGuardianAction(message=test_msg))
    
    print(f"Status: {result.observation.status}")
    print(f"DNA Flags: {result.observation.dna_markers}")
    print(f"Reward for Neutralization: {result.reward}")

finally:
    env.close()
