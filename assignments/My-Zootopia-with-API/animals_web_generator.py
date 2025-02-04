import data_fetcher

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
        print(f"No data found for '{animal_name}'.")
        return

    output = ''
    animals = animal_data if isinstance(animal_data, list) else list(animal_data)
    for animal in animals:
        output += animal_card(animal)

    with open('animals_template.html', 'r') as file:
        content = file.read()

    updated_content = content.replace('__REPLACE_ANIMALS_INFO__', output)

    with open(f'{animal_name}.html', 'w') as file:
        file.write(updated_content)

    print(f"Created/Updated animals.html with information about {animal_name}.")


def main():
    animal_name = input("Please enter an animal: ")
    update_html(animal_name)


if __name__ == "__main__":
    main()

