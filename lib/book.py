#!/usr/bin/env python3

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}"

        