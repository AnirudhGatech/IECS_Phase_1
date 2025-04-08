<<<<<<< HEAD
from tsearch.spiders.embeddings.tsearch_embedding_model_init import embedding_model

def get_vector_embeddings(documents):
    embeddings_list = list(embedding_model.embed(documents))
    return embeddings_list
=======
from tsearch.spiders.embeddings.tsearch_embedding_model_init import embedding_model

def get_vector_embeddings(documents):
    embeddings_list = list(embedding_model.embed(documents))
    return embeddings_list
>>>>>>> 60b3a166f83ab4482a098c96da17927672fa53d7
