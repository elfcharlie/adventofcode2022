import numpy as np
import pandas as pd
# Setup directories

directories = {}

#loading in input data
input = np.loadtxt("input.txt", dtype = "str")
#input = ["30373", "25512", "65332", "33549", "35390"]


class Forest:
    def __init__(self, input):
        self.trees = np.ndarray((len(input),len(input[0])),dtype=object)
        self.add_trees(input)
        self.set_neighbours()
        self.set_visible()

    def add_trees(self, input):
        for row in range(len(input)):
            for col in range(len(input[row])):
                self.trees[row][col] = Tree(int(input[row][col]))

    def print(self):
        temp_trees = [[None] * len(input[0])] * len(input)
        for row in range(len(self.trees[0])):
            for col in range(len(self.trees[0])):
                temp_trees[row][col] = self.trees[row][col].get_height()
        print(temp_trees)

    def set_neighbours(self):
        x = 0
        for row in range(len(self.trees)):
            for col in range(len(self.trees[0])):
                if col > 0:
                    self.trees[row][col].left_neighbour = self.trees[row][col - 1]
                    x+=1
                if col < (len(self.trees[row]) - 1):
                    self.trees[row][col].right_neighbour = self.trees[row][col + 1]
                    x+=1
                if row > 0:
                    self.trees[row][col].top_neighbour = self.trees[row - 1][col]
                    x+=1
                if row < (len(self.trees[row]) - 1):
                    self.trees[row][col].bottom_neighbour = self.trees[row + 1][col]
                    x+=1
                
    def set_visible(self):
        edge_trees = []
        for row in range(len(self.trees)):
            for col in range(len(self.trees[row])):
                if row == 0 or (row == len(self.trees[row]) - 1) or col == 0 or (col == len(self.trees[row]) - 1):
                    self.trees[row][col].visible = True
                    edge_trees.append(self.trees[row][col])
        
        
        for tree in edge_trees:
            visible_height = tree.height
            if tree.left_neighbour == None:
                current_tree = tree
                
                while current_tree.right_neighbour != None:
                    
                    if current_tree.right_neighbour.height > visible_height and current_tree.right_neighbour not in edge_trees:
                        current_tree.right_neighbour.visible = True
                        visible_height = current_tree.right_neighbour.height
                    current_tree = current_tree.right_neighbour
            
            if tree.right_neighbour == None:
                current_tree = tree
                while current_tree.left_neighbour != None:
                    if current_tree.left_neighbour.height > visible_height and current_tree.left_neighbour not in edge_trees:
                        current_tree.left_neighbour.visible = True
                        visible_height = current_tree.left_neighbour.height
                    current_tree = current_tree.left_neighbour
            
            if tree.top_neighbour == None:
                current_tree = tree
                while current_tree.bottom_neighbour != None:
                    if current_tree.bottom_neighbour.height > visible_height and current_tree.bottom_neighbour not in edge_trees:
                        current_tree.bottom_neighbour.visible = True
                        visible_height = current_tree.bottom_neighbour.height
                    current_tree = current_tree.bottom_neighbour

            if tree.bottom_neighbour == None:
                current_tree = tree
                while current_tree.top_neighbour != None:
                    if current_tree.top_neighbour.height > visible_height and current_tree.top_neighbour not in edge_trees:
                        current_tree.top_neighbour.visible = True
                        visible_height = current_tree.top_neighbour.height
                    current_tree = current_tree.top_neighbour                

    def get_visible_trees(self):
        total_visible_trees = 0
        for row in range(len(self.trees)):
            for col in range(len(self.trees[0])):
                if self.trees[row][col].visible == True:
                    #print(str(row) + ", " + str(col))
                    total_visible_trees += 1
        return total_visible_trees

    def get_scenic_score(self):

        scenic_score = 0
        for row in range(len(self.trees)):
            for col in range(len(self.trees[row])):
                tree = self.trees[row][col]
                left_score = 0
                right_score = 0
                top_score = 0
                bottom_score = 0

                visible_height = tree.height
                
                if tree.left_neighbour == None or tree.right_neighbour == None or tree.top_neighbour == None or tree.bottom_neighbour == None:
                    continue
                else:
                    current_tree = tree
                    left_score = 0
                    right_score = 0
                    top_score = 0
                    bottom_score = 0
                    
                    while current_tree.right_neighbour != None:
                        if current_tree.right_neighbour.height < visible_height:
                            right_score += 1
                            current_tree = current_tree.right_neighbour
                        else:
                            right_score += 1
                            break

                    current_tree = tree
                    while current_tree.left_neighbour != None:
                        if current_tree.left_neighbour.height < visible_height:
                            left_score += 1
                            current_tree = current_tree.left_neighbour
                        else:
                            left_score += 1
                            break
                
                
                    current_tree = tree
                    while current_tree.bottom_neighbour != None:
                        if current_tree.bottom_neighbour.height < visible_height:
                            bottom_score += 1
                            current_tree = current_tree.bottom_neighbour
                        else:
                            bottom_score += 1
                            break

                
                    current_tree = tree
                    while current_tree.top_neighbour != None:
                        if current_tree.top_neighbour.height < visible_height:
                            top_score += 1
                            current_tree = current_tree.top_neighbour   
                        else:
                            top_score += 1
                            break

                if scenic_score < left_score * right_score * bottom_score * top_score:
                    scenic_score = left_score * right_score * bottom_score * top_score
                    print(str(row) + ", " + str(col))
                    print(str(left_score) + str(right_score) + str(bottom_score) + str(top_score))
        
        return scenic_score



                    


class Tree:
    def __init__(self, height_, visible_=False, left_neighbour_=None, right_neighbour_=None, top_neighbour_=None, bottom_neighbour_=None):
        
        self.height = height_
        self.visible = visible_
        self.left_neighbour = left_neighbour_
        self.right_neighbour = right_neighbour_
        self.top_neighbour = top_neighbour_
        self.bottom_neighbour = bottom_neighbour_

    def get_height(self):
        return self.height

forest = Forest(input)

print("Visible trees: " + str(forest.get_visible_trees()))
print("Best scenic score: " + str(forest.get_scenic_score()))








    

