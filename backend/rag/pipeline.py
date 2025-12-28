from rag.retreiver import PGVectorRetreiver
from rag.generator import Generator

retreiver = PGVectorRetreiver()
generator = Generator()

def run_rag(query: str) -> str:
    context_chunks = retreiver.retreiver(
        query=query,
        top_k=3
    )
    
    if not context_chunks:
        return "I couldn't find relavent information in the course material"
    
    answer = generator.generate_response(
        query=query,
        context_chunks=context_chunks
    )
    
    return answer
    