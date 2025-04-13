from typing import Dict, Any, Optional
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import HuggingFacePipeline
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import os

MODEL_CHOICE = "Qwen"

MODEL_CONFIGS = {
    "Qwen": {
        # Can use Qwen/Qwen-14B-Chat for better results
        "model_name": "Qwen/Qwen-7B-Chat",
        "tokenizer_name": "Qwen/Qwen-7B-Chat"
    },
    "DeepSeek": {
        # Can use deepseek-ai/deepseek-llm-67b-chat for better results
        "model_name": "deepseek-ai/deepseek-llm-7b-chat",
        "tokenizer_name": "deepseek-ai/deepseek-llm-7b-chat"
    }
}

SUMMARY_TEMPLATE = """
You are an expert meeting assistant. Your task is to create a comprehensive summary of the following meeting transcript.
Focus on key points, decisions made, and important discussions.

TRANSCRIPT:
{transcript}

Please provide a structured summary with these sections:
1. Overview
2. Key Points
3. Action Items (with assignees if mentioned)
4. Next Steps

SUMMARY:
"""

ACTION_ITEMS_TEMPLATE = """
Extract all action items from the following meeting transcript. An action item is a task that someone committed to do.
For each action item, include:
1. The task
2. Who is responsible (if mentioned)
3. Any deadline mentioned

TRANSCRIPT:
{transcript}

ACTION ITEMS:
"""

# Initialize LLM model (will be loaded the first time it's used)
_llm_instance = None


def _get_llm_instance():
    """
    Lazy-loads the LLM model to avoid unnecessary memory usage at startup.
    Returns a LangChain-compatible LLM instance.
    """
    global _llm_instance

    if _llm_instance is None:
        model_config = MODEL_CONFIGS[MODEL_CHOICE]

        print(f"Loading {MODEL_CHOICE} model. This may take a few moments...")

        # Check if CUDA is available
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {device}")

        # Load tokenizer
        tokenizer = AutoTokenizer.from_pretrained(
            model_config["tokenizer_name"])

        # Load model with appropriate config
        model = AutoModelForCausalLM.from_pretrained(
            model_config["model_name"],
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            device_map="auto" if device == "cuda" else None,
            trust_remote_code=True  # Required for some models
        )

        # Create text generation pipeline
        text_pipeline = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=1024,
            temperature=0.1,
            top_p=0.95,
            repetition_penalty=1.15
        )

        # LangChain-compatible wrapper
        _llm_instance = HuggingFacePipeline(pipeline=text_pipeline)

        print(f"{MODEL_CHOICE} model loaded successfully")

    return _llm_instance


def generate_summary(transcript: str, language: Optional[str] = None) -> Dict[str, Any]:
    """
    Generates a structured summary of a meeting transcript using LLM.

    Args:
        transcript: The meeting transcript text
        language: Language code to customize the summarization

    Returns:
        dict: Summary with various components
    """
    # Check if transcript is long enough to summarize
    if len(transcript.split()) < 20:
        return {
            "overview": "Transcript too short for meaningful summarization.",
            "key_points": [],
            "action_items": []
        }

    try:

        llm = _get_llm_instance()

        # Truncate if the transcript is too long
        max_tokens = 6000
        words = transcript.split()
        if len(words) > max_tokens:
            print(
                f"Transcript too long ({len(words)} words), truncating to {max_tokens} words")
            transcript = " ".join(words[:max_tokens]) + \
                "... [truncated for length]"

        summary_prompt = PromptTemplate(
            input_variables=["transcript"],
            template=SUMMARY_TEMPLATE
        )
        summary_chain = LLMChain(llm=llm, prompt=summary_prompt)

        action_prompt = PromptTemplate(
            input_variables=["transcript"],
            template=ACTION_ITEMS_TEMPLATE
        )
        action_chain = LLMChain(llm=llm, prompt=action_prompt)

        # Run the chains
        print("Generating summary...")
        summary_result = summary_chain.run(transcript=transcript)

        print("Extracting action items...")
        action_result = action_chain.run(transcript=transcript)

        parts = summary_result.split("\n\n")
        overview = parts[0] if len(parts) > 0 else ""

        # Extract key points
        key_points = []
        for part in parts:
            if "Key Points" in part:
                points_text = part.split("Key Points:")[-1].strip()
                key_points = [p.strip("- ").strip()
                              for p in points_text.split("\n") if p.strip()]
                break

        action_items = []
        for line in action_result.split("\n"):
            if line.strip().startswith("-") or line.strip().startswith("*"):
                action_items.append(line.strip("- *").strip())

        return {
            "overview": overview,
            "key_points": key_points,
            "action_items": action_items,
            "full_summary": summary_result
        }

    except Exception as e:
        print(f"Error in summarization: {str(e)}")
        return {
            "overview": f"Error generating summary with {MODEL_CHOICE}.",
            "key_points": [],
            "action_items": [],
            "error": str(e)
        }
