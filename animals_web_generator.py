import data_fetcher
import os

def animal_card(animal_obj):
    """Generates an HTML card for a single animal object."""
    output = ""
    output += '<li class="cards__item">\n'
    if 'name' in animal_obj:
        output += f"<div class='card__title'>{animal_obj['name']}</div><br/>\n"
    output += "<p class='card__text'>\n"
    if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
        output += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n"
    if 'locations' in animal_obj and animal_obj['locations']:
        output += f"<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n"
    if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
        output += f"<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>\n"
    output += '</p>\n'
    output += '</li>\n'
    return output


def update_html(animal_name):
    """Fetches animal data from API and updates/creates HTML file."""
    animal_data = data_fetcher.fetch_data(animal_name)

    if not animal_data:
        # Generate a user-friendly message for the website when animal is not found
        output = f'''<li class="cards__item">
        <div class="card__title">Animal Not Found</div>
        <p class="card__text">
        Sorry, we couldn't find any information about "<strong>{animal_name}</strong>".<br/>
        Please check the spelling and try again with a new input.
        </p>
        </li>
        '''
    else:
        output = ''
        animals = animal_data if isinstance(animal_data, list) else [animal_data]
        for animal in animals:
            output += animal_card(animal)

    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, 'animals_template.html')
    
    with open(template_path, 'r') as file:
        content = file.read()

    updated_content = content.replace('__REPLACE_ANIMALS_INFO__', output)

    output_path = os.path.join(script_dir, f'{animal_name}.html')
    with open(output_path, 'w') as file:
        file.write(updated_content)

    if animal_data:
        print(f"Created/Updated {animal_name}.html with information about {animal_name}.")
    else:
        print(f"Created {animal_name}.html with a 'not found' message.")


def main():
    animal_name = input("Please enter an animal: ")
    update_html(animal_name)


if __name__ == "__main__":
    main()

