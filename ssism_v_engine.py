# ssism_v_engine.py - The SSISM V Smart Advisor Core Engine (Philosophical, Mathematical, and Emotional Defense System)
# Developed by U Ingar Soe & Gemini.
# Core Principle: "Doing Nothing as Value" (The Mandatory Lockout Command)

import numpy as np

def sigmoid(z):
    """The Sigmoid Function (Logistic Regression Model)."""
    # This transforms the Total Risk Score (Z) into a probability/score (Digital Trust Score Phi).
    return 1 / (1 + np.exp(-z))

def calculate_trust_score(A, U, L, R, T_delta, weights):
    """
    Calculates the Total Risk Score (Z) and the Digital Trust Score (Phi).
    Z = w_A*A + w_U*U + w_L*L + w_R*R + w_T*DeltaT
    Phi = Sigmoid(Z)
    """
    
    # 1. Total Risk Score (Z): Aggregation of weighted factors
    # A: Authority, U: Urgency, L: Linguistics, R: Link/File, T_delta: Time Anomaly
    Z = (weights['A'] * A + 
         weights['U'] * U + 
         weights['L'] * L + 
         weights['R'] * R + 
         weights['T'] * T_delta)
    
    # 2. Digital Trust Score (Phi): Z transformed by the Sigmoid function
    Phi = sigmoid(Z)
    
    return Z, Phi

def ssism_mandatory_lockout(Phi, threshold=0.2):
    """
    Implements the MANDATORY LOCKOUT command. 
    Triggers a 24-hour verification protocol if the Digital Trust Score (Phi) is below the threshold.
    """
    if Phi < threshold:
        lockout_message = f"🚨 MANDATORY LOCKOUT TRIGGERED (Phi={Phi:.2f} < {threshold}). INITIATE 24-HOUR VERIFICATION PROTOCOL."
        lockout_action = True
    else:
        lockout_message = f"✅ Digital Trust Score (Phi={Phi:.2f}). Communication may proceed with caution."
        lockout_action = False

    return lockout_action, lockout_message

# Example Usage & Test Case (High-Risk Scenario)
# Weights based on real-world scam experiences (Example weights for demonstration):
WEIGHTS = {'A': 0.4, 'U': 0.3, 'L': 0.1, 'R': 0.1, 'T': 0.1} 

# Scenario: High Authority (1.0), High Urgency (1.0), Poor Linguistics (0.5), Suspicious Link (1.0), Major Time Anomaly (1.0)
A_score, U_score, L_score, R_score, T_delta_score = 1.0, 1.0, 0.5, 1.0, 1.0 

# Calculate the scores
Z_score, Phi_score = calculate_trust_score(
    A_score, U_score, L_score, R_score, T_delta_score, WEIGHTS
)

# Apply the Mandatory Lockout
lockout, message = ssism_mandatory_lockout(Phi_score)

if __name__ == "__main__":
    print(f"--- SSISM V Smart Advisor Calculation ---")
    print(f"Parameters (A, U, L, R, DeltaT): {A_score}, {U_score}, {L_score}, {R_score}, {T_delta_score}")
    print(f"Total Risk Score (Z): {Z_score:.4f}")
    print(f"Digital Trust Score (Phi): {Phi_score:.4f}")
    print(f"Decision: {message}")
  
