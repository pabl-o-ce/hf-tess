---
title: Chat with Tess
emoji: 🔸
colorFrom: gray
colorTo: yellow
sdk: gradio
sdk_version: 4.44.1
app_file: app.py
pinned: false
license: apache-2.0
header: mini
fullWidth: true
models:
- migtissera/Tess-R1-Limerick-Llama-3.1-70B
- migtissera/Tess-v2.5.2-Qwen2-72B
short_description: Tess-R1 is designed with test-time compute in mind, and has the capabilities to produce a Chain-of-Thought (CoT) reasoning before producing the final output.
---
# 🔸 HF-Tess

Tess-Reasoning-1 (Tess-R1) series of models. Tess-R1 is designed with test-time compute in mind, and has the capabilities to produce a Chain-of-Thought (CoT) reasoning before producing the final output.

[![Discord](https://img.shields.io/discord/123456789?color=5865F2&logo=discord&logoColor=white)](https://discord.gg/KMZ6GdkzPf)
[![Open In Spaces](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/spaces/poscye/chat-with-tess)

## 🚀 Features

- **Chain-of-Thought Reasoning**: Tess-R1 first creates a structured thought process before generating responses
- **Multiple Model Support**: 
  - Tess-R1-Limerick-Llama-3.1-70B
  - Tess-v2.5.2-Qwen2-72B
- **Optimized Performance**: Designed with test-time compute efficiency
- **Interactive Web Interface**: Built with Gradio for easy interaction
- **Customizable Parameters**:
  - Temperature control
  - Top-p and Top-k sampling
  - Maximum token length
  - Repetition penalty
  - Custom system messages

## 💻 Technical Details

### Models

1. **Tess-R1-Limerick-Llama-3.1-70B**
   - Based on Llama 3.1 70B
   - Optimized for Q3_K_L quantization
   - Uses Llama 3 chat template

2. **Tess-v2.5.2-Qwen2-72B**
   - Based on Qwen2 72B
   - Optimized for Q3_K_M quantization
   - Uses ChatML template

### Implementation

- **Backend**: Python with llama-cpp-python
- **Frontend**: Gradio
- **GPU Optimization**: 
  - Flash Attention enabled
  - 81 GPU layers
  - Batch size of 1024
  - Context window of 8192 tokens

## 🔧 Usage

### Web Interface

Visit the [HuggingFace Space](https://huggingface.co/spaces/poscye/chat-with-tess) to interact with Tess directly through your browser.


## 🛠️ Configuration Options

- **Model Selection**: Choose between Tess-R1 and Tess-v2.5.2
- **Generation Parameters**:
  - `max_tokens`: 1-4096 (default: 2048)
  - `temperature`: 0.1-4.0 (default: 0.7)
  - `top_p`: 0.1-1.0 (default: 0.95)
  - `top_k`: 0-100 (default: 40)
  - `repeat_penalty`: 0.0-2.0 (default: 1.1)

## 🤝 Contributing

Feel free to:
- Join our [Discord community](https://discord.gg/KMZ6GdkzPf)
- Report issues
- Submit pull requests
- Share your experiences

## 📜 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- Model development by [migtissera](https://github.com/migtissera)
- Built with [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- Built with [llama-cpp-agent](https://github.com/Maximilian-Winter/llama-cpp-agent)
- Hosted on [🤗 HuggingFace Spaces](https://huggingface.co/spaces)