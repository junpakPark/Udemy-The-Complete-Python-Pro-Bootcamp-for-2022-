# import turtle
# # from turtle import Turtle

# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable

pokemon_name = ['Pikachu', 'Squirtle', 'Charmander']
types = ['Electiric', 'Water', 'Fire']

table = PrettyTable()
table.add_column('Pokemon Name', pokemon_name)
table.add_column('Type', types)
table.align = "l"
print(table)