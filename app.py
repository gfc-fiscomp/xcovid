import streamlit as st
from PIL import Image
import time

#PAGE_CONFIG = {"apge_title":"TesteGFC", "page_icon":"smiley", "layuot":"centered"}
st.set_option('deprecation.showfileUploaderEncoding', False)



def main():
	st.title("Classificação de imagens usando PyTorch")
	st.header("Diagnóstico de covid a partir de Raio-X pulmonar")
	st.text("Aqui é um text")
	file = st.file_uploader("Envie o exame:", type=["jpg", "png"])
	latest_it = st.empty()
	bar = st.progress(0)
	#for i in range(100):
	#	latest_it.text(f'Etapa {i+1}/{100}')
	#	bar.progress(i+1)
	#	time.sleep(0.6)
		
	add_selectbox = st.sidebar.selectbox("Conheça o GFC", ("Email", "Github"))


if __name__ == '__main__':
  main()
