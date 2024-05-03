from .entities.User import User
from werkzeug.security import check_password_hash, generate_password_hash


class ModelUser():
    
    @classmethod
    def create_user(cls, db, user):
        hashed_password = generate_password_hash(user.password, method='pbkdf2')
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO user (username, password, fullname) VALUES (%s, %s, %s);"
            cursor.execute(sql, (user.username, hashed_password, user.fullname))
            db.connection.commit()
            return True  # Indicar que la inserción fue exitosa
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def login(cls,db,user):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM user WHERE username LIKE %s;"
            cursor.execute(sql, (user.username,))
            row = cursor.fetchone()
            if row is not None:
                user = User(row[0], row[1], check_password_hash(row[2], user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(cls,db,user_id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT user_id, username, fullname FROM user WHERE user_id = %s;"
            cursor.execute(sql, (user_id,))
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_usernames(cls,db,username):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM user WHERE username LIKE %s;"
            cursor.execute(sql, (username,))
            row = cursor.fetchone()
            if not row:
                return 0
            else:
                return 1
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def insert_favorite_team(cls, db, team_id, user_id):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO favorite_teams (team_id, user_id) VALUES (%s, %s);"
            cursor.execute(sql, (team_id, user_id,))
            db.connection.commit()  # Guardar los cambios en la base de datos
            return True  # Indicar que la inserción fue exitosa
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def remove_favorite_team(cls, db, team_id, user_id):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM favorite_teams WHERE team_id = %s AND user_id = %s;"
            cursor.execute(sql, (team_id, user_id,))
            db.connection.commit()  # Guardar los cambios en la base de datos
            return True  # Indicar que la removida fue exitosa
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_favorite_teams(cls, db, user_id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT team_id FROM favorite_teams WHERE user_id = %s;"
            cursor.execute(sql, (user_id,))
            rows = cursor.fetchall()
            # Extraer solo los team_id de las filas
            favorite_team_ids = [row[0] for row in rows]
            return favorite_team_ids
        except Exception as ex:
            raise Exception(ex)
    
    
            