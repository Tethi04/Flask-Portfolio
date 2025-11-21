
## Interview Questions Answers:

1. **What is a template in Flask?**  
   A template is an HTML file that can contain placeholders for dynamic content using Jinja2 syntax.

2. **What's Jinja?**  
   Jinja2 is a templating engine for Python that allows you to embed Python-like expressions in HTML templates.

3. **How do you pass data to a template?**  
   Using the `render_template()` function with keyword arguments: `render_template('index.html', name=name, projects=projects)`

4. **How are forms handled in Flask?**  
   Using `request.form` to access form data and handling both GET and POST methods in route decorators.

5. **What is render_template()?**  
   A Flask function that renders HTML templates with the provided context variables.

6. **How to style your app?**  
   Using static CSS files placed in the `static/css/` directory and linked in templates.

7. **What's POST vs GET method in forms?**  
   GET sends data in URL, POST sends data in request body. POST is used for sensitive data and form submissions.

8. **What are static files?**  
   Files like CSS, JavaScript, and images that don't change and are served directly to the client.

9. **How is routing done in Flask?**  
   Using the `@app.route()` decorator to map URLs to Python functions.

10. **Can Flask serve HTML/CSS/JS?**  
    Yes, Flask can serve HTML templates and static files (CSS, JS, images).

This portfolio website showcases all your skills and projects from your resume in an interactive web format!