"""
The 3-Tier Nested TTSS Sports Analytics Framework Core Engine
Created by: [Your Full Name]
License: MIT License
"""

def calculate_tss(penalties, rank=None, rounds_played=None, is_expanded=False):
    """
    Tier 1: Team Success Stat (TSS)
    Measures single-season architectural performance.
    """
    numerator = sum(penalties)
    if is_expanded and rank is not None and rounds_played is not None:
        denominator = (rank + rounds_played) / 2
    else:
        denominator = rounds_played if rounds_played else len(penalties)
    return round(numerator / denominator, 4)


def calculate_nested_tss(sum_all_years_tss, total_knockout_rounds):
    """
    Tier 2: Nested TSS
    Calculates macro organizational capability across a multi-season meta-bracket.
    """
    if total_knockout_rounds == 0:
        return float('inf')
    return round(sum_all_years_tss / total_knockout_rounds, 4)


def calculate_nested_ttss(raw_nested_tss, total_years_active):
    """
    Tier 3: Nested TTSS
    Multiplies the Nested TSS by total operational years to eliminate lifespan bias.
    """
    return round(raw_nested_tss * total_years_active, 4)


if __name__ == "__main__":
    print("--- 3-Tier TTSS Analytical Engine Active ---\n")
    
    # 1. Tier 1 Test (Spain 2026 Expanded Layout)
    spain_2026_tss = calculate_tss([32, 16, 8, 4, 2, 1], rank=1, rounds_played=6, is_expanded=True)
    print(f"Tier 1: Single Season TSS (Spain 2026): {spain_2026_tss}\n")
    
    # 2. Tier 2 & 3 Test (The SRH vs RCB Paradox Fix)
    historical_db = {
        "Gujarat Titans (GT)": {"sum_tss": 22.20, "rounds": 8, "years": 5},
        "Chennai Super Kings (CSK)": {"sum_tss": 62.41, "rounds": 37, "years": 19},
        "Sunrisers Hyderabad (SRH)": {"sum_tss": 71.92, "rounds": 22, "years": 14},
        "Royal Challengers Bengaluru (RCB)": {"sum_tss": 68.31, "rounds": 26, "years": 19}
    }
    
    leaderboard = []
    for team, data in historical_db.items():
        n_tss = calculate_nested_tss(data["sum_tss"], data["rounds"])
        n_ttss = calculate_nested_ttss(n_tss, data["years"])
        leaderboard.append({"team": team, "ntss": n_tss, "nttss": n_ttss})
        
    # Sort: Lowest score = 1st Rank
    leaderboard.sort(key=lambda x: x["nttss"])
    
    print(f"{'Rank':<5} | {'Franchise':<30} | {'Nested TSS':<12} | {'Nested TTSS':<12}")
    print("-" * 68)
    for index, entry in enumerate(leaderboard, start=1):
        print(f"{index:<5} | {entry['team']:<30} | {entry['ntss']:<12} | {entry['nttss']:<12}")
