# chatwithcsv

## Conda

```sh
conda create -n chatcsv python=3.10
conda activate chatcsv
pip install -r requirements.txt
conda install -c anaconda urllib3
conda install -c huggingface transformers
streamlit run app.py
```

## Google Colab

```sh
!git clone https://github.com/marceloxp/chatwithcsv.git
%cd chatwithcsv
!ls
!wget --progress=bar:force https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin
!ls -lah
!pip install -r requirements.txt
!npm init -y

!pip install -r requirements.txt
!npm install localtunnel
!streamlit run app.py &>/content/logs.txt &
!npx localtunnel --port 8501
```

## Model

- Page: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin
- Link Address: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin

## Video

- https://www.youtube.com/watch?v=_WB10mFa4T8

## Utilização:

- Pergunta: Qual ator fez o filme com pior nota?
- Resposta: The actor who made the film with the worst note is Alexander Wilson, with a score of 8.4.

- Pergunta: Qual filme teve a melhor nota? Por favor me responda em português.
- Resposta: O melhor filme foi "Filme K" com nota 9.2.