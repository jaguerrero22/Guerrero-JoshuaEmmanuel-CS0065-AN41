
# TA3: AI-Based Legal Decision Support System

# This is a simple Case-Based Reasoning (CBR) program for a theft case
# involving an electronic bank transfer. The program is for our Intelligent


case_base = [
    {
        "case_id": "Case 1",
        "problem": {
            "offense": "online theft",
            "evidence": "account login records",
            "method": "unauthorized online purchase",
            "victim_type": "individual",
        },
        "solution": {
            "strategy": "Challenge the reliability of login records and establish that account access was not exclusive to the accused.",
            "evidence_focus": "Account access history and device ownership",
        },
        "outcome": "Charges reduced after reasonable doubt was raised.",
    },
    {
        "case_id": "Case 2",
        "problem": {
            "offense": "digital fraud",
            "evidence": "email correspondence and transaction logs",
            "method": "false online transaction",
            "victim_type": "business",
        },
        "solution": {
            "strategy": "Question whether the digital messages were authenticated and whether the accused controlled the account used.",
            "evidence_focus": "Email metadata and account authentication",
        },
        "outcome": "Acquittal after the digital evidence was found incomplete.",
    },
    {
        "case_id": "Case 3",
        "problem": {
            "offense": "unauthorized bank transfer",
            "evidence": "bank statements and transfer records",
            "method": "mobile banking transfer",
            "victim_type": "individual",
        },
        "solution": {
            "strategy": "Request a complete transaction audit and examine whether another device or person could have authorized the transfer.",
            "evidence_focus": "Bank audit trail, device logs, and authentication records",
        },
        "outcome": "Case dismissed because the transfer could not be linked exclusively to the accused.",
    },
    {
        "case_id": "Case 4",
        "problem": {
            "offense": "identity theft",
            "evidence": "social media messages and IP address records",
            "method": "stolen online identity",
            "victim_type": "individual",
        },
        "solution": {
            "strategy": "Separate identity ownership from device or network use and request independent verification of the IP evidence.",
            "evidence_focus": "IP attribution, account ownership, and identity verification",
        },
        "outcome": "Verdict was delayed pending additional forensic examination.",
    },
    {
        "case_id": "Case 5",
        "problem": {
            "offense": "online theft",
            "evidence": "CCTV footage and payment records",
            "method": "stolen card used online",
            "victim_type": "business",
        },
        "solution": {
            "strategy": "Compare the timing of the payment with the footage and test whether the payment account was directly controlled by the accused.",
            "evidence_focus": "Transaction timing, CCTV, and payment-account ownership",
        },
        "outcome": "Charges reduced after the evidence did not prove direct control.",
    },
]


new_case = {
    "case_id": "New Case",
    "problem": {
        "offense": "theft involving electronic transfer",
        "evidence": "bank statements and digital transaction records",
        "method": "unauthorized electronic bank transfer",
        "victim_type": "individual",
    },
}


# The weights show which facts are more important in comparing two cases.
ATTRIBUTE_WEIGHTS = {
    "offense": 0.30,
    "evidence": 0.25,
    "method": 0.30,
    "victim_type": 0.15,
}


def similarity_score(new_problem, old_problem):
    """Compare two cases and return a score from 0 to 100."""
    score = 0.0
    for attribute, weight in ATTRIBUTE_WEIGHTS.items():
        if new_problem[attribute] == old_problem[attribute]:
            score += weight
        # Give half credit when the wording is different but the idea is related.
        elif attribute == "offense" and {
            new_problem[attribute], old_problem[attribute]
        } <= {"online theft", "theft involving electronic transfer", "unauthorized bank transfer"}:
            score += weight * 0.5
        elif attribute == "evidence" and {
            new_problem[attribute], old_problem[attribute]
        } <= {"bank statements and digital transaction records", "bank statements and transfer records"}:
            score += weight * 0.5
    return score * 100


def retrieve_cases(case, cases):
    """Find and rank the cases that are closest to the new case."""
    ranked = []
    for old_case in cases:
        score = similarity_score(case["problem"], old_case["problem"])
        ranked.append((score, old_case))
    return sorted(ranked, key=lambda item: item[0], reverse=True)


def adapt_solution(retrieved_case, case):
    """Use the old strategy and adjust it for the new case."""
    old_solution = retrieved_case["solution"]
    return {
        "strategy": (
            old_solution["strategy"]
            + " For this case, specifically request the bank's complete audit trail, "
            "device and login records, authentication method, and proof that the accused "
            "person exclusively controlled the receiving account."
        ),
        "evidence_focus": (
            old_solution["evidence_focus"]
            + "; bank authentication records and recipient-account ownership"
        ),
        "adapted_to": case["problem"]["method"],
    }


def display_case_summary(case):
    for key, value in case["problem"].items():
        print(f"  {key.replace('_', ' ').title()}: {value}")


def main():
    print("AI-BASED LEGAL DECISION SUPPORT SYSTEM")
    print("A SIMPLE CASE-BASED REASONING PROGRAM")
    print("=" * 60)

    print("\nNEW PROBLEM")
    display_case_summary(new_case)

    print("\nRETRIEVE: Checking the old cases")
    ranked_cases = retrieve_cases(new_case, case_base)
    for rank, (score, case) in enumerate(ranked_cases, start=1):
        print(f"  {rank}. {case['case_id']}: {score:.2f}% similarity")

    best_score, best_case = ranked_cases[0]
    print(f"\nMOST RELEVANT PAST CASE: {best_case['case_id']} ({best_score:.2f}% similarity)")
    print(f"  Previous outcome: {best_case['outcome']}")

    print("\nREUSE AND REVISE: Adjusting the old strategy")
    adapted_solution = adapt_solution(best_case, new_case)
    print(f"  Strategy: {adapted_solution['strategy']}")
    print(f"  Evidence focus: {adapted_solution['evidence_focus']}")

    # RETAIN: add the new case so it can be used in a future comparison.
    retained_case = {
        **new_case,
        "solution": adapted_solution,
        "outcome": "Educational demonstration: strategy generated and retained for future comparison.",
    }
    case_base.append(retained_case)

    print("\nRETAIN: New case added to the case base")
    print(f"  Updated case-base size: {len(case_base)} cases")
    print("  Case IDs: " + ", ".join(case["case_id"] for case in case_base))

    print("\nCBR CYCLE COMPLETE")
    print("Retrieve -> Reuse -> Revise -> Retain")

if __name__ == "__main__":
    main()
