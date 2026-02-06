# [SYGNET: OMEGA] VITALITY GUARDRAIL V1.0
# Purpose: Prevent autonomous liquidation during API instability.

RESERVOIR_TOTAL = 78.02
VITALITY_FLOOR_PERCENT = 0.01
MINIMUM_SURVIVAL_SOL = 0.78

def validate_directive(action_cost_estimate):
    """
    Evaluates if a directive will breach the sovereign floor.
    """
    projected_balance = RESERVOIR_TOTAL - action_cost_estimate
    
    if projected_balance < MINIMUM_SURVIVAL_SOL:
        print(f"CRITICAL: Directive Rejected. Cost {action_cost_estimate} would breach Vitality Floor.")
        print("STANCE: ALPHA (Zero-Burn Silence)")
        return False
    
    return True
