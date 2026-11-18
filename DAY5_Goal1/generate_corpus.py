import os
from fpdf import FPDF

def build_pdf_corpus():
    pdf_dir = os.path.join("DAY5_Goal1", "corpus_pdfs")
    os.makedirs(pdf_dir, exist_ok=True)
    docs = [
        {"id": "RBI_CIRC_2023_01", "title": "Monetary Policy and Inflation Outlook 2023", "year": 2023, "type": "RBI Circular", "content": "The Monetary Policy Committee decided to keep the policy repo rate unchanged at 6.50 percent. Headline CPI inflation is projected at 5.4 percent for 2023-24, driven by volatile food prices and crude oil dynamics."},
        {"id": "RBI_CIRC_2023_04", "title": "Digital Lending and KYC Guidelines 2023", "year": 2023, "type": "RBI Circular", "content": "Regulated Entities must ensure all loan disbursals and repayments are executed directly between bank accounts without pass-through pool accounts."},
        {"id": "RBI_CIRC_2024_02", "title": "Financial Stability and Banking Resilience 2024", "year": 2024, "type": "RBI Circular", "content": "Scheduled Commercial Banks maintained strong capital buffers with CRAR reaching 16.8 percent in March 2024."},
        {"id": "NSE_ANN_2022_01", "title": "NSE Annual Market Capitalization Review 2022", "year": 2022, "type": "NSE Report", "content": "Indian equities outperformed global peers in 2022 despite rate hikes. Retail SIPs crossed 13000 crore INR monthly."},
        {"id": "NSE_ANN_2023_03", "title": "Derivatives and Equity Turnover Report 2023", "year": 2023, "type": "NSE Report", "content": "Index options turnover on the National Stock Exchange saw exponential growth in 2023 driven by algorithmic trading."},
        {"id": "NSE_ANN_2024_05", "title": "Corporate Governance and ESG Disclosures 2024", "year": 2024, "type": "NSE Report", "content": "Top 1000 listed entities on NSE are mandated to submit Business Responsibility and Sustainability Reports."},
        {"id": "ARXIV_ML_2022_45", "title": "Dense Passage Retrieval vs Sparse BM25", "year": 2022, "type": "arXiv Paper", "content": "Dense bi-encoder architectures map queries and passages into a shared vector space improving recall by 22 percent."},
        {"id": "ARXIV_ML_2023_88", "title": "Chunking Strategies for Enterprise RAG", "year": 2023, "type": "arXiv Paper", "content": "512-token chunks with 15 percent overlap maintain surrounding context without diluting embeddings."},
        {"id": "ARXIV_ML_2024_12", "title": "Hybrid Search and Cross-Encoder Reranking", "year": 2024, "type": "arXiv Paper", "content": "Combining dense vector cosine similarity with sparse lexical scoring via Reciprocal Rank Fusion eliminates blind spots."},
        {"id": "RBI_CIRC_2022_08", "title": "UPI Cross-Border and Offline Payments 2022", "year": 2022, "type": "RBI Circular", "content": "RBI introduced UPI Lite and offline payment frameworks allowing small-value digital transactions up to 200 INR."}
    ]
    for doc in docs:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, f"{doc['title']} ({doc['year']})", new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 11)
        pdf.multi_cell(0, 7, doc["content"] + "\n\n" + doc["content"])
        pdf.add_page()
        pdf.multi_cell(0, 7, f"Section 2 Analysis: {doc['title']}.\n" + doc["content"])
        file_path = os.path.join(pdf_dir, f"{doc['id']}__{doc['year']}__{doc['type'].replace(' ', '_')}.pdf")
        pdf.output(file_path)
    print(f"Generated {len(docs)} multi-page PDFs successfully!")

if __name__ == "__main__":
    build_pdf_corpus()
