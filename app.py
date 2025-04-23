import streamlit as st 
import requests 
from markdown2 import Markdown
from bs4 import BeautifulSoup

st.set_page_config(page_title="Medical Chatbot", page_icon=":camera:", layout="wide")

st.title("Medical Chatbot with Llama")

image_col,text_col=st.columns(2)

with image_col:
    image=st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if image is not None:
        st.write("Image preview:")
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("Image uploaded successfully!")
    else:
        st.write("No image uploaded yet.")

with text_col:
    query=st.text_input("Enter your query")
    submit_button=st.button("Submit")
    
    
response_text=""
    
if submit_button:


    if image and query:
        try:
            files={"image":image}
            data={"query":str(query)}
            response=requests.post("http://localhost:8000/upload_and_query", files=files, data=data)
            if response.status_code==200:
                result=response.json()
                markdown_response =result.get("llama","No response received from Llama API.")
                markdowner = Markdown()
                html = markdowner.convert(markdown_response)
                response_text = BeautifulSoup(html, "html.parser").get_text()
                st.success("Response received successfully!")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    
    
    
st.text_area("Response",value=response_text, height=300)
