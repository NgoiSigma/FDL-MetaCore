# modules/Δψ_monitor/lie_tension_analyzer.py

"""
Δψ-Monitor: Lie Tension Analyzer
Part of the Σ-FDL::MetaCore framework

This module evaluates narrative pressure, contradiction buildup, and systemic stress
based on FDL (Formally-Dialectical Logic) indicators in data streams (text/news/social).

Author: Sigma Avatarus
License: Apache 2.0
"""

import re
import math
from collections import Counter

class LieTensionAnalyzer:
    def __init__(self, contradiction_terms=None, context_weights=None):
        self.contradiction_terms = contradiction_terms or ["but", "however", "although", "nevertheless", "in reality", "despite"]
        self.context_weights = context_weights or {
            "war": 2.5,
            "elections": 1.8,
            "ethics": 2.0,
            "economy": 1.3,
            "AI": 1.5,
            "identity": 2.1,
            "corruption": 2.8
        }

    def analyze_text(self, text):
        """
        Main method to calculate 'tension score' of a narrative segment
        """
        contradiction_hits = sum(text.lower().count(term) for term in self.contradiction_terms)
        context_hits = Counter()

        for keyword in self.context_weights:
            hits = len(re.findall(rf"\b{keyword}\b", text.lower()))
            context_hits[keyword] = hits

        # Weighted context factor
        weighted_sum = sum(self.context_weights[key] * count for key, count in context_hits.items())
        base_score = contradiction_hits * 1.0 + weighted_sum

        # Normalize
        tension_score = round(math.log1p(base_score + 1) * 10, 2)
        return {
            "contradiction_hits": contradiction_hits,
            "context_hits": dict(context_hits),
            "weighted_sum": weighted_sum,
            "tension_score": tension_score
        }

    def classify_tension(self, score):
        """
        Classify narrative tension level
        """
        if score < 10:
            return "Low"
        elif score < 20:
            return "Moderate"
        elif score < 30:
            return "High"
        else:
            return "Critical"

# Example usage:
if __name__ == "__main__":
    analyzer = LieTensionAnalyzer()
    sample_text = "Despite economic sanctions, the war continues. However, Western unity shows signs of fatigue."
    result = analyzer.analyze_text(sample_text)
    result["classification"] = analyzer.classify_tension(result["tension_score"])
    print(result)
