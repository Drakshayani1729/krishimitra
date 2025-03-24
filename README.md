# Krishi Mitra

_Full-stack LLM application with OpenAI, Flask, React, and Pinecone to help farmers_

(https://github-production-user-asset-6210df.s3.amazonaws.com/99467488/303893192-14bcc58a-62ff-4c84-b7de-1adc846630f2.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250324%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250324T104647Z&X-Amz-Expires=300&X-Amz-Signature=454af7294036db30945919544d4d9d035a394dc35047e5e85fe29759f6ca37af&X-Amz-SignedHeaders=host)

##Architecture of our Krishi Mitra- LLM ChatBot
<img src="https://i.imgur.com/FqOr8t8.png" witdth="800">

### Overview

Krishi Mitra addresses the challenge faced by rural Indian farmers by providing a platform for agricultural education and guidance. It offers access to modern farming techniques, personalized mentorship, a 24/7 IVR helpline, and engagement with agricultural experts.

### Features

- Automated calling using vonage API.
- AI chatboat which is specifically trained on agriculture .
- Multiple language support.
- Education without internet.

### Problems it solves

- Lack of immediate support and guidance.
- Limited access to agricultural resources.
- Dependency on traditional farming methods.

### Components of the full application:

- **Backend (Flask):** This handles the logic to scrape the website and call OpenAI's Embeddings API to create embeddings from the website's text. It also stores these embeddings in the vector database (Pinecone) and retrieves relevant text to help the LLM answer the user's question.
- **OpenAI:** We'll call two different API's from OpenAI: (1) the Embeddings API to embed the text of the website as well as the user's question, and (2) the ChatCompletions API to get an answer from GPT-4 to send back to the user.
- **Pinecone:** This is the vector database that we'll use to (1) send the embeddings of the website's text to, and (2) retrieve the most similar text chunks for constructing the prompt to send to the LLM in step 3.
- **Frontend (React+ Tailwind CSS):** This is the interface that the user interacts with to input a URL and ask questions about the webpage.

## Setup

**Install React dependencies**

```s
#install all the dependencies present in requirements.txt
pip install -r requirements.txt
```

**Create .env file in krishi-mitra folder**

```sh
OPENAI_API_KEY=<YOUR_API_KEY>
PINECONE_API_KEY=<YOUR_API_KEY>
```

**Start the Flask server**

```sh
# In root directory
python run.py
```

**Install Python dependencies**

```sh
cd client
npm install
```

**Start the React app**

```sh
cd client
npm start
```
