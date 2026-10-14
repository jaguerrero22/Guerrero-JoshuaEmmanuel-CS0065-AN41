
facts = {
    "temperature": 32,      # Category 1: Environment
    "humidity": 85,         # Category 1: Environment
    "is_raining": True,     # Category 2: Status
    "is_cloudy": True,      # Category 2: Status
    "user_present": True    # Category 3: Presence
}


# -----------------------------
# Rule-Based Reasoning (RBR)
# -----------------------------

def rule_hot(facts):
    if facts.get("temperature", 0) > 30 and facts.get("user_present", False):
        return "Turn on the air conditioner"
    return None


def rule_rain(facts):
    if facts.get("is_raining", False):
        return "Bring an umbrella"
    return None


def rule_dehumidifier(facts):
    if facts.get("humidity", 0) > 80:
        return "Turn on the dehumidifier"
    return None


def run_rbr_inference_engine(facts_db, rules_list):
    inferred_actions = []

    for rule in rules_list:
        action = rule(facts_db)

        if action:
            inferred_actions.append(action)

    print("Rule-Based Reasoning Actions:")

    for action in inferred_actions:
        print(f"- {action}")

    return inferred_actions


# Execute RBR demonstration
rules = [
    rule_hot,
    rule_rain,
    rule_dehumidifier
]

run_rbr_inference_engine(facts, rules)

print("\n" + "=" * 40 + "\n")


# -----------------------------
# Case-Based Reasoning (CBR)
# -----------------------------

case_base = [
    {
        "problem": {
            "won't turn on": True,
            "noise": False
        },
        "solution": "Check the power cable."
    },
    {
        "problem": {
            "won't turn on": True,
            "noise": True
        },
        "solution": "Inspect the fan motor for blockage."
    },
    {
        "problem": {
            "won't turn on": False,
            "noise": True
        },
        "solution": "Clean or replace the fan bearings."
    }
]


def calculate_similarity(new_problem, case_problem):
    score = 0

    total_keys = set(new_problem.keys()).union(case_problem.keys())

    for key in total_keys:
        if new_problem.get(key) == case_problem.get(key):
            score += 1

    if total_keys:
        return score / len(total_keys)

    return 0.0


def retrieve_and_reuse(new_problem, case_base):
    best_match = None
    highest_score = -1.0

    for case in case_base:
        similarity = calculate_similarity(
            new_problem,
            case["problem"]
        )

        if similarity > highest_score:
            highest_score = similarity
            best_match = case

    print(
        f"[Retrieve & Reuse] Most similar case score: "
        f"{highest_score * 100:.1f}%"
    )

    if best_match:
        return best_match["solution"]

    return "No solution found."


def revise_solution(proposed_solution, manual_adjustment=None):
    if manual_adjustment:
        print(
            f"[Revise] Solution updated from "
            f"'{proposed_solution}' to '{manual_adjustment}'"
        )
        return manual_adjustment

    print(
        f"[Revise] Proposed solution accepted without changes: "
        f"'{proposed_solution}'"
    )

    return proposed_solution


def retain_case(case_base, new_problem, final_solution):
    new_case = {
        "problem": new_problem,
        "solution": final_solution
    }

    case_base.append(new_case)

    print(
        "[Retain] New case successfully learned "
        "and stored in the case base."
    )


# New problem input
new_user_problem = {
    "won't turn on": True,
    "noise": False
}

print(f"New Problem Input: {new_user_problem}")


# 1. Retrieve and reuse
retrieved_solution = retrieve_and_reuse(
    new_user_problem,
    case_base
)


# 2. Revise
final_solution = revise_solution(
    retrieved_solution,
    manual_adjustment="Check the power cable and fuse box."
)


# 3. Retain
retain_case(
    case_base,
    new_user_problem,
    final_solution
)