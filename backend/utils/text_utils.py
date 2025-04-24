import re

def extract_characters_and_topic(prompt: str):
    """
    Extracts two character names and a topic from the user prompt.
    E.g. "Batman and Elsa discuss AI in a coffee shop"
    returns (["Batman", "Elsa"], "AI")
    """
    # Very simple heuristic parser
    char_pattern = re.findall(r"([A-Z][a-zA-Z]+)", prompt)
    if len(char_pattern) >= 2:
        characters = char_pattern[:2]
    else:
        characters = ["Character A", "Character B"]

    # Try to extract the topic (simple version: everything after "about" or "discuss")
    topic_match = re.search(r"(?:about|discuss|talk about) (.+)", prompt, re.IGNORECASE)
    topic = topic_match.group(1).strip() if topic_match else "a mysterious topic"

    return characters, topic
