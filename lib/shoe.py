#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, color, size):
        self.brand = brand
        self.color = color
        self.size = size

    def is_available_in_size(self, target_size):
        return self.size == target_size
