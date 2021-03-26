import streamlit as st
from PIL import Image
import time
import base64
import pandas as pd
import numpy as np 
st.set_page_config(page_title="GFC-FiscomP", page_icon="💻️", layout="centered")
#PAGE_CONFIG = {"apge_title":"TesteGFC", "page_icon":"smiley", "layuot":"centered"}
st.set_option('deprecation.showfileUploaderEncoding', False)





def main():
	menu = ["Página Inicial", "Teste", "Sobre"]
	choice = st.sidebar.selectbox("Menu", menu)
	if choice == "Página Inicial":
		st.title("Página Inicial:")
		st.header("WebApp criado para o primeiro SCITEK + Datathon 2021")
		st.subheader("Projeto de diagnóstico de COVID-19 atráves de Raio-X Pulmonar usando Redes Neurais Convolucionais.")
		st.button("Navegue pelas abas na seção à esquerda.")
		#logo = Image.open("/home/mgteus/Datathon/xcovid/logoGFCNormal.png")
		#st.image(logo, width=120)
		st.text("")
		st.text("")
		st.text("")
		st.text("Oferecimento:")
		col1, col2 = st.beta_columns(2)
		#col1.markdown("![LogoGIF](https://media.giphy.com/media/4MXP8s6bSQC9LmMwme/giphy.gif)")
		col1.image("https://media.giphy.com/media/4MXP8s6bSQC9LmMwme/giphy.gif", width=300, caption="Ref:https://media.giphy.com/media/4MXP8s6bSQC9LmMwme/giphy.gif" )
		col2.markdown("**IMAGEM POATEK SCITEK DATATHON SEI LA**")

		
		
		
		

	elif choice == "Teste":
		st.title("Classificação de imagens usando Redes Neurais Convolucionais")
		st.header("Diagnóstico de COVID a partir de Raio-X pulmonar")
		file = st.file_uploader("Envie aqui o raio-x:", type=["jpg", "png"])
		bot = st.button("Enviar")
		if file is not None:
			image = Image.open(file)
			st.image(image, caption="Arquivo enviado", use_column_width=True)
			st.write("")
			st.write("Classificando...")
			latest_it = st.empty()
			bar = st.progress(0)
			for i in range(100):
				latest_it.text(f'Etapa {i+1}/100')
				bar.progress(i+1)
				time.sleep(0.1)
			st.success("Parabéns você enviou uma foto!")
			
				
			
		else: 
			st.warning("Exame não enviado.")
		
	elif choice == "Sobre":
		st.title("Sobre:")
		st.header("Conheça o GFC:")
		st.subheader("Grupo de Física Computacional é um grupo de alunos de graduação em Física interessados na área de Física Computacional. Desenvolvem projetos, participam de competições e se reunem semanalmente para discutir pesquisas e artigos.")
		c1, c2 = st.beta_columns(2)
		c1.subheader("GitHub: ")
		c1.markdown("Todos os arquivos usados no classificador quanto na produção e deploy do projeto estão disponíveis no nosso github.")
		c1.info("https://github.com/gfc-fiscomp/xcovid")
		
		c2.subheader("Email")
		c2.markdown("Não hesite em mandar um email caso tenha alguma dúvida.")
		c2.info("gfc.fiscomp@gmail.com")
		
		
	contact = ["Email", "GitHub"]
	#choice2 = st.sidebar.selectbox("Contato", contact)
	#if choice2 == "Email":
	#	st.title("Email:")
#		st.header("gfc.fiscomp@gmail.com")
#		st.subheader("Não hesite em mandar um email caso tenha alguma dúvida.")
#	elif choice2 == "GitHub":
#		st.title("GitHub:")
#		st.header("https://github.com/gfc-fiscomp/xcovid")
#		st.subheader("Todos os arquivos usados no classificador quanto na produção e deploy do projeto estão disponíveis no nosso github.")
		



if __name__ == '__main__':
  main()


#-------------BAGUNÇA----------------
	#latest_it = st.empty()
	#bar = st.progress(0)
	#for i in range(100):
	#	latest_it.text(f'Etapa {i+1}/{100}')
	#	bar.progress(i+1)
	#	time.sleep(0.6)


