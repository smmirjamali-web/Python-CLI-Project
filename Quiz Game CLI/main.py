import json
import os


def load_questions():
    if not os.path.exists("questions.json"):
        print("questions.json not found.")
        print("Creating a sample file...")

        sample_questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Berlin", "Paris", "Madrid"],
                "answer_index": 2
            }
        ]
        with open("questions.json", "w") as f:
            json.dump(sample_questions, f, indent=4)

        return sample_questions

    try:
        with open('questions.json') as f:
            questions = json.load(f)
            if not isinstance(questions, list):
                raise ValueError("JSON structure must be a list")

            return questions
    except json.JSONDecodeError:
        print("json file is invalid")
        print("a new file is created")

        sample_questions = [
            {
                "question": "What is 2 + 2?",
                "options": ["1", "2", "3", "4", "5"],
                "answer_index": 3
            }
        ]
        with open("Questions.json", "w") as f:
            json.dump(sample_questions, f, indent=4)

        return sample_questions

    except Exception as e:
        print("An unexpected error occurred:", e)
        return []


def run_quiz(questions):
    score = 0

    for q in questions:
        print("\n" + q['question'])

        for i, option in enumerate(q['options'], start=1):
            print(f"{i}. {option}")

        try:
            choice = int(input("\nYour Answer: ")) - 1
        except ValueError:
            print("Invalid answer.")
            continue

        if choice == q['answer_index']:
            print("correct answer")
            score += 1
        else:
            correct = q['options'][q['answer_index']]
            print(f"Wrong answer. Correct answer: {correct}")

    total_questions = len(questions)
    wrong_answers = total_questions - score
    percentage = (score / total_questions) * 100

    print("\n" + "=" * 30)
    print("Quiz Finished!")
    print(f"Correct Answer: {score}")
    print(f"Wrong Answer: {wrong_answers}")
    print(f"Final Score: {score}/{total_questions}")
    print(f"percentage: {percentage:.1f}%")
    print("=" * 30)


def main():
    questions = load_questions()

    if not questions:
        return
    run_quiz(questions)


if __name__ == '__main__':
    main()
