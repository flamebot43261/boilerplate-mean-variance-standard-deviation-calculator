import numpy as np

def calculate(list):

    #this if statement is for error handling. if the length of the 
    #given list is not equal to 9 digits, then the function raises
    #a value error, along with the message "List must contain nine numbers."
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")
    
    #converts the list into a numpy array.
    a = np.array(list)

    #converts the default 1x9 array into a 3x3 array.
    array = a.reshape(3,3)

    #return array
    calculations = {
        #returns the respective value using the axes. axis = 0 means that it reads the values from top to bottom
        # and axis = 1 reads the values from left to right. The .tolist() function turns the array values into lists,
        #for improved legibility in the output.
        'mean': [np.mean(array,axis = 0).tolist(),np.mean(array,axis = 1).tolist(),np.mean(array)] ,
        'variance':[np.var(array,axis = 0).tolist(),np.var(array,axis = 1).tolist(),np.var(array)] ,
        'standard deviation':[np.std(array,axis = 0).tolist(),np.std(array,axis = 1).tolist(),np.std(array)] ,
        'max':[np.max(array,axis = 0).tolist(),np.max(array,axis = 1).tolist(),np.max(array)] ,
        'min':[np.min(array,axis = 0).tolist(),np.min(array,axis = 1).tolist(),np.min(array)] ,
        'sum': [np.sum(array,axis = 0).tolist(),np.sum(array,axis = 1).tolist(),np.sum(array)]
    }

    return calculations
