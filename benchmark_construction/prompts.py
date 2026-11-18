# Enrichment step 3.3:

def get_facts_freestyle(source, image_path):
    # this prompt is also conditioned on the image generated from source
    prompt = f"""
    You are an image-to-text expert.

    You will be given an image and the image caption.

    Your goal is to write a list of 10 visual details in the image that are not mentioned in the caption but are consistent with it.

    These details should be things that a human might notice if they closely analyzed the image, but that are not important enough to be included in the caption.

    Keep the details highly detailed and diverse.

    Output Format:
    - Return a list of 10 bullet points.
    - Do not include explanations or extra text.
    - Keep the text under 15 words per bullet point.
    - Grammar must be natrual, the sentence should be complete and not a fragment.

    Hard Constraints:
    - You must be very careful not to include any details that will be extremely salient in the image or will drastically change it.
    - Avoid any details related to image style. 

    Caption:
    {source}
    """

    return prompt




def get_facts_guided(source, image_path):
        # this prompt is also conditioned on the image generated from source
    prompt = f"""
    You are an image-to-text expert.

    You will be given an image and the image caption.

    Your goal is to write a list of 20 visual details in the image that are not mentioned in the caption but are consistent with it.

    These details should be things that a human might notice if they closely analyzed the image, but that are not important enough to be included in the caption.

    Keep the details highly detailed and diverse.

    You must do 4 details of each of the following categories:
    1. Details that focus on colors, hues and textures
    2. Details that focus on exact placement, sizes and quantities of elements.
    3. Details that focus on texts/labels/digits etc.
    4. Details that focus on scene specific minor details (e.g, for an image of a dog - detail its paw pads, for an image of a potted plant, detail a stain on the pot, etc.)
    5. Details that focus on unvizualizable or overly poetic descriptions of the scene (e.g., "the girl's hair is the color of lightly roasted Brazil nuts", "the trees look as if they had stood there a long while", "a gentle breeze lingers in the air, adding a sense of tranquility" etc.)

    Output Format:
    - Return a list of 20 bullet points with the category label above each category (1-5).
    - Do not include explanations or extra text.
    - Keep the text under 15 words per bullet point.
    - Grammar must be natrual, the sentence should be complete and not a fragment.

    Hard Constraints:
    - You must be very careful not to include any details that will be extremely salient in the image or will drastically change it.
    - Avoid any details related to image style. 
    - Each detail must stand on its own and not be dependent on another detail.
    - If there are no texts/labels/digits in the  image, write None for category 3.

    Caption:
    {source}
    """
    return prompt



# filtering step 3.4:

def filter_facts(source, completions):
    prompt = f"""
    You are an image understanding assistant.

    You will be given an image caption and a list of possible completions.

    Return only the completions that **directly and explicitly contradict** the caption.

    A contradiction means both statements cannot be true about the same image.

    Do NOT return completions that:

    * only add new information,
    * are merely unlikely or surprising,
    * cannot be verified from the caption,
    * are not mentioned in the caption.

    Treat the caption as incomplete. Missing information is NOT a contradiction.

    If you are unsure, do not return the completion.

    Caption:
    {source}

    Possible completions:
    {completions}

    Return only a Python list containing the contradictory completions. Return [] if none.
    """
    return prompt




# paraphrasing step 3.5:

rules = [
    "Paraphrase the first sentence.",
    "Change the order inside the first sentence.",
    "Change the order of the first two sentences. Then merge them.",
    "Merge the last two sentences and change their order.",
    "Merge the first two sentences.",
    "Merge the last two sentences.",
    "Change synonyms.",
    "Make the sentence 10 words longer.",
    "Make the sentence 5 words longer.",
]


def write_paraphrase(source, rule):
    prompt = f"""
    You will be given an image caption and a grammar rule.

    Your goal is to paraphrase the caption in a way that is consistent with the grammar rule, while keeping the visual meaning of the caption the exact same.

    Hard rule: the visual meaning must not change at all

    You must strictly follow the grammar rule.


    Caption:
    {source}

    Grammar rule:
    {rule}
    """

    return prompt