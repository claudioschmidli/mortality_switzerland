<h1><center>Analysis and prediction of deaths in Switzerland</center></h1>
<h2><center>Project work, time series analysis FHNW Brugg</center></h2>
<h3><center>Claudio Schmidli</center></h3>
<h4><center>30.06.2023</center></h4>

In this timeseries project, I aim to analyze the weekly deaths in Switzerland and forecast future trends. Understanding the patterns and trends in mortality rates can provide valuable insights for various purposes, such as public health planning, resource allocation, and policy decision-making. By leveraging the power of data analysis and predictive modeling, we can gain a better understanding of the underlying factors driving mortality and make informed projections.

**Data source**<br>
The data for this project is sourced from the Swiss Federal Statistical Office. The dataset contains information on weekly numbers of deaths, expected deaths, and excess mortality by age groups (0-64, 65+), covering the period from 2010 to 2023.


<table>
<thead>
  <tr>
  </tr>
</thead>
<tbody>
<tr>
    <td>Label</td>
    <td>Weekly Deaths, 2010-2023</td>
  </tr>
<tr>
    <td>Publisher</td>
    <td>Federal Statistical Office</td>
  </tr>
  <tr>
  <tr>
    <td>Copyright</td>
    <td>Federal Statistical Office</td>
  </tr>
  <tr>
    <td>Terms of Use</td>
    <td>OPEN-BY-ASK</td>
  </tr>
  <tr>
    <td>Topic</td>
    <td>Health</td>
  </tr>
  <tr>
    <td>Federal Statistical Office Number</td>
    <td>ts-d-14.03.04.03-wr</td>
  </tr>
  <tr>
    <td>Data Collection, Statistics</td>
    <td><a href="https://www.bfs.admin.ch/bfs/en/home/statistics/health/surveys/ecod.html">Statistics of Causes of Death and Stillbirths</a></td>
  </tr>
  <tr>
    <td>Related Documents</td>
    <td><a href="https://www.bfs.admin.ch/bfs/en/home/statistics/catalogues-databases/gnpdetail.2023-0076.html" target="_blank" rel="noopener noreferrer">Mortality Monitoring (MOMO): Weekly Update</a></td>
  </tr>
  <tr>
    <td>Source</td>
    <td><a href="https://www.bfs.admin.ch/bfsstatic/dam/assets/25985341/master" target="_blank" rel="noopener noreferrer">CSV File</a></td>
  </tr>
</tbody>
</table>


**Data Visualization and Exploratory Data Analysis:**<br>
Before delving into the modeling process, I begin by visualizing the weekly death data to gain a preliminary understanding. I explore the data for any apparent seasonal patterns and assess its stationarity.

**Utilizing ARIMA for Model Fitting and Prediction:**<br>
Then I employ the ARIMA (AutoRegressive Integrated Moving Average) modeling technique to capture the dynamics of the weekly death data in Switzerland. ARIMA is a powerful tool for timeseries analysis, as it combines both autoregressive (AR) and moving average (MA) components with differencing to handle non-stationarity. After fitting an appropriate ARIMA model to the historical data, future values can be predicted.
In this project I will create two different ARIMA models. 

1. In the first approach, I manually select the order parameters for the ARIMA model based on my observations from the exploratory data analysis. Additionally, I perform a data transformation to remove the seasonal patterns and make the data stationary. This transformation ensures that the model captures the underlying patterns more effectively. I evaluate the model's performance by analyzing the residuals, density plot, autocorrelation function (ACF), partial autocorrelation function (PACF) and comparing the model to the actual (true) values. The later is done using different metrics as well as with visualizations.
2. In the second approach, I utilize a Python package to automatically fit an ARIMA model to the original, untransformed data. To handle the non-stationarity of the data, the differencing order parameter (I) of the ARIMA model is set to a value > 0. This allows the model to account for the trend and seasonality in the data itself (no pre-processing needed). The quality of the model is assessed in the same way as in approach 1.

**Conclusion**<br>
Finally, I compare the manually created model with the model generated by auto ARIMA. I discuss the outcome of both approaches and the final outcome of the project.

**Literature on this topic:**<br>
https://www.hanser-elibrary.com/doi/book/10.3139/9783446468146
