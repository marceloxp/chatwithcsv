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
!wget --progress=bar:force https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q8_0.bin
!ls -lah
!pip install -r requirements.txt
!npm init -y
!npm install localtunnel
!streamlit run app.py &>/content/logs.txt &
!npx localtunnel --port 8501
```

## Model

### Llama 2 7B Chat

- Page: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin
- Link Address: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin

### Llama 2 13B Chat

- Page: https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/blob/main/llama-2-13b-chat.ggmlv3.q8_0.bin
- Link Address: https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q8_0.bin

### Open Llama 3B v2

- Page: https://huggingface.co/SlyEcho/open_llama_3b_v2_ggml/blob/main/open-llama-3b-v2-q4_0.bin
- Link Address: https://huggingface.co/SlyEcho/open_llama_3b_v2_ggml/resolve/main/open-llama-3b-v2-q4_0.bin

### Mamba GPT-3B

- Page: https://huggingface.co/s3nh/mamba-gpt-3b-v3-GGML/blob/main/mamba-gpt-3b-v3.ggmlv3.q4_0.bin
- Link: https://huggingface.co/s3nh/mamba-gpt-3b-v3-GGML/resolve/main/mamba-gpt-3b-v3.ggmlv3.q4_0.bin

## Video

- https://www.youtube.com/watch?v=_WB10mFa4T8

## Utilização:

- Pergunta 1
  - Pergunta: Qual ator fez o filme com pior nota?
  - Resposta: The actor who made the film with the worst note is Alexander Wilson, with a score of 8.4.

- Pergunta 2
  - Pergunta: Qual filme teve a melhor nota? Por favor me responda em português.
  - Resposta: O melhor filme foi "Filme K" com nota 9.2.

- Pergunta 3
  - Pergunta: Which actor made the movie with worse rating?
  - Resposta: 
