# Background: Develop a Python function for calculating the area of various geometric shapes, including circles, rectangles, and triangles.

# Task: Implement a function named calculate_area that takes two parameters: a string representing the shape and a tuple of dimensions. The function should calculate the area for circles, rectangles, and triangles based on these dimensions.

# Input Specifications:

# The function accepts two arguments: the shape name (a string, one of "circle", "rectangle", or "triangle") and dimensions (a tuple).
# Circle: Requires one dimension (radius).
# Rectangle: Requires two dimensions (length, width).
# Triangle: Requires two dimensions (base, height).
# Expected Output:

# The function should return the area of the shape as a float rounded by 2 decimal places
# If an unknown shape is provided, It should raise theValueError with message f"Unknown shape: {shape}".
# If the dimensions are incorrect for the shape (e.g., negative numbers, incorrect number of dimensions), It should raise ValueError with message f"Invalid dimensions for shape: {shape}".


def calculate_area(shape, dimensions):
      # complete the function
      area=None
      try:
            if(shape=="Circle" and len(dimensions)==1):
                  for i in dimensions:
                        if(i<0):
                              raise Exception(f"Invalid dimensions for shape: {shape}")
                        else:
                              area=round(float(3.14*i*i),2)
                  return area
            elif(shape=="Rectangle" and len(dimensions)==2):
                  for i in dimensions:
                        if(i<0):
                              raise Exception(f"Invalid dimensions for shape: {shape}")
                  area=round(float(dimensions[0]*dimensions[1]),2)
                  return area
            elif(shape=="Triangle" and len(dimensions)==2):
                  for i in dimensions:
                        if(i<0):
                              raise Exception(f"Invalid dimensions for shape: {shape}")
                  area=round(float((dimensions[0]*dimensions[1])/2),2)
                  return area
            else:
                  raise Exception(f"Unknown shape: {shape}")
      except Exception as e:
            raise e
      

shape="hexagon"
dimensions=(10, 5)     
print(calculate_area(shape, dimensions))
            
            
