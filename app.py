import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Know Me", page_icon="🕴️", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_bdlrkrqv.json")
lottie_ds = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_8z6ubjgk.json")
lottie_transitom = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ut2g23nx.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Siddharth Nobell :wave:")
    st.title(
    """
    A Unix Python Developer and Application Architect who has been in roles of
    - Data Engineer / Data Analyst / Data Scientist 
    - Cloud Architect 
    - Even Embedded IoT using Raspberry Pi, Arduino and ESP Boards 🤔
    """)
    st.write("Check my [Linked-in](https://www.linkedin.com/in/siddharthnobell/) | [Kaggle] (https://www.kaggle.com/siddharthnobell/) | [GitHub] (https://github.com/siddharthnobell/) | [Resume] (https://www.linkedin.com/in/siddharthnobell/overlay/1635489084350/single-media-viewer/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.header("What I do")
        #st.write("##")
        st.write(
            """
            From past one year I am working on healthcare NLP projects and their Architectures with Cloud Deployments  
            - Created and deployed NLP projects that classify free texts into business needs (risky, claims like spam or ham, etc.) 
            - Topic modeling and text summarization  
            - Named entity recognition (disease, phenotypes, chemicals, organisms, etc.)
            - Hidden trend extraction for free texts repositories 
            - Context Search engine and Cloud Deployment   
            - These projects are developed on azure ml studio / azure databricks and jupyter notebooks   
            If this sounds interesting to you, ping me over [linkedin](https://www.linkedin.com/in/siddharthnobell/). 
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="what-i-do")
        st.write("#Python  #NLTK  #Spacy #SciSpacy  #BertTopic  #Bert #BioPython  #Medline #SpacyBioModels")

# ---- What is used to do ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.header("What I used to do")
        #st.write("##")
        st.write(
            """
            From April 2019 to June 2021, I was leading Cleair [Enviome Research Pvt. Limited]   
            - Practically measuring pollution using smart autonomous low-cost devices and using data science to predict hyperlocal air pollution
            - Creating IoT device prototypes   
            - Creating backend application with Geospatial endpoints 
            - Data ingestion pipelines from open apis and IoT Devices 
            - Error correction and Spatial dispersion models 
            - This all being developed on AWS using AWS Sagemaker and other AWS Services (mainly Sagemaker and EC2 was the backbone)

            This was one of the most interesting work I have done till now.
            """
        )
    with right_column:
        st_lottie(lottie_ds, height=300, key="what-i-used-to-do")
        st.write("#Python  #IDW #GreenRoutes #Flask  #Ngnix #redis #celery #GeoPandas  #Folium  #Pandas #RandomForrest  #Seaborn #Unix")
    

# ---- Previously ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.header("Previously")
        #st.write("##")
        st.write(
            """
            Previous to April 2019 I was associated with Ideationts and Cognizant where I worked on various assignments, few are as below   
            - Utility load prediction for US power sector using weather data 
            - Viewership Prediction for BARC, India    
            - Demand and Supply Prediction, RateGain India 
            - Go-Jek Demand and Forecast, Go-Jek (Indonesia) 
            - and Various other data warehousing and data migration projects   

            This was the time when I moved into python from SAS and started to work in the field of data science and data entirely. Data analysis, Data Science and Data Engineering was part of day to day activities.
            """
        )
    with right_column:
        st_lottie(lottie_transitom, height=300, key="Previously")
        st.write("#Python  #SAS  #XGBoost #fbProphet #  #Folium  #Pandas #RandomForrest  #Seaborn #Unix")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/a76f6e2c9416121d1aa5b7093e4de152" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
