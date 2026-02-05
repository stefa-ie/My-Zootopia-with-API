import data_fetcher
import os

def animal_card(animal_obj):
    """Generate an HTML card for a single animal.

    Args:
        animal_obj: A dictionary containing animal data with keys such as
            'name', 'characteristics', and 'locations'.

    Returns:
        A string containing the HTML markup for the animal card.
    """
    output = ""
    output += '<li class="cards__item">\n'
    if 'name' in animal_obj:
        output += f"<div class='card__title'>{animal_obj['name']}</div><br/>\n"
    output += "<p class='card__text'>\n"
    if ('characteristics' in animal_obj
            and 'diet' in animal_obj['characteristics']):
        diet = animal_obj['characteristics']['diet']
        output += f"<strong>Diet:</strong> {diet}<br/>\n"
    if 'locations' in animal_obj and animal_obj['locations']:
        output += f"<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n"
    if ('characteristics' in animal_obj
            and 'type' in animal_obj['characteristics']):
        animal_type = animal_obj['characteristics']['type']
        output += f"<strong>Type:</strong> {animal_type}<br/>\n"
    output += '</p>\n'
    output += '</li>\n'
    return output


def update_html(animal_name):
    """Fetch animal data from API and generate an HTML file.

    Retrieves animal information using the data_fetcher module and creates
    an HTML file using the template. If the animal is not found, generates
    a page with a user-friendly error message.

    Args:
        animal_name: The name of the animal to search for.
    """
    animal_data = data_fetcher.fetch_data(animal_name)

    if not animal_data:
        # Generate a user-friendly message for the website
        # when animal is not found
        output = (
            '<li class="cards__item">\n'
            '<div class="card__title">Animal Not Found</div>\n'
            '<p class="card__text">\n'
            f'Sorry, we couldn\'t find any information about '
            f'"<strong>{animal_name}</strong>".<br/>\n'
            'Please check the spelling and try again with a new input.\n'
            '</p>\n'
            '</li>\n'
        )
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
        print(f"Created/Updated {animal_name}.html "
              f"with information about {animal_name}.")
    else:
        print(f"Created {animal_name}.html with a 'not found' message.")


def main():
    """Run the animal web generator application.

    Prompts the user to enter an animal name and generates an HTML page
    with information about that animal.
    """
    animal_name = input("Please enter an animal: ")
    update_html(animal_name)


if __name__ == "__main__":
    main()

