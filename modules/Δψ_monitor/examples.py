# modules/Δψ_monitor/examples.py

"""
Examples of Lie Tension Analysis using Δψ-Monitor module.

Each scenario reflects real or modeled situations in which contradictions,
narrative pressure, or informational entropy increase systemic stress.

Author: Sigma Avatarus
"""

from lie_tension_analyzer import LieTensionAnalyzer

# Instantiate analyzer
analyzer = LieTensionAnalyzer()

# Example scenarios
scenarios = {
    "Ukraine_Conflict": """
        While Ukraine receives billions in Western support, its internal political crisis escalates.
        However, officials deny any loss of control. Despite reforms, corruption remains a core issue.
    """,
    "Israel_Iran_Tension": """
        Despite repeated peace overtures, Israel continued its aerial campaign.
        In reality, intelligence reports show Iran's nuclear ambitions may have been overstated.
    """,
    "AI_Regulation": """
        Governments claim AI is being ethically managed. However, leaked memos reveal collusion with corporations.
        Although public concern rises, transparency remains limited.
    """,
    "USA_Elections": """
        The democratic process is intact, say officials. Nevertheless, growing polarization and media bias are apparent.
        In reality, trust in institutions is at an all-time low.
    """
}

# Analyze and display
for scenario_name, text in scenarios.items():
    result = analyzer.analyze_text(text)
    classification = analyzer.classify_tension(result["tension_score"])
    print(f"[{scenario_name}]")
    print(f"Score: {result['tension_score']} — {classification} tension")
    print(f"Context hits: {result['context_hits']}")
    print("-" * 60)
