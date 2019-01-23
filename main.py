# Import libraries ------------------------------------------------------------------------
import numpy as np


# Define Functions ------------------------------------------------------------------------
def infoGain(l_dataset, r_dataset): # NEEDS IMPLEMENTING
    gain = 0
    return gain


def FIND_SPLIT(dataset): # DONE. CHECK?
    max_gain = 0
    best_split = [0, 0]
    
    for attr in range(dataset.shape[1]-1):
        # Sort dataset by this attribute column
        ordered = a[a[:,attr].argsort(),:]
        
        for row in range(1, ordered.shape[0]):
            # Identify potential split point
            if ordered[row, -1] != ordered[row-1, -1]:
                # 1. FIND SPLIT
                value = np.mean([ordered[row-1, attr], ordered[row, attr]])
                split = [attr, value]
                
                # 2. SPLIT DATASET BY THIS
                l_dataset, r_dataset = split_dataset(split)
                
                # 3. COMPUTE INFORMATION GAIN
                gain = infoGain(l_dataset, r_dataset)
                
                # 4. IF THIS IS HIGHEST GAIN, UPDATE MAX_GAIN and BEST_SPLIT
                if gain > max_gain:
                    max_gain = gain
                    best_split = split
    
    return best_split


def is_leaf(dataset): # DONE. CHECK?
    if len(np.unique(dataset[:,-1])) == 1:
        return 1
    else:
        return 0


def split_dataset(split): # NEEDS IMPLEMENTING
    
    return l_dataset, r_dataset


def DECISION_TREE_LEARNING(dataset, depth=0): # DONE. CHECK?
    if is_leaf():
        node = {'attribute': [], 'value': [], 'left': [], 'right': [], 'leaf': 1}
        return node, depth
    else:
        split = FIND_SPLIT(dataset)
        l_dataset, r_dataset = split_dataset(split)
        node = {'attribute': split[0], 'value': split[1], 'left': {}, 'right': {}, 'leaf': 0}
        l_branch, l_depth = DECISION_TREE_LEARNING(l_dataset, depth+1)
        node['left'] = l_branch
        r_branch, r_depth = DECISION_TREE_LEARNING(r_dataset, depth+1)
        node['right'] = r_branch
        return node, max([l_depth, r_depth])

# Main -----------------------------------------------------------------------------------
if __name__ == "__main__":
    # LOAD DATASET
    dataset = np.loadtxt('wifi_db/clean_dataset.txt')

    # TRAIN TREE
    tree, depth = DECISION_TREE_LEARNING(dataset, depth=0)

