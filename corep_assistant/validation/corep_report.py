# Toggle this flag for demo purposes
DEMO_HAS_ERROR = True   # 🔴 change to False for correct output

if DEMO_HAS_ERROR:
    # ❌ Incorrect COREP data (will trigger validation issue)
    COREP_REPORT = {
        "R010": 800.0,   # CET1
        "R020": 400.0,   # AT1
        "R030": 300.0,   # Tier 2
        "R040": 1400.0   # Total Own Funds (WRONG on purpose)
    }
else:
    # ✅ Correct COREP data (passes validation)
    COREP_REPORT = {
        "R010": 800.0,   # CET1
        "R020": 400.0,   # AT1
        "R030": 300.0,   # Tier 2
        "R040": 1500.0   # Total Own Funds (CORRECT)
    }

