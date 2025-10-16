import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

class UserService:
    def __init__(self):

        if not firebase_admin._apps:
            cred = credentials.Certificate(r"C:\Users\Estudiante\Documents\POO\TArepooo\serviceAccountKey.json")
            firebase_admin.initialize_app(cred)
        
        self.db = firestore.client()
        self.collection = self.db.collection("users")
    
    def crear_usuario(self, nombre, email, edad):
  
        usuario_data = {
            'nombre': nombre,
            'email': email,
            'edad': edad,
            'creado_en': datetime.now()
        }
        
        doc_ref = self.collection.document()
        doc_ref.set(usuario_data)
        
        print(f"✅ Usuario creado: {doc_ref.id}")
        return doc_ref.id
    
    def obtener_usuario(self, usuario_id):
    
        doc = self.collection.document(usuario_id).get()
        
        if doc.exists:
            datos = doc.to_dict()
            datos['id'] = doc.id
            return datos
        return None
    
    def obtener_todos(self):
        
        usuarios = []
        docs = self.collection.stream()
        
        for doc in docs:
            datos = doc.to_dict()
            datos['id'] = doc.id
            usuarios.append(datos)
        
        return usuarios
    
    def actualizar_usuario(self, usuario_id, **campos):
       
        doc_ref = self.collection.document(usuario_id)
        
        if not doc_ref.get().exists:
            print("❌ Usuario no encontrado")
            return False
        
        campos['actualizado_en'] = datetime.now()
        doc_ref.update(campos)
        print(f"✅ Usuario actualizado: {usuario_id}")
        return True
    
    def eliminar_usuario(self, usuario_id):
        
        doc_ref = self.collection.document(usuario_id)
        
        if not doc_ref.get().exists:
            print("❌ Usuario no encontrado")
            return False
        
        doc_ref.delete()
        print(f"✅ Usuario eliminado: {usuario_id}")
        return True