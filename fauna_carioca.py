import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.image("Fauna.png", caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

df = pd.read_excel('fauna_carioca_rev.xlsx')

col1, col2 = st.columns(2)
tab1, tab2, tab3, tab4 = st.tabs(["Nome científico", "Nome comum", "Estado de Conservação", "Gráfico de Conservação"])

with col1:
   option1 = st.selectbox(
   "Escolha o seu municipio: ",
   ('Angra Dos Reis', 'Araruama', 'Areal', 'Armacao Dos Buzios', 'Arraial Do Cabo', 'Barra Do Pirai', 'Barra Mansa', 'Belford Roxo', 'Bom Jesus Do Itabapoana', 'Cabo Frio', 'Cachoeiras De Macacu', 'Cambuci', 'Campos Dos Goytacazes', 'Cantagalo', 'Carapebus', 'Carmo', 'Casimiro De Abreu', 'Comendador Levy Gasparian', 'Conceicao De Macabu', 'Cordeiro', 'Duas Barras', 'Duque De Caxias', 'Engenheiro Paulo De Frontin', 'Guapimirim', 'Iguaba Grande', 'Itaborai', 'Itaguai', 'Itaocara', 'Itaperuna', 'Itatiaia', 'Japeri', 'Laje Do Muriae', 'Macae', 'Macuco', 'Mage', 'Mangaratiba', 'Marica', 'Mendes', 'Miguel Pereira', 'Miracema', 'Natividade', 'Niteroi', 'Nova Friburgo', 'Nova Iguacu', 'Paracambi', 'Paraiba Do Sul', 'Parati', 'Petropolis', 'Pinheiral', 'Pirai', 'Porciuncula', 'Porto Real', 'Quatis', 'Quissama', 'Resende', 'Rio Claro', 'Rio Das Flores', 'Rio Das Ostras', 'Rio De Janeiro', 'Santa Maria Madalena', 'Santo Antonio De Padua', 'Sao Fidelis', 'Sao Francisco De Itabapoana', 'Sao Goncalo', 'Sao Joao Da Barra', 'Sao Jose De Uba', 'Sao Jose Do Vale Do Rio Preto', 'Sao Pedro Da Aldeia', 'Sao Sebastiao Do Alto', 'Sapucaia', 'Saquarema', 'Seropedica', 'Silva Jardim', 'Sumidouro', 'Teresopolis', 'Trajano De Morais', 'Tres Rios', 'Valenca', 'Varre-Sai', 'Vassouras', 'Volta Redonda'),
   index=None)
   st.write("Você escolheu:", option1)

with tab1:
    filtered_df = df[df['Municipio'] == option1]
    unique_species = filtered_df['Nome cientifico'].drop_duplicates().sort_values()
    for specie in unique_species:
       st.subheader(f"{specie}")
       
with tab2: 
    filtered_df = df[df['Municipio'] == option1]
    unique_names = filtered_df['Nome comum'].drop_duplicates().sort_values()
    unique_names = unique_names[unique_names != "Sem Informações"]
    for name in unique_names:
        common_name = name.lower()
        st.subheader(f"{name}")

with tab3:
    option2 = st.selectbox(
        "Escolha as espécies pelo seu estado de conservação:",
        ('Espécie Ameaçada', 'Espécie não Ameaçada'),
        index=None)
    st.write("Você escolheu:", option2)
    filtered_df = df[(df['Municipio'] == option1) & (df['Estado de conservacao'] == option2)]
    unique_species = filtered_df[['Nome cientifico', 'Nome comum']].drop_duplicates().sort_values(by='Nome cientifico')
    for _, row in unique_species.iterrows():
        scientific_name = row['Nome cientifico']
        common_name = row['Nome comum']
        st.subheader(f"{scientific_name}")
        st.write(f"Nome Comum: {common_name}")

with tab4: 
    filtered_df = df[df['Municipio'] == option1]
    species_count = filtered_df['Nome cientifico'].nunique()
    total_species_count = df['Nome cientifico'].nunique()
   
    labels = ['Espécie Ameaçada', 'Espécie não Ameaçada']
    sizes = [species_count, total_species_count - species_count] 
    colors = ['lightcoral', 'lightskyblue']
    explode = (0.1, 0)
   
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')

    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

