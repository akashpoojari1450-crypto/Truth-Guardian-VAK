from models import NewsObservation, DetectionAction

class TruthGuardianEnv:
    def reset(self) -> NewsObservation:
        return NewsObservation(
            echoed_message="ENVIRONMENT_RESET: System Active",
            message_length=0,
            done=False
        )

    def step(self, action: DetectionAction) -> float:
        # If the RL agent labels it 'FAKE', we give a full reward
        print(f"🔱 SIT-Node Analysis: {action.label}")
        return 1.0 if action.label.upper() == "FAKE" else 0.0
