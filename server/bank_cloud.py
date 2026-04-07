import random
import time

def verify_with_bank_hq(otp_code):
    """
    Simulates the Bank's Backend Database.
    In a real system, this checks if the Bank's server 
    generated this OTP for Akash's phone number.
    """
    print(f"🔱 [BANK-HQ] Verifying Session for OTP: {otp_code}...")
    
    # Simulate network latency (The "Bank Delay")
    time.sleep(2) 
    
    # 🔱 THE TRUTH LOGIC:
    # We simulate a 20% chance it's a real bank session
    # and an 80% chance it's a fraudulent intercept.
    is_official_session = random.random() < 0.2 
    
    if is_official_session:
        return "SUCCESS: OFFICIAL_BANK_SESSION_CONFIRMED"
    else:
        return "ALERT: NO_ACTIVE_SESSION_FOUND_POTENTIAL_FRAUD"

if __name__ == "__main__":
    # Test the cloud directly
    print(verify_with_bank_hq("882291"))
