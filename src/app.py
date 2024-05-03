from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user




from config import config

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

# API Calls
from api.views import get_laliga_teams, get_laliga_matches, get_laligastandings


app = Flask(__name__)

csrf = CSRFProtect()

db = MySQL(app)
login_manager_app = LoginManager(app)

laliga_team = get_laliga_teams()
laliga_standing = get_laligastandings()

@login_manager_app.user_loader
def load_user(user_id):
    return ModelUser.get_by_id(db, user_id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash("Complete data")
            return render_template('auth/login.html')
        else:
            user = User(0, request.form['username'], request.form['password'])
            logged_user = ModelUser.login(db, user)
            if logged_user != None:
                if logged_user.password:
                    login_user(logged_user)
                    return redirect(url_for('home'))
                else:
                    flash("Invalid password...")
                    return render_template('auth/login.html')                
            else:
                flash("User not found...")
                return render_template('auth/login.html')
    else:
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        else:
            return render_template('auth/login.html')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Verificar si todos los campos están completos
        if not all([request.form['username'], request.form['password'], request.form['repeatpassword'], request.form['fullname']]):
            flash("Todos los campos son requeridos")
            return render_template('auth/register.html')
        
        # Verificar si las contraseñas coinciden
        if request.form['password'] != request.form['repeatpassword']:
            flash("Las contraseñas deben coincidir")
            return render_template('auth/register.html')
        
        # Verificar si el nombre de usuario ya existe
        if ModelUser.get_usernames(db, request.form['username']):
            flash("El nombre de usuario ya está escojido")
            return render_template('auth/register.html')
        
        # Crear un nuevo usuario y agregarlo a la base de datos
        user = User(0, request.form['username'], request.form['password'], request.form['fullname'])
        try:
            ModelUser.create_user(db, user)
            flash("Usuario creado, ya puedes ingresar.")
            return render_template('auth/login.html')
        except Exception as ex:
            flash("Un error ha ocurrido, por favor, intentalo de nuevo.")
            # Log the error for debugging purposes
            print(ex)
            return render_template('auth/register.html')
    
    # Si el método es GET, mostrar el formulario de registro
    else:
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        else:
            return render_template('auth/register.html')
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    current_matchday = laliga_standing[0]['current_matchday']
    laliga_match = get_laliga_matches(current_matchday)
    
    if request.method == 'POST': 
        boton_jornada = request.form['boton_jornada']
        laliga_match = get_laliga_matches(boton_jornada)
    
     
    return render_template('home.html', laliga_teams = laliga_team, laliga_matches = laliga_match, laliga_standings = laliga_standing)

@app.route('/perfil', methods=['GET', 'POST'])
@login_required
def user_profile():
    if request.method == 'POST':
        boton_id_equipo = request.form['boton_favorito']
        print(boton_id_equipo)
        ModelUser.remove_favorite_team(db, boton_id_equipo, current_user.id)
        
    user_favorite_teams_id = ModelUser.get_favorite_teams(db, current_user.id)
    user_favorite_teams_info = []
    
    for team in laliga_team:
        for ids in user_favorite_teams_id:
            if ids == team['team_id']:
                user_favorite_teams_info.append(team)      
            
    return render_template('user_profile.html', favorite_teams = user_favorite_teams_info)

@app.route('/equipo/<team_name>', methods=['GET', 'POST'])
@login_required
def teams(team_name):
    
    user_favorite_teams_id = ModelUser.get_favorite_teams(db, current_user.id)
    team_id = None
    clicked_team = None
    team_city = None
    is_favorite = False
        
    laliga_teams_cities = {
        'Deportivo Alavés': 'Vitoria-Gasteiz, País Vasco',
        'UD Almería': 'Almería, Andalucía',
        'Athletic Club': 'Bilbao, País Vasco',
        'Club Atlético de Madrid': 'Madrid, Comunidad de Madrid',
        'FC Barcelona': 'Barcelona, Cataluña',
        'RC Celta de Vigo': 'Vigo, Galicia',
        'Cádiz CF': 'Cádiz, Andalucía',
        'Getafe CF': 'Getafe, Comunidad de Madrid',
        'Girona FC': 'Girona, Cataluña',
        'Granada CF': 'Granada, Andalucía',
        'UD Las Palmas': 'Las Palmas de Gran Canaria, Canarias',
        'RCD Mallorca': 'Palma, Islas Baleares',
        'CA Osasuna': 'Pamplona, Comunidad Foral de Navarra',
        'Rayo Vallecano de Madrid': 'Madrid, Comunidad de Madrid',
        'Real Betis Balompié': 'Sevilla, Andalucía',
        'Real Madrid CF': 'Madrid, Comunidad de Madrid',
        'Real Sociedad de Fútbol': 'San Sebastián, País Vasco',
        'Sevilla FC': 'Sevilla, Andalucía',
        'Valencia CF': 'Valencia, Comunidad Valenciana',
        'Villarreal CF': 'Villarreal, Comunidad Valenciana'
    }
            
    for team in laliga_team:        
        if team["team_tla"] == team_name:
            clicked_team = team          
            team_id = clicked_team['team_id']
            team_city = laliga_teams_cities[team["team_name"]]
            
            for ids in user_favorite_teams_id:
                if ids == team_id:
                    is_favorite = True
    
    if request.method == 'POST':
        if is_favorite:
            ModelUser.remove_favorite_team(db, team_id, current_user.id)
            is_favorite = False  # Actualizar el estado
        else:
            if len(user_favorite_teams_id) >= 3:
                flash("Solo puedes añadir hasta 3 equipos favoritos")
            else:
                ModelUser.insert_favorite_team(db, team_id, current_user.id)
                is_favorite = True  # Actualizar el estado
    
    return render_template('teams.html', clicked_team_data=clicked_team, team_city=team_city, is_favorite_team=is_favorite)

@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados</h1>"

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()