from application import application

def main():
    app = application()
    while(app.running):
        app.step()

if __name__ == "__main__":
    main()
