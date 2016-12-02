from flask import Flask, request, render_template
app = Flask(__name__)  

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/contact") 
@app.route('/contact/<name>')
def name(name=None):         
	return render_template('contact.html', name=name)
@app.route("/index")
def paris(name=None): 
     return app.send_static_file('index.html')
	
@app.route("/poll/")
def poll(name=None):
    return render_template('poll.html', name=name)
	
if __name__ == "__main__":     
	app.run()
