from jinja2 import Environment,FileSystemLoader


env = Environment(loader=FileSystemLoader(searchpath="./"))

template = env.get_template('about.html')
output = template.render()
print(output)

# python3 render.py