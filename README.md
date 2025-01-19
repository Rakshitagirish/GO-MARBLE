# GoMarble: AI Engineer Assignment

## Overview

This project implements an API server to extract product reviews from any product page dynamically.

### Features

- Dynamic CSS selector identification using OpenAI LLMs.
- Complete review extraction with pagination handling.
- Universal compatibility with product review pages.

### Installation

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set the OpenAI API key in a `.env` file.

### Run the API

```bash
uvicorn api.main:app --reload
