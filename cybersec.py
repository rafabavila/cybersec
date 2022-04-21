import streamlit as st
import re
import requests
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

numpas = requests.get("https://dalcol99.github.io/grc.json")
nompas = requests.get("https://cspinheiro.github.io/interpol.json")

dict_num = numpas.json()['grc']
dict_nom = nompas.json()['interpol']

lisnom = []
for idx, sub in enumerate(dict_nom, start=0):
    if idx == 0:
        lisnom.append(list(sub.keys()))
        lisnom.append(list(sub.values()))
    else:
        lisnom.append(list(sub.values()))
lisnomx = [item for sublist in lisnom for item in sublist]
lisnomx.remove('interpol')
lisnomf = '(% s)' % ')|('.join(lisnomx)


def main():
    html_temp = """ 
    <div style ="background-color:blue;padding:15px"> 
    <h1 style ="color:white;text-align:center;">Checagem de Imigração</h1> 
    </div> 
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    numpass = st.text_input('Digite o Número do Passaporte - sem as letras iniciais')
    nompass = st.text_input('Digite o Nome Completo do indivíduo')
    check = st.button('CHECAR')

    def checknum(field):
        for item in dict_num:

            for value in item.values():

                if str(field) == str(value):
                    return st.error('Não pode entrar no país')

        return st.success('Pode entrar no país') and st.balloons()

    def checkfuzzy(field):
        search_list = process.extract(field, lisnomx)
        result = []

        for text in search_list:
            if text[1] >= 96:
                result.append(text)
        if len(result) == 0:
            return checknum(numpass)
        return st.error('Não pode entrar no país')

    def checknom(field):
        match = re.search(f'(?i){lisnomf}', field.lower())
        if check:
            if match:
                st.error('Não pode entrar no país')
            else:
                checkfuzzy(field)

    checknom(nompass)


if __name__ == '__main__':
    main() 
