# Define a class
class Circle:
    def __init__(self, radius):  # Constructor to initialize the Circle
        self.radius = radius  # Instance attribute
    
    def area(self):  # Method to calculate area
        return 3.14 * (self.radius ** 2)
    
    def circumference(self):  # Method to calculate circumference
        return 2 * 3.14 * self.radius
    
    def resize(self, new_radius):  # Method to change the radius
        self.radius = new_radius
        print(f"Radius updated to: {self.radius}")

# Define another class that manages shapes
class ShapeManager:
    def __init__(self):
        self.shapes = []  # Initialize an empty list to store shapes
    
    def add_shape(self, shape):  # Add a shape to the list
        self.shapes.append(shape)
        print(f"Shape added. Total shapes: {len(self.shapes)}")
    
    def calculate_all_areas(self):  # Calculate and print areas of all shapes
        for index, shape in enumerate(self.shapes):
            print(f"Shape {index + 1} Area: {shape.area()}")
    
    def calculate_all_circumferences(self):  # Calculate and print circumferences
        for index, shape in enumerate(self.shapes):
            print(f"Shape {index + 1} Circumference: {shape.circumference()}")

# Example usage
if __name__ == "__main__":
    # Create a Circle object
    my_circle = Circle(5)  # Circle with radius 5
    print(f"Circle Radius: {my_circle.radius}")
    print(f"Circle Area: {my_circle.area()}")
    print(f"Circle Circumference: {my_circle.circumference()}")
    
    # Resize the circle
    my_circle.resize(7)  # Change the radius to 7
    print(f"Updated Circle Area: {my_circle.area()}")
    
    # Create a ShapeManager object
    manager = ShapeManager()
    
    # Add shapes to the manager
    manager.add_shape(my_circle)
    manager.add_shape(Circle(10))  # Add another circle with radius 10
    
    # Calculate areas and circumferences of all shapes in the manager
    manager.calculate_all_areas()
    manager.calculate_all_circumferences()
