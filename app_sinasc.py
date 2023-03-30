import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
sns.set()  

def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index,aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index,aggfunc=func).unstack().plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index,aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    st.pyplot(fig=plt)
    return None

st.set_page_config (layout= 'wide', 
                    page_title ='Sinasc Rôndonia - 2019',
                    initial_sidebar_state="expanded",
                    menu_items={ 
         'Get Help': 'https://www.linkedin.com/in/sandra-lin-costa-894a05174/',
         'Report a bug': "https://github.com/sannlin9/Streamlit-app/issues",
        'About': "# Este aplicativo foi criado como projeto por Sandra Lin Costa!"},
                    page_icon= 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQwAAAC8CAMAAAC672BgAAAA/1BMVEUAJYAAmUzz5xj///8AAIb+8QAAk08AlE4Al0397BIAmE0AAHcAIn/26BcAAHjz5gAAHH0AEXoAGXwAFnzo4xsAD3rv8fYAB3kAlEIAkTrZ3SFNXJr19/oABXjJzt////u2zi3c3+oZM4cgOImXnsDl5/CfpsU8TpOnrspTYp23vNNibqRrdqh0f63Lz99/iLIAAG3//+X06TT48ZP8+tb373z27GL69bL+/fFOrGn585748InC1Cl6uDwln0mWwjVEp0Vhr0AuQ46LlLpAUZR8vonk8eCezqW627xotnz7+MXR59GHw5MuolfB4MxlslGJvTg3o0elyDFUq0JztT009KpLAAAHDklEQVR4nO2baVvaTBSGA3lfICRhCaKgSKVFBETUVlvtXmmr3evy/39LB0KEJAeyzZJM5v7YANfk7jl5nOREkgQCgUAgEAgEAoFAIBAIBAKBQCAQCAQCgSBBaBrrFcQH7eqZsGFR63ZrrNcQG9ROR2W9hrigPZXlp6JPTKoTWZ5UWa8iJqgdWRZ9YqI9kxEiT2ZUu1MZXdEnU9T9qYx90SeIypU846rCeiUxoN4zZfTqrFcSA9RNU8am6BOpciDPORB9Uu9bMvqiT6wuEX2CumRHfmQn7X2y1V/I6G+xXg1j1NZCRivlfVIZyEsM0t0nu8NlGcNd1uthSqm1LKNVYr0elhiHso1Dg/WKGFIa2mUM01waquwgxRcNY+SUMUpvn6htp4x2av/U0GpOF7JcS+utUOPILeMorX2ijt0yxintE63idiHLlXT2Se0YknHM5SNorYIwjJpJtVqtI7YQu6VSSUWcAF2C+uRkekxFH9mdfnj6JfRd80cMY/qbCSwd7WowGByORkfHiMlk0u32+v3hjHa7PR53Oh3IhSzvoyPjMfrM7LP9fr/X7aLvo185Go0O0Y9eJdCG5PojAg9jKYEyNBVIzugcqwl0gagfbHqfXDA2DxJ7C71Swtwq7VKC74VpKhifYUlqi1hs4WuVzYPE3z2v1DG1Srua4Bax0NQJDheThLeIxdbnlvfJrqf1mZt7YJVqxFYZ1zja2UdsFV5axEIN3yqtHe7umRsGuEn1Zmxw1CIWmtoN46LLWYtYlHYCt0prh9vbgEYlYKt0NA5bxELbDdQqvV0+W8RCHXg7sBhw2yIWhrbidp+7Rbi8NWxHU3u+WoTTFHFysu/tYv+E9SrpsJgJXkdK5oWrvhIlJe+fqL6uoOl4T0uT/LiQ5SQ+HgkM/IjVDZ8PXR24x3Vg0jDEA43rwKRgiMc5+rmaFAyFbg29NZgME/+YxBPV9z0N/l8yWH7Zxgv6L+P8RxlfuzSTHu21Sf9T5hQ67S9foH89pb02KUuX58BJf/3VaPz6Chx4TnlxlGWUX7hP+bqZQTSv3UdelOmujraMM+cJX1zOXGQyjcsL57EzzmU4z/em2chYNG+cR7mWUT63n+yTb83MEs1vT+zHz+naoCzju+1cfzQaGRuNxg/bB75zLcP2P/+zmXHR/GmrHI5llF8unSgKVLcLVBy2kH1J1QZdGa8Wp3kNlMW8OJZC9hXHMh7D8+ISLAtXyF7wK+Pxz8+blWUxL47HkKX6RyhNGeXXYKCCNqyQfU2zNKjKOIUDFWyVecie8iojuzJQweIwQ5bm+ijKKL9ZHahgccxC9g3F0qAp42xdoILFcU13s0ZTxmKH6rs4UMhyKaN8/jugillx/Ka4WaMmQ8/+8X21sBXHH/RVStCSobzNFMK4yKCvvVUoLZKODF1/lyuGc5HJFHPvdDrFQUWGsv0+H1bFlPz7bSrFQUGGrnwIXxZWcXxQKBQHeRnKxsdIZTEvjo8b5IuDuAxlrxDyymmnkN8jboOwDD37KYdDxZTcJ9IhS1ZG+ECFIB6yJGVEClQI0iFLUEbUQIUgG7LEZGAIVAiiIUtKho4lUCFQyJKyQUiGspfHeOW0Qy5kicjAGagQpEKWhAy8gQpBKGTxy9CVvySunHaKub8EQha7DBKBCkEiZDHL0JW7PPGyMCnmsYcsXhnkAhUCe8hilYFrh+qXQgFvyGKUQTpQIfCGLD4Z5AMVAmvI4pJBJVAhUMhiu45ikqFs31K8ctrJ3+IKWSwyKAYqRDF/h6c4cMjQN+6ZlYVJ/h5LyGKQoewVGVw57RSKOEI2sgw9+0A9UCFyD9FDNqoMtBVhXhYmheiblWgymAUqRPSQjSSDZaBCRA3ZCDKmgRqTFrEoRAvZ8DLYBypEpJANLUN5yz5QIQrF8JuVkDJ0/SE+V047xfAhG05GfAIVInTIhpERq0CFCBuyIWQoG/EKVIj8bZjZlsAyYhioEKFCNqgMPXsfi62IN7n7wNfRgDLiGqgQwUM2kIwYByoECtlgj92CyIh3oEIEDFn/MghNn5Al2GyLbxlJCFSIICHrV4ZyR/dhGT6mIYtVBouHZfjw/djNlww2D8vw4fexmw8Z2Mc56eNzgNRbBq3pE7L4mm3xkpHIQIXwE7IeMvC8HxEPvN/SWC+D9vQJWTwHSNfJSHagQniE7BoZSQ9UiPUhu1IGB4EKsTZkV8ngI1Ah1oQsLIObQIVYHbKgDLrjnPRZNUAKySD5fkQ8WBGybhn8BSoEGLIuGTwGKgQUsg4ZsX9Yhg/gLQ27DH4DFcIVsssyGI9z0sf5lsaSDN4DFcIesgsZfO1Q/WJ7S8OSkY5AhVgKWSldgQqxCFkpZYEK8TjbImXjN85Jn/kAqZS+QIUw39KQ4jnOSZ/pAKmUykCFQCH7D36CMJSKMhCXAAAAAElFTkSuQmCC')

st.title('Análise Sinasc Rôndonia - 2019')

st.markdown("Este é um projeto do curso de cientista de dados da EBAC")

st.markdown("### Iremos analisar o banco de dados do Sinasc do estado de Rôndonia do ano de 2019, mais informações sobre sobre o que é o sinasc estão disponiveis abaixo.")

st.text_area('O Sinasc', value="O sistema de Informações sobre Nascidos Vivos (SINASC), implantado em 1990 para coletar dados sobre nascimentos em todo o Brasil e fornecer informações sobre natalidade para o sistema de saúde. A coleta de dados é realizada por meio da Declaração de Nascidos Vivos (DN), preenchida pelos profissionais de saúde responsáveis pela assistência ao parto ou recém-nascido, ou por parteiras tradicionais vinculadas a unidades de saúde. As DN são distribuídas pelo Ministério da Saúde para os estados, e pelos estados para os municípios, que digitam, processam e consolidam as informações no SINASC local. Os dados são transferidos para o nível estadual e, posteriormente, para o nível federal, onde são agregados por Unidade da Federação e analisados pela Coordenação-Geral de Informações e Análises Epidemiológicas (CGIAE). O SINASC possibilita a construção de indicadores úteis para o planejamento de gestão dos serviços de saúde, especialmente na área da saúde materno-infantil. O Ministério da Saúde incentiva o uso dos dados do SINASC para a formulação de indicadores epidemiológicos como instrumentos estratégicos de suporte ao planejamento das ações, atividades e programas voltados à gestão em saúde.")

@st.cache_data
def load_data(url):
    sinasc = pd.read_csv(url)
    return sinasc

sinasc = load_data(r"https://github.com/sannlin9/Streamlit-app/blob/b801536b7749f05be7ac20fff768f435d0536692/input/SINASC_RO_2019.csv")

st.markdown("Gostaria de visualizar os dados? clique em mostrar dados.")

if st.checkbox('Mostrar dados'):
    st.subheader('Dataframe completo.')
    st.write(sinasc)

sinasc.DTNASC = pd.to_datetime(sinasc.DTNASC)
min_data = sinasc.DTNASC.min()
max_data = sinasc.DTNASC.max()

datas = sinasc.DTNASC.unique()
datas.sort()

data_inicial = st.sidebar.date_input('Data inicial',
                             value = min_data, 
                             min_value = min_data, 
                             max_value = max_data)

st.sidebar.write('Data inicial = ',data_inicial)

data_final = st.sidebar.date_input('Data final', 
                           value = max_data,
                             min_value=min_data,
                             max_value=max_data)

st.sidebar.write('Data final = ',data_final)

sinasc = sinasc[(sinasc['DTNASC'] <= pd.to_datetime(data_final)) & (sinasc['DTNASC'] >= pd.to_datetime (data_inicial))]

st.subheader('Média da idade das mães por data de nascimento.')
plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'mean', 'média idade mãe por data', 'data nascimento')

st.subheader('Média da idade das mães por data de nascimento.')
st.markdown('### Distribuido por genero do bebê')
plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'media idade mae','data de nascimento','unstack')

st.subheader('Média de peso dos bebês por data de nascimento.')
st.markdown('### Distribuido por genero do bebê')
plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe','data de nascimento','unstack')

st.subheader('Média de peso dos bebês por nivel de escolaridade da mãe.')
plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'PESO mediano','escolaridade mae','sort')

st.subheader('APGAR1 médio dos bebês por tempo de gestação.')
plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio','gestacao','sort')

