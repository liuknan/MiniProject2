from image_detect import image_detect as id
#instantiate a class instance
image=id()
# you could use this function to load a model and it will return the graph
# image.load_graph('')
# you could us this function to load labels and it will return the label
# image.load_labels('')
#change the image you want to detect
image.cfile('input the path of an image')
#change the model
image.cgraph('input the path of a model')
#change the label
image.clabel('input the path of the label')
#detect
image.detect()