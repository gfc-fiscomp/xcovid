import streamlit as st
from PIL import Image
import time
st.set_page_config(page_title="GFC-FiscomP", page_icon="💻️", layout="centered")
#PAGE_CONFIG = {"apge_title":"TesteGFC", "page_icon":"smiley", "layuot":"centered"}
st.set_option('deprecation.showfileUploaderEncoding', False)





def main():
	menu = ["Página Inicial", "Teste", "Sobre"]
	choice = st.sidebar.selectbox("Menu", menu)
	if choice == "Página Inicial":
		st.title("Página Inicial:")
		st.header("WebApp criado para o primeiro SCITEK + Datathon 2021")
		st.subheader("Navegue pelas abas na seção à esquerda.")

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
		st.header("Conheça o GFC")
		c1, c2 = st.beta_columns(2)
		c1.write("Email")
		c2.info("GitHub")
		
		
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


