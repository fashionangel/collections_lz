import numpy as np
import matplotlib.pyplot as plt             
#область определения
x = np.linspace(0,10,100)       
#функция           
y = -x**5 + x**2 + x -13     
#создаем график                   
plt.plot(x, y)         
#рисуем его                     
plt.show()                                  