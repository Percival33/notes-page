from website import create_app
# print("Hello World!")

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)