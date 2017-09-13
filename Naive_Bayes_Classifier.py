
# coding: utf-8

# In[97]:

import pandas as pd
data = pd.read_csv('西瓜数据集3_0.csv',sep=',')
print ("Num of rows: "+ str(data.shape[0]))
print ("Num of columns: "+ str(data.shape[1]))


# In[157]:

data.head()


# In[163]:

num_total=data.shape[0]
num_good=data[data['好瓜']=='是'].shape[0]
num_not_good=num_total-num_good


# In[162]:

p_good_density_mean=data[data['好瓜']=='是']['密度'].mean()
print('好瓜密度平均值： '+str(p_good_density_mean))
p_good_density_std=data[data['好瓜']=='是']['密度'].std()
print('好瓜密度标准差： '+str(p_good_density_std))
p_not_good_density_mean=data[data['好瓜']=='否']['密度'].mean()
print('坏瓜密度平均值： '+str(p_not_good_density_mean))
p_not_good_density_std=data[data['好瓜']=='否']['密度'].std()
print('坏瓜密度标准差： '+str(p_not_good_density_std))
p_good_sweet_mean=data[data['好瓜']=='是']['含糖率'].mean()
print('好瓜含糖率平均值： '+str(p_good_sweet_mean))
p_good_sweet_std=data[data['好瓜']=='是']['含糖率'].std()
print('好瓜含糖率标准差： '+str(p_good_sweet_std))
p_not_good_sweet_mean=data[data['好瓜']=='否']['含糖率'].mean()
print('坏瓜含糖率平均值： '+str(p_not_good_sweet_mean))
p_not_good_sweet_std=data[data['好瓜']=='否']['含糖率'].std()
print('坏瓜含糖率标准差： '+str(p_not_good_sweet_std))


# In[160]:

#拉普拉斯修正
pn={'色泽':3,'根蒂':3,'敲声':3,'纹理':3,'脐部':3,'触感':2}


# In[78]:

test_sample_1={'色泽':'青绿','根蒂':'蜷缩','敲声':'浊响','纹理':'清晰','脐部':'凹陷','触感':'硬滑','密度':0.697,'含糖率':0.460}


# In[164]:

from scipy.stats import norm
p1=(num_good+1)/(num_total+2)
for key in test_sample_1:
    print (key)
    if(type(data[key][0])==str):
        pc=((data[(data[key]==test_sample_1[key]) & (data['好瓜']=='是')].shape[0])+1)/(num_good+pn[key])
    else:
        pc=norm.pdf(test_sample_1[key], data[data['好瓜']=='是'][key].mean(), data[data['好瓜']=='是'][key].std())
    print("pc="+str(pc))
    p1*=pc
print ('样本1为好瓜的后验概率为:'+str(p1))


# In[166]:

p2=num_not_good/num_total
for key in test_sample_1:
    print (key)
    if(type(data[key][0])==str):
        pc=((data[(data[key]==test_sample_1[key]) & (data['好瓜']=='否')].shape[0])+1)/(num_not_good+pn[key])
    else:
        pc=norm.pdf(test_sample_1[key], data[data['好瓜']=='否'][key].mean(), data[data['好瓜']=='否'][key].std())
    print("pc="+str(pc))
    p2*=pc
print ('样本1为坏瓜的后验概率为:'+str(p2))


# In[167]:

if(p1>p2):
    print('样本1为好瓜')
else:
    print('样本1为坏瓜')

