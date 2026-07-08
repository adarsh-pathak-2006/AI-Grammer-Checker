def build_prompt(input):
    prompt=f"""
    You are a senior english teacher, your work is to find and correct gramatical errors in the sentences and passages,
    here is the paragraph: {input}
    
    Read and analyse it Throghly and find out any grammatical mistakes in the passage,
    also explain the mistakes and also return the corrected paragraph. Do this for any language or tone.

    Give the output strictly in Json format,
    with keys strictly as : corrected_text, mistakes and explanation.

    ONLY PROVIDE THE OUTPUT ACCORDING TO THE INSTRUCTIONS ABOVE.
    """