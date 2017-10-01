### Computer Vision with Artificial Neural Networks a Primer 
#
### Research Notes Collated by : Rohit Dhankar
#
### Introduction :-   
Artificial neural networks are used to solve problems of pattern
recognition and computer vision.   

As ANN's are a higher level abstraction of complexity - they follow the basic Classification Logistic or Sigmoid functions.  
We should look at the Multiclass Logistic Regression with help of R , before we can understand ANN's .   
We shall code and implement ANN's with both R and Python.   
#
### Basic definitions :-  


- Nodes => Artificial Neurons a SINGLE NODE or MULTIPLE NODES aligned vertically form a INPUT / HIDDEN / OUTPUT Layer.   

- Indicator-Flag-variables => Car-TRUE , No Car-FALE , Bus-FALSE ==  1,0,0   

- Continous Output => ANN nodes will output Continous values within Range - 0 to 1.   

- Priori or Prior Threshold values => Above or below certain priorly decided value  
presume we have Car >0.55 and NO Car < 0.54 . This shall help us encode the Categorical outputs.  

- Completely Connected ANN => All nodes from the INPUT LAYER  are CONNECTED to All NODES of the   
HIDDEN LAYER and also All NODES of each HIDDEN LAYER are connected to all nodes of next hidden  
layer which are in turn connected to all Nodes of OUTPUT Layer .   
Nodes within the same layer are NOT Connected to each other.   
Each Connection between Nodes has a WEIGHT == W1A , associated with it.  

- Feed Forward ANN => Information flows only in the Forward direction , its Fed Forward Only .  

- Number of INPUT LAYER NODES => Usually equal to Number of INDEPENDENT VARIABLES being used to PREDICT   
or CLASSIFY the DEPENDENT VARIABLE.  

- Number of UNITS or NODES within HIDDEN LAYERS => This number can vary , as an example we can have a HIDDEN Layer   
with TWO Nodes and another with THREE etc .   

- THETA - [ Maths Symbols to be Inserted here ] the unknown PARAMETER or WEIGHT => Its similar in functionality to   
the BETA or Error Term from LOGISTIC REGRESSION MODEL.   



- TBD 


#

For ANN's all attribute values are to be provided between the Minimum 0 and Maximum 1 .  
Even Categorical and Ordinal variables have to be coded between Minimum 0 and Maximum 1 .  
For continous variables we apply the ``` min-max normalization```.  

#
The common ANN structure mandates three layers - ```input layer , hidden layer and output layer```  
For simple Classification problems we may use a ``` Single Output Node``` , but mostly the Output Layer like the    
two other layers shall have Multiple Nodes or Neurons.    
Thumb rule is to have as many NODES in OutPut Layer as there are DEPENDENT Variable CLASSES.   

#

The OutPut of ANN's Output layer NODE always lies between RANGE - 0 and 1.   
Thus to understand this output and utilize it for Prediction we - ```denormalize --- PRED VALUE = Output( Data Range ) + Min Value of Data```   
- Output == Continous decimal value between - 0 to 1 . 
- Data Range == Initial RAW Data , MAX VALUE - MIN VALUE. 
- Min Value of Data == Initial RAW Data , MIN VALUE. 

### Data Inputs and Initial Values of WEIGHTS 
#
We look at some of these basic questions and try to answer them briefly ...   


- What are WEIGHTS ? 
- What is the BIAS UNIT ? 
- What is a BIAS TERM ?
- How does a NODE FIRE - whats an ACTIVATION FUCTION ?
- How is ACTIVATION related to the SIGMOID FUNCTION ?
- What is COST FUNCTION ? 
- How to MINIMIZE COST FUNC. How to calculate DERIVATIVE ? 

#


#


#


#


#


#


#


#


#

### The PERCEPTRON 

The litterature i have been able to read about PERCEPTRON's has ended up confusing me .   
I site certain examples below :-  

- A seemingly reputed and popular blog -- [http://neuralnetworksanddeeplearning.com/chap1.html]"http://neuralnetworksanddeeplearning.com/chap1.html" , doesnt provide a clear understanding of the PERCEPTRON .   
- It mentions the word PERECPTRON - 99 times within Chapter-1 .  
- It stated " So how do perceptrons work? A perceptron takes several binary inputs, x1,x2,…, and produces a single binary output".  
- Seems incorrect to me - also other refrences to PERCEPTRON's are either dated or inconsistent or just passing remarks.  
Thus we dont deal with PERECPTRON's.   
#
Perceptron_Image_1: 
![alt text](../master/screen_captures/Perceptron_1.png "Perceptron_Image_1")
#

Perceptron_Image_2: 
![alt text](../master/screen_captures/Perceptron_2.png "Perceptron_Image_2")
#  

Perceptron_Image_3: 
![alt text](../master/screen_captures/Perceptron_3.png "Perceptron_Image_3")
#  

###  SUPPORT VECTOR MACHINES vs. NEURAL NETS 
In lots of litterature sources i have read - the SVM is preffered as a Classifier in place of the ANN .  
Quoted verbatim from WIKI -- dated - 02 OCT 17 :-
 
```
Support vector machines and other, much simpler methods such as linear classifiers gradually overtook neural networks in machine learning popularity.

Earlier challenges in training deep neural networks were successfully addressed with methods such as unsupervised pre-training, while available computing power increased through the use of GPUs and distributed computing. Neural networks were deployed on a large scale, particularly in image and visual recognition problems. This became known as "deep learning", although deep learning is not strictly synonymous with deep neural networks.
```
WIKI Image --- 

SVM_WIKI_Image_1: 
![alt text](../master/screen_captures/SVM_WIKI_Image_1.png "SVM_WIKI_Image_1")
#  





#

Test --- 

```math

E = m c^2


``$ y=\sum_{i=1}^n g(x_i) $``

```

#

|INPUT LAYER    |HIDDEN LAYER   |OUTPUT LAYER |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned |  |
| col 2 is      | centered      |  |
| zebra stripes | are neat      |  |








#









