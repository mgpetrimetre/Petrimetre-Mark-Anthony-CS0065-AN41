#Set cases
case_base = [
    {
        "problem": {"topic": "tones", "error_pattern": "confusing tone 2 (rising) and tone 3 (falling-rising)", "level": "beginner"},
        "solution": {"feedback": "Watch the Tone 2 vs Tone 3 comparison video and practice shadowing audio clips.", "practice_items": 5}
    },
    {
        "problem": {"topic": "characters", "error_pattern": "wrong stroke order (right to left)", "level": "beginner"},
        "solution": {"feedback": "Review the golden rule of characters: Top to bottom, left to right. Trace the provided worksheet.", "practice_items": 3}
    },
    {
        "problem": {"topic": "pinyin", "error_pattern": "confusing 'zh' and 'z' sounds", "level": "intermediate"},
        "solution": {"feedback": "Check your tongue placement. 'zh' requires curling the tongue back, 'z' is flat behind the teeth.", "practice_items": 4}
    },
    {
        "problem": {"topic": "grammar", "error_pattern": "forgetting measure words", "level": "beginner"},
        "solution": {"feedback": "Numbers and nouns must always be connected by a measure word (e.g., 'yi ge ren'). Review the common measure words chart.", "practice_items": 6}
    },
    {
        "problem": {"topic": "pinyin", "error_pattern": "struggling with the 'ü' sound", "level": "beginner"},
        "solution": {"feedback": "Say the English 'ee' sound, hold it, and round your lips like you are whistling. Practice with 'nü' and 'lü'.", "practice_items": 5}
    },
    {
        "problem": {"topic": "characters", "error_pattern": "confusing similar characters (e.g., 我 and 找)", "level": "intermediate"},
        "solution": {"feedback": "Pay close attention to the radicals. '找' (to find) has the hand radical on the left, which implies an action.", "practice_items": 4}
    }
]


#Similarity Assessment
def retrieve_similar_case(new_problem):
    best_case = None
    highest_score = -1
    
    for case in case_base:
        score = 0
        # Give higher weight if the specific error pattern matches
        if case["problem"]["error_pattern"] == new_problem["error_pattern"]:
            score += 3
        if case["problem"]["topic"] == new_problem["topic"]:
            score += 2
        if case["problem"]["level"] == new_problem["level"]:
            score += 1
            
        if score > highest_score:
            highest_score = score
            best_case = case
            
    return best_case


#Adapt Retrieved Solution 
def adapt_solution(old_solution, new_prob):
    adapted = old_solution.copy()
    
    if new_prob["level"] == "absolute_beginner":
        adapted["practice_items"] += 5
        adapted["feedback"] += " Also, review the basic Pinyin chart introduction before attempting the exercises."
    
    return adapted


#Main interactive loop
print("--- CBR Intelligent Tutoring System: Mandarin Chinese ---")

while True:
    print(f"\nCurrent Case Base Size: {len(case_base)}")
    
    new_student_problem = {
        "topic": input("Topic (grammar, tones, characters, pinyin): ").strip().lower(), 
        "error_pattern": input("Specific error pattern: ").strip().lower(), 
        "level": input("Proficiency level (e.g., beginner, absolute_beginner, intermediate): ").strip().lower()
    }

    print(f"\nNew Student Issue: {new_student_problem}\n")

    #Retrieve Step
    matched_case = retrieve_similar_case(new_student_problem)
    print(f"Retrieved Past Problem: {matched_case['problem']}")
    print(f"Original Solution: {matched_case['solution']}\n")

    #Adapt Step 
    final_solution = adapt_solution(matched_case["solution"], new_student_problem)
    print(f"Adapted Solution for New Student: {final_solution}\n")

    #Retain Step
    new_case = {
        "problem": new_student_problem,
        "solution": final_solution
    }
    case_base.append(new_case)

    print("--- Retain Stage ---")
    print(f"New case learned and stored! Total cases in Knowledge Base: {len(case_base)}\n")

    #Prompt user to continue or exit
    repeat = input("Do you want to enter another student issue? (yes/no): ").strip().lower()
    if repeat not in ["yes", "y"]:
        print("\nExiting system. Final case base count:", len(case_base))
        break