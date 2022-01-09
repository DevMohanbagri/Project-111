import csv 
import pandas as pd 
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as stats
import random

df = pd.read_csv('medium_data.csv')
data = df['responses'].tolist()

#plotting the graph
fig = ff.create_distplot([data], ['responses'], show_hist = False)
fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(1,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = stats.mean(dataset)
    return mean

#getting mean of 100 sample data of size 30 each
mean_list = []
for i in range(0,100):
    mean_sample = random_set_of_mean(30)
    mean_list.append(mean_sample)

mean_population = stats.mean(mean_list)
stdev = stats.stdev(mean_list)

mean_population = stats.mean(data)
stdev_population = stats.stdev(data)

print("Mean of population",mean_population)
print("STdev of population",stdev_population)
#print(mean_list)
stdev = stats.stdev(mean_list)
mean = stats.mean(mean_list)
print("Mean of sampling distribution",mean)
print("STdev of sampling distribution",stdev)

first_stdev_start, first_stdev_end = mean-stdev , mean+stdev
second_stdev_start, second_stdev_end = mean-(2*stdev) , mean+(2*stdev)
third_stdev_start, third_stdev_end = mean-(3*stdev), mean +(3*stdev)


list_of_data_within_1_std_deviation = [result for result in mean_list if result > first_stdev_start and result < first_stdev_end]
print("{}% of data lies within one standard deviation".format(len(list_of_data_within_1_std_deviation)*100/len(mean_list)))


list_of_data_within_2_std_deviation = [result for result in mean_list if result > second_stdev_start and result < second_stdev_end]
print("{}% of data lies within two standard deviation".format(len(list_of_data_within_2_std_deviation)*100/len(mean_list)))

list_of_data_within_3_std_deviation = [result for result in mean_list if result > third_stdev_start and result < third_stdev_end]
print("{}% of data lies within three standard deviation".format(len(list_of_data_within_3_std_deviation)*100/len(mean_list)))


fig = ff.create_distplot(
    [mean_list],
    ['responses']
    show_hist = False
)

fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_stdev_start,first_stdev_start],y = [0,0.17],mode = "lines",name = "STDEV 1 start"))
fig.add_trace(go.Scatter(x = [first_stdev_end,first_stdev_end],y = [0,0.17],mode = "lines",name = "STDEV 1 end"))
fig.add_trace(go.Scatter(x = [second_stdev_start,second_stdev_start],y = [0,0.17],mode = "lines",name = "STDEV 2 start"))
fig.add_trace(go.Scatter(x = [second_stdev_end,second_stdev_end],y = [0,0.17],mode = "lines",name = "STDEV 2 end"))
fig.add_trace(go.Scatter(x = [third_stdev_start,third_stdev_start],y = [0,0.17],mode = "lines",name = "STDEV 3 start"))
fig.add_trace(go.Scatter(x = [third_stdev_end,third_stdev_end],y = [0,0.17],mode = "lines",name = "STDEV 3 end"))
fig.show()


# finding the z-score using the formula
z_score = (mean_sample - mean)/stdev
print('Z score  is ',z_score)

