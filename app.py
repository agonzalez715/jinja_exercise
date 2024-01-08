from flask import Flask, render_template, request #imports the flask class
app = Flask(__name__) #creates instance of flask class
from stories import story

@app.route('/')  #defines the route for the home page
def home():  #the function thats called when the home route is accessed.
    prompts = story.prompts #assuming 'story' ia your Story instance 
    return render_template('home.html', prompts=prompts)

@app.route('/story', methods=['POST'])
def show_story():
    answers = request.form
    story_text = story.generate(answers)
    return render_template('story.html', story=story_text)    

if  __name__== '__main__':
    app.run(debug=True)

