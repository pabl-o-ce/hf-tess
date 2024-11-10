from llama_cpp_agent import MessagesFormatterType

def get_messages_formatter_type(model_name):
    if "Tess-R1" in model_name:
        return MessagesFormatterType.LLAMA_3
    if "Tess-v2.5" in model_name:
        return MessagesFormatterType.CHATML
    else:
        raise ValueError(f"Unsupported model: {model_name}")