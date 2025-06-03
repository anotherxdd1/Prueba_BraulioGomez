usuarios={}
peliculas={}
actores={}
max_votos=0
sw_principal=True

while sw_principal:
    if peliculas:
        max_votos-=1
        pelicula_mas_votada = ""
        for titulo, info in peliculas.items():
            if info['votos'] > max_votos:
                max_votos = info['votos']
                pelicula_mas_votada = titulo
                print(" ")
        print(f"Película con más votos: '{pelicula_mas_votada}' con {max_votos} votos.")
        print(" ")
    else:
        print(" ")
        print("No hay películas votadas aún.")
    print(" ")
    print("--- Gestión de Cine ---")
    print("1. Crear cuenta de usuario")
    print("2. Gestionar películas")
    print("3. Gestionar actores")
    print("4. Añadir actor a película")
    print("5. Votar por una película")
    print("6. Salir")
    
    opcion_principal = input("Seleccione una opción: ")
    
    
    ############# CREAR CUENTA DE USUARIO ################
    
    
    if opcion_principal == '1':
        print(" ")
        new_user = input("Nombre de usuario: ")
        print(" ")
        new_key = input("Contraseña: ")
        if new_user not in usuarios:
            usuarios[new_user] = new_key
            print(" ")
            print(f"Usuario '{new_user}' creado exitosamente.")
            print(" ")
            
        else:
            print(f"El usuario '{new_user}' ya existe.")
            print(" ")
            
    ############# GESTIONAR PELICULAS ################
            
    elif opcion_principal == '2':
        print(" ")
        inicio_sesion=input("Ingrese su usuario: ")
        print(" ")
        clave=input("Ingrese su contraseña: ")
        if inicio_sesion not in usuarios or clave != usuarios[inicio_sesion]:
            print(" ")
            print("Usuario o contraseña incorrectos.")
            continue
        else:
            print(" ")
            print(f"Bienvenido {inicio_sesion}")
            print(" ")
        print("--- Gestión de Películas ---")
        print("a. Agregar película")
        print("b. Editar película")
        print("c. Eliminar película")
        print("d. Volver al menú principal")
        print(" ")
        opcion_peliculas = input("Seleccione una opción: ")
        
        if opcion_peliculas == "a":
            print(" ")
            agregar_pelicula = input("Título de la película: ")
            print(" ")
            if agregar_pelicula not in peliculas:
                peliculas[agregar_pelicula] = {'actores': [], 'votos': 0}
                print(" ")
                print(f"Película '{agregar_pelicula}' agregada.")
                print(" ")
            else:
                print(" ")
                print(f"La película '{agregar_pelicula}' ya existe.")
                print(" ")
        
        elif opcion_peliculas == "b":
            print(" ")
            edit_pelicula_vieja = input("Título de la película a editar: ")
            print(" ")
            if edit_pelicula_vieja in peliculas:
                print(" ")
                edit_pelicula_nueva = input("Nuevo título de la película: ")
                print(" ")
                peliculas[edit_pelicula_nueva] = peliculas.pop(edit_pelicula_vieja)
                print(" ")
                print(f"Película '{edit_pelicula_vieja}' editada a '{edit_pelicula_nueva}'.")
            else:
                print(f"La película '{edit_pelicula_vieja}' no existe.")
                
        elif opcion_peliculas == "c":
            print(" ")
            eliminar_pelicula = input("Título de la película a eliminar: ")
            print(" ")
            if eliminar_pelicula in peliculas:
                del peliculas[eliminar_pelicula]
                print(" ")
                print(f"Película '{eliminar_pelicula}' eliminada.")
                print(" ")
            else:
                print(f"La película '{eliminar_pelicula}' no existe.")
        
        elif opcion_peliculas == "d":
            continue
        else:
            print(" ")
            print("Opción inválida.")
            print(" ")
            
    ############# GESTIONAR ACTORES ################        
    
    elif opcion_principal == '3':
        print(" ")
        inicio_sesion=input("Ingrese su usuario: ")
        clave=input("Ingrese su contraseña: ")
        print(" ")
        if inicio_sesion not in usuarios or clave != usuarios[inicio_sesion]:
            print("Usuario o contraseña incorrectos.")
            continue
        else:
            print(f"Bienvenido {inicio_sesion}")
            print(" ")
        print("--- Gestion de Actores ---")
        print("a. Agregar actor")
        print("b. Editar actor")
        print("c. Eliminar actor")
        print("d. Volver al menú principal")
        
        opcion_actores = input("Seleccione una opción: ")
        
        if opcion_actores == 'a':
            print(" ")
            agregar_actor = input("Nombre del actor: ")
            print(" ")
            if agregar_actor not in actores:
                actores[agregar_actor] = {}
                print(" ")
                print(f"Actor '{agregar_actor}' agregado.")
                print(" ")
            else:
                print(" ")
                print(f"El actor '{agregar_actor}' ya existe.")
                print(" ")
        
        elif opcion_actores == 'b':
            print(" ")
            editar_actor_viejo=input("Nombre del actor a editar: ")
            print(" ")
            if editar_actor_viejo in actores:
                print(" ")
                editar_actor_nuevo=input("Nuevo nombre del actor: ")
                print(" ")
                actores[editar_actor_nuevo]=actores.pop(editar_actor_viejo)
                print(" ")
                print(f"Actor '{editar_actor_viejo}' editado a '{editar_actor_nuevo}'.")
                print(" ")
            else:
                print(" ")
                print(f"El actor '{editar_actor_viejo}' no existe.")
                print(" ")
                
        elif opcion_actores == 'c':
            print(" ")
            eliminar_actor=input("Nombre del actor a eliminar: ")
            print(" ")
            if eliminar_actor in actores:
                del actores[eliminar_actor]
                print(" ")
                print(f"Actor '{eliminar_actor}' eliminado.")
                print(" ")
            else:
                print(" ")
                print(f"El actor '{eliminar_actor}' no existe.")
                print(" ")
                
        elif opcion_actores == 'd':
            continue
        else:
            print(" ")
            print("Opción inválida.")
            print(" ")
    
    
    ############# AÑADIR ACTOR A PELICULA ################
    elif opcion_principal == '4':
        print(" ")
        inicio_sesion=input("Ingrese su usuario: ")
        print(" ")
        clave=input("Ingrese su contraseña: ")
        print(" ")
        if inicio_sesion not in usuarios or clave != usuarios[inicio_sesion]:
            print(" ")
            print("Usuario o contraseña incorrectos.")
            print(" ")
            continue
        else:
            print(" ")
            print(f"Bienvenido {inicio_sesion}")
            print(" ")
        print("--- Añadir Actor a Película ---")
        print(" ")
        pelicula = input("Título de la película: ")
        print(" ")
        actor = input("Nombre del actor: ")
        print(" ")
        
        if pelicula in peliculas and actor in actores:
            peliculas[pelicula]['actores'].append(actor)
            print(" ")
            print(f"Actor '{actor}' añadido a la película '{pelicula}'.")
            print(" ")
        else:
            print("Película o actor no encontrado.")
            print(" ")
            
            
    ############# VOTAR PELICULA ################
    
    
    
    elif opcion_principal == '5':
        print(" ")
        inicio_sesion=input("Ingrese su usuario: ")
        clave=input("Ingrese su contraseña: ")
        print(" ")
        print(tuple(peliculas))
        print(" ")
        if inicio_sesion not in usuarios or clave != usuarios[inicio_sesion]:
            print("Usuario o contraseña incorrectos.")
            print(" ")
            continue
        else:
            print(" ")
            print(f"Bienvenido {inicio_sesion}")
            print(" ")
        print("--- Votar por una Película ---")
        pelicula_voto = input("Título de la película a votar: ")
        print(" ")
        
        if pelicula_voto in peliculas:
            peliculas[pelicula_voto]['votos'] += 1
            print(f"Voto registrado para la película '{pelicula_voto}'.")
            print(" ")
        else:
            print("Película no encontrada.")
            print(" ")
            
    ############# SALIR ################
            
    elif opcion_principal == '6':
        print("Saliendo del programa.")
        print(" ")
        sw_principal = False
        
        
    else:
        print("Opción inválida.")
        

# Finalizar el programa
print("End of the program")

#Modificacion para probar git 