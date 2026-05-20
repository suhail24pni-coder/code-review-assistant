import sys
from code_review_assistant.crew import CodeReviewAssistantCrew

def run():
    """
    Run the crew.
    """
    # Example code snippet with a bug (mutable default argument) and a very long line
    sample_code = """
def process_user_data(name, age, items=[]):
    print(f"Processing data for user: {name} who is currently {age} years old and enjoys programming heavily.")
    items.append(name)
    return {"user": name, "age": age, "items": items}
"""

    inputs = {
        'code_input': sample_code
    }
    
    print("🚀 Initiating Code Review Crew...")
    CodeReviewAssistantCrew().crew().kickoff(inputs=inputs)
    print("✅ Review complete! Check 'code_review.md' for the output.")

if __name__ == "__main__":
    run()