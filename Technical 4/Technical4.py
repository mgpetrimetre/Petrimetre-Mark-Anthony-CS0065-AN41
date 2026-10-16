# PART 1: KNOWLEDGE REPRESENTATION (KR) SETUP
facts = {
    #Temperature
    "temperature": 43,             
    
    #Status
    "battery_percent": 12,          
    "storage_full": True,         
    "screen_brightness": 100,
    
    #Presence
    "charger_connected": False,
    "headphone_plugged": False  
}

# PART 2: RULE-BASED REASONING (RBR)

# Task 2A: Create 3 simple IF-THEN rules
def rule_overheating(data):
    if data["temperature"] > 40:
        return "Turn on cooling mode and dim screen"
    return None

def rule_low_battery(data):
    if data["battery_percent"] < 15 and not data["charger_connected"]:
        return "Enable Battery Saver mode immediately"
    return None

def rule_storage_full(data):
    if data["storage_full"]:
        return "Prompt user to clear cache and delete large files"
    return None

# Task 2B: Inference Engine loop
rules = [rule_overheating, rule_low_battery, rule_storage_full]
actions_found = []

for rule in rules:
    action = rule(facts)
    if action:
        actions_found.append(action)

# Task 2C: Display Output
print("=== RULE-BASED REASONING (RBR) ===")
print("Current Facts Checked:")
for key, val in facts.items():
    print(f"  {key}: {val}")

print("\nActions Triggered:")
for act in actions_found:
    print(f"  - {act}")


# PART 3: CASE-BASED REASONING (CBR)

# Task 3A: Case Base 
case_base = [
    {
        "case_name": "Issue #1",
        "problem": {"drain_fast": True, "app_crashing": False, "hot_phone": True},
        "solution": "Close background apps and turn off GPS"
    },
    {
        "case_name": "Issue #2",
        "problem": {"drain_fast": False, "app_crashing": True, "hot_phone": False},
        "solution": "Update apps and restart device"
    },
    {
        "case_name": "Issue #3",
        "problem": {"drain_fast": True, "app_crashing": True, "hot_phone": False},
        "solution": "Uninstall recently installed rogue app"
    }
]

# New problem
new_problem = {
    "drain_fast": True,
    "app_crashing": False,
    "hot_phone": False  
}

def check_similarity(p1, p2):
    matches = 0
    for key in p1:
        if key in p2 and p1[key] == p2[key]:
            matches += 1
    return matches / len(p1)

# Task 3B: RETRIEVE 
best_case = None
best_score = -1

for past_case in case_base:
    score = check_similarity(new_problem, past_case["problem"])
    if score > best_score:
        best_score = score
        best_case = past_case

# Task 3C: REUSE
reused_solution = best_case["solution"]

# Task 3D: REVISE 
revised_solution = "Close background apps (Phone is cool, no need to turn off GPS)"

# Task 3E: RETAIN 
new_entry = {
    "case_name": "Issue #4",
    "problem": new_problem,
    "solution": revised_solution
}
case_base.append(new_entry)

print("\n" + "=" * 35)
print("=== CASE-BASED REASONING (CBR) ===")
print("New Problem:")
for k, v in new_problem.items():
    print(f"  {k}: {v}")

print(f"\n1. RETRIEVE : Found '{best_case['case_name']}' ({best_score * 100:.0f}% match)")
print(f"2. REUSE    : {reused_solution}")
print(f"3. REVISE   : {revised_solution}")
print(f"4. RETAIN   : Stored Issue #4 into memory. Total cases now: {len(case_base)}")