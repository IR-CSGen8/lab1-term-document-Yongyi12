#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
datas = pd.read_csv('tdoc.csv', header = None)

datas


# In[6]:


# get the keys of the documents and store it in the list
key_documents = list(datas.keys())

# display the list of the key documents
print(key_documents)
#title = datas[0].tolist()
#title
#content = datas[1].tolist()
#content


# In[7]:


# Extract the content values and put them in a list
document_content_list = list(datas[1])

# Display the list of document content
print(document_content_list)


# In[8]:


# Gather the set of all unique terms from the list content of document and diplay the result
unique_terms = set()

# Iterate through each document content to extract unique terms
for content in document_content_list:
    terms = content.split()
    unique_terms.update(terms)

#Display the result
unique_terms = list(unique_terms)
print(unique_terms)


# In[3]:


# create a matrix for the document by using the unique term
doc_term_matrix = {}

# your code here
for key in unique_terms: 
    doc_term_matrix[key] = []
    for doc in key_documents:
        if key in datas[1]:
            doc_term_matrix[key].append(1)
        else: 
            doc_term_matrix[key].append(0)


# display the result of the matrix
doc_term_matrix


# In[4]:


import csv

# Convert the set to a list
my_list = list(unique_terms)

# Specify the CSV file path
csv_file_path = 'unique_terms_01.csv'

# Write the data to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the data as a single row
    csv_writer.writerow(my_list)

print(f"Set saved as {csv_file_path}")


# In[9]:


# Convert unique_terms back to a list (if needed)
unique_terms_list = list(unique_terms)

# Define the file path where you want to save the unique terms
file_path = 'unique_terms.txt'

# Open the file in write mode and write the unique terms
with open(file_path, 'w') as file:
    for term in unique_terms_list:
        file.write(term + '\n')

# Display a message indicating that the terms have been saved
print(f'Unique terms have been saved to {file_path}')


# In[ ]:




