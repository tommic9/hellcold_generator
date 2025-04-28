# Plik: app.py

import streamlit as st
import pandas as pd

# Wczytaj dane ze słownika
@st.cache_data
def load_data():
    file_path = 'Generator nazw HellCold - MARIACKA.xlsx'
    data = {}
    sheets = ['ETAP', 'AUTOR', 'BRANźA', 'POZIOM', 'UKŁAD', 'TYP PLIKU']
    for sheet in sheets:
        df = pd.read_excel(file_path, sheet_name=sheet)
        df.columns = ['Kod', 'Opis']
        data[sheet] = df
    return data

def main():
    st.title("📚 Generator Nazw HellCold BIM")
    st.write("Wybierz parametry projektu, aby wygenerować poprawną nazwę pliku.")

    data = load_data()

    with st.form("generator_form"):
        etap = st.selectbox("Wybierz etap projektu", data['ETAP']['Opis'])
        autor = st.selectbox("Wybierz autora", data['AUTOR']['Opis'])
        branza = st.selectbox("Wybierz branżę", data['BRANźA']['Opis'])
        poziom = st.selectbox("Wybierz poziom", data['POZIOM']['Opis'])
        uklad = st.selectbox("Wybierz układ", data['UKŁAD']['Opis'])
        typ_pliku = st.selectbox("Wybierz typ pliku", data['TYP PLIKU']['Opis'])

        submitted = st.form_submit_button("Generuj nazwę")

    if submitted:
        kod_etap = data['ETAP'].loc[data['ETAP']['Opis'] == etap, 'Kod'].values[0]
        kod_autor = data['AUTOR'].loc[data['AUTOR']['Opis'] == autor, 'Kod'].values[0]
        kod_branza = data['BRANźA'].loc[data['BRANźA']['Opis'] == branza, 'Kod'].values[0]
        kod_poziom = data['POZIOM'].loc[data['POZIOM']['Opis'] == poziom, 'Kod'].values[0]
        kod_uklad = data['UKŁAD'].loc[data['UKŁAD']['Opis'] == uklad, 'Kod'].values[0]
        kod_typ = data['TYP PLIKU'].loc[data['TYP PLIKU']['Opis'] == typ_pliku, 'Kod'].values[0]

        nazwa = f"{kod_etap}_{kod_autor}_{kod_branza}_{kod_poziom}_{kod_uklad}_{kod_typ}"

        st.success(f"Wygenerowana nazwa pliku:")
        st.code(nazwa, language="text")

        st.download_button(
            label="Pobierz nazwę jako plik TXT",
            data=nazwa,
            file_name="nazwa_projektu.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()


# Plik: requirements.txt
# Zawartość:
# streamlit
# pandas
# openpyxl
