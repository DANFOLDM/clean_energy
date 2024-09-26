from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Flask-Login setup
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if not authenticated

# Mock user data (replace this with database connection later)
users = {}

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    # Get the user by ID
    if user_id in users:
        return User(user_id, users[user_id]['username'])
    return None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Saving user data (for now, storing in memory)
        user_id = len(users) + 1
        users[user_id] = {'username': form.username.data, 'email': form.email.data, 'password': form.password.data}
        
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Simulating a user lookup (replace with database lookup)
        for user_id, user_info in users.items():
            if user_info['email'] == form.email.data and user_info['password'] == form.password.data:
                user = User(user_id, user_info['username'])
                login_user(user)  # Log the user in
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))  # Redirect to dashboard after login
        
        # If login fails, show this message
        flash('Login unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    # Example data for the logged-in user (replace with real data from the database)
    user_data = {
        'username': current_user.username,
        'current_consumption': 320,  # Example energy consumption (in kWh)
        'daily_consumption': [30, 50, 60, 40, 55, 70, 65],  # Graph data for last 7 days
        'recommendation': 'Consider reducing usage during peak hours to save costs.'
    }
    return render_template('dashboard.html', user_data=user_data)

@app.route('/logout')
@login_required
def logout():
    logout_user()  # Log the user out
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
