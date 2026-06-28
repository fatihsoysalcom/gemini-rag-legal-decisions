import os
import google.generativeai as genai

# --- Configuration ---
# Set your Google API key as an environment variable (e.g., GOOGLE_API_KEY)
# You can get one from Google AI Studio: https://aistudio.google.com/app/apikey
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable not set. Please set it to your Gemini API key.")
genai.configure(api_key=API_KEY)

# --- Simulated Document Corpus ---
# In a real RAG system, these would be chunks from actual legal documents,
# potentially stored in a vector database or indexed for efficient retrieval.
documents = [
    "Case A: Applicant denied asylum due to lack of credible fear. Decision based on 8 CFR § 208.13.",
    "Case B: Petition for H-1B visa approved. Employer demonstrated need for specialized knowledge worker under INA § 214(g).",
    "Case C: Adjustment of status denied due to criminal inadmissibility. Applicant failed to qualify for a waiver under INA § 212(h).",
    "Case D: Naturalization application approved. Applicant met continuous residence and good moral character requirements per INA § 316.",
    "Case E: Asylum claim granted. Applicant provided sufficient evidence of past persecution based on political opinion, satisfying 8 CFR § 208.13(b)(2).",
    "Case F: Removal proceedings terminated. Respondent demonstrated U.S. citizenship through birth certificate, making them not subject to INA § 237.",
    "Case G: L-1B visa petition denied. Company failed to establish specialized knowledge of the beneficiary. See 8 CFR § 214.2(l)(1)(ii)(D).",
    "Case H: Waiver of inadmissibility granted for a nonimmigrant visa applicant under INA § 212(d)(3)(A).",
]

# --- Retrieval Component (Simplified) ---
# This function simulates retrieving relevant document chunks based on a query.
# In a full RAG system, this would involve embeddings and vector similarity search.
def retrieve_documents(query, corpus, top_k=3):
    """
    Retrieves relevant document snippets from the corpus based on keywords in the query.
    """
    query_keywords = query.lower().split()
    relevant_docs = []
    for doc in corpus:
        # Simple keyword matching for demonstration
        if any(keyword in doc.lower() for keyword in query_keywords if len(keyword) > 2): # Ignore very short keywords
            relevant_docs.append(doc)
    # For simplicity, just return all found docs, or a subset if top_k is used.
    # A real system would rank these by relevance using embeddings.
    return relevant_docs[:top_k] if top_k else relevant_docs

# --- Generation Component (using Gemini) ---
def generate_answer(query, context):
    """
    Generates an answer to the query using the provided context with Google Gemini.
    """
    model = genai.GenerativeModel('gemini-pro')
    prompt = (
        f"You are an AI assistant specialized in USCIS legal decisions. "
        f"Answer the following question based ONLY on the provided context. "
        f"If the answer cannot be found in the context, state that you don't have enough information.

"
        f"Context:
{context}

"
        f"Question: {query}

"
        f"Answer:"
    )
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"

# --- RAG System Integration ---
def rag_system(query, corpus):
    """
    Integrates retrieval and generation to answer a query using RAG.
    """
    # 1. Retrieve relevant documents
    retrieved_context = retrieve_documents(query, corpus)
    
    if not retrieved_context:
        return "No relevant documents found in the corpus to answer your question."
    
    context_string = "\n".join(retrieved_context)
    print(f"\n--- Retrieved Context ---\n{context_string}\n") # Inline comment: This shows the context retrieved by the system.

    # 2. Generate answer using the retrieved context
    answer = generate_answer(query, context_string) # Inline comment: The retrieved context is passed to Gemini for generation.
    return answer

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Simple RAG System for USCIS Decisions (Simulated) ---")
    
    # Example 1: Query with relevant info in corpus
    query1 = "What are the reasons for asylum denial according to the provided cases?"
    print(f"\nQuery 1: {query1}")
    response1 = rag_system(query1, documents)
    print(f"\nAnswer 1: {response1}")

    # Example 2: Query with relevant info in corpus (different topic)
    query2 = "Which cases discuss waivers for inadmissibility?"
    print(f"\nQuery 2: {query2}")
    response2 = rag_system(query2, documents)
    print(f"\nAnswer 2: {response2}")

    # Example 3: Query with limited or no relevant info in corpus
    query3 = "What is the processing time for an I-485 application?"
    print(f"\nQuery 3: {query3}")
    response3 = rag_system(query3, documents)
    print(f"\nAnswer 3: {response3}")
