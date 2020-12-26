import streamlit as st
from headliner.model.summarizer_attention import SummarizerAttention

DATASET_ATTENTION_HEADLINER_FILEPATH = 'data/summarizer'

def main():
    # summarizer_transformer = SummarizerTransformer.load(DATASET_TRANSFORMER_HEADLINER_FILEPATH)
    summarizer_attention = SummarizerAttention.load(DATASET_ATTENTION_HEADLINER_FILEPATH)

    st.title('English-Russian Translator')
    st.markdown('''
    Построена тестовая модель переводчика с английского на русский.
    Представленный переводчик довольно скуден на слова. Основной целью работы было опробовать `Streamlit`. 
    В основе используется библиотека [`headliner`](https://github.com/as-ideas/headliner).
    Обучение проводится на карточках [Anki](http://www.manythings.org/anki/rus-eng.zip). 
    подробное описание ниже.   
    ''')
    input = st.text_input(label='Input some English words:', value='I really like you.')
    # st.write('(transformer) {}'.format(summarizer_transformer.predict(input)))
    st.write('(attention) {}'.format(summarizer_attention.predict(input)))

    st.markdown('''


    ## Описание модели

    Проведено оучение простой модели на карточках  [Anki](http://www.manythings.org/anki/rus-eng.zip).
    Ноутбук с обучением находится [тут]()
    ''')

if __name__ == "__main__":
    main()