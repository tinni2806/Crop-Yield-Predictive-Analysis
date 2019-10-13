## **INTRODUCTION:**

Research in precision agriculture concentrates on farming management concept based on observing, measuring and responding to inter and intra-field variability in crops. 
Crop variability typically has both a spatial and temporal component which makes statistical/computational treatments quite involved. The holy grail of this project has been the ability to define a Decision Support System for farm management in India with the goal of optimizing returns on inputs while preserving resources.

Presently, I am developing big data analytic tools to estimate the nutrient status of the plants to improve the efficiency of the fertilizer use.

**PREDICTIVE ANALYSIS AND ITS BENEFITS :**

Precision agriculture follows recognizing the previous 
year yield values,understanding the current requirement of environment and exploiting information that quantifies variations in soil and crop within agricultural fields.

The precise crop variety selection,exact type of 
     fertilizers,proper irrigation meet the demand of crops
     for optimum growth and development.
It may lead to increase the yield,especially in main 
     areas.

**EXPLORATORY DATA ANALYSIS**

1. Need to check for missing or null values.
2. Understanding the data to implement the required model type on the basis of the outcome or output value.
	1. CLASSIFICATION MODEL
	2. REGRESSION MODEL
3. Analysis of data and deciding the independent and dependent variables.
4. Use necessary techniques to determine the outcome with good efficiency and plot visualisations if any. 

**SAMPLE OF DATA**

![](https://github.com/tinni2806/Crop-Yield-Predictive-Analysis/blob/master/Snapshots/Capture1.jpg)

**Factors effecting the Crop productivity**

From the data, we can observe the factors on which the crop productivity i.e., Yield is dependent are :-
1. TYPE OF SEED.
2. TYPE OF SEASON.
3. TYPE OF SOIL.
4. HUMIDITY.
5. AIR QUALITY.
6. LABOUR COST.
7. TYPE OF FERTILIZERS.
8. WATER LEVEL.

These factors are responsible for change in the Yield of crop so these are called independent variables and the outcome i.e., Yield is the dependent variable

**METHOD OF APPROACH**

1. The first step for any data analysis is importing the libraries which are required for the program.
2. Then we need to import our data set to the program and split the data set into independent(X-variables) and dependent(Y-variables).
3. Splitting the data into Train and Test is one of the key step to train the model to gain perfect accuracy.
4. Choosing the type of model based on the data, here it is a regression model and I chose Multi-variable linear regression.
5. Fitting the model with train values predicting the result with test values.
6. Observing the accuracy between predicted and actual values and based on it deciding the choice of model.

**VISUALISATION OF THE DATA**

![](https://github.com/tinni2806/Crop-Yield-Predictive-Analysis/blob/master/Snapshots/Capture2.jpg)

**RELATION BETWEEN INDEPENDENT AND DEPENDENT VARIABLES**

Type of seeds effecting the yield

![](https://github.com/tinni2806/Crop-Yield-Predictive-Analysis/blob/master/Snapshots/Capture3.jpg)

Type of soil effecting the yield

![](https://github.com/tinni2806/Crop-Yield-Predictive-Analysis/blob/master/Snapshots/Capture4.jpg)

Type of fertilizer effecting the yield

![](https://github.com/tinni2806/Crop-Yield-Predictive-Analysis/blob/master/Snapshots/Capture5.jpg)

Type of season effecting the yield

![](https://github.com/tinni2806/Crop-Yield-Predictive-Analysis/blob/master/Snapshots/Capture6.jpg)


**USER INTERFACE**

The means by which the User and the computer system interact,in particular the use of input devices and software.

By deploying the code into the Watson Studio in IBM cloud we can generate a scoring uid.

To generate a Flow we use NODE-RED flow editor.

NODE-RED is a flow based development tool for visual programming developed by IBM for wiring together hardware devices, APIs and Online services.

**CONCLUSION**

Predictive analysis in agriculture is crop yield monitoring concept. Implementation of this concept should help farmer to produce higher yield. System can find required amount of land, water, fertilizer, pesticides to maximize the crop product. So that farmers obtain a return on their investment by saving on fertilizer cost. Another benefit of this concept is adjusting with environmental factors.

Accuracy of the model : 0.8252
