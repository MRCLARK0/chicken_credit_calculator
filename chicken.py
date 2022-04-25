import math

class Chicken():
    def __init__(self, name, min_piece_per_case, min_weight_per_piece, max_weight_per_piece):
        self.name = name
        self.min_piece_per_case = min_piece_per_case
        self.min_weight_per_piece = min_weight_per_piece
        self.max_weight_per_piece = max_weight_per_piece
        self.average_weight_per_piece = math.ceil((self.max_weight_per_piece + self.min_weight_per_piece) / 2)

    def __repr__(self):
        return f"\n{self.name}\n" \
            f"Max Weight Per Piece: {self.max_weight_per_piece}\n" \
            f"Min Weight Per Piece: {self.min_weight_per_piece}\n" \
            f"Min Piece Per Case: {self.min_piece_per_case}\n" \
            f"Average Weight Per Piece: {self.average_weight_per_piece}\n" 
        

        # getters and setters
        @property
        def name(self):
            return self.name
        
        @name.setter
        def name(self, value):
            self.name = value

        @property
        def min_piece_per_case(self):
            return self.min_piece_per_case

        @min_piece_per_case.setter
        def min_piece_per_case(self, value):
            self.min_piece_per_case = value

        @property
        def min_weight_per_piece(self):
            return self.min_weight_per_piece

        @min_weight_per_piece.setter
        def min_weight_per_piece(self, value):
            self.min_weight_per_piece = value

        @property
        def max_weight_per_piece(self):
            return self.max_weight_per_piece

        @max_weight_per_piece.setter
        def max_weight_per_piece(self, value):
            self.max_weight_per_piece = value

        @property
        def average_weight_per_piece(self):
            return self.average_weight_per_piece

        @average_weight_per_piece.setter
        def average_weight_per_piece(self, value):
            self.average_weight_per_piece = value

