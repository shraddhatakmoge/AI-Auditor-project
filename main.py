from app.auditor.final_audit import FinalAuditor


def main():

    decision = input(
        "Enter your decision:\n> "
    )

    auditor = FinalAuditor()

    print("\nAnalyzing decision...")

    result = auditor.audit(decision)

    print("\n" + "=" * 60)
    print("              AI DECISION AUDIT")
    print("=" * 60)

    print("\nDECISION")
    print(result["decision"])

    print("\nDOMAIN")
    print(result["domain"])

    print("\nASSUMPTIONS")

    for assumption in result["assumptions"]:
        print(
            f"- {assumption.text} "
            f"[{assumption.importance}]"
        )

    print("\nEXPECTED OUTCOME")
    print(result["expected_outcome"])

    print("\nMISSING INFORMATION")

    for item in result["missing_information"]:
        print(f"- {item}")

    print("\nEVIDENCE VERIFICATION")

    verification = result["verification"]

    print("Status:")
    print(verification.status.value)

    print("Confidence:")
    print(verification.confidence)

    print("Reasoning:")
    print(verification.reasoning)

    print("\nRETRIEVED EVIDENCE")

    for document in result["evidence"]:
        print(f"- {document.page_content}")

    print("\nCOUNTERARGUMENT")

    counterargument = result["counterargument"]

    print("Argument:")
    print(counterargument.argument)

    print("\nReasoning:")
    print(counterargument.reasoning)

    print("\nRISK ASSESSMENT")

    risk = result["risk"]

    print(f"Score: {risk['score']}/10")
    print(f"Level: {risk['level'].upper()}")

    print("\nWhy:")

    for reason in risk["reasons"]:
        print(f"- {reason}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()