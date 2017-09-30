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


- Nodes => Artificial Neurons   

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

- Number of Input Nodes => Usually equal to Number of INDEPENDENT VARIABLES being used to PREDICT   
or CLASSIFY the DEPENDENT VARIABLE.  

- TBD 

- TBD


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
Thus to understand this out and utilize it for Prediction we - ```denormalize --- PRED VALUE = Output( Data Range ) + Min Value of Data```   



#









