from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Personal information
personal_info = {
    'name': 'TETHI BISWAS',
    'email': 'biswastethi2004@gmail.com',
    'phone': '(+91) 9800831765',
    'github': 'https://github.com/Tethi04',
    'linkedin': 'https://www.linkedin.com/in/tethi-biswas-555792358'
}


# Technical skills
skills = {
    'Languages': ['Python', 'C++', 'C', 'Java', 'JavaScript', 'HTML', 'CSS', 'TypeScript'],
    'Tools & Platforms': ['Git & GitHub', 'VS Code', 'Flask', 'Windows/Linux OS'],
    'Concepts': ['Data Structures & Algorithms (DSA)', 'Object-Oriented Programming (OOP)', 'Computer Networking']
}

# Education
education = [
    {
        'degree': 'Bachelor of Science in Computer Science',
        'institution': 'Siliguri College, Siliguri',
        'period': '2023 â€“ Present (Expected: Aug 2027)'
    },
    {
        'degree': 'Higher Secondary (XII), WBCHSE',
        'institution': 'Sunitibala Sadar Girls\' High School',
        'period': '71.8% | 2023'
    }
]

# Certifications
certifications = [
    {
        'name': 'Diploma in Information Technology',
        'institution': 'Jawaharlal Nehru Youth Computer Centre (JNYCC), Jalpaiguri, West Bengal',
        'period': 'October 2021 - Sept 2022',
        'description': 'Completed "A" Grade training focused on Operating Systems, Web Technologies, and programming logic.'
    }
]

# Simple projects data (minimal to test)
projects = [
      {
        'title': 'Flask Portfolio Website',
        'description': 'Personal Portfolio & Web Application',
        'details': 'Developed and deployed a responsive personal portfolio using Python Flask framework. Implemented dynamic templating with Jinja2 and custom CSS styling. Features contact form with backend processing, project showcase, and fully responsive design.',
        'technologies': ['Python', 'Flask', 'HTML5', 'CSS3', 'JavaScript', 'Jinja2'],
        'live_demo': 'https://tethi-portfolio-17yk.onrender.com',
        'github': 'https://github.com/Tethi04/flask-portfolio'
    },
    {
        'title': 'Code Treasure Hunt Web App',
        'description': 'Multi-stage coding hunt game',
        'details': 'Engineered a complex web application using TypeScript, HTML, and CSS for a multi-stage coding hunt. Implemented advanced game logic, user state management, and interactive challenges. Enhanced code maintainability with static typing and designed a responsive, fast-loading architecture.',
        'technologies': ['TypeScript', 'HTML', 'CSS', 'JavaScript'],
        'live_demo': 'https://cth-demo.onrender.com',
        'github': 'https://github.com/Tethi04/code-treasure-hunt'
    },
    {
        'title': 'Colour Hex Detector',
        'description': 'Instant color identification tool',
        'details': 'Built a high-speed, client-side web tool using JavaScript and Canvas API to identify precise hex codes from user-uploaded images instantly. Features real-time color detection without server reliance and includes a clean, intuitive interface with instant visual feedback.',
        'technologies': ['JavaScript', 'Canvas API', 'HTML', 'CSS'],
        'live_demo': 'https://colour-hex-detector.onrender.com',
        'github': 'https://github.com/Tethi04/Colour-Hex-Detector'
    },
    {
        'title': 'Mood Tracker Website',
        'description': 'Daily mood tracking application',
        'details': 'Created a personal mood tracking website with persistent data management using Local Storage. Implemented front-end state management allowing users to log daily moods, review tracking history across sessions, and visualize mood patterns over time.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'Local Storage'],
        'live_demo': 'https://mood-tracker-website.onrender.com',
        'github': 'https://github.com/Tethi04/Mood-Tracker-Website'
    },
    {
        'title': 'Animated Birthday Greeting',
        'description': 'Re-usable animated greeting card',
        'details': 'Built a dynamic, animated greeting website using modern CSS animations and transitions. Optimized the code as a public template for easy re-use and customization by other developers. Features smooth animations, responsive design, and cross-browser compatibility.',
        'technologies': ['HTML', 'CSS', 'CSS Animations', 'Responsive Design'],
        'live_demo': 'https://animated-birthday-greeting.onrender.com',
        'github': 'https://github.com/Tethi04/Animated-Birthday-Greeting'
    }
]

# Languages
languages = [
    {'name': 'Bengali', 'proficiency': 'Native'},
    {'name': 'Hindi', 'proficiency': 'Fluent'},
    {'name': 'English', 'proficiency': 'Advanced Working Proficiency'},
    {'name': 'Korean', 'proficiency': 'Beginner/Conversational'}
]

@app.route('/')
@app.route('/')
def index():
    return render_template('index.html', 
                         personal_info=personal_info,
                         skills=skills)

@app.route('/projects')
def projects_page():
    return render_template('projects.html',
                         personal_info=personal_info,
                         projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        flash(f'Thank you {name}! Your message has been received.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', personal_info=personal_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)


