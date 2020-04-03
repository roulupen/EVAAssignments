**_Imdb Review Classification Using Word Embedding_**

Downloaded Imdb data set and dwonloaded Glove 6B embedding from https://nlp.stanford.edu/projects/glove/ and saved in google drive.

Coming to the Notebook:

- Mounted google drive with Colab notebook to download word embedding and actual imdb rattings zip files.
- Installed unzip package in Colab runtime to unzip zip files.
- Unzip and process both rating and embedding.
- While processing the rating file we are using Keras library for tokenization and hot encoding.
- In tokenization maximum 10,000 high frequency words were taken and from each review first 100 words were taken.


Created a simple Sequential network and very first layer of the network weights are set from the word embedding weights. Since word embedding is pre-defined weights we test it without training the first layer by setting the parameter "**trainable = False**".

Then we train the network for 10 epochs and we got a **train accuracy 0.7385 and test accuracy 0.5488**.


 