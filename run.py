from app import app

if(__name__ == '__main__'):
    app.run(host="", port=3000, debug=True, load_dotenv=True)