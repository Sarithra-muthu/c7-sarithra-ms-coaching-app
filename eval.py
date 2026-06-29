from main import analyse_work

SAMPLES = {
    "Maths": (
        "1. 345 + 278 = 613\n"
        "2. 12 × 9 = 98\n"
        "3. Area of a rectangle with length 8 cm and width 5 cm = 40 cm²\n"
        "4. What is 3/4 of 48? Answer: 36\n"
        "5. A train travels 120 miles in 2 hours. Speed = 60 mph"
    ),
    "Comprehension": (
        "Passage: 'The old lighthouse stood alone on the rocky cliff, its beam sweeping "
        "the dark sea below. For fifty years it had warned sailors of the jagged rocks, "
        "but now the automated signal had made the keeper's role obsolete.'\n\n"
        "Q1. What is the purpose of the lighthouse? To warn sailors of rocks.\n"
        "Q2. Why is the keeper no longer needed? Because it is automated now.\n"
        "Q3. What does 'obsolete' mean here? Not needed anymore.\n"
        "Q4. What impression does the writer give of the lighthouse? It is sad and old."
    ),
    "Creative Writing": (
        "The Storm\n\n"
        "It was a dark and stormy night. The wind was blowing very hard. I was scared. "
        "Suddenly there was a loud bang. I went to the window and looked out. A big tree "
        "had fallen down in the garden. My mum came in and said it was okay. We had hot "
        "chocolate and watched the storm from inside. In the morning the sun came out "
        "and everything was fine. The end."
    ),
}


def main():
    for subject, work in SAMPLES.items():
        print(f"{'=' * 60}")
        print(f"SUBJECT: {subject}")
        print(f"{'=' * 60}")
        result = analyse_work(subject, work)
        print(result)
        print()


if __name__ == "__main__":
    main()
