oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

# SECTION A:
oscar_winners.add("Emma Watson")
print('SECTION A:',oscar_winners)

# SECTION B:
oscar_copy = oscar_winners.copy()
oscar_copy.discard("Meryl Streep")
print('BEFORE CLR:',oscar_copy)
oscar_copy.clear()
print('SECTION B:', oscar_copy)

# SECTION C:
print('SECTION C:',titanic_actors & dark_knight_actors)

# SECTION D:
print('SECTION D:',iron_man_actors & avengers_actors)

# SECTION E:
print('SECTION E:',actor_list <= oscar_winners)

# SECTION F:
print('SECTION F:',actor_list >= avengers_actors)

# SECTION G:
movie_cast.pop()    # RANDOM REMOVE!!!!!!
print('SECTION G:',movie_cast)

# SECTION H:
movie_cast.discard("Matt Damon")
print('SECTION H:',movie_cast)

# SECTION I:
print('SECTION I:',titanic_actors - oscar_copy)

# SECTION J:
print('SECTION J:',titanic_actors ^ dark_knight_actors)

# SECTION K:
oscar_copy.update({"Cate Blanchett", "Daniel Day-Lewis"})
print('SECTION K:',oscar_winners)

# SECTION L:
print('SECTION L:',titanic_actors | dark_knight_actors)