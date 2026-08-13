def calculate_overall_risk(audit_results, assumptions=None, missing_information=None):

    score = 0
    reasons = []

    # Evidence risk
    for result in audit_results:

        if result.status.value == "contradicted":
            score += 4
            reasons.append(
                f"Claim contradicted by available evidence: {result.claim}"
            )

        elif result.status.value == "insufficient_evidence":
            score += 3
            reasons.append(
                f"Important claim lacks sufficient evidence: {result.claim}"
            )

        elif result.status.value == "supported":
            score += 0

    # Missing information
    if missing_information:
        score += min(len(missing_information), 3)

        if missing_information:
            reasons.append(
                f"{len(missing_information)} important pieces of information "
                "are missing."
            )

    # Assumption risk
    if assumptions:
        high_assumptions = sum(
            1
            for assumption in assumptions
            if assumption.importance.lower() == "high"
        )

        score += min(high_assumptions, 3)

        if high_assumptions:
            reasons.append(
                f"{high_assumptions} high-importance assumptions "
                "require validation."
            )

    score = min(score, 10)

    if score >= 7:
        level = "high"
    elif score >= 4:
        level = "medium"
    else:
        level = "low"

    return {
        "score": score,
        "level": level,
        "reasons": reasons
    }