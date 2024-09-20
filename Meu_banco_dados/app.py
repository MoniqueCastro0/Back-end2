from app import create_app


app = create_app()

#configuração banco dados SQLite
""" app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) """


if __name__ == "__main__":
    app.run(debug=True)