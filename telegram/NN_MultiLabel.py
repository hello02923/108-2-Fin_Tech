#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
import os
os.environ["CUDA_VISIBLE_DEVICES"]= '1'
gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)


# In[50]:


dataset = pd.read_csv('/Users/lai/Downloads/Final_Dataset_NN.csv')


# In[51]:


dataset = dataset.drop(['Unnamed: 0'],axis = 1)


# In[91]:


dataset.columns[-70:]


# In[ ]:





# In[59]:


x = dataset.iloc[:,1:4116].values


# In[60]:


y = dataset.iloc[:,4116:].values


# In[82]:


y[0].shape


# In[62]:


y.shape


# In[63]:


x.shape


# In[64]:


from sklearn.model_selection import train_test_split


# In[65]:


x_train,x_val,y_train,y_val = train_test_split(x,y,test_size = 0.1,random_state = 1)


# In[146]:


model = keras.models.Sequential()
model.add(keras.layers.Dense(2000, activation="tanh",input_shape = (4115,)))
model.add(keras.layers.Dense(1000, activation="tanh"))
model.add(keras.layers.Dense(500, activation="tanh"))
model.add(keras.layers.Dense(250, activation="tanh"))
model.add(keras.layers.Dense(100, activation="tanh"))
model.add(keras.layers.Dense(70, activation="sigmoid"))


# In[147]:


model.compile(loss="binary_crossentropy",
              optimizer="sgd",
              metrics=["accuracy"])


# In[148]:


logdir = 'NN_Fintech_MultiLabel'
callbacks = keras.callbacks.TensorBoard(log_dir = logdir)


# In[149]:


history = model.fit(x_train, y_train, epochs=10,
                    validation_data=(x_val, y_val),callbacks = [callbacks])


# In[164]:


from tensorflow.keras.models import load_model


# In[165]:


model = load_model('test.h5')


# In[134]:


x_val.shape


# In[138]:


x_val[0].shape


# In[139]:


y_val[0].shape


# In[167]:


x_val[0]


# In[170]:


x_val.ndim


# In[173]:


x_val[0].ndim


# In[166]:


model.predict([[x_val[0]]])


# In[137]:


y_pred = model.predict(x_val)


# In[174]:


# model.predict(x_val[0])


# In[79]:


y_val[12]


# In[98]:


dataset.iloc[:, -70:]


# In[101]:


type(dataset)


# In[100]:


type(y_pred)


# In[96]:


dataset.columns[-70:]


# In[95]:


y_pred[12]


# In[94]:


sorted(y_pred[12], reverse=True)[:5]


# In[108]:


array = np.concatenate(y_pred[12], axis=None)


# In[112]:


df = pd.DataFrame(dataset.columns[-70:])


# In[119]:


merge = pd.DataFrame(pd.np.column_stack([df, y_pred[12]]))


# In[123]:


merge


# In[130]:


s = merge.sort_index()


# In[133]:


s.sort_values(1, ascending=False)[:5]


# In[ ]:





# In[ ]:





# In[ ]:





# In[20]:


ind = np.argpartition(y_pred[9], -11)[-11:]


# In[42]:


ind


# In[43]:


y_pred[9][ind]


# In[ ]:




