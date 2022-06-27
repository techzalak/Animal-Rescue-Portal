import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode("utf-8")
    buffer.close()
    return graph

def get_plot(cdog,ccat,cbird,ccow):
    plt.switch_backend('AGG')
    fig=plt.figure()
    fig.figsize=(5,5)
    fig.patch.set_facecolor('white')
    plt.title('Animals Rescued')
    labels='Dog','Cat','Bird','Cow'
    sizes=[cdog,ccat,cbird,ccow]
    colors = ['yellow', 'pink', 'blue', 'red']
    explode = (0.1, 0, 0, 0)  
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.xticks(rotation=45)
    plt.tight_layout()
    graph=get_graph()
    return graph

def get_bargraph():
    buffer=BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    barimage_png=buffer.getvalue()
    graph=base64.b64encode(barimage_png)
    graph=graph.decode("utf-8")
    buffer.close()
    return graph

def get_barplot(x,y):
    plt.switch_backend('AGG')
    fig=plt.figure()
    fig.figsize=(5,5)
    fig.patch.set_facecolor('white')
    plt.title('Animals Rescued')
    plt.bar(x,y,color='DeepSkyBlue')
    plt.xticks(rotation=45)
    plt.xlabel('Cities')
    plt.ylabel('No. of animals rescued')
    plt.tight_layout()
    graph=get_bargraph()
    return graph
