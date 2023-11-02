import streamlit as st
import openai
import requests
import json

url = "https://stablediffusionapi.com/api/v3/text2img"

headers = {
  'Content-Type': 'application/json'
}

def page2():
    st.title("OpenAI DALL·E Image Generation")
    st.info("""#### NOTE: you can download image by \
    right clicking on the image and select save image as option""")

    with st.form(key='form'):
        prompt = st.text_input(label='Enter text prompt for image generation')
        size = st.selectbox('Select size of the images', 
                            ('256x256', '512x512', '1024x1024'))
        num_images = st.selectbox('Enter number of images to be generated', (1,2,3,4))
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if prompt:
            response = 
json.dumps({
  "key": "",
  "prompt": prompt,
  "negative_prompt": None,
  "width": "512",
  "height": "512",
  "samples": "1",
  "num_inference_steps": "20",
  "seed": None,
  "guidance_scale": 7.5,
  "safety_checker": "yes",
  "multi_lingual": "no",
  "panorama": "no",
  "self_attention": "no",
  "upscale": "no",
  "embeddings_model": null,
  "webhook": None,
  "track_id": None
})
            
            for idx in range(num_images):
                image_url = response["data"][idx]["url"]

                st.image(image_url, caption=f"Generated image: {idx+1}",
                         use_column_width=True)
