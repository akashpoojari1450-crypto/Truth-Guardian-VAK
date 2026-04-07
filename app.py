import gradio as gr

def hunter_engine(user_input):
    if not user_input:
        return "Ready..."
    return "Verified"

def reset():
    return "reset done"

def step():
    return "step done"

with gr.Blocks() as demo:
    gr.Markdown("# Hunter Engine")

    inp = gr.Textbox(label="Input")
    out = gr.Textbox(label="Output")

    btn1 = gr.Button("Run")
    btn2 = gr.Button("Reset")
    btn3 = gr.Button("Step")

    btn1.click(hunter_engine, inp, out)
    btn2.click(lambda: "reset done", None, out)
    btn3.click(lambda: "step done", None, out)

demo.launch()
