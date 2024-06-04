import streamlit as st
import pandas as pd

df = pd.read_excel('fauna_carioca_rev.xlsx')

col1, col2 = st.columns(2)

with col1:
   option1 = st.selectbox(
   "Escolha o seu municipio: ",
   ('Angra Dos Reis', 'Araruama', 'Areal', 'Armacao Dos Buzios', 'Arraial Do Cabo', 'Barra Do Pirai', 'Barra Mansa', 'Belford Roxo', 'Bom Jesus Do Itabapoana', 'Cabo Frio', 'Cachoeiras De Macacu', 'Cambuci', 'Campos Dos Goytacazes', 'Cantagalo', 'Carapebus', 'Carmo', 'Casimiro De Abreu', 'Comendador Levy Gasparian', 'Conceicao De Macabu', 'Cordeiro', 'Duas Barras', 'Duque De Caxias', 'Engenheiro Paulo De Frontin', 'Guapimirim', 'Iguaba Grande', 'Itaborai', 'Itaguai', 'Itaocara', 'Itaperuna', 'Itatiaia', 'Japeri', 'Laje Do Muriae', 'Macae', 'Macuco', 'Mage', 'Mangaratiba', 'Marica', 'Mendes', 'Miguel Pereira', 'Miracema', 'Natividade', 'Niteroi', 'Nova Friburgo', 'Nova Iguacu', 'Paracambi', 'Paraiba Do Sul', 'Parati', 'Petropolis', 'Pinheiral', 'Pirai', 'Porciuncula', 'Porto Real', 'Quatis', 'Quissama', 'Resende', 'Rio Claro', 'Rio Das Flores', 'Rio Das Ostras', 'Rio De Janeiro', 'Santa Maria Madalena', 'Santo Antonio De Padua', 'Sao Fidelis', 'Sao Francisco De Itabapoana', 'Sao Goncalo', 'Sao Joao Da Barra', 'Sao Jose De Uba', 'Sao Jose Do Vale Do Rio Preto', 'Sao Pedro Da Aldeia', 'Sao Sebastiao Do Alto', 'Sapucaia', 'Saquarema', 'Seropedica', 'Silva Jardim', 'Sumidouro', 'Teresopolis', 'Trajano De Morais', 'Tres Rios', 'Valenca', 'Varre-Sai', 'Vassouras', 'Volta Redonda'),
   index=None)
   st.write("Você escolheu:", option1)

with col2:
   filtered_df = df[df['Municipio'] == option1]
   result = filtered_df['Nome cientifico']
   unique_results = result.drop_duplicates()
   for column in result.columns:
      li = result[column].tolist()
      listaOrdenada = sorted(li)
   st.write(listaOrdenada)

        
