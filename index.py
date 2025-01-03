from keras.models import Model
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.models import load_model
from PIL import Image
import streamlit as st
import pickle

# Tambahkan CSS untuk menengahkan judul
st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
    }
    </style>
    <div class="centered-title">Spam or Ham</div>
    """,
    unsafe_allow_html=True,
)

max_words = 1000
max_len = 150
model = load_model('model.h5')

# Membuat container untuk memposisikan gambar di tengah
col1, col2, col3 = st.columns(3)
with col2:  # Menempatkan gambar di kolom tengah
    image = Image.open('./Meta/spam.png').resize((200, 200))
    st.image(image, use_column_width=True)

sample_texts = st.text_input('Enter text you want to classify: ')

with open('tokenizer.pickle', 'rb') as handle:
    tok = pickle.load(handle)

txts = tok.texts_to_sequences([sample_texts])
txts = pad_sequences(txts, maxlen=max_len)
preds = model.predict(txts)

if st.button('Predict'):
    if(preds <= 0.2):
        st.success("Ham")
    else:
        st.error("Spam")
