<h1>Python Exercises</h1>
As part of the second submission task for the Data Science module, Python, NumPy, Jupiter Notebook and Panda data frame were used.
<br>
<h2>Q1: Write 2 python function to get the indices of the sorted elements of given lists and compare the speed. one is without numpy package and the other is with numpy. (raise a error message if the input is null or not numerical)</h2>
<ul>
  <li>List 1: [23, 104, 5, 190, 8, 7, -3]</li>
  <li>List 2 : []</li>
  <li>List 3 : random generate 1000000 integers </li>
</ul>
<br>
The output for exercise Q1 is (output for list3 is commented out):
<br>
<div>
Sorted indices without NumPy for list 1: [6, 2, 5, 4, 0, 1, 3] <br>
<b>Time taken without NumPy for list1: 0.000997304916381836 seconds</b> <br>
Sorted indices with NumPy for list 1: [6 2 5 4 0 1 3]<br>
<b>Time taken with NumPy for list1: 0.0 seconds</b><br>
Input list is empty<br>
Input list is empty<br>
<b>Time taken without NumPy for list3: 1.224100112915039 seconds</b><br>
<b>Time taken with NumPy for list3: 0.402069091796875 seconds</b><br>
</div>
<br>
As we aspected the output time with NumPy is much shorter.

<h2>Q2: Do the following exercise in a Jupyter Notebook</h2>
<ul>
  <li> Load the countries.csv directly via URL import into your panda data frame!</li>
  <li>Display descriptive statistics for the numerical column (count, mean, std, min, 25%, 50%, 75%, max) HINT: describe</li>
  <li>Show the last 4 rows of the data frame.</li>
  <li>Show all the rows of countries that have the EURO</li>
  <li>Show only name and Currency in a new data frame</li>
  <li>Show only the rows/countries that have more than 2000 GDP (it is in Milliarden USD Bruttoinlandsprodukt)</li>
  <li>Select all countries where with inhabitants between 50 and 150 Mio</li>
  <li>Calculate the GDP average (ignore the missing value)</li>
  <li>Calculate the GDP average (missing value treated as 0)</li>
  <li>Calculate the population density (population/area)  of all countries and add as new column</li>
  <li>Sort by country name alphabetically</li>
  <li>Create a new data frame from the original where the area is changed: all countries with > 1000000 get BIG and <= 1000000 get SMALL in the cell replaced!</li>
</ul>
