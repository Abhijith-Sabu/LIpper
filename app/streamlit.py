import os
import tensorflow as tf
import streamlit as st
from utils import load_data, num_to_char
from modelutil import load_model
import imageio
import subprocess
st.set_page_config(layout='wide')
# side bar setup
st.title("LIpper Full Stack")
with st.sidebar:
    st.image('fedor-PtW4RywQV4s-unsplash.jpg')
    st.title('LIpper')
    st.info('This application is originally developed by the LipNet Deeplearning model')


files=os.listdir(os.path.join('data','s1'))
selected_video= st.selectbox('Choose video',files)


# Generate columns

col1,col2 =st.columns(2)
with col1:
    st.info("Video below is converted to mp4")
    file_path = os.path.join('data','s1',selected_video)
    command = f'C:/ffmpeg/ffmpeg -i "{file_path}" -vcodec libx264 test_video.mp4 -y'
    try:
        subprocess.run(command,check=True)
        print("conversion successfull.")
    except subprocess.CalledProcessError as e:
        print("conversion unsuccessfull",e)
# Rendering video
    video = open("test_video.mp4",'rb')
    video_bytes = video.read()
    st.video(video_bytes)

with col2:
    st.info("This is what the model sees when makeing prediction.")
    video , annotations = load_data(tf.convert_to_tensor(file_path))
    imageio.mimsave("animation.gif",video,fps=10)
    st.image("animation.gif",width=400)

    st.info("The output of the model as Tokens")
    model = load_model()
    y_pred =model.predict(tf.expand_dims(video,axis=0))
    decoder = tf.keras.backend.ctc_decode(y_pred,[75],greedy=True)[0][0].numpy()
    st.text(decoder)
    
    st.info("This is tokens converted to charecters")
    st.text(tf.strings.reduce_join( num_to_char(decoder)).numpy().decode('utf-8'))

