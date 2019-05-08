import matplotlib.pyplot as plt
#creating a graph structure
    x = [268, 609, 366, 230, 895] #received data by running application on local machine several time
    y = [0.0003647804260253906, 0.00010395050048828125, 0.0002181529998779297, 0.00023603439331054688, 0.00037789344787597656]
    plt.plot(x,color='orange')
    plt.plot(y, color='g')
    plt.xlabel('size')
    plt.ylabel('runtime')
    plt.title('sort method')
    plt.show()
