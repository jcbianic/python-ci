from backend.application import create_app


app = create_app("Test App", "development")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
