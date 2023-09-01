import os
import base64
import json
from jinja2 import Template


def decode_base64_to_dict(base64_string):
    decoded_bytes = base64.b64decode(base64_string)
    decoded_string = decoded_bytes.decode('utf-8')
    data_dict = json.loads(decoded_string)
    return data_dict


def render_provider_tf(account_ids):
    # Open and read the template file
    with open('aft-providers.jinja', 'r') as file:
        template_string = file.read()
    # Create a template instance
    template = Template(template_string)
    # Render the template
    rendered_template = template.render(account_ids=account_ids)
    # Open and write to the output file
    with open('aft-providers.tf', 'w') as file:
        file.write(rendered_template)


def render_customization_module_tf(module_content):
    # Open and read the template file
    with open('customizations/main.tf.jinja', 'r') as file:
        template_string = file.read()
    # Create a template instance
    template = Template(template_string)
    # Render the template
    rendered_template = template.render(content=module_content)
    # Open and write to the output file
    with open('customizations/main.tf', 'w') as file:
        file.write(rendered_template)

def render_versions_tf(account_ids):
    # Open and read the template file
    with open('versions.tf.jinja', 'r') as file:
        template_string = file.read()
    # Create a template instance
    template = Template(template_string)
    # Render the template
    rendered_template = template.render(account_ids=account_ids)
    # Open and write to the output file
    with open('versions.tf', 'w') as file:
        file.write(rendered_template)


def render_main_tf(account_ids):
    # Open and read the template file
    with open('main.tf.jinja', 'r') as file:
        template_string = file.read()
    # Create a template instance
    template = Template(template_string)
    # Render the template
    rendered_template = template.render(account_ids=account_ids)
    # Open and write to the output file
    with open('main.tf', 'w') as file:
        file.write(rendered_template)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Read environment variable $TF_VARIABLES that is in base64 format and convert it to dictionary
    tf_variables = os.getenv('TF_VARIABLES')
    if tf_variables:
        variables_dict = decode_base64_to_dict(tf_variables)
        print(variables_dict)
    else:
        print("Environment variable $TF_VARIABLES not found.")
        exit(1)
    render_provider_tf(variables_dict['account_ids'])
    render_customization_module_tf(variables_dict['module_content'])
    render_versions_tf(variables_dict['account_ids'])
    render_main_tf(variables_dict['account_ids'])

