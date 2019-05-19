### Architectural Basics:

## While working on the experiment I have tested different parameters in a CNN as mentioned below.

###  **In first model all the basic points are used**
- ##### How many layers,
   - Number of layers in a network depends on receptive fields, depends on size of the kernel, and available computation units. If we have less number of computation units then we can reduce number of layers using Maxpooling layer(or transition layer).
- ##### MaxPooling,
    - MaxPooling is used to reduce number of kernels(computational unit requirment) and Maxpooling takes values with higher weightage to output, so it reduces any noise but at the same time it may supress some feature as well.
    - We should not use maxpooling just immediately after start layer as we may loose many inputs from the original image and also we should not use Maxpooling before 2 layers of last layer as we may loose some important information which is coming through Convolution.
- ##### 1x1 Convolutions,
    - 1x1 convolution is used to reduce number of channel in a network. Before invention of 1x1 convolution we were using normal convolution for reducing number of channels.
    - Example: 392x392x256 | (3x3x256)x512 | 390x390x512
    - MaxPooling
    - 195x195x512 | (?x?x512)x32    | ?x?x32 RF of 22x22
    - By reducing the number of kernels from 512 to 32 will work fine but here we are compting 512 to get 32 this is not correct intuitively.
    - The **1x1** convultion doesn't revalues all 512 kernels to pick 32, instead it merges all 512 to generate 32. If some feature will have less weitage it will be supressed in output and with back-propagation it helps the network to reevalutes those weights to give better prediction.
- ##### 3x3 Convolutions,
    - We can use any other size kernels like 5x5, 7x7. But to capture all the pixels of an image in receptive fields 3x3 channels uses less coputational power.
- ##### Receptive Field,
    - In a network before applying any transitional layer we should be sure that the size of the receptive field at that layer is equal to object size in that images or else the network may not identify all the features in the image.
- ##### SoftMax,
    - Softmax activation function is used for multi class classification problem. Using softmax each output class is associated with a probalily like score and based on that model predict what would be the output of a given input. Sum of all softmax score for different classes of a given input will be 1.
- ##### Kernels and how do we decide the number of kernels?
    - Genrally in a network the number of kernels placed in each layer in incremental fashion, like 8, 16, 32, 64... The kernel size directly affects the number of paramter, so higher the kernel size more coputation power needed to train the model. If we have less coputation power then we need to reduce number of kernels and also Maxpooling is used to reduce number of kernels in a network.
    - In our case we have used 10, 20 sequence to make sure number of parameter not going beyond 15k.

### Below paramters are introduced in 2nd model.
- ##### Number of Epochs and when to increase them,
    - Number of epoch means number of times a network passes the entire training dataset from begining of the model to get the result.
    - We should increase our number of epoch when we see there in increase in trend of training accuracy  and which is not relatively constants in last few epochs. It means there is no significant change in training accracy.
    - I have increased the number of epochs from 25 to 40. I'll keep it that level in subsequent models.
- ##### DropOut
    - Dropout drops some of the paramters from one layer to other layer. This makes the model to train harder. Dropout reduces the gap between training and validation accuracy.
    - Droout should not be used immediately after input layer as the model will loose some of the feature. It should be used after 2-3 layers.
    - Also, dropout should be used at the last layer. It should be used before 2 layers of last layer.
### Below parameters are introduced in 3rd model:
- ##### Batch Normalization,
    - In different layers of CNN we get some input values from previous layer and the values can be anything. Using Batch Normalization we normalize the input values. So it standardizes the inputs to a layer and this stabilizes the learning rate.
### In Model 4 I'm modifying below paramters
    - Fine tuning different parameters.
