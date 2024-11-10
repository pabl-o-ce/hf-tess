import spaces
import json
import subprocess
from llama_cpp import Llama
from llama_cpp_agent import LlamaCppAgent
from llama_cpp_agent.providers import LlamaCppPythonProvider
from llama_cpp_agent.chat_history import BasicChatHistory
from llama_cpp_agent.chat_history.messages import Roles
import gradio as gr
from huggingface_hub import hf_hub_download
from utils.ui import css, PLACEHOLDER
from utils.settings import get_messages_formatter_type

llm = None
llm_model = None

hf_hub_download(
    repo_id="bartowski/Tess-v2.5.2-Qwen2-72B-GGUF",
    filename="Tess-v2.5.2-Qwen2-72B-Q3_K_M.gguf",
    local_dir = "./models"
)
hf_hub_download(
    repo_id="bartowski/Tess-R1-Limerick-Llama-3.1-70B-GGUF",
    filename="Tess-R1-Limerick-Llama-3.1-70B-Q3_K_L.gguf",
    local_dir = "./models"
)

@spaces.GPU(duration=120)
def respond(
    message,
    history: list[tuple[str, str]],
    model,
    system_message,
    max_tokens,
    temperature,
    top_p,
    top_k,
    repeat_penalty,
):
    global llm
    global llm_model
    chat_template = get_messages_formatter_type(model)
    if llm is None or llm_model != model:
        llm = Llama(
            model_path=f"./models/{model}",
            flash_attn=True,
            n_gpu_layers=81,
            n_batch=1024,
            n_ctx=8192,
        )
        llm_model = model
    provider = LlamaCppPythonProvider(llm)

    agent = LlamaCppAgent(
        provider,
        system_prompt=f"{system_message}",
        predefined_messages_formatter_type=chat_template,
        debug_output=True
    )

    settings = provider.get_provider_default_settings()
    settings.temperature = temperature
    settings.top_k = top_k
    settings.top_p = top_p
    settings.max_tokens = max_tokens
    settings.repeat_penalty = repeat_penalty
    settings.stream = True

    messages = BasicChatHistory()

    for msn in history:
        user = {
            'role': Roles.user,
            'content': msn[0]
        }
        assistant = {
            'role': Roles.assistant,
            'content': msn[1]
        }
        messages.add_message(user)
        messages.add_message(assistant)

    stream = agent.get_chat_response(
        message,
        llm_sampling_settings=settings,
        chat_history=messages,
        returns_streaming_generator=True,
        print_output=False
    )

    outputs = ""
    for output in stream:
        outputs += output
        yield outputs

demo = gr.ChatInterface(
    respond,
    additional_inputs=[
        gr.Dropdown([
                'Tess-v2.5.2-Qwen2-72B-Q3_K_M.gguf',
                'Tess-R1-Limerick-Llama-3.1-70B-Q3_K_L.gguf'
            ],
            value="Tess-R1-Limerick-Llama-3.1-70B-Q3_K_L.gguf",
            label="Model"
        ),
        gr.Textbox(
            value="You are Tess-R1, an advanced AI that was created for complex reasoning. Given a user query, you are able to first create a Chain-of-Thought (CoT) reasoning. Once the CoT is devised, you then proceed to first think about how to answer. While doing this, you have the capability to contemplate on the thought, and also provide alternatives. Once the CoT steps have been thought through, you then respond by creating the final output.",
            label="System message"
        ),
        gr.Slider(
            minimum=1,
            maximum=4096,
            value=2048,
            step=1,
            label="Max tokens"
        ),
        gr.Slider(
            minimum=0.1,
            maximum=4.0,
            value=0.7,
            step=0.1,
            label="Temperature"
        ),
        gr.Slider(
            minimum=0.1,
            maximum=1.0,
            value=0.95,
            step=0.05,
            label="Top-p",
        ),
        gr.Slider(
            minimum=0,
            maximum=100,
            value=40,
            step=1,
            label="Top-k",
        ),
        gr.Slider(
            minimum=0.0,
            maximum=2.0,
            value=1.1,
            step=0.1,
            label="Repetition penalty",
        ),
    ],
    theme=gr.themes.Base(
        primary_hue="amber",
        secondary_hue="yellow",
        neutral_hue="gray",
        font=[
            gr.themes.GoogleFont("Exo"),
            "ui-sans-serif",
            "system-ui",
            "sans-serif"
        ]).set(
            body_background_fill_dark="#09090b",
            block_background_fill_dark="#09090b",
            block_border_width="1px",
            block_title_background_fill_dark="#09090b",
            input_background_fill_dark="#171618",
            button_secondary_background_fill_dark="#171618",
            border_color_accent_dark="#2e1c00",
            border_color_primary_dark="#2e1c00",
            background_fill_secondary_dark="#09090b",
            color_accent_soft_dark="transparent",
            code_background_fill_dark="#171618",
        ),
    css=css,
    # retry_btn="Retry",
    # undo_btn="Undo",
    # clear_btn="Clear",
    # submit_btn="Send",
    description="Llama-cpp-agent: Chat with Tess",
    chatbot=gr.Chatbot(
        scale=1,
        placeholder=PLACEHOLDER,
        # likeable=False,
        sanitize_html=False,
        show_copy_button=True
    )
)

if __name__ == "__main__":
    demo.launch()
