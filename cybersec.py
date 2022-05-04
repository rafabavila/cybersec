import streamlit as st
import re
import requests
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

nompas = requests.get("https://cspinheiro.github.io/interpol.json")
dict_nom = nompas.json()['interpol']

lisnom = []
for idx, sub in enumerate(dict_nom, start = 0):
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

    st.markdown(html_temp, unsafe_allow_html = True)
      
    idpass = st.text_input('Digite a identificação do Passaporte (iniciais do país + número do passaporte): ')
    nompass = st.text_input('Digite o nome completo do indivíduo: ')
    check = st.button('CHECAR')

    def text_num_split(field):
      for index, letter in enumerate(field, 0):
          if letter.isdigit():
              return [field[:index],field[index:]]

    def checkfuzzy(field):
      search_list = process.extract(field, lisnomx)
      result = []
      for text in search_list: 
          if text[1] >= 96:
            result.append(text)
      if len(result) == 0:
          return st.success('Pode entrar no país') and st.balloons()
      return st.error('Não pode entrar no país')

    def checknom(field):
      match = re.search(f'(?i){lisnomf}', field.lower())
      if match:
        st.error('Não pode entrar no país')
      else:
        checkfuzzy(field)

    def checknum(field):
      for item in dict_num:
          for value in item.values():
            if str(field) == str(value):
              return st.error('Não pode entrar no país')
      return checknom(nompass)
  
    if check:
      listaid = text_num_split(idpass)
      pais, numpass = listaid
      checagem = re.search('(?i)((bra)|(fra)|(ago)|(ita)|(aus)|(ind)|(mng)|(can)|(grc)|(hun)|(arg)|(irl)|(npl)|(irq)|(bel)|(nic)|(prt)|(mdv)|(col)|(hnd)|(pry))', pais.lower())
      if checagem:
        if pais.lower() == "bra":
          numpas = requests.get("https://cspinheiro.github.io/bra2.json")
          dict_num = numpas.json()['bra2']
        elif pais.lower() == "fra":
          numpas = requests.get("https://henricobela.github.io/fra.json")
          dict_num = numpas.json()['fra']
        elif pais.lower() == "ago":
          numpas = requests.get("https://the-icaro.github.io/ago.json")
          dict_num = numpas.json()['ago']
        elif pais.lower() == "ita":
          numpas = requests.get("https://isabellitankian.github.io/ita.json")
          dict_num = numpas.json()['ita']
        elif pais.lower() == "aus":
          numpas = requests.get("https://cesarnorena.github.io/aus.json")
          dict_num = numpas.json()['aus']
        elif pais.lower() == "ind":
          numpas = requests.get("https://eduardomatoss.github.io/ind.json")
          dict_num = numpas.json()['ind']
        elif pais.lower() == "mng":
          numpas = requests.get("https://emgabrielly.github.io/mng.json")
          dict_num = numpas.json()['mng']
        elif pais.lower() == "can":
          numpas = requests.get("https://educunhamxk.github.io/CAN.json")
          dict_num = numpas.json()['CAN']
        elif pais.lower() == "grc":
          numpas = requests.get("https://dalcol99.github.io/grc.json")
          dict_num = numpas.json()['grc']
        elif pais.lower() == "hun":
          numpas = requests.get("https://guhdalla.github.io/hun.json")
          dict_num = numpas.json()['hun']
        elif pais.lower() == "arg":
          numpas = requests.get("https://kndhvh.github.io/arg.json")
          dict_num = numpas.json()['arg']
        elif pais.lower() == "irl":
          numpas = requests.get("https://victorswory.github.io/irl.json")
          dict_num = numpas.json()['irl']
        elif pais.lower() == "npl":
          numpas = requests.get("https://rodrigofer89.github.io/npl.json")
          dict_num = numpas.json()['npl']
        elif pais.lower() == "irq":
          numpas = requests.get("https://felps2003.github.io/irq.json")
          dict_num = numpas.json()['irq']
        elif pais.lower() == "bel":
          numpas = requests.get("https://rafael-pereira-silva.github.io/bel.json")
          dict_num = numpas.json()['bel']
        elif pais.lower() == "nic":
          numpas = requests.get("https://rafael-pereira-silva.github.io/bel.json") ### Endpoint está errado, é o mesmo da Bélgica
          dict_num = numpas.json()['bel']
        elif pais.lower() == "prt":
          numpas = requests.get("https://0verthrive.github.io/prt.json")
          dict_num = numpas.json()['prt']
        elif pais.lower() == "mdv":
          numpas = requests.get("https://jluizgomes.github.io/mdv.json")
          dict_num = numpas.json()['mdv']
        elif pais.lower() == "col":
          numpas = requests.get("https://caiogoes.github.io/col.json")
          dict_num = numpas.json()['col']
        elif pais.lower() == "hnd":
          numpas = requests.get("https://ricardoaugu.github.io/excel-to-json.json")
          dict_num = numpas.json()['HND']
        elif pais.lower() == "pry":
          numpas = requests.get("https://danielthelink.github.io/pry.json")
          dict_num = numpas.json()['pry']
        checknum(numpass)
      else:
        checknom(nompass)

if __name__=='__main__': 
    main()
