# -*- coding: utf-8 -*-
"""GRADIO: GPT-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o_-QIR8yVphfnbNZGYemyEr111CHHxSv

## Using Gradio to wrap a text to text interface around GPT-2 

Check out the library on [github](https://github.com/gradio-app/gradio-UI) and see the [getting started](https://gradio.app/getting_started.html) page for more demos.

### Installs and Imports
"""

!pip install -q gradio
!pip install -q git+https://github.com/huggingface/transformers.git

import gradio as gr
import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

pip freeze > requirements.txt

"""### Loading the model and creating the generate function

Note: You can also change `gpt2` to `gpt2-xl` for a much more powerful model!
"""

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = TFGPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)

def generate_text(inp):
    input_ids = tokenizer.encode(inp, return_tensors='tf')
    beam_output = model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)
    output = tokenizer.decode(beam_output[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return ".".join(output.split(".")[:-1]) + "."

"""###Creating the interface and launching!"""

output_text = gr.outputs.Textbox()
gr.Interface(generate_text,"textbox", output_text, title="GPT-2",
             description="OpenAI's GPT-2 is an unsupervised language model that \
             can generate coherent text. Go ahead and input a sentence and see what it completes \
             it with! Takes around 20s to run.").launch()

"""#### The model is now live on the gradio.app link shown above. Go ahead and open that in a new tab!

Please contact us [here](mailto:team@gradio.app) if you have any questions, or [open an issue](https://github.com/gradio-app/gradio-UI/issues/new/choose) at our github repo.
"""