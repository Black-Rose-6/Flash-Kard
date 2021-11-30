from flashkard import create_app
import random

if __name__ == "__main__":
    app, api = create_app()
    
    app.run(debug=True,
    host ='0.0.0.0',
    port = 5000
    )