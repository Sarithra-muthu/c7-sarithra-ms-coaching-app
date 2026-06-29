import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SUBJECT_CONFIG = {
    "Maths": {
        "total": 50,
        "criteria": (
            "arithmetic (addition, subtraction, multiplication, division), "
            "fractions, decimals, percentages, ratio and proportion, "
            "basic algebra and sequences, geometry (area, perimeter, volume, angles, 2D/3D shapes), "
            "data handling (mean, mode, median, range, charts and tables), "
            "word problems and problem-solving, time, money, and measurement"
        ),
    },
    "Comprehension": {
        "total": 25,
        "criteria": (
            "literal comprehension (retrieving information directly from the text), "
            "inference (reading between the lines, deducing meaning), "
            "vocabulary in context (explaining word meanings from surrounding text), "
            "language effects (identifying and explaining the impact of the writer's word choices and techniques), "
            "summary and sequencing"
        ),
    },
    "Creative Writing": {
        "total": 20,
        "criteria": (
            "content and ideas (5 marks): originality, engagement, and relevance to the task; "
            "structure and organisation (4 marks): clear opening, development, and ending with effective paragraphing; "
            "vocabulary (5 marks): varied, ambitious, and precisely chosen words; "
            "sentence construction (3 marks): varied and controlled sentence structures; "
            "grammar and punctuation (2 marks): accurate grammar and a range of punctuation; "
            "spelling (1 mark): accurate spelling throughout"
        ),
    },
}


def analyse_work(subject: str, work_content: str) -> str:
    if subject not in SUBJECT_CONFIG:
        raise ValueError(
            f"Invalid subject '{subject}'. Must be one of: {', '.join(SUBJECT_CONFIG)}"
        )

    config = SUBJECT_CONFIG[subject]
    total = config["total"]
    criteria = config["criteria"]

    system_prompt = (
        f"You are an expert CSSE 11+ examiner marking {subject} work for 10–11 year old pupils "
        f"sitting the UK selective school entrance exam (CSSE). "
        f"You mark rigorously and honestly against official CSSE 11+ criteria. "
        f"The total marks available for this {subject} paper are {total}. "
        f"The marking criteria cover: {criteria}. "
        f"Your feedback must be specific, actionable, and pitched at the level of a Year 6 pupil and their tutor."
    )

    user_prompt = (
        f"Please analyse the following {subject} work submitted by a student.\n\n"
        f"--- STUDENT WORK ---\n{work_content}\n--- END OF WORK ---\n\n"
        f"Provide your analysis in exactly this format:\n\n"
        f"MARKS: [score] / {total}\n\n"
        f"DONE WELL:\n[Specific strengths, referencing the student's actual work]\n\n"
        f"WENT WRONG:\n[Specific errors or weaknesses, referencing the student's actual work]\n\n"
        f"STEPS TO IMPROVE:\n"
        f"1. [Concrete, actionable step]\n"
        f"2. [Concrete, actionable step]\n"
        f"3. [Concrete, actionable step]\n"
        f"[Add more steps if needed]"
    )

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    return completion.choices[0].message.content
