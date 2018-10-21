# MiniProject2
It's a MiniPorject about image recognition

## 1.retrain.py
For image recognition, you need to train your model before you use it, so retrain.py is a good python program to train your own model.
To use it, you need to program it with command line and run it with at least one argument "--image_dir". Then, the program will traverse 
the image directory and find all the images in it(the type of those images should be ".jpg"). After that, the program will train a model(or your model)
with these images and output a ".pb" file, a label file to your "~/tmp/" path, which means you'd better not reboot your computer, or the
new model and label will disappear(you could use some arguments to change the directory of the output path, I will list these arguments later)
### Arguments for Retrain.py
'--image_dir',  
default='',  
Path to folders of labeled images.  
  
'--output_graph',  
default='/tmp/output_graph.pb',  
Where to save the trained graph.  
  
'--intermediate_output_graphs_dir',  
default='/tmp/intermediate_graph/',  
Where to save the intermediate graphs.  
  
'--intermediate_store_frequency',  
default=0,How many steps to store intermediate graph.   
If "0" then will not store.  
  
'--output_labels',  
default='/tmp/output_labels.txt',  
help='Where to save the trained graph\'s labels.'  
  
'--summaries_dir',  
default='/tmp/retrain_logs',  
Where to save summary logs for TensorBoard.  
  
'--how_many_training_steps'  
default=4000,  
How many training steps to run before ending.  
  
 '--learning_rate',  
  default=0.01,  
  How large a learning rate to use when training.  
    
  '--testing_percentage',  
  default=10,  
  'What percentage of images to use as a test set.'  
    
  '--validation_percentage',  
  default=10,  
  'What percentage of images to use as a validation set.'  
    
  '--eval_step_interval',  
  default=10,  
  'How often to evaluate the training results.'  
    
  '--train_batch_size',  
  default=100,  
  'How many images to train on at a time.'  
    
  '--test_batch_size',  
  default=-1,  
  How many images to test on. This test set is only used once, to evaluate
  the final accuracy of the model after training completes.
  A value of -1 causes the entire test set to be used, which leads to more
  stable results across runs.
  
  '--validation_batch_size'  
  default=100,  
  How many images to use in an evaluation batch. This validation set is
      used much more often than the test set, and is an early indicator of how
      accurate the model is during training.
      A value of -1 causes the entire validation set to be used, which leads to
      more stable results across training iterations, but may be slower on large
      training sets.
      
  ## 2.image_label.py
