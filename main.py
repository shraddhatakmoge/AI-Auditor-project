from app.auditor.final_audit import FinalAuditor


def main():

    decision = input(
        "Enter your decision:\n> "
    )

    auditor = FinalAuditor()

    result = auditor.audit(decision)

    print("\n" + "=" * 60)
    print("              AI DECISION AUDIT")
    print("=" * 60)

    print("\nDECISION")
    print(result["decision"])

    print("\nDOMAIN")
    print(result["domain"])

    print("\nCLAIMS")

    for claim in result["claims"]:
        print(
            f"- {claim.text} "
            f"[{claim.importance}] "
            f"[{claim.claim_type.value}] "
            f"[{claim.verifiability.value}]"
        )

    print("\nASSUMPTIONS")

    for assumption in result["assumptions"]:
        print(
            f"- {assumption.text} "
            f"[{assumption.importance}]"
        )

    print("\nMISSING INFORMATION")

    for item in result["missing_information"]:
        print(f"- {item}")

    print("\nEVIDENCE AUDIT")

    for audit in result["audit_results"]:

        print("\nClaim:")
        print(audit.claim)

        print("Status:")
        print(audit.status.value)

        print("Confidence:")
        print(audit.confidence)

        print("Reasoning:")
        print(audit.reasoning)

        print("Evidence:")

        for evidence in audit.evidence:
            print(f"- {evidence.content}")
            print(f"  Source: {evidence.source}")

    print("\nCOUNTERARGUMENT")

    print(
        result["counterargument"].argument
    )

    print("\nReasoning:")

    print(
        result["counterargument"].reasoning
    )

    print("\nRISK ASSESSMENT")

    print(
        f"Score: {result['risk']['score']}/10"
    )
    
    print(
        f"Level: {result['risk']['level'].upper()}"
    )
    
    print("\nWhy:")
    
    for reason in result["risk"]["reasons"]:
        print(f"- {reason}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()