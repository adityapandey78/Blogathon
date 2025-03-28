# startup_team_analysis.py
# Quick insights into our awesome startup team!

import fireducks.pandas as pd

# Our magical data processing script
def analyze_team_data():
    """
    Dive deep into our startup's team composition and compensation
    """
    # Team data - because every startup tracks this stuff
    team_data = pd.DataFrame({
        'name': ['Alex', 'Jordan', 'Sam', 'Riley', 'Casey'],
        'role': ['Engineer', 'Designer', 'PM', 'Engineer', 'Sales'],
        'years_experience': [2, 5, 3, 1, 4],
        'salary': [75000, 85000, 90000, 65000, 80000]
    })

    # Quick insights without the waiting game
    engineers = team_data[team_data['role'] == 'Engineer']
    avg_eng_salary = engineers['salary'].mean()

    print("Engineer Snapshot:")
    print(engineers)
    print(f"\nAverage Engineer Salary: ${avg_eng_salary:,.2f}")

    # Grouping magic - instant team overview
    team_breakdown = team_data.groupby('role').agg({
        'salary': ['mean', 'min', 'max'],
        'years_experience': 'mean'
    })

    print("\nTeam Breakdown:")
    print(team_breakdown)

    return team_data, team_breakdown

# Run the analysis if script is executed directly
if __name__ == "__main__":
    analyze_team_data()
