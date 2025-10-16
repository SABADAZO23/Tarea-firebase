from user_service import UserService

def mostrar_menu():
    print("\n" + "="*50)
    print("🎮 CRUD INTERACTIVO - TÚ CONTROLAS")
    print("="*50)
    print("1. 📝 CREAR usuario")
    print("2. 👀 VER todos los usuarios") 
    print("3. 🔍 BUSCAR usuario por ID")
    print("4. ✏️ ACTUALIZAR usuario")
    print("5. 🗑️ ELIMINAR usuario")
    print("6. 📊 CONTAR usuarios")
    print("0. ❌ SALIR")
    print("="*50)

def main():
    usuarios = UserService()
    
    print("🚀 BIENVENIDO AL CRUD INTERACTIVO")
    print("💡 Tú decides qué hacer en cada momento")
    
    while True:
        mostrar_menu()
        opcion = input("\n🎯 ¿Qué quieres hacer? (0-6): ")
        
        if opcion == "1":
           
            print("\n📝 CREANDO NUEVO USUARIO")
            nombre = input("Nombre: ")
            email = input("Email: ")
            edad = int(input("Edad: "))
            
            usuario_id = usuarios.crear_usuario(nombre, email, edad)
            if usuario_id:
                print(f"🎉 ¡Creado! ID: {usuario_id}")
        
        elif opcion == "2":
            
            print("\n👀 LISTA DE TODOS LOS USUARIOS:")
            todos = usuarios.obtener_todos()
            
            if not todos:
                print("📭 No hay usuarios registrados")
            else:
                for i, user in enumerate(todos, 1):
                    print(f"{i}. {user['nombre']} - {user['email']} - {user['edad']} años")
                    print(f"   ID: {user['id']}")
                    print()
        
        elif opcion == "3":
            print("\n🔍 BUSCAR USUARIO POR ID")
            user_id = input("Ingresa el ID del usuario: ")
            
            usuario = usuarios.obtener_usuario(user_id)
            if usuario:
                print(f"✅ ENCONTRADO:")
                print(f"   Nombre: {usuario['nombre']}")
                print(f"   Email: {usuario['email']}")
                print(f"   Edad: {usuario['edad']} años")
                print(f"   Creado: {usuario['creado_en']}")
            else:
                print("❌ Usuario no encontrado")
        
        elif opcion == "4":
            
            print("\n✏️ ACTUALIZAR USUARIO")
            user_id = input("ID del usuario a actualizar: ")
            
          
            usuario = usuarios.obtener_usuario(user_id)
            if not usuario:
                print("❌ Usuario no encontrado")
                continue
            
            print(f"📋 Actualizando a: {usuario['nombre']}")
            print("💡 Deja en blanco los campos que NO quieras cambiar")
            
            nuevo_nombre = input(f"Nuevo nombre [{usuario['nombre']}]: ")
            nuevo_email = input(f"Nuevo email [{usuario['email']}]: ")
            nueva_edad = input(f"Nueva edad [{usuario['edad']}]: ")
            
            campos_actualizar = {}
            if nuevo_nombre:
                campos_actualizar['nombre'] = nuevo_nombre
            if nuevo_email:
                campos_actualizar['email'] = nuevo_email
            if nueva_edad:
                campos_actualizar['edad'] = int(nueva_edad)
            
            if campos_actualizar:
                if usuarios.actualizar_usuario(user_id, **campos_actualizar):
                    print("✅ ¡Actualizado correctamente!")
            else:
                print("⚠️ No se cambiaron campos")
        
        elif opcion == "5":
            
            print("\n🗑️ ELIMINAR USUARIO")
            user_id = input("ID del usuario a eliminar: ")
            
            usuario = usuarios.obtener_usuario(user_id)
            if usuario:
                print(f"⚠️ Vas a eliminar: {usuario['nombre']} - {usuario['email']}")
                confirmar = input("¿Estás seguro? (s/n): ")
                
                if confirmar.lower() == 's':
                    if usuarios.eliminar_usuario(user_id):
                        print("✅ ¡Usuario eliminado!")
                else:
                    print("❌ Eliminación cancelada")
            else:
                print("❌ Usuario no encontrado")
        
        elif opcion == "6":
           
            print("\n📊 CONTANDO USUARIOS")
            todos = usuarios.obtener_todos()
            print(f"👥 Total de usuarios: {len(todos)}")
        
        elif opcion == "0":
            
            print("\n👋 ¡Hasta luego!")
            break
        
        else:
            print("❌ Opción inválida. Intenta de nuevo.")
        
        input("\n⏎ Presiona Enter para continuar...")

if __name__ == "__main__":
    main()