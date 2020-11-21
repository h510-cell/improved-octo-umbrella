import pandas as pd
import csv
import statistics

#reading scores data
df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()
#Calculating the mean and standard deviation
mean = sum(data) / len(data)
std_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)
#Finding 1 standard deviation start and end values ,and 2 standard deviation start and end values
first_std_deviation_start,first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start,second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
#Printing the findings
list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]
print("Mean of this data is {}" .format(mean))
print("Meadian of this data is {}" .format(median))
print("Mode of this data is {}" .format(mode))
print("Standard Deviation of this data is {}".format(std_deviation))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))