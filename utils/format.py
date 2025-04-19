def format_transcript(raw_transcript: str) -> str:
    """
    Format a raw transcript to make it more suitable for LLM processing.
    This helps prevent hallucinations and empty arrays.
    """
    import re

    # If transcript is already well-structured, don't modify it
    if "\n\n" in raw_transcript and len(raw_transcript.split("\n")) > 5:
        return raw_transcript

    # Step 1: Try to detect if this is a single-line or poorly formatted transcript
    if raw_transcript.count("\n") < raw_transcript.count(". ") / 3:
        print("Detected single-line or poorly formatted transcript. Reformatting...")

        # Step 2: Split on potential speaker indicators
        # Common patterns like "Person:", "John:", "[John]:", "Speaker 1:" etc.
        speaker_pattern = r'(?:\n|^|\. )([A-Z][a-zA-Z\s]*|\[[^\]]+\]|Speaker\s*\d+):[ \t]'

        formatted = raw_transcript

        # If we detect speaker patterns, split on them
        if re.search(speaker_pattern, raw_transcript):
            formatted = re.sub(speaker_pattern, r'\n\n\1: ', formatted)
        else:
            # If no speaker patterns, try to split on sentences
            formatted = re.sub(r'\.(\s)', r'.\n\n', formatted)

        # Ensure consistent newlines
        formatted = re.sub(r'\n{3,}', '\n\n', formatted)

        # Clean up any trailing whitespace
        formatted = re.sub(r' +$', '', formatted, flags=re.MULTILINE)

        # print(f"Reformatted transcript from {raw_transcript.count('\n')} to {formatted.count('\n')} line breaks")
        return formatted

    return raw_transcript
