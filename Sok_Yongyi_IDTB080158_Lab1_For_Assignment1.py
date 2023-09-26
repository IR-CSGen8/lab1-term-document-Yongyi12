#!/usr/bin/env python
# coding: utf-8

# In[52]:


# Define the documents as a dictionary where keys are document titles and values are document content
documents = {
    "Article: Pandas Basics": "This article covers the basics of using Pandas in Python.",
    "Tutorial: Data Visualization": "Learn about data visualization techniques with Python libraries.",
    "Case Study: Sales Analysis": "Analyze sales data using Python for a real-world case study."
}


# In[53]:


# get the keys of the documents and store it in the list
key_documents = list(documents.keys())

# display the list of the key documents
print(key_documents)


# In[54]:


# Extract the category from the key documents and store it in a list
categories = [title.split(':')[0] for title in documents.keys()]

# Display the list of categories
print(categories)


# In[55]:


# Extract the content values and put them in a list
document_content_list = list(documents.values())

# Display the list of document content
print(document_content_list)


# In[56]:


# Gather the set of all unique terms from the list content of document and diplay the result
unique_terms = set()

# Iterate through each document content to extract unique terms
for content in document_content_list:
    terms = content.split()
    unique_terms.update(terms)

#Display the result
unique_terms = list(unique_terms)
print(unique_terms)


# In[57]:


# create a matrix for the document by using the unique term
doc_term_matrix = {}

# your code here
for key in unique_terms: 
    doc_term_matrix[key] = []
    for doc in key_documents:
        if key in documents[doc]:
            doc_term_matrix[key].append(1)
        else: 
            doc_term_matrix[key].append(0)


# display the result of the matrix
doc_term_matrix



# In[68]:


# import the numpy library if it doesn't work you need to install numpy
import numpy as np

docs_array = np.array(document_content_list, dtype='object')

v1 = np.array(doc_term_matrix['the'])    
v2 = np.array(doc_term_matrix['Python'])

print('==== Matrices Checking by each contents ====')
print(v1)
print(v2)
print('-------')

# find the documents that have both terms from v1 and v2
v3 = v1 & v2
print('This the result after multiplication of matrices' , v3)

# display the content document from the result

[result for result in v3*docs_array if result]


# In[69]:


# find the document for those have at least one word
import numpy as np

docs_array = np.array(document_content_list, dtype='object')

v1 = np.array(doc_term_matrix['data'])    
v2 = np.array(doc_term_matrix['Python'])

print('==== Matrices Checking by each contents ====')
print(v1)
print(v2)
print('-------')

# find the documents that have both terms from v1 and v2
v3 = v1 | v2
print('This the result after multiplication of matrices' , v3)

# display the content document from the result
#docs_array[v3]
[result for result in v3*docs_array if result]


# In[ ]:




