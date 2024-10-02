from vector2d import Vector2D

class Node:
    def __init__(self, position=None, parent=None):
        if position is None:
            position = Vector2D()  # Default to (0, 0) if no position is given
        self.position = position  # Ensure this is a Vector2D object
        self.parent = parent
        self.g = 0  # Distance from start node
        self.h = 0  # Heuristic distance to goal node
        self.f = 0  # Total cost (f = g + h)

    # Compare nodes based on position for equality
    def __eq__(self, other):
        return self.position == other.position if isinstance(other, Node) else False
    
    def __repr__(self):
        return f"Node(position={self.position}, g={self.g}, h={self.h}, f={self.f})"

    # Add a method to return the position as Vector2D
    def to_vector2d(self):
        return self.position  # Already a Vector2D object

"""
# A node class to store information about each node in the search space
class Node:
    def __init__(self, position=None, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance from start node
        self.h = 0  # Heuristic distance to goal node
        self.f = 0  # Total cost (f = g + h)

    # Compare nodes based on f value for the priority queue
    def __eq__(self, other):
        return self.position == other.position
    
    def __repr__(self):
        return f"Node(position={self.position}, g={self.g}, h={self.h}, f={self.f})"
        
        """