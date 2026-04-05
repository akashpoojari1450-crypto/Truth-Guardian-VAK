from models import NewsObservation, DetectionAction

class TruthGuardianEnv:
    def reset(self) -> NewsObservation:
        return NewsObservation(news_text="SHOCKING: Drinking lemon juice cures cancer!")

    def step(self, action: DetectionAction) -> float:
        print(f"🔱 Action Received: {action.label}")
        return 1.0 if action.label == "FAKE" else 0.0
