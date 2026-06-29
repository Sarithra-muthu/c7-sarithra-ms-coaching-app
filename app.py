import os
import httpx
import gradio as gr

BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000/analyse")
SUBJECTS = ["Maths", "Comprehension", "Creative Writing"]


def analyse(subject, work_content, history):
    if not work_content.strip():
        history.append({"role": "assistant", "content": "Please paste your child's work before submitting."})
        return history, history, ""

    history.append({"role": "user", "content": f"**Subject:** {subject}\n\n{work_content}"})

    try:
        response = httpx.post(
            BACKEND_URL,
            json={"subject": subject, "work_content": work_content},
            timeout=60,
        )
        if response.status_code == 200:
            feedback = response.json()["feedback"]
        else:
            feedback = f"Server error {response.status_code}: {response.json().get('detail', 'Unknown error')}"
    except httpx.ConnectError:
        feedback = "Could not connect to the analysis server. Is the FastAPI backend running?"

    history.append({"role": "assistant", "content": feedback})
    return history, history, ""


with gr.Blocks(title="CSSE 11+ Work Analyser") as demo:
    gr.Markdown(
        "# CSSE 11+ Work Analyser\n"
        "Select a subject, paste your child's work, and receive detailed feedback."
    )

    chatbot = gr.Chatbot(label="Analysis", height=500)
    state = gr.State([])

    subject = gr.Dropdown(choices=SUBJECTS, value="Maths", label="Subject")
    work_input = gr.Textbox(
        lines=8,
        placeholder="Paste your child's work here…",
        label="Student Work",
    )

    with gr.Row():
        submit_btn = gr.Button("Analyse", variant="primary")
        clear_btn = gr.Button("Clear")

    submit_btn.click(
        fn=analyse,
        inputs=[subject, work_input, state],
        outputs=[chatbot, state, work_input],
    )
    clear_btn.click(
        fn=lambda: ([], [], ""),
        outputs=[chatbot, state, work_input],
    )


if __name__ == "__main__":
    demo.launch()
