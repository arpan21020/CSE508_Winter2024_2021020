from Components.data_preprocessing import DataPreprocessing

obj=DataPreprocessing("Loving these vintage springs on my vintage strat. They have a good tension and great stability. If you are floating your bridge and want the most out of your springs than these are the way to go.")
obj.process_all()
print(obj.data)