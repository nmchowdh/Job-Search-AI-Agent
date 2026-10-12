# Job Search AI Agent Dashboard

An interactive Streamlit dashboard with job filters, four interactive charts, summary metrics, and CSV export.

## Data note
This version uses fictional demo listings. Match scores are illustrative, not AI-generated predictions. No live jobs API is connected yet.

## Run locally
```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Deploy for a public URL
1. Create a GitHub repository and upload `app.py`, `requirements.txt`, and `README.md`.
2. Visit https://share.streamlit.io/ and sign in with GitHub.
3. Choose **Create app**, select your repository and branch, and set **Main file path** to `app.py`.
4. Deploy. Streamlit Community Cloud will provide a public `https://....streamlit.app` URL.
5. Test that public URL and submit it on Handshake. A local `localhost` URL is only available on your computer.

## Next step
Replace the `JOBS` demo list in `app.py` with results from your `search_jobs(query)` function and a live job-listings API.
