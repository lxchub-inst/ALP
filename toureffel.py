import turtle as t

# Fonction pour dessiner un rectangle
def draw_rectangle(width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# Configuration de la fenêtre
t.bgcolor("white")
t.title("Tour Eiffel Simplifiée avec Pieds")
t.speed(10)  # Vitesse de dessin

# Dessiner la base de la Tour Eiffel
t.penup()
t.goto(-50, -150)
t.pendown()
draw_rectangle(100, 20)

# Dessiner la première section de la Tour Eiffel
t.penup()
t.goto(-30, -130)
t.pendown()
draw_rectangle(60, 10)

# Dessiner la deuxième section de la Tour Eiffel
t.penup()
t.goto(-20, -120)
t.pendown()
draw_rectangle(40, 10)

# Dessiner la troisième section de la Tour Eiffel
t.penup()
t.goto(-10, -110)
t.pendown()
draw_rectangle(20, 10)

# Dessiner le sommet de la Tour Eiffel
t.penup()
t.goto(0, -100)
t.pendown()
t.goto(0, 50)

# Dessiner les pieds de la Tour Eiffel
t.penup()
t.goto(-20, -100)
t.pendown()
for _ in range(4):
    t.forward(20)
    t.left(90)

# Cacher la tortue
t.hideturtle()

# Fermer la fenêtre en cliquant dessus
t.exitonclick()
